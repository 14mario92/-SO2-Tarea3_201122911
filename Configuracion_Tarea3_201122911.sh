#!/bin/bash

mkdir /home/Tarea3_201122911

cp ServidorHttp.py /home/Tarea3_201122911

cp [SO2]Tarea3_201122911 /etc/init.d

update-rc.d [SO2]Tarea3_201122911 defaults

echo "Instalacion Completa. Reiniciar para que hagan efecto los cambios"
