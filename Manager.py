import tkinter as tk
import threading
import time
import sys
from ExportExcel import *
from style import styles


from screens.Altas import Altas
from screens.Cope import Cope
from screens.Clientes import Clientes
from screens.Empresas import Empresas
from screens.Solicitudes import Solicitudes
import Bot2
 
class Manager(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.configure(background=styles.BACKGROUND)
        self.text= tk.StringVar()
        self.onoff=2
        self.bot= Bot2
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
        self.botoni=tk.Button(self,textvariable=self.text, command=self.export,**styles.STYLE,relief=tk.FLAT,activebackground=styles.BACKGROUND,activeforeground=styles.TEXT).pack(**styles.PACK)
        self.botonapa=tk.Button(self,textvariable=self.text, command=self.end,**styles.STYLE,relief=tk.FLAT,activebackground=styles.BACKGROUND,activeforeground=styles.TEXT).pack(**styles.PACK)
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
    def inibot(self):
        try:
           self.bot.iniciarbot()
        except:
            pass
    def apagabot(self):
        try:
            self.botstop()
        except:
            pass
   
    
    def botstop(self):
        self.bot.detener()
    def export(self):
        self.event=threading.Event()
        excel=threading.Thread(target=self.exportacion,args=(self.event,))
        excel.start()
    def exportacion2(self):
        func=ExportExcel()
        func.exportar()

    def exportacion(self,event):
        x=0
        func=ExportExcel()
        while True:
            if event.is_set():
                break
            time.sleep(1)
            x+=1
            var=x%60
            if (x>0 and (var==0)):
                func.exportar()
                func.eliminarregistros()
                x=0
    def end(self):
        self.event.set()





