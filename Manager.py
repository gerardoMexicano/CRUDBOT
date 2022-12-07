import tkinter as tk #libreria para creacion de interfaz 
import threading #libreria para ejecutar multihilos
import time #libreria tiempo
import sys
from ExportExcel import * #libreria que generar nuestros archivos con el formato creado en este
from style import styles #importa una serie de estilos para su uso practico 

#importa las vista  interfaz graficas creada con tkinter 
from screens.Altas import Altas
from screens.Cope import Cope
from screens.Clientes import Clientes
from screens.Empresas import Empresas
from screens.Solicitudes import Solicitudes

#importa el codigo del bot 
import Bot2
 
class Manager(tk.Tk):
    #inicializa todo el sistema bot
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.configure(background=styles.BACKGROUND)
        self.text= tk.StringVar()
        self.onoff=2
        self.bot= Bot2
        self.text.set("Iniciarbot")
        self.init_widgets()# sejecuta toda la interfaz del programa se encuentra dentro de esta funcion


    def init_widgets(self):
        self.title("controlador de BOT")#titulo encabezado
        container= tk.Frame(self)#se genera el frame principal
        container.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )
        container.configure(
            background=styles.BACKGROUND
        )
        #etiqueta contiene el titulo
        tk.Label(
            self,
            text="Bienvenido al controlador",
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )
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
        #botones tkinter
        tk.Button(
            self,
            text="COPE",
            command=self.camb_cope,
            **styles.STYLE, #desempaquetado del estilo
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
    
    #funciones para generar nuevas ventanas  por cada una una funcion
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
    
    #funcion de prueba
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
    #funcion que inicia al bot
    def inibot(self):
        try:
            #en el archivo bot existe una funcion que debe ejecutarse para que que este se inicie es lo que realiza
           self.bot.iniciarbot()
        except:
            pass

    #apaga al bot llamando una funcion del clase bot que lo hace
    def apagabot(self):
        try:
            self.botstop()
        except:
            pass
    def botstop(self):
        self.bot.detener()

    #este genera un hilo nuevo donde se ejcutara la funcion de exportar datos
    def export(self):
        self.event=threading.Event()
        excel=threading.Thread(target=self.exportacion,args=(self.event,))
        excel.start()
    #genera  los reportes llamando a la clase Exportexcel los genera cada tiempo que puede determinarse
    def exportacion(self,event):
        x=0
        func=ExportExcel()
        while True:
            if event.is_set():#permite finalizar el hilo
                break#
            time.sleep(1)
            x+=1
            var=x%1800 #tiempo entre cada reporte se genere
            if (x>0 and (var==0)):
                func.exportar()
                func.eliminarregistros()
                x=0
    #finaliza el hilo de tal manera que cerrando la aplicacion esta deja de generar reportes
    def end(self):
        self.event.set()





