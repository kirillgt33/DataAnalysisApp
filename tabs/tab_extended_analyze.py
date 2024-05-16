import customtkinter as CTk
import pandas as pd
import numpy as np
from pandastable import Table
from extends.blowouts_iqr_z import outliers_iqr_mod, outliers_z_score_mod

# Вкладки настроек нахождения выбросов
class BlowoutSettingsTabs(CTk.CTkTabview):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.add('Z-отклонения')
        self.add('Тьюки')
        
        # Фрейм для элементов настроек метода z
        self.frame_blowout_z = CTk.CTkFrame(master=self.tab('Z-отклонения'))
        self.frame_blowout_z.pack(pady=5)
        
        # Надпись левого порога в фрейме настроек метода z
        self.label_blowout_z_left_thresh = CTk.CTkLabel(master=self.frame_blowout_z, text='Левый порог')
        self.label_blowout_z_left_thresh.pack(pady=5)
        
        # Поле ввода значения левого порога в фрейме настроек метода z
        self.entry_blowout_z_left_thresh = CTk.CTkEntry(master=self.frame_blowout_z, state='disabled')
        self.entry_blowout_z_left_thresh.pack(pady=5)
        
        # Надпись правого порога в фрейме настроек метода z
        self.label_blowout_z_right_thresh = CTk.CTkLabel(master=self.frame_blowout_z, text='Правый порог')
        self.label_blowout_z_right_thresh.pack(pady=5)
        
        # Поле ввода значения правого порога в фрейме настроек метода z
        self.entry_blowout_z_right_thresh = CTk.CTkEntry(master=self.frame_blowout_z, state='disabled')
        self.entry_blowout_z_right_thresh.pack(pady=5)
        
        # Надпись лог масштаба в фрейме настроек метода z
        self.label_blowout_z_log_scale = CTk.CTkLabel(master=self.frame_blowout_z, text='Логарифмический масштаб')
        self.label_blowout_z_log_scale.pack(pady=5)
        
        # Combobox для выбора лог масштаба в фрейме настроек метода z
        self.combobox_blowout_z_log_scale = CTk.CTkComboBox(master=self.frame_blowout_z, values=['Да', 'Нет'], state='disabled')
        self.combobox_blowout_z_log_scale.pack(pady=5)
        
        # Фрейм для элементов настроек метода Тьюки
        self.frame_blowout_iqr = CTk.CTkFrame(master=self.tab('Тьюки'))
        self.frame_blowout_iqr.pack(pady=5)
        
        # Надпись левого порога в фрейме настроек метода Тьюки
        self.label_blowout_iqr_left_thresh = CTk.CTkLabel(master=self.frame_blowout_iqr, text='Левый порог')
        self.label_blowout_iqr_left_thresh.pack(pady=5)
        
        # Поле ввода значения левого порога в фрейме настроек метода Тьюки
        self.entry_blowout_iqr_left_thresh = CTk.CTkEntry(master=self.frame_blowout_iqr, placeholder_text='1.5')
        self.entry_blowout_iqr_left_thresh.pack(pady=5)
        
        # Надпись правого порога в фрейме настроек метода Тьюки
        self.label_blowout_iqr_right_thresh = CTk.CTkLabel(master=self.frame_blowout_iqr, text='Правый порог')
        self.label_blowout_iqr_right_thresh.pack(pady=5)
        
        # Поле ввода значения правого порога в фрейме настроек метода Тьюки
        self.entry_blowout_iqr_right_thresh = CTk.CTkEntry(master=self.frame_blowout_iqr, placeholder_text='1.5')
        self.entry_blowout_iqr_right_thresh.pack(pady=5)
        
        # Надпись лог масштаба в фрейме настроек метода Тьюки
        self.label_blowout_iqr_log_scale = CTk.CTkLabel(master=self.frame_blowout_iqr, text='Логарифмический масштаб')
        self.label_blowout_iqr_log_scale.pack(pady=5)
        
        # Combobox для выбора лог масштаба в фрейме настроек метода Тьюки
        self.combobox_blowout_iqr_log_scale = CTk.CTkComboBox(master=self.frame_blowout_iqr, values=['Да', 'Нет'], state='readonly')
        self.combobox_blowout_iqr_log_scale.set('Нет')
        self.combobox_blowout_iqr_log_scale.pack(pady=5)


   
