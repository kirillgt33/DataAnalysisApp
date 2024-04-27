import customtkinter as CTk

# Окно настроек
class OptionsWindow(CTk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title('Настройки')
        self.geometry("600x500")

        # Надпись масштаба интерфейса
        self.scaling_label = CTk.CTkLabel(self, text='Масштаб интерфейса:')
        self.scaling_label.pack()
        
        # Меню выбора масштаба интерфейса
        self.scaling_optionmenu = CTk.CTkOptionMenu(self, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionmenu.set(str(round(CTk.ScalingTracker.get_widget_scaling(self.scaling_optionmenu)*100)) + '%')
        self.scaling_optionmenu.pack()
        
    # Смена масштаба интерфейса
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        CTk.set_widget_scaling(new_scaling_float)