#!/usr/bin/env python
'''
Proyecto integrador
Monitoreo de la competencia en Mercado libre
---------------------------
Autor: Sebastian Volpe
Version: 1.00
Descripcion:
Programa que se utiliza para monitorear a la competencia en MercadoLibre
y generar un archivo “csv”. 
Filtra y analizar la información e informa
la diferencia de precios entre la Cuenta principal 
y 3 competidores previamente asignados.

'''

__author__ = "Sebastian Volpe"
__email__ = "compras@bari.com.ar"
__version__ = "1.00"

import csv
import re
