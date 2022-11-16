import sqlite3

class Data():
    def __init__(self):
        self.conexion=sqlite3.connect('db\\registros.db')
        self.cursor =self.conexion.cursor()

    def returtALLAltas(self):
        sql="SELECT * from alta"
        self.cursor.execute(sql)
        consulta=self.cursor.fetchall()
        return consulta

    def insertaltas(self,nombre,cut):
        sql= "INSERT INTO alta(alta_name, alta_cut) VALUES('{}', '{}')".format(nombre,cut)
        self.cursor.execute(sql)
        self.conexion.commit()
"""
if __name__ == "__main__":
    c=Data()
    c.returtALLAltas()"""