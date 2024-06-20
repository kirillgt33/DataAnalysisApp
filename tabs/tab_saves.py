import customtkinter as CTk
from ctkcomponents import CTkNotification
from datetime import datetime

### Вкладка <Сохранение> ###
class TabSaves(CTk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.master = master
        
        self.master.add("Сохранение")
        
        
        # Фрейм для сохранения графика
        self.frame_save_graphic = CTk.CTkFrame(master=self.master.tab('Сохранение'))
        self.frame_save_graphic.pack(anchor='nw', pady=5)
        
        # Кнопка сохранения графика
        self.btn_save_graph_img = CTk.CTkButton(master=self.frame_save_graphic, text='Сохранить график', state='disabled', command=self.save_graphic)
        self.btn_save_graph_img.pack(side='left', pady=5)
        
        # Checkbox для выбора быстрого сохранения графика
        self.checkbox_save_graph_img_var = CTk.StringVar(value='off')
        self.checkbox_save_graph_img = CTk.CTkCheckBox(master=self.frame_save_graphic, variable=self.checkbox_save_graph_img_var, text='Быстрое сохранение',
                                                       onvalue='on', offvalue='off', state='disabled')
        self.checkbox_save_graph_img.pack(side='right', pady=5, padx=5)
        
        # Фрейм для сохранения данных
        self.frame_save_filter_df = CTk.CTkFrame(master=self.master.tab('Сохранение'))
        self.frame_save_filter_df.pack(anchor='nw', pady=5)
        
        # Кнопка сохранения данных
        self.btn_save_filter_df = CTk.CTkButton(master=self.frame_save_filter_df, text='Сохранить данные', state='disabled', command=self.save_filter_data)
        self.btn_save_filter_df.pack(side='left', pady=5)
        
        # Комбоменю выбора данных для сохранения
        self.save_filter_df_types = ['Отфильтрованные']
        self.combobox_save_filter_df = CTk.CTkComboBox(master=self.frame_save_filter_df, values=self.save_filter_df_types, state='disabled', width=180, corner_radius=12)
        self.combobox_save_filter_df.pack(side='right', pady=5, padx=5)
        
        # Кнопка сохранения данных анализа
        self.btn_save_extended_data = CTk.CTkButton(master=self.master.tab('Сохранение'), text='Сохранить данные анализа', state='disabled', command=self.save_analyze_data)
        self.btn_save_extended_data.pack(anchor='nw', pady=5)


    # Сохранение графика
    def save_graphic(self):
        if self.checkbox_save_graph_img_var.get() == 'on':
            try:
                date_time = datetime.now().strftime('%Y-%m-%d')
                fast_save_graph_name = f'{self.master.tab_graphics.menu_graph_type.get()} ({self.master.tab_graphics.menu_graph_feature_x.get()} + {self.master.tab_graphics.menu_graph_feature_y.get()}) {date_time}.png'
                self.master.tab_graphics.fig.savefig(fast_save_graph_name, format='png')
                    
                # Уведомление о успешном сохранении
                CTkNotification(self.master.app, message='Сохранение прошло успешно')
                
            except Exception as e:
                # Уведомление об ошибке при сохранении
                CTkNotification(self.master.app, message='Произошла ошибка при сохранении', state='error')
            
        else:
            file_path = CTk.filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")], initialfile="График.png")
            
            if file_path:
                try:
                    self.master.tab_graphics.fig.savefig(file_path, format='png')

                    # Уведомление о успешном сохранении
                    CTkNotification(self.master.app, message='Сохранение прошло успешно')
            
                except Exception as e:
                    # Уведомление об ошибке при сохранении
                    CTkNotification(self.master.app, message='Произошла ошибка при сохранении', state='error')
                    
    # Сохранение данных
    def save_filter_data(self):
        file_path = CTk.filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv"),
                                                                                         ("Excel files", "*.xlsx"),
                                                                                         ("HTML files", "*.html")])
        # Если пользователь выбрал файл
        if file_path:
            try:
                if self.combobox_save_filter_df.get() == 'Отфильтрованные':
                    save_data = self.master.tab_filtration_sort.filtration_dataframe
                    
                elif self.combobox_save_filter_df.get() == 'Отфильтрованные и отсортированные':
                    save_data = self.master.tab_filtration_sort.sorted_dataframe
                    
                if file_path.endswith('.csv'):
                    # Сохраняем данные в CSV-файл
                    save_data.to_csv(file_path, index=False)
                
                elif file_path.endswith('.xlsx'):
                    # Сохраняем данные в Excel-файл
                    save_data.to_excel(file_path, index=False)
                    
                elif file_path.endswith('.html'):
                    # Сохраняем данные в Html-файл
                    save_data.to_html(file_path, index=False)
                    
                # Уведомление о успешном сохранении
                CTkNotification(self.master.app, message='Сохранение прошло успешно')
                    
            except Exception as e:
                # Уведомление об ошибке при сохранении
                CTkNotification(self.master.app, message='Произошла ошибка', state='error')
                
    def save_analyze_data(self):
        file_path = CTk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("TXT files", "*.txt")])
        
        data = self.master.tab_extended_analyze.textbox_analyze.get(1.0, 'end')
        
        # Если пользователь выбрал файл
        if file_path:
            try:
                if file_path.endswith('.txt'):
                    # Открываем файл для записи (режим 'w')
                    with open(file_path, 'w') as file:
                        # Записываем текст из переменной в файл
                        file.write(data)
                    
                # Уведомление о успешном сохранении
                CTkNotification(self.master.app, message='Сохранение прошло успешно')
                    
            except Exception as e:
                # Уведомление об ошибке при сохранении
                CTkNotification(self.master.app, message='Произошла ошибка', state='error')