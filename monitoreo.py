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

# Creo funciones que voy a usar mas de una vez para simplificar:
def numero_entero():
    while True:
        valor = input()
        try:
            valor = int(valor)
            return valor
        except ValueError:
            print("ATENCIÓN: Debe ingresar un número entero.")

def minusculas():
    clave = str(input("Ingrese el producto a monitorear\n"))
    clave = clave.lower()
    return clave

def monitoreo():
    with open("monitoreo_origen.csv") as csvfile:
        data = list(csv.DictReader(csvfile))

    # Saco la informacion de los nicks disponibles para las comparaciones
    usuarios = []
    usuarios.append(data[0].get("nick"))
    cantidad_filas = len(data)

    for i in range(cantidad_filas):
        row = data[i]
        comparar = str(row.get("nick"))
        if comparar not in usuarios:
            usuarios.append(comparar)

    # Creo un Bucle para obtener el usuario principal
    # Y lo borro de la lista para continuar
    while True: 
        print("Listas de usuarios disponibles:")
        print("1 - ",usuarios[0])
        print("2 - ",usuarios[1])
        print("3 - ",usuarios[2])
        print("4 - ",usuarios[3])
        print("Ingrese el usuario de la cuenta principal:")
        opcion = numero_entero()
        try:
            if opcion < 4:
                cuenta_principal = usuarios[opcion-1]
                usuarios.remove(cuenta_principal)
                break
            else:
                print("Error vuelva a ingresar")
        except:
            print("Error vuelva a ingresar")

    # Creo la opcion para elegir si comparamos con 
    # 1 competidor o con todos
    while True:    
        print("ingrese que competidor desea monitorear:")
        print("1 - ",usuarios[0])
        print("2 - ",usuarios[1])
        print("3 - ",usuarios[2])
        print("4 -  Todos")
        opcion = numero_entero()
        if opcion < 4:
            competidor = usuarios[opcion-1]
            break
        elif opcion == 4:
            break
        else:
            print("Error Vuelva a ingresar")
        

    # Empiezo con las comparaciones
    # Creo un diccionario para organizar y almacenar

    comparaciones_salida = {
        "cuenta principal":str,
        "competidor":str,
        "titulo":str,
        "precio":int,
        "diferencia precio":int,
        "cantidad vendida":int,
        "diferencia cantidad":int,
        }
    fo = open('salida.csv', 'w', newline='')
    writer = csv.DictWriter(fo, fieldnames=comparaciones_salida)
    writer.writeheader()
    print(comparaciones_salida)

    # Creo un Try para la comparacion de un solo competidor
    # Si el usuario eligio Todos, no se creo una varibale COMPETIDOR
    # Por lo tanto intenta Except
    try:
        palabra_clave = minusculas()
        print(palabra_clave)
        for i in range(cantidad_filas):
            row = data[i]
            titulo = str(row.get("titulo"))
            titulo = titulo.lower()
            if palabra_clave in titulo:
                writer.writerow({
                    'titulo':titulo
                    })
        fo.close()

    except:
        fo.close()



        


if __name__ == '__main__':
    monitoreo()