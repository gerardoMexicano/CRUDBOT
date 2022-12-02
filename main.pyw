from Manager import *
if __name__=="__main__":
    print("Aplication Starting ... ")
    app=Manager()
    app.inibot()
    app.export()
    app.mainloop()
    app.apagabot()
    app.end()
    print("Application Closing ... ")