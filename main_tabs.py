import customtkinter as CTk
from tabs.tab_data_overview import TabDataOverView
from tabs.tab_graphics import TabGraphics
from tabs.tab_filtration_sort import TabFiltrationSort
from tabs.tab_extended_analyze import TabExtendedAnalyze
from tabs.tab_saves import TabSaves
from tabs.tab_documentation import TabDocumentation



# Вкладки
class Tabs(CTk.CTkTabview):
    def __init__(self, app, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.app = app

        # Создание вкладок
        self.tab_data_overview = TabDataOverView(master=self)
        self.tab_graphics = TabGraphics(master=self)
        self.tab_filtration_sort = TabFiltrationSort(master=self)
        self.tab_extended_analyze = TabExtendedAnalyze(master=self)
        self.tab_saves = TabSaves(master=self)
        self.tab_documentation = TabDocumentation(master=self)
 
    # Игнор ошибки чтобы вывод таблицы работал в TabView
    def bind_all(self, sequence=None, func=None, add=None):
        # raise AttributeError("'bind_all' is not allowed, could result in undefined behavior")
        pass