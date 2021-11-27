'''
Importacion
'''
#Importaciones de 
import os


#Clase para hacer varias cosas de la instalacion. 
class core():
        
    #Este seria el constructor de la clase core
    def __init__(self):
        pass

    #Metodo para borrar la pantalla del terminal.
    def clearTerminal(self):
        os.system('clear')
    
    #Metodo para hacer una pausa del timepo que le sea necesario.
    def sleep(self, time):
        sleep='sleep ' + str(time)
        os.system(sleep)

    #Metodo para hacer lo de pulsa para continuar.
    def ptc(self):
    #os.system('read -n1 -p "Pulsa una tecla para continuar..."')
        cmd="""bash -c 'read -s -n 1 -p "Press any key to continue..."'"""
        os.system(cmd)
        
    #Metodo para comprobar y or n

    def yesOrNo(self):
        yorn=0
        while yorn!="y" or yorn!="n":
            yorn=input("Ingresa la respuesta de y/n: ")
            if yorn=="y":
                return True
                break
            elif yorn=="n":
                return False
                break
            else:
                print("Intentalo de nuevo por favor.")
    
    #Metodo para pedir un mensaje de texto y que guarde un valor.
    def intro(self, msg):
        valor=input(msg)
        return valor
    
    #Funcion para comprobar si existe un directorio o no.
    def exDirect(self, path):
        if not os.path.exists(path):
            print("Creando la carpeta " + path + " ...")
            command="mkdir -p " + path
            os.system(command)
        
            
    #Metodo para borrar los archivos de logs.
    def deletelogs (self, path):
        command="rm -frd "
        print("Borrando la carpeta " + path)
        if path == "info":
            #Mediante esta concatenacion hacemos que el comando rm este completo
            command=command + "./logs/info/"
            os.system(command)
        elif path == "dic":
            command=command + "./logs/dic/"
            os.system(command)
        elif path == "passoff":
            command=command + "./logs/passoff/"
            os.system(command)
        elif path == "passon":
            command=command + "./logs/passon/"
            os.system(command)
        elif path == "snif":
            command=command + "./logs/snif/"
            os.system(command)
        print("Borrado completado.")    
        

    #Metodo para poner un banner aleatorio en el cmd.
    def ranBanner(self, list):
        pass