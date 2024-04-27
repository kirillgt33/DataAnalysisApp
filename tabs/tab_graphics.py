import customtkinter as CTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns

### Вкладка <Графики и визуализация> ###
class TabGraphics(CTk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        master.add("Графики и визуализация")
        
        # Фрейм - правый блок
        self.frame_right_options = CTk.CTkFrame(master=master.tab("Графики и визуализация"))
        self.frame_right_options.pack(side='right', fill='y')
        
        # Фрейм настроек создания графика
        self.frame_graph_options = CTk.CTkFrame(master=self.frame_right_options)
        self.frame_graph_options.pack(padx=5)
        
        # Надпись настроек графика
        self.graph_options_lbl = CTk.CTkLabel(master=self.frame_graph_options, text='Настройки графика')
        self.graph_options_lbl.pack(pady=5)
        
        # Меню выбора типа графика
        self.graphics_type = {'График рассеяния': 'scatterplot',
                              'Линейный график': 'lineplot',
                              'Ящик с усами': 'boxplot',
                              'Гистограмма': 'histplot',
                              'Столбчатая диаграмма': 'barplot',
                              'График скрипок': 'violinplot'}
        
        self.menu_graph_type = CTk.CTkOptionMenu(master=self.frame_graph_options,
                                                 values=list(self.graphics_type.keys()),
                                                 width=180, state='disabled', dynamic_resizing=False, corner_radius=12, command=self.options_plus_view)
        self.menu_graph_type.set('Тип графика')
        self.menu_graph_type.pack(pady=10, padx=5)
        
        # Меню выбора признака по x
        self.menu_graph_feature_x = CTk.CTkOptionMenu(master=self.frame_graph_options, width=180, state='disabled', dynamic_resizing=False, corner_radius=12)
        self.menu_graph_feature_x.set('Признак по X')
        self.menu_graph_feature_x.pack(pady=10)
        
        # Меню выбора признака по y
        self.menu_graph_feature_y = CTk.CTkOptionMenu(master=self.frame_graph_options, width=180, state='disabled', dynamic_resizing=False, corner_radius=12)
        self.menu_graph_feature_y.set('Признак по Y')
        self.menu_graph_feature_y.pack(pady=10)
        
        # Меню выбора признака для раскраса графика
        self.menu_graph_feature_hue = CTk.CTkOptionMenu(master=self.frame_graph_options, width=180, state='disabled', dynamic_resizing=False, corner_radius=12,
                                                        command=lambda x: self.menu_graph_feature_hue.set('Признак разделения') if x == 'Не использовать' else None)
        self.menu_graph_feature_hue.set('Признак разделения')
        self.menu_graph_feature_hue.pack(pady=10)
        
        # Checkbox для построения графика на отфильтрованном dataframe
        self.check_on_filterdf_var = CTk.StringVar(value="off")
        self.check_on_filterdf = CTk.CTkCheckBox(master=self.frame_graph_options, text='Данные с фильтром', variable=self.check_on_filterdf_var, 
                                                 onvalue="on", offvalue="off", state='disabled', corner_radius=12)
        self.check_on_filterdf.pack(anchor='w', pady=10, padx=5)
        
        # Кнопка для создания графика
        self.create_graphic_btn = CTk.CTkButton(master=self.frame_graph_options, text='Создать/Обновить', state='disabled', command=self.create_graphic)
        self.create_graphic_btn.pack(pady=10)
        
        # Фрейм доп настроек по конкретному графику
        self.frame_graph_options_plus = CTk.CTkFrame(master=self.frame_right_options)
        self.frame_graph_options_plus.pack(padx=5, pady=5)
        
        # Надпись доп настроек по конкретному графику
        self.graph_options_plus_lbl = CTk.CTkLabel(master=self.frame_graph_options_plus, text='Дополнительно')
        self.graph_options_plus_lbl.pack(pady=5)
        
        # Меню выбора признака для стилизации
        self.menu_graph_feature_style = CTk.CTkOptionMenu(master=self.frame_graph_options_plus, width=180, dynamic_resizing=False, corner_radius=12,
                                                          command=lambda x: self.menu_graph_feature_style.set('Признак стилизации') if x == 'Не использовать' else None)
        self.menu_graph_feature_style.set('Признак стилизации')
        
        # Меню выбора признака для размера маркеров на графике
        self.menu_graph_feature_size = CTk.CTkOptionMenu(master=self.frame_graph_options_plus, width=180, dynamic_resizing=False, corner_radius=12,
                                                         command=lambda x: self.menu_graph_feature_size.set('Признак размера') if x == 'Не использовать' else None)
        self.menu_graph_feature_size.set('Признак размера')
        
        # Фрейм для надписи и слайдера для выбора прозрачности
        self.frame_sldr_lbl_alpha = CTk.CTkFrame(master=self.frame_graph_options_plus)
        
        # Надпись над слайдером выбора прозрачности
        self.lbl_graph_choice_alpha = CTk.CTkLabel(master=self.frame_sldr_lbl_alpha, text='Прозрачность')
        self.lbl_graph_choice_alpha.pack(pady=5)
        
        # Слайдер для выбора прозрачности маркеров на графике
        self.sldr_graph_choice_alpha = CTk.CTkSlider(master=self.frame_sldr_lbl_alpha, from_=1, to=0, number_of_steps=10, width=180)
        self.sldr_graph_choice_alpha.set(1.0)
        self.sldr_graph_choice_alpha.pack(pady=5)
        
        # Фрейм для надписи и комбоменю выбора ориентации графика
        self.frame_graph_choice_orient = CTk.CTkFrame(master=self.frame_graph_options_plus)
        
        # Надпись над комбоменю выбора ориентации графика
        self.lbl_graph_choice_orient = CTk.CTkLabel(master=self.frame_graph_choice_orient, text='Ориентация')
        self.lbl_graph_choice_orient.pack(pady=5)
        
        # Комбо меню выбора ориентации графика
        self.combobox_graph_choice_orient = CTk.CTkComboBox(master=self.frame_graph_choice_orient, values=['Вертикальная', 'Горизонтальная'],
                                                            state='readonly', width=180, corner_radius=12)
        self.combobox_graph_choice_orient.set('Вертикальная')
        self.combobox_graph_choice_orient.pack(pady=5)
        
        self.fig, self.ax = plt.subplots()
        #self.ax.set_facecolor('black')
        #self.fig.patch.set_facecolor('black')
        
        # Создаем объект FigureCanvasTkAgg
        self.canvas = FigureCanvasTkAgg(self.fig, master=master.tab("Графики и визуализация"))
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(expand=True, fill='both')
    
    # Вывод доп настроек по графикам
    def options_plus_view(self, choice):
        # Тип выбранного графика
        selected_graph = self.graphics_type[choice]
   
        if selected_graph == 'scatterplot' or selected_graph == 'lineplot':
            # Вывод доп настроек для scatterplot или lineplot
            self.menu_graph_feature_style.pack(pady=5, padx=5)
            self.menu_graph_feature_size.pack(pady=5, padx=5)
            self.frame_sldr_lbl_alpha.pack(pady=5, padx=5)
            
        else:
            # Скрытие доп настроек для scatterplot или lineplot
            self.menu_graph_feature_style.pack_forget()
            self.menu_graph_feature_size.pack_forget()
            self.frame_sldr_lbl_alpha.pack_forget()

        
        if selected_graph == 'boxplot' or selected_graph == 'lineplot':
            # Обновление отображения фрейма
            self.frame_graph_choice_orient.pack_forget()
            self.frame_graph_choice_orient.pack(pady=5)
                
        else:
            self.frame_graph_choice_orient.pack_forget()    
        
    # Создание графика    
    def create_graphic(self):
        
        # Тип выбранного графика
        choise_graph = self.graphics_type[self.menu_graph_type.get()]
        
        # Признаки по x и y
        feature_x = self.menu_graph_feature_x.get()
        feature_y = self.menu_graph_feature_y.get()
        
        # Признак разделения по цвету
        feature_hue = self.menu_graph_feature_hue.get()
        
        # Проверка на отфильтрованный dataframe
        if self.check_on_filterdf_var.get() == 'off':
            dataframe = self.master.app.left_frame.dataframe
        
        else:
            dataframe = self.master.tab_filtration_sort.filtration_dataframe
        
        # Если не выбран один из признаков
        if feature_x == 'Признак по X' and feature_y != 'Признак по Y':
            feature_x = None
            
        elif feature_y == 'Признак по Y' and feature_x != 'Признак по X':
            feature_y = None
            
        # Если не выбран признак разделения по цвету
        if feature_hue == 'Признак разделения':
            feature_hue = None
            
        # Удаляем предыдущий график если был
        self.ax.clear()
        
        # Строим график взависимости от выбора в меню
        if choise_graph == 'scatterplot' or choise_graph == 'lineplot':
            # Доп признаки
            feature_style = None if self.menu_graph_feature_style.get() == 'Признак стилизации' else self.menu_graph_feature_style.get()
            feature_size = None if self.menu_graph_feature_size.get() == 'Признак размера' else self.menu_graph_feature_size.get()
            choice_alpha = self.sldr_graph_choice_alpha.get()
            
            if choise_graph == 'scatterplot':
                sns.scatterplot(data=dataframe, x=feature_x, y=feature_y, hue=feature_hue,
                                style=feature_style, size=feature_size, alpha=choice_alpha)
                
            elif choise_graph == 'lineplot':
                # Выбор ориентации
                choice_orient = 'x' if self.combobox_graph_choice_orient.get() == 'Вертикальная' else 'y'
                
                sns.lineplot(data=dataframe, x=feature_x, y=feature_y, hue=feature_hue,
                             style=feature_style, size=feature_size, alpha=choice_alpha, orient=choice_orient) 
            
        elif choise_graph == 'boxplot':
            # Выбор ориентации
            choice_orient = 'x' if self.combobox_graph_choice_orient.get() == 'Вертикальная' else 'y'
            
            sns.boxplot(data=dataframe, x=feature_x, y=feature_y, hue=feature_hue, orient=choice_orient)    

        elif choise_graph == 'histplot':
            sns.histplot(data=dataframe, x=feature_x, y=feature_y, hue=feature_hue)
            
        elif choise_graph == 'barplot':
            sns.barplot(data=dataframe, x=feature_x, y=feature_y, hue=feature_hue)
        
        elif choise_graph == 'violinplot':
            sns.violinplot(data=dataframe, x=feature_x, y=feature_y, hue=feature_hue)   

        # Перерисовываем canvas
        self.canvas.draw_idle()
        
        # Активация кнопки сохранения графика после построения графика
        self.master.tab_saves.btn_save_graph_img.configure(state='normal')
        
        # Активация checkbox быстрого сохранения графика после построения графика
        self.master.tab_saves.checkbox_save_graph_img.configure(state='normal')