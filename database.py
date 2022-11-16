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

    def actualizaraltas(self,ref,nombre,cut):
        sql="UPDATE alta set alta_id ='{}',alta_name = '{}',alta_cut ='{}' WHERE alta_id = '{}'".format(ref,nombre,cut,ref)
        self.cursor.execute(sql)
        self.conexion.commit()

    def deletealtas(self,ref):
        sql="DELETE from alta where alta_id = '{}'".format(ref)
        self.cursor.execute(sql)
        self.conexion.commit()

    def returtALLcopes(self):
        sql="SELECT * from cope"
        self.cursor.execute(sql)
        consulta=self.cursor.fetchall()
        return consulta

    def insertcopes(self,nombre,cut):
        sql= "INSERT INTO cope(cope_name, cope_cut) VALUES('{}', '{}')".format(nombre,cut)
        self.cursor.execute(sql)
        self.conexion.commit()

    def actualizarcopes(self,ref,nombre,cut):
        sql="UPDATE cope set cope_id ='{}',cope_name = '{}',cope_cut ='{}' WHERE cope_id = '{}'".format(ref,nombre,cut,ref)
        self.cursor.execute(sql)
        self.conexion.commit()

    def deletecopes(self,ref):
        sql="DELETE from cope where cope_id = '{}'".format(ref)
        self.cursor.execute(sql)
        self.conexion.commit()
    
    
    def returtALLempresas(self):
        sql="SELECT * from empresa"
        self.cursor.execute(sql)
        consulta=self.cursor.fetchall()
        return consulta

    def insertempresas(self,nombre,cut):
        sql= "INSERT INTO empresa(empresa_name, empresa_cut) VALUES('{}', '{}')".format(nombre,cut)
        self.cursor.execute(sql)
        self.conexion.commit()

    def actualizarempresas(self,ref,nombre,cut):
        sql="UPDATE empresa set empresa_id ='{}',empresa_name = '{}',empresa_cut ='{}' WHERE empresa_id = '{}'".format(ref,nombre,cut,ref)
        self.cursor.execute(sql)
        self.conexion.commit()

    def deleteempresas(self,ref):
        sql="DELETE from empresa where empresa_id = '{}'".format(ref)
        self.cursor.execute(sql)
        self.conexion.commit()

    
    def returtALLsolicitudes(self):
        sql="SELECT * from solicitud"
        self.cursor.execute(sql)
        consulta=self.cursor.fetchall()
        print(consulta)
        return consulta

    def insertsolicitudes(self,nombre,cut):
        sql= "INSERT INTO solicitud(solicitud_name, solicitud_cut) VALUES('{}', '{}')".format(nombre,cut)
        self.cursor.execute(sql)
        self.conexion.commit()

    def actualizarsolicitudes(self,ref,nombre,cut):
        sql="UPDATE solicitud set solicitud_id ='{}',solicitud_name = '{}',solicitud_cut ='{}' WHERE solicitud_id = '{}'".format(ref,nombre,cut,ref)
        self.cursor.execute(sql)
        self.conexion.commit()

    def deletesolicitudes(self,ref):
        sql="DELETE from solicitud where solicitud_id = '{}'".format(ref)
        self.cursor.execute(sql)
        self.conexion.commit()



if __name__ == "__main__":
    c=Data()
    c.returtALLsolicitudes()