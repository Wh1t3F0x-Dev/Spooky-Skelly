#!/bin/bash
#Instalador de Spooky-Skelly
#Necesita permisos de ejecucion y debe ejecutarse para empezar la instalacion

clear

echo "
 _____                 _           _____  _         _  _      
|   __| ___  ___  ___ | |_  _ _   |   __|| |_  ___ | || | _ _ 
|__   || . || . || . || '_|| | |  |__   || '_|| -_|| || || | |
|_____||  _||___||___||_,_||_  |  |_____||_,_||___||_||_||_  |
       |_|                 |___|                         |___|

 ___               _            _   _             
|_ _|  _ _    ___ | |_   __ _  | | | |  ___   _ _ 
 | |  | ' \  (_-< |  _| / _' | | | | | / -_) | '_|
|___| |_||_| /__/  \__| \__,_| |_| |_| \___| |_|                                                 
"
# Agregar permiso de ejecucion al desinstalador.
echo "Cambiando el permiso a uninstall.sh."
sudo chmod +x uninstall.sh

echo "Creando carpeta de logs."
if [ ! -e ./logs/ ]; then
sudo mkdir ./logs/
fi

opcion=0
while [ $opcion -ne 1 ]
    do
    #Aceptar el acuerdo para iniciar la instalacion.
    echo "Bienvenido al instalador de Spooly-Skelly, esta herramienta esta pensada para su uso en auditorias
    y en entornos que estan controlados, a parte de que su uso es especialmente para fines educativos y/o laborales.
    A si que abstente de instalar la herramienta si la quieres usar para propositos ilicitos."
    read -p "¿Deseas proseguir con la instalación? (y/n): " sino

        if [[ $sino == "y" ]];then
            echo "Has aceptado la instalacion..."
            echo "Preparando instalador..."
            sleep 2
            clear
            opcion=1 
        elif [[ $sino == "n" ]];then
            echo "No has aceptado la instalacion..."
            echo "Saliendo del programa de instalacion..."
            read -n1 -p "Pulsa una tecla para continuar..."
            clear
            exit 0
        else
            echo "Argumento no valido"
            echo "Introduce un argumento de tipo y/n"
            clear
            
        fi
    done

#Actualizacion de la lista de paquetes disponibles por si acaso el usuario se le olvida hacerlo.
sudo apt-update

#Instalacion de las nuevas versiones de los paquetes.
sudo apt-upgrade

# Descargar python3 por si no tuviera para que se pueda iniciar el menu sin problemas.
echo "Instalando la instalacion de python."
sudo apt-get install python3.9
echo "Instalando nmap."
sudo apt-get install nmap
sleep 2

clear