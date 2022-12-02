import tkinter as tk
from tkinter import Button,Entry,Label,ttk,PhotoImage
from style import styles
from tkinter import StringVar, Scrollbar, Frame, messagebox
from time import strftime
import pandas as pd
from database import  Data
from style import style
import Bot2
from screens.Mensaje import Mensaje


class Clientes(tk.Toplevel):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Clientes")
        self.nombre = StringVar()
        self.cut = StringVar()
        self.basededatos=Data()
        self.bot= Bot2
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
        tk.Button(self.frame1,text='Refrescar',**style.STYLEB,command=lambda:self.refrescar()).grid(column=2,row=1,pady=5)
        #tk.Button(self.frame1, text="Volver", command=self.volver).grid(column=2,row = 1)
        tk.Label(self.frame1,text='Respuesta a Clientes',bg='white',fg='black',font=('Kaufmann BT', 13,'bold')).grid(columnspan=2, column=0,row = 0,pady=5)
        tk.Label(self.frame1,text='Nombre',**style.STYLEL).grid(column=0,row=1,pady=5)
        tk.Label(self.frame1,text='Abreviatura',**style.STYLEL).grid(column=0,row=2,pady=5)

        tk.Entry(self.frame1,textvariable=self.nombre,**style.STYLEE).grid(column=1,row=1)
        tk.Entry(self.frame1,textvariable=self.cut,**style.STYLEE).grid(column=1,row=2)
        
        tk.Button(self.frame1,text='LISTO',**style.STYLEB,command=lambda:self.listo()).grid(column=2,row=2,pady=5,padx=5)
        tk.Button(self.frame1,text='COMUNICATE',**style.STYLEB,command=lambda:self.comunicate()).grid(column=2,row=3,pady=5,padx=5)
        tk.Button(self.frame1,text='Personalizado',**style.STYLEB,command=lambda:self.personal()).grid(column=2,row=4,pady=5,padx=5)
        tk.Button(self.frame1,text='ELIMINAR',**style.STYLEB,command=lambda:self.borrar()).grid(column=2,row=5,pady=5,padx=5)

        self.dibujarTabla()

        #tabla

    def listo(self):
        id=self.obtenerid()
        chat_id=self.basededatos.obtenerclient(id)
        txt="Su Solicitud ha sido atendida"
        self.bot.mensaje(chat_id=chat_id,mensaje=txt)
        self.borrar()



    def comunicate(self):
        id=self.obtenerid()
        chat_id=self.basededatos.obtenerclient(id)
        txt="Comunicate con tu proveedor"
        self.bot.mensaje(chat_id=chat_id,mensaje=txt)
        self.borrar()
    def personal(self): 
        id=self.obtenerid()
        self.chat_id=self.basededatos.obtenerclient(id)
        self.mensaje=tk.Toplevel
        self.mensaje.geometry("400x300")
        self.mensaje.title("Mensaje")
        self.mensaje.titulo=tk.Label(text="Mensaje al contacto")
        def passt(self):
            pass


    def limpiar_campos(self):
        self.nombre.set('')
        self.cut.set('')
      
    def dibujarTabla(self):
        self.tabla=ttk.Treeview(self.frame2,columns=(1,2,3,4,5,6,7),show="headings",height="8" )  
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="#0051C8",relief="flat",foreground="white")
        style.map("Treeview", background=[('selected', 'yellow')], foreground=[('selected', 'black')])

        self.tabla.heading(1,text="Id")
        self.tabla.heading(2,text="Referencia")
        self.tabla.heading(3,text="Alta")
        self.tabla.heading(4,text="Folio")
        self.tabla.heading(5,text="Cope")
        self.tabla.heading(6,text="Solicitud")
        self.tabla.heading(7,text="Empresa")
        self.tabla.pack(
        **styles.PACK
        )
        self.llenarregistros()
        self.tabla.bind("<<TreeviewSelect>>",self.obtener_fila)
        
    def llenarregistros(self):
        #fill list
        elements= self.basededatos.returtALLclientes()
        for i in elements:
            self.tabla.insert('',tk.END,values = i)
    
    
    
    def Eliminartabla(self):
        self.tabla.delete(*self.tabla.get_children()) 

    def agregar(self):
        nombre=self.nombre.get()
        cut=self.cut.get()
        if  nombre!= "" and cut!="":
            self.basededatos.insertaltas(nombre,cut)
            messagebox.showinfo(title="Alerta",message="se inserto correctamente")
            self.Eliminartabla()
            self.llenarregistros()
            self.limpiar_campos()
        else:
            messagebox.showinfo(title="Error",message="debes llenar los campos para guardar")
    def refrescar(self):
        self.Eliminartabla()
        self.llenarregistros()

    def obtener_fila(self,event):
        current_item= self.tabla.focus()
        if not current_item:
            return
        data = self.tabla.item(current_item)
        nombre=data["values"][1]
        cut=data["values"][2]
        self.nombre.set(nombre)
        self.cut.set(cut)
        

    def obtenerid(self):
        current_item= self.tabla.focus()
        if not current_item:
            return
        data = self.tabla.item(current_item)
        id=data["values"][0]
        return id
    def actualizar(self):
        id=self.obtenerid()
        nombre=self.nombre.get()
        cut=self.cut.get()
        self.basededatos.actualizaraltas(id,nombre,cut)
        self.limpiar_campos()
        self.refrescar()

    def borrar(self):
        id=self.obtenerid()
        self.basededatos.deleteclientes(id)
        self.limpiar_campos()
        self.refrescar()




        

        

        
    