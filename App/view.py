﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- REQ. 1: Encontrar buenos videos por categoría y país")
    print("3- REQ. 2: Encontrar video tendencia por país")
    print("4- REQ. 3: Encontrar video tendencia por categoría")
    print("5- REQ. 4: Buscar los videos con más Likes")
    print("0- Salir")


def initCatalog(tipoDeLista: int):
    """
    Inicializa el catálogo de videos.
    """
    return controller.initCatalog(tipoDeLista)


def loadData(catalog):
    """
    Carga los videos en la estructura de datos.
    """
    controller.loadData(catalog)


catalog = None


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        tipoDeLista = int(input("¿Qué tipo de representación de lista desea? (escriba el número):\n(1)-ARRAY_LIST\n(2)-SINGLE_LINKED\n~"))
        
        # Se inicializa el catálogo.
        catalog = initCatalog(tipoDeLista)

        # Se cargan los videos en la estructura de datos.
        loadData(catalog)

        print("Videos cargados: {0}".format(lt.size(catalog['videos'])))
        
        print("Categorías cargadas: {0}".format(lt.size(catalog['category_id'])))

    elif int(inputs[0]) == 2:
        pass

    else:
        sys.exit(0)
sys.exit(0)
