#!/bin/bash
#Desinstalador de Spooky-Skelly.
#Necesita permisos de ejecucion y debe ejecutarse para empezar la desinstalacion.

clear

echo "
 _____                 _           _____  _         _  _      
|   __| ___  ___  ___ | |_  _ _   |   __|| |_  ___ | || | _ _ 
|__   || . || . || . || '_|| | |  |__   || '_|| -_|| || || | |
|_____||  _||___||___||_,_||_  |  |_____||_,_||___||_||_||_  |
       |_|                 |___|                         |___|     
  ___               _               _            _   _             
 |   \   ___   ___ (_)  _ _    ___ | |_   __ _  | | | |  ___   _ _ 
 | |) | / -_) (_-< | | | ' \  (_-< |  _| / _' | | | | | / -_) | '_|
 |___/  \___| /__/ |_| |_||_| /__/  \__| \__,_| |_| |_| \___| |_|                                                                                         
"

#Para borrar la carpeta que contiene a todo.
cd .. && rm -rf ./Spooky-Skelly


#Para terminar la desinstalacion.
read -n1 -p "Dale a una tecla para continuar..."

clear
