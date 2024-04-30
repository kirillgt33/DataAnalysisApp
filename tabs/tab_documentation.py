import customtkinter as CTk

# ANSI escape codes для цветов текста
class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'



### Вкладка <Документация> ###
class TabDocumentation(CTk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        master.add("Документация")
        
        # Блок с текстом
        self.documentation_text = CTk.CTkTextbox(master=master.tab('Документация'))
        self.documentation_text.pack(expand=True, fill='both')
        
        # Создание тегов для цвета текста
        self.documentation_text.tag_config("red", foreground="red")
        self.documentation_text.tag_config("green", foreground="green")
        self.documentation_text.tag_config("blue", foreground="blue")
        self.documentation_text.tag_config("yellow", foreground="yellow")
        
        # Документация
        self.documentation_text.insert('end', 'Перед началом работы необходимо слева нажать кнопку ')
        self.documentation_text.insert('end', 'Загрузить ', 'yellow')
        self.documentation_text.insert('end', 'после чего нужно выбрать формат файла данных: ')
        self.documentation_text.insert('end', '.CSV ', 'green')
        self.documentation_text.insert('end', 'или ')
        self.documentation_text.insert('end', '.XLSX\n', 'green')
        self.documentation_text.insert('end', 'Вкладка ')
        self.documentation_text.insert('end', '"Обзор данных"', 'blue')
        self.documentation_text.insert('end', ': С помощью таблицы можно просмотреть загруженные данные, также в правом нижнем углу расположились ')
        self.documentation_text.insert('end', 'элементы ', 'yellow')
        self.documentation_text.insert('end', 'для управления шириной столбцов и масштабом отображения таблицы.\n')
        self.documentation_text.insert('end', 'Вкладка ')
        self.documentation_text.insert('end', '"Графики и визуализация"', 'blue')
        self.documentation_text.insert('end', ': Для создания графика необходимо выбрать обязательные параметры такие как ')
        self.documentation_text.insert('end', 'Тип графика', 'yellow')
        self.documentation_text.insert('end', ' , ')
        self.documentation_text.insert('end', 'Признак по X', 'yellow')
        self.documentation_text.insert('end', ' и ')
        self.documentation_text.insert('end', 'Признак по Y', 'yellow')
        self.documentation_text.insert('end', '. Остальные параметры являются необязательными, но при их использовании расширяется информативность графика. ')
        self.documentation_text.insert('end', 'Строить графики на отфильтрованных данных будет возможно только после фильтрации данных на вкладке ')
        self.documentation_text.insert('end', '"Фильтрация и сортировка"', 'blue')
        self.documentation_text.insert('end', '.\n')
        self.documentation_text.insert('end', 'Вкладка ')
        self.documentation_text.insert('end', '"Фильтрация и сортировка"', 'blue')
        self.documentation_text.insert('end', ': Имеется таблица для вывода отфильтрованных и отсортированных данных. Выбирается признак а затем его значение, ')
        self.documentation_text.insert('end', 'после чего можно выбрать условие фильтрации и отфильтровать данные. ')
        self.documentation_text.insert('end', 'Так же стоит сразу обратить внимание что можно вводить значение признака самостоятельно с помощью переключателя ')
        self.documentation_text.insert('end', 'Ручной ввод', 'yellow')
        self.documentation_text.insert('end', '. Обратите внимание и на то что условие фильтрации можно выбрать если тип данных признака ')
        self.documentation_text.insert('end', 'числовой', 'green')
        self.documentation_text.insert('end', '. При строковом же типе данных условие фильтрации может быть только - ')
        self.documentation_text.insert('end', 'равняется', 'green')
        self.documentation_text.insert('end', '.\n')
        self.documentation_text.insert('end', 'Вкладка ')
        self.documentation_text.insert('end', '"Расширенный анализ"', 'blue')
        self.documentation_text.insert('end', ': Нахождение статистических данных и выбросов, можно настроить пороги у методов нахождения выбросов.\n')
        self.documentation_text.insert('end', 'Вкладка ')
        self.documentation_text.insert('end', '"Сохранение"', 'blue')
        self.documentation_text.insert('end', ': Можно сохранять графики, отфильтрованные и отсортированные данные. Есть возможность быстрого сохранения графика, ')
        self.documentation_text.insert('end', 'то есть без открытия диалогово окна.\n')
        self.documentation_text.insert('end', '"Настройки"', 'blue')
        self.documentation_text.insert('end', ': Выбор масштаба интерфейса приложения.\n')
        self.documentation_text.insert('end', '"Выбор темы"', 'blue')
        self.documentation_text.insert('end', ': По умолчанию устанавливается системная тема, можно выбрать между светлой и темной.\n')
        
        self.documentation_text.configure(state='disabled')