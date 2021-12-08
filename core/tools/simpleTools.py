'''
Importacion
'''
import os
from ..core import *
from ..banners import *
#import pyshorteners
'''
Clases
'''
#Clase para hacer las diferentes herramientas.
class simpleTool():

    #Este es el constructor de la clase tool.
    def __init__(self):
        pass

#Funcion para el ping
    def ping(self):
        ping=core()
        ping.clearTerminal()
        print(banners.bannerPing)
        print("Desea guardar la informacion de este comando en un archivo¿?")
        yorn=ping.yesOrNo()
        promt=ping.prompt("Ping#~ ")
        value=ping.intro(promt)
        #Con esta variable del archivo guardaremos diferentes logs en diferentes archivos.
        archive="./logs/info/ping-to-" + value + ".txt"
        if yorn:
            ping.exDirect("./logs/info/")
            os.system("touch " + archive)
            with open(archive, "a") as txt:
                    txt.write(banners.bannerPing)
                    txt.write('\n')
            parametros="-c 5 " + value + " | tee -a " + archive
            parametros="ping " + parametros
            os.system(parametros)
        else:
            parametros="-c 5 " + value
            parametros="ping " + parametros
            os.system(parametros)

#Funcion para el whois
    def whois(self):
        whois=core()
        whois.clearTerminal()
        print(banners.bannerWhois)
        print("¿Desea guardar la informacion de este comando en un archivo?")
        yorn=whois.yesOrNo()
        promt=whois.prompt("Whois#~ ")
        value=whois.intro(promt)
        #Con esta variable del archivo guardaremos diferentes logs en diferentes archivos.
        archive="./logs/info/whois-to-" + value + ".txt"
        if yorn:
            whois.exDirect("./logs/info/")
            os.system("touch " + archive)
            with open(archive, "a") as txt:
                    txt.write(banners.bannerWhois)
                    txt.write('\n')
            value="whois " + value + " | tee -a " + archive
            os.system(value)
        else:
            value="whois " + value
            os.system(value)

#Funcion para el trace
    def trace(self):
        trace=core()
        trace.clearTerminal()
        print(banners.bannerTraccer)
        print("¿Desea guardar la informacion de este comando en un archivo?")
        yorn=trace.yesOrNo()
        promt=trace.prompt("Trace#~ ")
        value=trace.intro(promt)
        #Con esta variable del archivo guardaremos diferentes logs en diferentes archivos.
        archive="./logs/info/trace-to-" + value + ".txt"
        if yorn:
            trace.exDirect("./logs/info/")
            os.system("touch " + archive)
            with open(archive, "a") as txt:
                    txt.write(banners.bannerTraccer)
                    txt.write('\n')
            value="traceroute " + value + " | tee -a " + archive
            os.system(value)
        else:
            value="traceroute " + value
            os.system(value)


#Funcion para el nslookup
    def nslookup(self):
        lnsl="-type=ALL "
        nslookup=core()
        nslookup.clearTerminal()
        print(banners.bannerNslookup)
        print("¿Desea guardar la informacion de este comando en un archivo?")
        yorn=nslookup.yesOrNo()
        promt=nslookup.prompt("Nslookup#~ ")
        value=nslookup.intro(promt)
        #Con esta variable del archivo guardaremos diferentes logs en diferentes archivos.
        archive="./logs/info/nslookup-to-" + value + ".txt"
        os.system("touch " + archive)
        #Bucle para hacerle todos los tipos de nslookup al value.
        
        if yorn:
            nslookup.exDirect("./logs/info/")
            os.system("touch " + archive)
            with open(archive, "a") as txt:
                txt.write(banners.bannerNslookup)
                txt.write('\n')
            value="nslookup " + lnsl + value + " | tee -a " + archive
            os.system(value)
        else:
            value="nslookup " + lnsl + value 
            os.system(value)

#Funcion para la mezcla de 4 comandos
    def allinone(self):
        pwtn=["ping -c 5 ", "whois ", "traceroute ", "nslookup -type=ALL "]
        bannerpwtn=[banners.bannerPing, banners.bannerWhois, banners.bannerTraccer, banners.bannerNslookup]
        allinone=core()
        #Para crear el directorio de logs en caso de que no estuviera.
        allinone.exDirect("./logs/info/")
        promt=allinone.prompt("Ping-Whois-Trace-Nslookup#~ ")
        value=allinone.intro(promt)
        #Con esta variable del archivo guardaremos diferentes logs en diferentes archivos.
        archive="./logs/info/pwtn-to-" + value + ".txt"
        os.system("touch " + archive)
        for x in range(4):
            command=pwtn[x] + value + " | tee -a " + archive
            #Con el with open abrimos el archivo y le metemos el banner antes de que haga el comando.
            with open(archive, "a") as txt:
                txt.write(bannerpwtn[x])
                txt.write('\n')
            print("Este proceso puede tardar un momento espere...")
            os.system(command)
        print("Ya puedes consultar el fichero " + archive + " en la carpeta de logs")

    '''
    def urlShortener(self):
        urlShortener=core()
        urlShortener.exDirect("./logs/analysis/")
        promt=urlShortener.prompt("UrlShortener#~ ")
    '''
    