# Отображение выбросов
class ViewBlowouts(CTk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.master = master
        
        self.minsize(600, 600)
        
        self.frame_options = CTk.CTkFrame(self)
        self.frame_options.grid(row=1, column=3, sticky='ne', padx=5)
        
        self.blowouts_switch_btn = CTk.CTkButton(self.frame_options, text='Сменить данные', width=180, corner_radius=12,
                                                 command=self.blowouts_switch)
        self.blowouts_switch_btn.grid(pady=5, padx=5)
        
        self.view_data_table = CTk.CTkLabel(self.frame_options)
        self.view_data_table.grid(pady=5)
        
        self.blowout_z_table = Table(self, dataframe=self.master.outliers_z,
                              editable=False, enable_menus=False, showstatusbar=True, showtoolbar=False)
        
        self.blowout_iqr_table = Table(self, dataframe=self.master.outliers_iqr,
                              editable=False, enable_menus=False, showstatusbar=True, showtoolbar=False)
        
    def blowouts_switch(self):
        if self.view_data_table.cget('text') == 'Выбросы метода Тьюки':
            self.blowout_iqr_table.grid_forget()
            self.blowout_z_table.show()
            self.view_data_table.configure(text='Выбросы метода z-отклонений')
        
        else:
            self.blowout_z_table.grid_forget()
            self.blowout_iqr_table.show()
            self.view_data_table.configure(text='Выбросы метода Тьюки')     




### Вкладка <Расширенный анализ> ###
class TabExtendedAnalyze(CTk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.master = master
        
        self.master.add("Расширенный анализ")
        
        # Фрейм для настроек анализа
        self.frame_settings_right = CTk.CTkFrame(master=self.master.tab('Расширенный анализ'))
        self.frame_settings_right.pack(anchor='n', side='right', fill='y', pady=5, padx=5)
        
        # Меню выбора признака для анализа
        self.menu_feature_analyze = CTk.CTkOptionMenu(master=self.frame_settings_right, width=180, state='disabled', dynamic_resizing=False,
                                                      corner_radius=12, command=self.activate_btn_checkboxs_analyze)
        self.menu_feature_analyze.set('Признак')
        self.menu_feature_analyze.pack(pady=5)
        
        # Фрейм для checkbox'ов выбора метода выбросов
        self.frame_blowout_analyze = CTk.CTkFrame(master=self.frame_settings_right)
        self.frame_blowout_analyze.pack(pady=5)
        
        # Надпись выбора метода нахождения выбросов
        self.label_blowout_analyze = CTk.CTkLabel(master=self.frame_blowout_analyze, text='Найти выбросы по методам')
        self.label_blowout_analyze.pack(pady=5)
        
        # Checkbox для нахождения выбросов по методу z
        self.checkbox_blowout_analyze_z_var = CTk.StringVar(value="off")
        self.checkbox_blowout_analyze_z = CTk.CTkCheckBox(master=self.frame_blowout_analyze, text='Z-отклонения', state='disabled',
                                                          variable=self.checkbox_blowout_analyze_z_var, onvalue='on', offvalue='off', corner_radius=12)
        self.checkbox_blowout_analyze_z.pack(anchor='w', pady=5, padx=5)
        
        # Checkbox для нахождения выбросов по методу Тьюки
        self.checkbox_blowout_analyze_iqr_var = CTk.StringVar(value="off")
        self.checkbox_blowout_analyze_iqr = CTk.CTkCheckBox(master=self.frame_blowout_analyze, text='Тьюки', state='disabled',
                                                            variable=self.checkbox_blowout_analyze_iqr_var, onvalue='on', offvalue='off', corner_radius=12)
        self.checkbox_blowout_analyze_iqr.pack(anchor='w', pady=5, padx=5)
        
        # Надпись настроек методов нахождения выбросов
        self.label_blowouts_tabs = CTk.CTkLabel(master=self.frame_blowout_analyze, text='Настройки методов')
        self.label_blowouts_tabs.pack()
        
        # Вкладки для настройки методов нахождения выбросов
        self.settings_blowouts_tabs = BlowoutSettingsTabs(master=self.frame_blowout_analyze, width=30, state='disabled')
        self.settings_blowouts_tabs.pack()
        
        # Кнопка анализа
        self.analyze_btn = CTk.CTkButton(master=self.frame_settings_right, text='Анализировать', state='disabled',
                                         width=160, command=self.analyze_extend)
        self.analyze_btn.pack(pady=5)
        
        # Кнопка для открытия окна с таблицами выбросов
        self.view_blowouts_btn = CTk.CTkButton(master=self.frame_settings_right, text='Просмотреть выбросы', state='disabled', corner_radius=12,
                                               width=160, command=self.view_blowouts)
        self.view_blowouts_btn.pack(pady=10)
        
        # TextBox для вывода статистического анализа
        self.textbox_analyze = CTk.CTkTextbox(master=self.master.tab('Расширенный анализ'), state='disabled', font=("Helvetica", 18))
        self.textbox_analyze.pack(expand=True, fill='both', pady=5)
        
    # Активация кнопки и checkbox в анализе
    def activate_btn_checkboxs_analyze(self, choice):
        # Активация checkbox для выбора методов поиска выбросов
        self.checkbox_blowout_analyze_z.configure(state='normal')
        self.checkbox_blowout_analyze_iqr.configure(state='normal')
        
        # Активация вкладок с настройками методов нахождения выбросов
        self.settings_blowouts_tabs.configure(state='normal')
        self.settings_blowouts_tabs.entry_blowout_z_left_thresh.configure(state='normal', placeholder_text='3')
        self.settings_blowouts_tabs.entry_blowout_z_right_thresh.configure(state='normal', placeholder_text='3')
        self.settings_blowouts_tabs.combobox_blowout_z_log_scale.configure(state='readonly')
        self.settings_blowouts_tabs.combobox_blowout_z_log_scale.set('Нет')
        
        # Активация кнопки анализа
        self.analyze_btn.configure(state='normal')
        
    # Вывод анализа по данным
    def analyze_extend(self):
        data = self.master.app.left_frame.dataframe
        feature = self.menu_feature_analyze.get()
        
        # Список выборов в combobox для log_scale
        combobox_answers = {'Да': True, 'Нет': False}
        
        # Проверка на ввод
        z_left = 3 if self.settings_blowouts_tabs.entry_blowout_z_left_thresh.get() == '' else float(self.settings_blowouts_tabs.entry_blowout_z_left_thresh.get())
        z_right = 3 if self.settings_blowouts_tabs.entry_blowout_z_right_thresh.get() == '' else float(self.settings_blowouts_tabs.entry_blowout_z_right_thresh.get())
        z_log_scale = combobox_answers[self.settings_blowouts_tabs.combobox_blowout_z_log_scale.get()]
        
        iqr_left = 1.5 if self.settings_blowouts_tabs.entry_blowout_iqr_left_thresh.get() == '' else float(self.settings_blowouts_tabs.entry_blowout_iqr_left_thresh.get())
        iqr_right = 1.5 if self.settings_blowouts_tabs.entry_blowout_iqr_right_thresh.get() == '' else float(self.settings_blowouts_tabs.entry_blowout_iqr_right_thresh.get())
        iqr_log_scale = combobox_answers[self.settings_blowouts_tabs.combobox_blowout_iqr_log_scale.get()]
        
        
        # Если тип данных признака не object
        try:
            quartiles = np.percentile(data[feature], [25, 50, 75])
            
            # Получение выбросов
            if self.checkbox_blowout_analyze_z.get() == 'on':
                self.outliers_z, cleaned_z = outliers_z_score_mod(data, feature, left=z_left, right=z_right, log_scale=z_log_scale)
                
                result_z = f'Число выбросов по методу Z-отклонения: {self.outliers_z.shape[0]}\n' \
                           f'Число записей без выбросов: {cleaned_z.shape[0]}\n' \
            
            else:
                result_z = ''
                self.outliers_z = pd.DataFrame()
            
            if self.checkbox_blowout_analyze_iqr.get() == 'on':
                self.outliers_iqr, cleaned_iqr = outliers_iqr_mod(data, feature, left=iqr_left, right=iqr_right, log_scale=iqr_log_scale)
                
                result_iqr = f'Число выбросов по методу Тьюки: {self.outliers_iqr.shape[0]}\n' \
                             f'Число записей без выбросов: {cleaned_iqr.shape[0]}\n' \
            
            else:
                result_iqr = ''
                self.outliers_iqr = pd.DataFrame()
            
            # Нахождение основных статистических метрик
            result_analyze_str = f"Среднее: {data[feature].mean()}\nМедиана: {data[feature].median()}\nСтандартное отклонение: {data[feature].std()}\n" \
                                 f"Минимум: {data[feature].min()}\nМаксимум: {data[feature].max()}\n" \
                                 f"Первый квартиль: {quartiles[0]}\nТретий квартиль: {quartiles[2]}\n" \
                                 f"Межквартильный размах: {quartiles[2] - quartiles[0]}\n" \
                                 f"Мода: {data[feature].mode()[0]}\nАсимметрия: {data[feature].skew()}\nЭксцесс: {data[feature].kurtosis()}\n" \
                                 '\n'            
            
            # Активация кнопки просмотра выбросов
            self.view_blowouts_btn.configure(state='normal')
            
        # Если тип данных признака не числовой    
        except Exception as e:
            result_analyze_str = 'Выбранный признак должен быть числовым'
            result_z = ''
            result_iqr = ''
            
            
        # Вставка данных в TextBox с аналитикой
        self.textbox_analyze.configure(state='normal')
        self.textbox_analyze.delete(1.0, 'end')
        self.textbox_analyze.insert('end', result_analyze_str + result_z + result_iqr)
        self.textbox_analyze.configure(state='disabled')
    
    def view_blowouts(self):
        self.blowouts_window = ViewBlowouts(master=self)
        
        if self.outliers_z.empty:
            self.blowouts_window.blowout_iqr_table.show()
            self.blowouts_window.view_data_table.configure(text='Выбросы метода Тьюки')
        
        elif not self.outliers_z.empty:
            self.blowouts_window.blowout_z_table.show()
            self.blowouts_window.view_data_table.configure(text='Выбросы метода z-отклонений')
        
        # Захват фокуса на окно
        self.blowouts_window.grab_set()
        
    # Игнор ошибки чтобы вывод таблицы работал в TabView
    def bind_all(self, sequence=None, func=None, add=None):
        # raise AttributeError("'bind_all' is not allowed, could result in undefined behavior")
        pass