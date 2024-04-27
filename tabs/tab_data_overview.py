import customtkinter as CTk
from pandastable import Table

### Вкладка <Обзор Данных> ###
class TabDataOverView(CTk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        master.add("Обзор данных")
        
        # Добавление таблицы и отображение
        self.df_table = Table(master.tab("Обзор данных"),
                              editable=False, enable_menus=False, showstatusbar=True, showtoolbar=False)
        self.df_table.show()
        
        
    
    
    
