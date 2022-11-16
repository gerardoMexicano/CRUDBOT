import tkinter as tk
from style import styles

from screens.Altas import Altas

class Manager(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.configure(background=styles.BACKGROUND)
        self.title("controlador de BOT")
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        contenedor = tk.Frame(self,bg='white')
        contenedor.grid(padx=40, pady= 50,sticky="nsew")
    
        self.todos_frames= dict()




        self.init_widgets()

    