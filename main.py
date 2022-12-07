from Manager import *#importamos toda la clase manager que es el cerebro de nuestro aplicacion y controla los porcesos 
if __name__=="__main__":
    #esta clase es para tener un boton de inicio de los procesos  que mientras la palicacion se ejecuta deben estar ejecutandose 
    
    print("Aplication Starting ... ")

    app=Manager()#iniciamos la clase en una variable local para poder usarla aqui
    app.inibot()#iniccia el bot
    app.export()#inicia un proceso que exporta el bot
    app.mainloop()#el CRUD de la aplicacion para controlar registros y emitir respuestas
    app.apagabot()#apaga el bot
    app.end()#apaga la exportacion de excel
    print("Application Closing ... ")