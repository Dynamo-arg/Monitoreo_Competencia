#!/usr/bin/env python
import csv

'''
Proyecto integrador
Monitoreo de la competencia en Mercado libre
---------------------------
Autor: Sebastian Volpe
Version: 1.00
Descripcion:
Programa que se utiliza para monitorear a la competencia en MercadoLibre
generar un archivo csv 
Filtra y analizar la información e informa
la diferencia de precios entre la Cuenta principal
y 3 competidores previamente asignados
'''

__author__ = "Sebastian Volpe"
__email__ = "compras@bari.com.ar"
__version__ = "1.00"


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
    bucle = 1
    while bucle == 1:
        print(
            "\nListas de usuarios disponibles:\n"
            "1 - ", usuarios[0], "\n"
            "2 - ", usuarios[1], "\n"
            "3 - ", usuarios[2], "\n"
            "4 - ", usuarios[3], "\n"
            "Ingrese el usuario de la cuenta principal:"
            )
        opcion = numero_entero()

        if opcion < 4:
            cuenta_principal = usuarios[opcion-1]
            usuarios.remove(cuenta_principal)
        else:
            print("ERROR VUELVA A INGRESAR")
        # Creo la opcion para elegir si comparamos con
        # 1 competidor o con todos
        while True:
            print(
                "\ningrese que competidor desea monitorear:\n"
                "1 - ", usuarios[0], "\n"
                "2 - ", usuarios[1], "\n"
                "3 - ", usuarios[2], "\n"
                "4 -  Todos"
                )
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
            "nombre cuenta": str,
            "nombre competidor": str,
            "titulo": str,
            "precio": int,
            "diferencia precio": int,
            "cantidad vendida": int,
            "diferencia cantidad": int,
            }
        fo = open('salida.csv', 'w', newline='')
        writer = csv.DictWriter(fo, fieldnames=comparaciones_salida)
        writer.writeheader()
        palabra_clave = minusculas()
        error = 0
        for i in range(cantidad_filas):
            row = data[i]
            titulo = str(row.get("titulo"))
            titulo = titulo.lower()
            precio = int(row.get("precio"))
            cuenta = str(row.get("nick"))
            vendidas = int(row.get("cantidad"))
            if (palabra_clave in titulo) and (cuenta == cuenta_principal):
                writer.writerow({
                    "nombre cuenta": cuenta,
                    "titulo": titulo,
                    "precio": precio,
                    "cantidad vendida": vendidas,
                    })
                precio_comparar = precio
                cantidad_comparar = vendidas
                error += 1

        # Creo un Try para la comparacion de un solo competidor
        # Si el usuario eligio Todos, no se creo una varibale COMPETIDOR
        # Por lo tanto intenta Except
        try:
            for i in range(cantidad_filas):
                row = data[i]
                titulo = str(row.get("titulo"))
                titulo = titulo.lower()
                precio = int(row.get("precio"))
                cuenta = str(row.get("nick"))
                vendidas = int(row.get("cantidad"))
                if (palabra_clave in titulo) and (cuenta == competidor):
                        writer.writerow({  
                            "nombre competidor": cuenta,
                            "titulo": titulo,
                            "precio": precio,
                            "cantidad vendida": vendidas,
                            "diferencia cantidad": vendidas - cantidad_comparar,
                            "diferencia precio": precio - precio_comparar,
                            })
            fo.close()
        except:
            print("ERROR")
            for i in range(cantidad_filas):
                row = data[i]
                titulo = str(row.get("titulo"))
                titulo = titulo.lower()
                precio = int(row.get("precio"))
                cuenta = str(row.get("nick"))
                vendidas = int(row.get("cantidad"))
                if (palabra_clave in titulo) and (cuenta != cuenta_principal):
                        writer.writerow({
                            "nombre competidor": cuenta,
                            "titulo": titulo,
                            "precio": precio,
                            "cantidad vendida": vendidas,
                            "diferencia cantidad": vendidas - cantidad_comparar,
                            "diferencia precio": precio - precio_comparar,
                            })
            fo.close()
        if error == 0:
            print(
                "NO HAY COINCIDENCIA\n",
                "1 - Volver a ingresar\n",
                "2 - SALIR"
                )
            bucle = numero_entero()
            if bucle == 1:
                usuarios.append(cuenta_principal)
            else:
                break
        else:
            print("Archivo generado y Almacenado como ", fo.name)
            print(
                "Eliga algunas de estas opciones:\n"
                "1 - Volver a generar el Archivo\n"
                "2 - Ver resultados por consola\n"
                "3 - Salir"
                )
            bucle = numero_entero()
            if bucle == 1:
                usuarios.append(cuenta_principal)
            elif bucle == 2:
                with open('salida.csv') as csvfile:
                    data = list(csv.DictReader(csvfile))
                filas = len(data)
                for i in range(filas):
                    row = data[i]
                    print(
                        'Cuenta Principal:', row.get('nombre cuenta'),
                        'Competidor:', row.get('nombre competidor'),
                        'Titulo:', row.get('titulo'),
                        'Precio:', row.get('precio'),
                        'Diferencia Precio:', row.get('diferencia precio'),
                        'Vendidas:', row.get('cantidad vendida'),
                        'Cantidad Vendidas:', row.get('diferencia cantidad')
                    )
            else:
                break
                     
if __name__ == '__main__':
    monitoreo()
