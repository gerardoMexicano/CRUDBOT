import sqlite3
class Databot():
    def __init__(self):
        self.conexion=sqlite3.connect('db\\registros.db')
        self.cursor =self.conexion.cursor()

    def returtALLAltas(self):
        sql="SELECT * from alta"
        self.cursor.execute(sql)
        consulta=self.cursor.fetchall()
        return consulta

    def returtALLcopes(self):
        sql="SELECT * from cope"
        self.cursor.execute(sql)
        consulta=self.cursor.fetchall()
        return consulta
    def returtALLempresas(self):
        sql="SELECT * from empresa"
        self.cursor.execute(sql)
        consulta=self.cursor.fetchall()
        return consulta
    def returtALLsolicitudes(self):
        sql="SELECT * from solicitud"
        self.cursor.execute(sql)
        consulta=self.cursor.fetchall()
        return consulta

    def insertclientes(self,mid,alta,folio,cope,solicitud,empresa,coment):
        sql= "INSERT INTO cliente(cliente_ref, c_alta, c_folio, c_cope, c_solicitud, c_empresa, cliente_comentario) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(mid,alta,folio,cope,solicitud,empresa,coment)
        self.cursor.execute(sql)
        self.conexion.commit()

    def insertclientes2(self,mid,alta,folio,cope,solicitud,empresa,coment):
        sql= "INSERT INTO cliente2(cliente_ref, c_alta, c_folio, c_cope, c_solicitud, c_empresa, cliente_comentario) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(mid,alta,folio,cope,solicitud,empresa,coment)
        self.cursor.execute(sql)
        self.conexion.commit()

if __name__ == "__main__":
    c=Databot()
