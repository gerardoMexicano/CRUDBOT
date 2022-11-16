import tkinter as tk
from style import styles

from screens.Altas import Altas
from screens.Cope import Cope
from screens.Clientes import Clientes
from screens.Empresas import Empresas
from screens.Solicitudes import Solicitudes
 
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
            command=self.camb_cope,
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
            command=self.camb_solicitud,
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
            command=self.camb_empresa,
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
            command=self.camb_clientes,
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
        self.cope=Cope()

    def camb_empresa(self):
        self.empresa=Empresas()

    def camb_solicitud(self):
        self.solicitud=Solicitudes()

    def camb_clientes(self):
        self.clientes=Clientes()