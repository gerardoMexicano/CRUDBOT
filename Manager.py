import tkinter as tk
import threading
import time
from style import styles


from screens.Altas import Altas
from screens.Cope import Cope
from screens.Clientes import Clientes
from screens.Empresas import Empresas
from screens.Solicitudes import Solicitudes
from Bot import *
 
class Manager(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.configure(background=styles.BACKGROUND)
        self.text= tk.StringVar()
        self.onoff=2
        self.bot=recibir_mensajes
        self.text.set("Iniciarbot")
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
        self.botoni=tk.Button(self,textvariable=self.text, command=self.ibot,**styles.STYLE,relief=tk.FLAT,activebackground=styles.BACKGROUND,activeforeground=styles.TEXT).pack(**styles.PACK)

        self.botonaltas=tk.Button(
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
    
    def ibot(self):
        timer_runs=threading.Event()
        timer_runs.set()
        hilo=threading.Thread(target=self.bot,args=(timer_runs)) 
        hilo.start()
        time.sleep(10)
        timer_runs.clear()
        print("proceso detenido")


    def botes(self):
        try:
            while self.onoff==2:
                if self.onoff==2:
                    self.onoff=0
                    self.text.set("Apagar Bot")
                elif self.onoff==0:
                    hilo=threading.Thread(name="hilo",target=self.bot) 
                    hilo.start()
                    self.onoff=1
                    self.text.set("Apagar Bot")
                else:
                    
                    self.onoff=0
                    self.text.set("Iniciar Bot")
                    pass
                
        except:
           pass

            
