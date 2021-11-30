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
    VARIABLES
    '''
    #Contador que usaremos mas adelante.
    contador=0

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

    def getContador(self):
        return self.contador

    '''
    SETTERS
    '''

    def setContador(self, contador):
        self.contador=contador

    '''
    METODOS DE LA PROPIA CLASE
    '''

    def run(self):
        contador=self.getContador()
        contador+=1
        self.setContador(contador)
        self.indexTool()
        
    def indexTool(self):
        number=self.getContador()
        nameTool=self.getNameTool()
        if number==1:
            if nameTool == "netdiscover":
                self.insNetdiscover()
            elif nameTool == "cupp":
                self.insCupps()
            elif nameTool == "crunch":
                #self.crunch()
                pass
            elif nameTool == "delvedleak":
                self.insDelved()
            elif nameTool == "littlebrother":
                self.insLittle()
            elif nameTool == "":
                pass
            elif nameTool == "":
                pass
            elif nameTool == "":
                pass
            elif nameTool == "":
                pass
            elif nameTool == "":
                pass
        else:
            if nameTool == "netdiscover":
                self.netDiscover()
            elif nameTool == "cupp":
                self.cupp()
            elif nameTool == "crunch":
                #self.crunch()
                pass
            elif nameTool == "delvedleak":
                self.delvedleak()
            elif nameTool == "littlebrother":
                self.littlebrother()
            elif nameTool == "":
                pass
            elif nameTool == "":
                pass
            elif nameTool == "":
                pass
            elif nameTool == "":
                pass
            elif nameTool == "":
                pass    
    '''
    INSTALADORES DE LAS APLICACIONES
    '''

    #Metodo para instalar NetDiscover  
    def insNetdiscover(self):
        os.system("sudo apt-get install netdiscover")
        self.netDiscover()

    #Metodo apra instalar Cupps
    def insCupps(self):
        os.system("git clone https://github.com/Mebus/cupp.git ./ins-tools/cupp")
        self.cupp()
    
    #Metodo para instalar delvedleak
    def insDelved(self):
        os.system("git clone https://github.com/Sh4rk0-666/DelvedLeak.git ./ins-tools/delvedleak")
        #Se le de permisos de ejecucion al instalador de la aplicacion
        command="sudo chmod +x ./ins-tools/delvedleak/setup.sh"
        os.system(command)

        #Se le ejecuta el instalador de la aplicacion.
        command="./ins-tools/delvedleak/setup.sh"
        os.system(command)
        codigo='''
	except: 
		print("Por algunos inconvenientes no se puede ejecutar esta opcion, perdone las molestias.")
		Main()
            '''
        archive2="./ins-tools/delvedleak/delvedleak.py"
        with open(archive2, "a") as txt:
            txt.write(codigo)
        
        self.delvedleak()
    

    def insLittle(self):
        os.system("git clone https://github.com/lulz3xploit/LittleBrother.git ./ins-tools/littlebrother")
        #Se le de permisos de ejecucion al instalador de la aplicacion
        print("Instalando los requisitos de la aplicacion...")
        os.system("python3 -m pip install -r ./ins-tools/littlebrother/requirements.txt")
        self.littlebrother()
        



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
    
    
    
    '''
    #Metodo par ausar la herramienta de crunch
    #Problema con la herramienta es que puede tener demasiadas opciones para que se use asi a la ligera
    #Encontrar una forma tipo menu o algo que haga que se pueda hacer mas facil o lo que sea.
    
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
        #Se ejecuta la herramienta delvedleak.
        command="python3 ./ins-tools/delvedleak/delvedleak.py | tee -a " + archive
        os.system(command)

    #Metodo para LittleBrother

    def littlebrother(self):
        littlebrother=core()
        littlebrother.clearTerminal()
        #Se crea el directorio donde iran los logs
        littlebrother.exDirect("./logs/social/")
        #variable que almacena el nombre del archivo y donde ira.
        archive = "./logs/social/littlebrother-" + strftime("%Y-%m-%d-%H-%M-%S", gmtime())+".txt"
        #Se ejecuta la herramienta delvedleak.
        command="python3 ./ins-tools/littlebrother/LittleBrother.py | tee -a " + archive
        os.system(command)