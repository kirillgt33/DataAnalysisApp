import customtkinter as CTk

#
class WarningWindow(CTk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title('Внимание')
        self.geometry("600x500")

        self.label = CTk.CTkLabel(self, text="Внимание")
        self.label.pack(padx=20, pady=20)