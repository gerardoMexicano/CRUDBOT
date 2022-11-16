import tkinter as tk
from tkinter import Button,Entry,Label,ttk,PhotoImage
from style import styles
from tkinter import StringVar, Scrollbar, Frame, messagebox
from conexion_sqlite import Comunicacion
from time import strftime
import pandas as pd
from style import style


class Altas(tk.Toplevel):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Altas")
        self.nombre = StringVar()
        self.cut = StringVar()
        self.init_widgets()


    def init_widgets(self):
        #Frames
        self.frame1=tk.Frame(self)
        self.frame2=tk.Frame(self)
        self.frame1.config(bg="white")
        self.frame1.config(width=800,height=200)
        self.frame1.columnconfigure([0,1,2], weight=1)
        self.frame1.rowconfigure([0,1,2,3,4,5], weight=1)
        self.frame1.pack(fill="both",expand=1)
        self.frame2.config(bg="white")
        self.frame2.config(width=800,height=300)
        self.frame2.pack(fill="both",expand=1)

        # primer frame
        tk.Label(self.frame1,text='opciones',bg='white',fg='black',font=('Kaufmann BT', 13,'bold')).grid(column=2,row = 0)
        tk.Button(self.frame1,text='Refrescar',**style.STYLEB,command=lambda:print("REFRESCAR")).grid(column=2,row=1,pady=5)
        #tk.Button(self.frame1, text="Volver", command=self.volver).grid(column=2,row = 1)
        tk.Label(self.frame1,text='Agregar y Actualizar datos',bg='white',fg='black',font=('Kaufmann BT', 13,'bold')).grid(columnspan=2, column=0,row = 0,pady=5)
        tk.Label(self.frame1,text='Nombre',**style.STYLEL).grid(column=0,row=1,pady=5)
        tk.Label(self.frame1,text='Abreviatura',**style.STYLEL).grid(column=0,row=2,pady=5)

        tk.Entry(self.frame1,textvariable=self.nombre,**style.STYLEE).grid(column=1,row=1)
        tk.Entry(self.frame1,textvariable=self.cut,**style.STYLEE).grid(column=1,row=2)
        
        tk.Button(self.frame1,text='AÑADIR DATOS',**style.STYLEB,command=lambda:print("Añadir datos")).grid(column=2,row=2,pady=5,padx=5)
        tk.Button(self.frame1,text='LIMPIAR CAMPOS',**style.STYLEB,command=lambda:print("Limpiar campos")).grid(column=2,row=3,pady=5,padx=5)
        tk.Button(self.frame1,text='ACTUALIZAR',**style.STYLEB,command=lambda:print("Actualizar")).grid(column=2,row=4,pady=5,padx=5)
        tk.Button(self.frame1,text='ELIMINAR',**style.STYLEB,command=lambda:print("Eliminar")).grid(column=2,row=5,pady=5,padx=5)


        #tabla
        self.tabla=ttk.Treeview(self.frame2,
        columns=("col1","col2")
        )  
        self.tabla.heading("#0",text="Id")
        self.tabla.heading("col1",text="Nombre")
        self.tabla.heading("col2",text="Abreviatura")
        self.tabla.pack(
        **styles.PACK
        )

      
        

        
    