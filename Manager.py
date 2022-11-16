import tkinter as tk
from style import styles

from screens.Altas import Altas

class Manager(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.configure(background=styles.BACKGROUND)
        self.init_widgets()

    def init_widgets(self):
        self.title("controlador de BOT")
        container= tk.Frame(self)
        container.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )
        container.configure(
            background=styles.BACKGROUND
        )
        tk.Label(
            self,
            text="Bienvenido al controlador",
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )
        tk.Button(
            self,
            text="IniciarBot",
            command=lambda: print("has clicado  iniciar bot"),
            **styles.STYLE, 
            relief=tk.FLAT, 
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )

        tk.Button(
            self,
            text="Altas",
            command=self.camb_altas,
            **styles.STYLE, 
            relief=tk.FLAT, 
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )
        tk.Button(
            self,
            text="COPE",
            command=lambda: print("has clicado  iniciar bot"),
            **styles.STYLE, 
            relief=tk.FLAT, 
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )
        tk.Button(
            self,
            text="Solicitud",
            command=lambda: print("has clicado  iniciar bot"),
            **styles.STYLE, 
            relief=tk.FLAT, 
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )
        tk.Button(
            self,
            text="Empresas",
            command=lambda: print("has clicado  iniciar bot"),
            **styles.STYLE, 
            relief=tk.FLAT, 
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )
        tk.Button(
            self,
            text="Clientes",
            command=lambda: print("has clicado  iniciar bot"),
            **styles.STYLE, 
            relief=tk.FLAT, 
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )
        
    def camb_altas(self):
        self.altas=Altas()
       

    def camb_cope(self):
        pass