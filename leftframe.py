import customtkinter as CTk
from ctkcomponents import CTkNotification
import pandas as pd
from pandastable import TableModel
from options_window import OptionsWindow

# Левый блок
class LeftFrame(CTk.CTkFrame):
    def __init__(self, app, master, **kwargs):
        super().__init__(master, **kwargs)

        self.app = app
        
        # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure((2), weight=1)
        
        # Надпись приложения
        self.name = CTk.CTkLabel(self, text='DataPulse', font=("Helvetica", 26, 'bold'))
        self.name.grid(row=0, padx=10, pady=75)
        
        # Блок работы с файлами
        self.frame_files_work = CTk.CTkFrame(self)
        self.frame_files_work.grid(row=1, padx=5, pady=5)
        
        # Надпись в блоке работы с файлами
        self.label_file_frame = CTk.CTkLabel(self.frame_files_work, text='Данные', font=("Helvetica", 14))
        self.label_file_frame.grid(pady=5)
        
        # Кнопка загрузки файла
        self.load_file_btn = CTk.CTkButton(self.frame_files_work, text='Загрузить', command=self.load_file, width=160, font=("Helvetica", 14), corner_radius=12)
        self.load_file_btn.grid(pady=5)
        
        # Кнопка перехода на вкладку сохранения
        self.save_file_btn = CTk.CTkButton(self.frame_files_work, text='Сохранить', width=160, font=("Helvetica", 14), corner_radius=12,
                                           command=lambda: self.app.tab_view.set('Сохранение'))
        self.save_file_btn.grid(pady=5)
        
        self.options_window = None

        # Фрейм выбора темы
        self.frame_appearance = CTk.CTkFrame(self)
        self.frame_appearance.grid(sticky='s', row=2, pady=30)
        
        # Надпись выбора темы
        self.appearance_name = CTk.CTkLabel(self.frame_appearance, text='Выбор темы', font=("Helvetica", 14))
        self.appearance_name.grid(pady=5)
        
        # Словарь тем
        self.themes = {"Светлая": 'light', "Темная": 'dark', "Системная": 'system'}
        
        # Меню выбора темы   
        self.appearance_menu = CTk.CTkOptionMenu(self.frame_appearance, values=list(self.themes.keys()), command=self.appearance_menu_callback,
                                                 width=160, corner_radius=12, font=("Helvetica", 14))
        self.appearance_menu.set("Системная")
        self.appearance_menu.grid(pady=5)
        
        # Кнопка настроек
        self.options_btn = CTk.CTkButton(self, text='Настройки', command=self.open_options, width=160, font=("Helvetica", 14), corner_radius=12)
        self.options_btn.grid(sticky='s', row=3, pady=10)
        
    # Загрузка файла в DataFrame
    def load_file(self):
        file_path = CTk.filedialog.askopenfilename(title="Выберите файл", filetypes=[("CSV files", "*.csv"),
                                                                                     ("EXCEL files", "*.xlsx *.xls"),
                                                                                     ("JSON files", "*.json")])
        
        if file_path:
            try:
                # Чтение данных из файла csv
                if file_path.endswith('.csv'):
                    sep_df = CTk.CTkInputDialog(text="Введите разделитель в данных:", title="Sep")
                    self.dataframe = pd.read_csv(file_path, sep=sep_df.get_input())
                
                # Чтение данных из файла xlsx, xls
                elif file_path.endswith('.xls'): 
                    
                    self.dataframe = pd.read_excel(file_path) 

                # Чтение данных из файла json
                elif file_path.endswith('.json'): self.dataframe = pd.read_json(file_path) 
                
                # Передача dataframe в таблицу и её обновление
                self.app.tab_view.tab_data_overview.df_table.updateModel(TableModel(self.dataframe))
                self.app.tab_view.tab_data_overview.df_table.redraw()
                
                # Передача столбцов dataframe в менюшки
                features_dataframe = self.dataframe.columns.to_list()
                self.app.tab_view.tab_graphics.menu_graph_feature_x.configure(values=features_dataframe)
                self.app.tab_view.tab_graphics.menu_graph_feature_y.configure(values=features_dataframe)
                self.app.tab_view.tab_graphics.menu_graph_feature_hue.configure(values=['Не использовать'] + features_dataframe)
                self.app.tab_view.tab_graphics.menu_graph_feature_style.configure(values=['Не использовать'] + features_dataframe)
                self.app.tab_view.tab_graphics.menu_graph_feature_size.configure(values=['Не использовать'] + features_dataframe)
                self.app.tab_view.tab_filtration_sort.menu_feature_filter.configure(values=features_dataframe)
                self.app.tab_view.tab_filtration_sort.menu_feature_sorted.configure(values=features_dataframe)
                self.app.tab_view.tab_extended_analyze.menu_feature_analyze.configure(values=features_dataframe)
                
                # Активация менюшек параметров графика после загрузки данных
                self.app.tab_view.tab_graphics.menu_graph_type.configure(state='normal')
                self.app.tab_view.tab_graphics.menu_graph_feature_x.configure(state='normal')
                self.app.tab_view.tab_graphics.menu_graph_feature_y.configure(state='normal')
                self.app.tab_view.tab_graphics.menu_graph_feature_hue.configure(state='normal')
                
                # Активация кнопки создания графика после загрузки данных
                self.app.tab_view.tab_graphics.create_graphic_btn.configure(state='normal')
                
                # Активация меню фильтрации
                self.app.tab_view.tab_filtration_sort.menu_feature_filter.configure(state='normal')
                
                # Активация меню выбора признака для анализа
                self.app.tab_view.tab_extended_analyze.menu_feature_analyze.configure(state='normal')
                
                # Окно с сообщением о успешной загрузке данных
                CTkNotification(self.app, message='Данные загружены успешно')
                
                # Изменение цвета надписи 'Данные' при успешной загрузки данных
                self.label_file_frame.configure(text_color='#228F19')
                
            except Exception as e:
                # Окно с сообщением о ошибке при загрузке данных
                CTkNotification(self.app, message='Произошла ошибка', state='error')

                # Изменение цвета надписи 'Данные' при ошибке загрузки данных
                self.label_file_frame.configure(text_color='#9E1C1A')
                
                self.dataframe = None
                
    # Смена темы
    def appearance_menu_callback(self, choice):
        CTk.set_appearance_mode(self.themes[choice])
        
    # Открытие окна настроек
    def open_options(self):
        self.options_window = OptionsWindow(self)
        # Захват фокуса на окно
        self.options_window.grab_set()