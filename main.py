import os
import json

federacion ={}

grupos = {
    "A": [],
    "B": []
}
fechasJuego ={

}

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
    if (op == 1):
        isAddTeam = True
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
                "gc":0,
                "estado":0
            }
            isAddTeam = bool(input("Desea continuar agregando mas equipos S(Si) o Enter(No)"))
            federacion.update({str(len(federacion)+1).zfill(4):equipo})
        
    elif (op == 2):
        for key,valor in federacion.items():
            if valor["estado"]== 0:
                os.system('cls')
                print(F"Seleccione el grupo al que quiere ingresar el equipo 
                      {valor["nombre"]}")
                for key2 in grupos:
                    if (len(grupos[key2]) < 4):
                        print(f"{key2}. grupo {key2}")
                grp = input(":)_").upper()
                equip ={
                    "codEquipo" : key,
                    "nombre" : valor["nombre"]
                }
                federacion.get(key)["estado"] = 1
                grupos.get(grp).append(equip)
    elif(op == 4):
        isActive = False


print(json.dumps(federacion,indent=4))

