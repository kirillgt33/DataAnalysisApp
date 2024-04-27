import customtkinter as CTk
import warnings
from leftframe import LeftFrame
from main_tabs import Tabs



# Игнор FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)



# Основное окно
class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        # Основные настройки окна
        self.title('DataPulse')
        #self.iconbitmap('img/Tray.ico')
        self.geometry('1150x700')
        self.minsize(1120, 600)
        
        # Цветовая тема
        CTk.set_default_color_theme('dark-blue')
        
        CTk.set_appearance_mode('system')
        
        # Левый блок и его отбражение
        self.left_frame = LeftFrame(master=self, app=self)
        self.left_frame.pack(fill='y', side='left')
        
        # Вкладки и их отображение
        self.tab_view = Tabs(master=self, app=self, anchor='nw')
        self.tab_view.pack(expand=True, fill='both', side='right')
        
        # Начальное окно
        # self.warning_window = WarningWindow(master=self)
        # self.warning_window.grab_set()
    
def on_closing():
    app.withdraw()
    app.quit()

if __name__ == '__main__':
    app = App()
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()