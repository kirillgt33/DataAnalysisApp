import customtkinter as CTk

### Вкладка <Документация> ###
class TabDocumentation(CTk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        master.add("Документация")
        
        # Блок с текстом
        self.documentation_text = CTk.CTkTextbox(master=master.tab('Документация'))
        self.documentation_text.pack(expand=True, fill='both')
        self.documentation_text.insert('end', 'Документация')
        self.documentation_text.configure(state='disabled')