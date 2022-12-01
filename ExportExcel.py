import pandas as pd
from database import  Data
from openpyxl import Workbook
from time import strftime
class ExportExcel():
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.datos=Data()


    def exportar(self):
        self.datos=Data()
        datos=self.datos.returtALLclientes2()
        """i = -1
        Clienteref,c_alta,c_folio,c_cope,c_solicitud,c_empresa,c_comentario= [],[],[],[],[],[],[]
        for dato in datos:
            i=i+1
            Clienteref=dato[i][1]
            c_alta=dato[i][2]
            c_folio=dato[i][3]
            c_cope=dato[i][4]
            c_solicitud=dato[i][5]
            c_empresa=dato[i][6]
            c_comentario=dato[i][7]"""
        fecha = str(strftime('%d-%m-%y_%H-%M-%S'))
        #datos = {Clienteref,c_alta,c_folio,c_cope,c_solicitud,c_empresa,c_comentario}
        #datos = {'clienteref':Clienteref,'c_alta':c_alta,'c_folio':c_folio,'c_cope':c_cope,'c_solicitud':c_solicitud,'c_empresa':c_empresa,'c_comentario':c_comentario}
        df = pd.DataFrame(datos,columns=['ID','CHAT_NUM','Alta','Folio','COPE','Solicitud','Empresa','Comentario' ])
        df.to_excel((f'Reportes/DATOS {fecha} .xlsx'))

    def eliminarregistros(self):
        self.datos=Data()
        self.datos.eliminarregiclien2()


if __name__ == "__main__":
    print("inicio")
    c=ExportExcel()
    
    c.exportar()
    c.eliminarregistros()
    print("fin")





