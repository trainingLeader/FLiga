import os
import json

federacion ={}
menu = ("1.Agregar equipo","2.Crear grupos","3.Ver grupo","4.Salir")
#Equipo PJ PP PE PG GF GC
#update o Agregar o Modificar informacion en el diccionario
isAddTeam = True
isActive = True
mensaje = """
    ++++++++++++++++++++++++++++++++++
    + TORNEO BETPLAY - COLOMBIA 2024 +
    ++++++++++++++++++++++++++++++++++
"""
while isActive :
    os.system('cls')
    print(mensaje)
    for item in menu:
        print(item)
    op = int(input(":)_"))

while isAddTeam:
    os.system('cls')
    nombre= input("Ingrese el nombre del equipo :")
    equipo={
        "nombre" : nombre,
        "pj":0,
        "pp":0,
        "pe":0,
        "pg":0,
        "gf":0,
        "gc":0
    }
    isAddTeam = bool(input("Desea continuar agregando mas equipos S(Si) o Enter(No)"))
    federacion.update({str(len(federacion)+1).zfill(4):equipo})
print(json.dumps(federacion,indent=4))

