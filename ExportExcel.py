import pandas as pd #libreria utilizada para generar excel teine mas funciones
from database import  Data #importamos las consultas sql
from openpyxl import Workbook 
from time import strftime # importar una funcion de tiempo

#creamos la clase para que pueda ser llamada e instanciada dedesde cualquier lugar
class ExportExcel():
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.datos=Data()
        #inicailiza estos datos seran utilizados en cualquier lugar 

    def exportar(self):
        self.datos=Data()
        datos=self.datos.returtALLclientes2()
        fecha = str(strftime('%d-%m-%y_%H-%M-%S'))
        #datos = {Clienteref,c_alta,c_folio,c_cope,c_solicitud,c_empresa,c_comentario}
        #datos = {'clienteref':Clienteref,'c_alta':c_alta,'c_folio':c_folio,'c_cope':c_cope,'c_solicitud':c_solicitud,'c_empresa':c_empresa,'c_comentario':c_comentario}
        df = pd.DataFrame(datos,columns=['ID','CHAT_NUM','Alta','Folio','COPE','Solicitud','Empresa','Comentario' ]) #datos
        df.to_excel((f'Reportes/DATOS {fecha} .xlsx'))#ubicacion

        #crea el formato excel que se pidio y lo export

    def eliminarregistros(self):
        self.datos=Data()
        self.datos.eliminarregiclien2()
        #elimina los datos de los la base de datos para que no haya registros duplicados

"""
if __name__ == "__main__":
    print("inicio")
    c=ExportExcel()
    
    c.exportar()
    c.eliminarregistros()
    print("fin")
"""




