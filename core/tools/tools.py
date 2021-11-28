########################
######Comando NMAP######
########################
#Importamos la clase de tools para ahora crear los objetos
import os
from ..core import *
from ..banners import *
from ..menutxt import *
from time import gmtime, strftime


class tool():
    '''
    Constantes de clases
    '''
    command={
        "netdiscover" : "sudo apt-get install netdiscover",
        "cupp" : "git clone https://github.com/Mebus/cupp.git ./ins-tools/cupp",
        "crunch":"sudo apt-get install crunch",
        "delvedleak":"git clone https://github.com/Sh4rk0-666/DelvedLeak.git ./ins-tools/delvedleak",
        #"":"",
        #"":"",
        #"":"",
        #"":"",
        #"":"",
    }

    '''
    Constructor de clase
    '''

    def __init__(self, nameTool):
        self.nameTool= nameTool
    '''
    GETTERS
    '''
    def getNameTool(self):
        return self.nameTool
        
    def getCommand(self):
        nameTool=self.getNameTool()
        return self.command[nameTool]

    '''
    METODOS DE LA PROPIA CLASE
    '''



    #Este metodo es para comprobar si cualquier herramienta esta instalada.
    def installed(self):
        nameTool=self.getNameTool()
        path="/usr/bin/"+nameTool
        path2="/usr/local/bin/"+nameTool
        path3="/usr/local/sbin/"+nameTool
        if os.path.isfile(path) or os.path.isfile(path2) or os.path.isfile(path3):
            return True
        else:
            return False

    #Este metodo es para instalar la aplicacion que haga falta e iniciarla una vez instalada, por su defecto llama al metodo de comprobar si esta instalada
    def install(self):
        nameTool=self.getNameTool()
        command=self.getCommand()
        if self.installed():
            print("Herramienta ya instalada.")
            ############################################################importanteeeeeeeeeeeeeeeeeeee
            self.run()
        else:
            print("Instalando la aplicacion de " + nameTool)
            print("Esto puede tardar un momento, por favor espere...")
            os.system(command)
            self.run()
  

    def run(self):
        nameTool=self.getNameTool()
        
        if nameTool == "netdiscover":
            print("Iniciando el netDiscover...")
            self.netDiscover()
        elif nameTool == "cupp":
            print("Iniciando cupp...")
            self.cupp()
        elif nameTool == "crunch":
            #print("Iniciando crunch...")
            #self.crunch()
            pass
        elif nameTool == "delvedleak":
            print("Iniciando delvedleak...")
            self.delvedleak()
        elif nameTool == "littlebrother":
            print("")
            pass
        elif nameTool == "":
            print("")
            pass
        elif nameTool == "":
            print("")
            pass
        elif nameTool == "":
            print("")
            pass
        elif nameTool == "":
            print("")
            pass
        elif nameTool == "":
            print("")
            pass

    '''
    METODOS PARTICULARES DE LAS HERRAMIENTAS
    '''

    #Metodo para usar la herramienta de netdiscover
    def netDiscover(self):
        netD=core()
        netD.clearTerminal()
        print(banners.bannerNetD)
        print("¿Desea activar el modo pasivo de netDiscover?")
        print("Si lo activa este proceso tardara mucho mas pero sera mas indetectable.")
        print("Por otro lado si lo deja desactivado el proceso sera mas rapido pero disparará el nivel de trafico de la red.")
        yorn=netD.yesOrNo()
        promt=netD.prompt("netDiscover#~ ")
        #Creamos la carpeta para los logs.
        netD.exDirect("./logs/info/")
        if yorn:
            #Creamos el archivo con el siguiente nombre, lo abrimos para meterle el banner y despues le hacemos el netDiscover pasivo
            archive="./logs/info/netDiscover-passive.txt"
            os.system("touch " + archive)  
            with open(archive, "a") as txt:
                txt.write(banners.bannerNetD)
                txt.write('\n')
            command="netdiscover -pP | tee -a " + archive
            #netdiscover -r 192.168.1.0/24 -L | tee -a output.txt 
            os.system(command)
        else:
            #Creamos el archivo con el siguiente nombre, lo abrimos para meterle el banner y despues le hacemos el netDiscover de manera activa pasandole como parametro un rango.
            print("Pasa un valor de tipo (192.168.1.0/8, /16, /24)")
            value=netD.intro(promt)
            #Con esta variable del archivo guardaremos diferentes logs en diferentes archivos.
            archive = "./logs/info/netdiscover-" + strftime("%Y-%m-%d-%H-%M-%S", gmtime())+".txt"
            os.system("touch " + archive)
            #Abrimos el archivo para meter dentro el banner de la herramienta y un salto.
            with open(archive, "a") as txt:
                txt.write(banners.bannerNetD)
                txt.write('\n')
            value="netdiscover -r " + value + " -P | tee -a " + archive
            #netdiscover -r 192.168.1.0/24 -L | tee -a output.txt   
            os.system(value)
    
    # Metodo para usar la herramienta de cupp       
    def cupp(self):
        cupp=core()
        cupp.clearTerminal()
        print(banners.bannerCupp)

        #Se crea el directorio donde iran los logs
        cupp.exDirect("./logs/dic/")
        #variable que almacena el nombre del archivo y donde ira.
        archive = "./logs/dic/dictionaryCupps-" + strftime("%Y-%m-%d-%H-%M-%S", gmtime())+".txt"

        #Se ejecuta la herramienta cupss.
        command="python3 ../../ins-tools/cupp/cupp.py -i"
        os.system(command)
        #Se crea el archivo
        os.system("touch " + archive) 
        #Para el diccionario que se crea se metera en el archivo que hemos creado anteriormente
        command="cat *.txt >> " + archive 
        os.system(command)
        #Se borra el archivo que se ha creado en la carpeta de cupps
        command="rm -f *.txt"
        os.system(command)
    
    
    #Metodo par ausar la herramienta de crunch
    #Problema con la herramienta es que puede tener demasiadas opciones para que se use asi a la ligera
    #Encontrar una forma tipo menu o algo que haga que se pueda hacer mas facil o lo que sea.
    '''
    def crunch(self):
        promt="Crunch#~ "
        crunch=core()
        crunch.clearTerminal()
        print(banners.bannerCrunch)
        #
        print("Introduzca el numero de minimo de caracteres que desea meter:")
        try:
            minChar=crunch.intro(promt)
            minChar=int(minChar)
        except ValueError:
            print("Introduce un numero por favor.")
            self.crunch()
        #
        print("Introduzca el numero de maximo de caracteres que desea meter:")
        try:
            maxChar=crunch.intro(promt)
            maxChar=int(maxChar)
        except ValueError:
            print("Introduce un numero por favor.")
            self.crunch()
        
        #Se crea el directorio donde iran los logs
        crunch.exDirect("./logs/dic/")
        #variable que almacena el nombre del archivo y donde ira.
        archive = "./logs/dic/dictionaryCrunch-" + strftime("%Y-%m-%d-%H-%M-%S", gmtime())+".txt"

        commnad= "crunch"
    '''
    #Metodo para delvedleak   
        
    def delvedleak(self):
        delvedleak=core()
        delvedleak.clearTerminal()
        print(banners.bannerDelved)

        #Se crea el directorio donde iran los logs
        delvedleak.exDirect("./logs/social/")
        #variable que almacena el nombre del archivo y donde ira.
        archive = "./logs/social/delvedleak-" + strftime("%Y-%m-%d-%H-%M-%S", gmtime())+".txt"
        try:
            #Se le de permisos de ejecucion al instalador de la aplicacion
            command="sudo chmod +x ./ins-tools/delvedleak/setup.sh"
            os.system(command)

            #Se le ejecuta el instalador de la aplicacion.
            command="./ins-tools/delvedleak/setup.sh"
            os.system(command)
            delvedleak.clearTerminal()
            #Se ejecuta la herramienta delvedleak.
            command="python3 ./ins-tools/delvedleak/delvedleak.py | tee -a " + archive
            os.system(command)
            #Se crea el archivo
            os.system("touch " + archive)
        except ConnectionRefusedError:  
            print("Por algunos inconvenientes no se puede ejecutar esta opcion, perdone las molestias.")
            self.delvedleak()