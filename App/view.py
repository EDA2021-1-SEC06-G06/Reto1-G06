"""
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




def printResults(ord_videos, sample=10):
    size = lt.size(ord_videos)

    if size > sample:
        print("Los primeros {0} vídeos ordenados son:".format(sample))

        i = 1

        while i <= sample:

            video = lt.getElement(ord_videos, i)

            print("Fecha de tendencia: {0}   Título: {1}   Canal: {2}   Fecha de publicación: {3}   Visitas: {4}   Likes: {5}   Dislikes: {6}".format(video['trending_date'], video['title'], video['channel_title'], video['publish_time'], video['views'], video['likes'], video['dislikes']))

            i += 1




def printCountryData(country):
    if country:
        print("Nombre: {0}".format(country['name']))
        print('Total videos: {0}'.format(lt.size(country['videos'])))
    else:
        print("No se encontró el país")



def printCategoryData(category):
    if category:
        print('Nombre: {0}'.format(category['name']))
        print("Cantidad de vídeos en la categoría: {0}".format(lt.size(category['videos'])))
    else:
        print("No se encontró")


def printPrimerVideo(video):
    if video:
        return("Fecha de tendencia: {0}   Título: {1}   Canal: {2}   Fecha de publicación: {3}   Visitas: {4}   Likes: {5}   Dislikes: {6}".format(video['trending_date'], video['title'], video['channel_title'], video['publish_time'], video['views'], video['likes'], video['dislikes']))
    else:
        return("No se encontró el primero video")


def printCategoryID(catalog):
    if catalog:
        print("El ID y el nombre de las categorias el lo siguiente:")
        for category in lt.iterator(catalog["category_id"]):

            print("{0} --- {1}".format(category['category_id'], category['name']))


def initCatalog():
    """
    Inicializa el catálogo de videos.
    """
    return controller.initCatalog()




def loadData(catalog):
    """
    Carga los videos en la estructura de datos.
    """
    controller.loadData(catalog)




catalog = None
default_limit = 1000
sys.setrecursionlimit(default_limit * 10)



"""
Menu principal
"""


while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    

    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        
        # Se inicializa el catálogo.
        catalog = initCatalog()

        # Se cargan los videos en la estructura de datos.
        loadData(catalog)

        print("Videos cargados: {0}".format(lt.size(catalog['videos'])))
        
        print("Categorías cargadas: {0}".format(lt.size(catalog['category_id'])))

        print("El primero video es:\n{0}".format(printPrimerVideo(controller.primerVideo(catalog))))

        printCategoryID(catalog)



    elif int(inputs[0]) == 2:

        countryName = input("Ingrese el nombre del país que desea:\n~ ")

        countryCatalog = controller.getVideosByCountry(catalog, countryName)  # Nuevo catálogo filtrado del país elegido
      


        # Inputs secundarios del usuario
        
        
        
        categoryName = input("Ingrese el nombre de la categoría que desea:\n~ ")

        categoryCatalog = controller.getVideosByCategory(countryCatalog, categoryName, catalog)  # Mirar parámetros

        printCategoryData(categoryCatalog)  # Se imprime la información filtrada por categoría y país
    


        size = input("Indique el tamaño de la muestra:\n No puede ser mayor que el Total de videos de arriba\n~ ")
        
        cantidad_videos = int(input("Ingrese la cantidad de vídeos que desea listar:\n~ "))
        


        result = controller.sortVideos(categoryCatalog, int(size))  # Ordenamiento por views
   
    
        print("Para la muestra de {0} elementos, el tiempo (mseg) es: {1}".format(size, result[0]))

        printResults(result[1], sample=cantidad_videos)



    elif int(inputs[0]) == 3:

        countryName = input("Ingrese el nombre del país que le interesa:\n~ ")

        countryCatalog = controller.getVideosByCountry(catalog, countryName)  # Nuevo catálogo filtrado del país elegido

        ordenados = controller.sortByTitle(countryCatalog)  # Vídeos ordenados según su título

        print(ordenados)

        video = controller.masDiasTrending(ordenados)  # No funciona

        print("El vídeo con más días de tendencia en el país {0} fue:\nTítulo: {1} -- Canal: {2}  -- Días: {3}".format(countryName, video['title'], video['channel_title'], video['dias_t']))



    elif int(inputs[0]) == 4:

        categoryName = input("Ingrese el nombre de la categoría que le interesa:\n~ ")

        categoryCatalog = controller.getVideosByCategory(catalog, categoryName, catalog)  # Catálogo filtrado por la categoría

        ordenados = controller.sortByTitle(categoryCatalog)  # Vídeos ordenados según su título

        video = controller.masDiasTrending(ordenados)

        print("El vídeo con más días de tendencia en la categoría {0} fue:\nTítulo: {1} -- Canal: {2} -- ID de la Categoría: {3} -- Días: {4}".format(categoryName, video['title'], video['channel_title'], video['category_id'], video['dias_t']))



    elif int(inputs[0]) == 5:

        cantidad_videos = int(input("Ingrese la cantidad de vídeos que desea listar:\n~ "))

        tag = input("Ingrese el tag que desea consultar:\n~ ")

        likesCatalog = controller.sortByLikes(catalog)

        printResults(likesCatalog, cantidad_videos)


    else:
        sys.exit(0)
sys.exit(0)
