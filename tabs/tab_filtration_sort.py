import customtkinter as CTk
from pandastable import Table, TableModel
from extends.check_on_float import is_numeric_with_dots

### Вкладка <Фильтрация и сортировка> ###
class TabFiltrationSort(CTk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.master = master
        
        self.master.add("Фильтрация и сортировка")
        
        # Добавление таблицы и отображение
        self.df_table_filter = Table(self.master.tab("Фильтрация и сортировка"),
                              editable=False, enable_menus=False, showstatusbar=True, showtoolbar=False)
        self.df_table_filter.show()
        
        # Фрейм для фреймов фильтрации и сортировки
        self.frame_filter_sort = CTk.CTkFrame(master=self.master.tab("Фильтрация и сортировка"))
        self.frame_filter_sort.grid(row=1, column=3, sticky='ne')
        
        # Фрейм фильтрации
        self.frame_filters = CTk.CTkFrame(master=self.frame_filter_sort)
        self.frame_filters.grid(row=0, padx=5, pady=10)
        
        # Надпись фильтрации
        self.label_filter = CTk.CTkLabel(master=self.frame_filters, text='Фильтрация')
        self.label_filter.grid(row=0, pady=5)
        
        # Меню выбора признака для фильтрации
        self.menu_feature_filter = CTk.CTkOptionMenu(master=self.frame_filters, width=180, state='disabled', dynamic_resizing=False,
                                                     command=self.get_feature_value, corner_radius=12)
        self.menu_feature_filter.set('Признак')
        self.menu_feature_filter.grid(row=1, pady=5, padx=5)
        
        # Меню выбора значения признака для фильтрации
        self.menu_feature_filter_value = CTk.CTkOptionMenu(master=self.frame_filters, width=180, state='disabled', dynamic_resizing=False,
                                                           command=lambda x: self.filter_apply_btn.configure(state='normal'),
                                                           corner_radius=12)
        self.menu_feature_filter_value.set('Значение')
        self.menu_feature_filter_value.grid(row=2, pady=5)
        
        # Поле ручного ввода значения признака для фильтрации 
        self.entry_feature_filter_value = CTk.CTkEntry(master=self.frame_filters, width=180, placeholder_text='Значение')
        
        # Фрейм выбора условия фильтрации
        self.condition_filter_frame = CTk.CTkFrame(master=self.frame_filters)
        self.condition_filter_frame.grid(row=3, pady=5)
        
        # Словарь условий фильтрации
        self.condition_filter_values = {'Равняется': '==', 'Больше': '>', 'Меньше': '<', 'Больше или равно': '>=', 'Меньше или равно': '<='}
        
        # Надпись выбора условии фильтрации
        self.condition_filter_label = CTk.CTkLabel(master=self.condition_filter_frame, text='Условие фильтрации')
        self.condition_filter_label.grid(row=0, pady=5)
        
        # Combobox для выбора условия фильтрации
        self.combobox_filter_action = CTk.CTkComboBox(master=self.condition_filter_frame, values=list(self.condition_filter_values.keys()),
                                                      state='disabled', width=180, corner_radius=12)
        self.combobox_filter_action.grid(row=1, pady=5)
        
        # Переключение между полем для ввода и меню значения признака
        self.switch_manual_input_filter = CTk.CTkSwitch(master=self.frame_filters, text='Ручной ввод', state='disabled', command=self.switch_manual_input_filter_call,
                                                        switch_width=38, switch_height=20, border_width=0)
        self.switch_manual_input_filter.grid(sticky='w', row=4, pady=5, padx=5)
        
        # Кнопка для фильтрации и вывода dataframe
        self.filter_apply_btn = CTk.CTkButton(master=self.frame_filters, text='Применить фильтр', state='disabled', command=self.apply_filter)
        self.filter_apply_btn.grid(row=5, pady=5)
        
        # Фрейм сортировки
        self.frame_sorted = CTk.CTkFrame(master=self.frame_filter_sort)
        self.frame_sorted.grid(row=1, padx=5, pady=10)
        
        # Надпись сортировки
        self.label_sorted = CTk.CTkLabel(master=self.frame_sorted, text='Сортировка')
        self.label_sorted.grid(row=0, pady=5)
        
        # Меню выбора признака для сортировки
        self.menu_feature_sorted = CTk.CTkOptionMenu(master=self.frame_sorted, width=180, state='disabled', dynamic_resizing=False,
                                                     command=self.sorted_switch_btn_active, corner_radius=12)
        self.menu_feature_sorted.set('Признак')
        self.menu_feature_sorted.grid(row=1, pady=5, padx=5)
        
        # Выбор сортировки по убыванию
        self.switch_sort_ascending = CTk.CTkSwitch(master=self.frame_sorted, text='По убыванию', state='disabled',
                                                   switch_width=38, switch_height=20, border_width=0)
        self.switch_sort_ascending.grid(sticky='w', row=2, pady=5, padx=5)
        
        # Кнопка для сортировки и вывода dataframe
        self.sorted_apply_btn = CTk.CTkButton(master=self.frame_sorted, width=180, text='Сортировать', state='disabled', command=self.apply_sorted, corner_radius=12)
        self.sorted_apply_btn.grid(row=3, pady=5)
        
    # Применение фильтра и вывод данных в таблицу
    def apply_filter(self):
        # Выбранный признак
        filter_feature = self.menu_feature_filter.get()
        switch_value = self.switch_manual_input_filter.get()
        
        # Проверка на ручной ввод
        if switch_value == 0:
            # Выбранное значение признака
            filter_feature_value = self.menu_feature_filter_value.get()
        
        else:
            filter_feature_value = self.entry_feature_filter_value.get()
        
        dataframe = self.master.app.left_frame.dataframe
        
        # Если строка только из чисел то конвертация в int
        if filter_feature_value.isdigit():
            filter_feature_value = int(filter_feature_value)
        
        # Если строка из чисел и точек то конвертация в float
        elif is_numeric_with_dots(filter_feature_value):
            filter_feature_value = float(filter_feature_value)
        
        # Условие фильтрации
        condition_filter = self.condition_filter_values[self.combobox_filter_action.get()]
        
        if condition_filter == '==':
            # Отфильтрованный dataframe
            self.filtration_dataframe = dataframe[dataframe[filter_feature] == filter_feature_value]
        
        elif condition_filter == '>':
            # Отфильтрованный dataframe
            self.filtration_dataframe = dataframe[dataframe[filter_feature] > filter_feature_value]
        
        elif condition_filter == '<':
            # Отфильтрованный dataframe
            self.filtration_dataframe = dataframe[dataframe[filter_feature] < filter_feature_value]
            
        elif condition_filter == '>=':
            # Отфильтрованный dataframe
            self.filtration_dataframe = dataframe[dataframe[filter_feature] >= filter_feature_value]
        
        elif condition_filter == '<=':
            # Отфильтрованный dataframe
            self.filtration_dataframe = dataframe[dataframe[filter_feature] <= filter_feature_value]
            
        # Передача отфильтрованного dataframe в таблицу и её обновление
        self.df_table_filter.updateModel(TableModel(self.filtration_dataframe))
        self.df_table_filter.redraw()
        
        # Активация меню сортировки
        self.menu_feature_sorted.configure(state='normal')

        # Активация checkbox для построения на отфильтрованных данных
        self.master.tab_graphics.check_on_filterdf.configure(state='normal')
        
        # Активация кнопки сохранения отфильтрованных данных
        self.master.tab_saves.btn_save_filter_df.configure(state='normal')
        
        # Активация комбоменю выбора типа данных для сохранения
        self.master.tab_saves.combobox_save_filter_df.configure(state='readonly')
        self.master.tab_saves.combobox_save_filter_df.set(self.master.tab_saves.save_filter_df_types[0])
        
    # Активация свитча и кнопки сортировки 
    def sorted_switch_btn_active(self, choice):
        self.switch_sort_ascending.configure(state='normal')
        self.sorted_apply_btn.configure(state='normal')
    
    # Сортировка отфильтрованного dataframe и его вывод
    def apply_sorted(self):
        ascending_choice = {1: False, 0: True}
        feature = self.menu_feature_sorted.get()
        
        # Сортировка dataframe
        self.sorted_dataframe = self.filtration_dataframe.sort_values(by=feature, ascending=ascending_choice[self.switch_sort_ascending.get()])
        
        # Передача отсортированного dataframe в таблицу и её обновление
        self.df_table_filter.updateModel(TableModel(self.sorted_dataframe))
        self.df_table_filter.redraw()
        
        if len(self.master.tab_saves.save_filter_df_types) == 1:
            # Вставка отсортированных и отфильтрованных данных в combobox для выбора при сохранении данных
            self.master.tab_saves.save_filter_df_types.append('Отфильтрованные и отсортированные')
            self.master.tab_saves.combobox_save_filter_df.configure(values=self.master.tab_saves.save_filter_df_types)
        
    # Получение признака и вставка его уникальных значений в меню
    def get_feature_value(self, choice):
        # Нахождение уникальных значений признака
        uniques = sorted(list(self.master.app.left_frame.dataframe[choice].unique()))
        
        # Конвертация в str
        str_uniques = [str(value) for value in uniques]
        
        # Передача списка в меню и его активация
        self.menu_feature_filter_value.configure(state='normal', values=str_uniques)
        
        # Активация свитча выбора ручного ввода
        self.switch_manual_input_filter.configure(state='normal')

        # Активация combobox выбора условия для фильтрации и установка стандартного условия
        self.combobox_filter_action.configure(state='readonly')
        self.combobox_filter_action.set('Равняется')
        
        # Если у  признака тип данных object то условия для фильтрации не нужны
        if self.master.app.left_frame.dataframe[choice].dtype == 'object':
            self.combobox_filter_action.configure(state='disabled')
        
    # Вывод поля для ручного ввода вместо меню и наоборот
    def switch_manual_input_filter_call(self):
        if self.switch_manual_input_filter.get() == 1:
            self.menu_feature_filter_value.grid_forget()
            
            self.entry_feature_filter_value.grid(row=2, pady=5)
            
            # Активация кнопки фильтрации
            self.filter_apply_btn.configure(state='normal')
            
        else:
            self.entry_feature_filter_value.grid_forget()
            
            self.menu_feature_filter_value.grid(row=2, pady=5)

            if self.menu_feature_filter_value.get() == 'Значение':
                # Деактивация кнопки фильтрации
                self.filter_apply_btn.configure(state='disabled')