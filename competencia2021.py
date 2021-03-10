#!/usr/bin/env python

__author__ = "Sebas Volpe"
__email__ = "compras@bari.com.ar"
__version__ = "1.00"

import json
import requests
from datetime import datetime
import numpy as np
import sqlite3
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from mercadolibre.client import Client




# Ingreso nombre de la competencia

def competencia():
    dato = str(input("Ingrese Nick Competencia:\n"))
    return dato
    


def fetch(data):
    filtrado = [x for x in data if x.get("currency_id") == "ARS"]
    return filtrado


    

if __name__ == '__main__':


    client = Client('902100072489015', 'yGLQLlydWcFnRqsJTmaguXCCKY7TQVWx', site='MLA')
    url = client.authorization_url('https://mercadolibre.com.ar')

    token = client.exchange_code('https://mercadolibre.com.ar', 'TG-6047c1d6fe3ea50007636cad-184827283')
    client.set_token('TOKEN')
    new_token = client.refresh_token()


    parte1 = "https://api.mercadolibre.com//sites/MLA/search?nickname="
    parte2 = competencia()
    parte3 = "&offset=1010"
    url = parte1 + parte2 + parte3


    response = requests.get(url)
    
    ml = response.json()
    results = ml["results"]

    dataset = [
        {"Titulo":x.get("title"),
        "Precio":x.get("price"),
        "Cantidad disponible":x.get("available_quantity"),
        "Cantidades Vendidas":x.get("sold_quantity")
        } 
        for x in results
        ]

    
    print(dataset)


    # Filtro solo los de Pesps
    pesos = fetch(results)

    # Filtro solo Precios, condicion...
    dataset = [
        {"Price":x.get("price"),
        "Condition":x.get("condition")
        } 
        for x in pesos
        ]

    trasn = transform(dataset,10000,110000)
    x = report(trasn)
    print(x) 



    


    



