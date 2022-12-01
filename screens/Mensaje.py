import tkinter as tk
from tkinter import Button,Entry,Label,ttk,PhotoImage
from style import styles
from tkinter import StringVar, Scrollbar, Frame, messagebox
from time import strftime
import pandas as pd
from database import  Data
from style import style

class Mensaje(tk.Toplevel):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Mensaje")
        


