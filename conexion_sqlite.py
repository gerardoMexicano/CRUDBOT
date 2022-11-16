import sqlite3

class Comunicacion():
    def __init__(self):
        self.conexion=sqlite3.connect('db\\registros.db')

    def inserta_datos_al(self,nombre,cut):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO alta (alta_name, alta_cut)
        VALUES('{}','{}')'''.format(nombre,cut)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    def mostrar_datos_al(self):
        cursor = self.conexion.cursor()
        bd= "SELECT * FROM alta "
        cursor.execute(bd)
        altas= cursor.fetchall()
        return altas

    def elimina_datos_al(self,nombre):
        cursor = self.conexion.cursor()
        bd = '''DELETE FROM alta WHERE alta_id = '{}' '''.format(nombre)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    def actualizar_datos_al(self,id,nombre,cut):
        cursor = self.conexion.cursor()
        bd = '''UPDATE alta SET alta_id = '{}' , alta_cut = '{}' 
        WHERE  alta_id = '{}' '''.format(nombre,cut,id)
        cursor.execute(bd)
        alta = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return cursor
