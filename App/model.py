"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
import time
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort
from DISClib.Algorithms.Sorting import selectionsort
from DISClib.Algorithms.Sorting import mergesort
from DISClib.Algorithms.Sorting import quicksort
assert cf


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las 
categorias de los mismos.
"""


# Construccion de modelos


def newCatalog(tipoDeLista: str):
    """
    Inicializa el catálogo de videos. Crea una lista vacía para guardar
    todos los videos. Adicionalmente, crea una lista vacía para las categorías.
    
    Retorna el catálogo inicializado
    """

    tipoDeLista = 'ARRAY_LIST'

    catalog = {
        'videos': None,
        'category_id': None,
        }
    
    # Se crean las listas bajo esas llaves
    catalog['videos'] = lt.newList(datastructure=tipoDeLista, cmpfunction=cmpVideosByViews)

    # Se puede cambiar el cmpfunction
    catalog['category_id'] = lt.newList(datastructure=tipoDeLista, cmpfunction=None)  # la cmpfunction depende de lo que se necesite encontrar

    catalog['country'] = lt.newList(datastructure=tipoDeLista, cmpfunction=cmpByCountry)

    return catalog


# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    """
    Adiciona un video a la lista de videos.
    """

    # Se adiciona el vidieo en la última posición de la lista de videos.
    lt.addLast(catalog['videos'], video)


def addCategoryID(catalog, category):
    """
    Adiciona una categoría a la lista de categorías.
    """
    # Se crea la nueva categoría
    i = newCategoryID(category['name'], category['id'])
    lt.addLast(catalog['category_id'], i)


def addVideoCountry(catalog, countryName, video):

    paises = catalog['country']
    poscountry = lt.isPresent(paises, countryName)
    if poscountry > 0:
        country = lt.getElement(paises, poscountry)
    else:
        country = newCountry(countryName)
        lt.addLast(paises, country)
    lt.addLast(country['videos'], video)


# Funciones para creacion de datos


def newCategoryID(name, id_):
    """
    Esta estructura almacena las categorías utilizadas para marcar videos.
    """

    category = {'name': '', 'category_id': ''}

    category['name'] = name
    category['category_id'] = id_

    return category


def newCountry(countryName):

    country = {'name': '', 'videos': None}
    country['name'] = countryName
    country['videos'] = lt.newList('ARRAY_LIST')
    return country


# Funciones de consulta


def getVideosByCountry(catalog, countryName):
    posCountry = lt.isPresent(catalog['country'], countryName)
    if posCountry > 0:
        country = lt.getElement(catalog['country'], posCountry)
        return country
    return None


# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosByViews(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
        video1: informacion del primer video que incluye su valor 'views'
        video2: informacion del segundo video que incluye su valor 'views'
    """

    return (float(video1['views']) > float(video2['views']))


def cmpByCountry(countryName1, countryname):
    if (countryName1.lower() in countryname['name'].lower()):
        return 0
    return -1


def cmpByCategory(name, category):
    return (name == category['name'])


# Funciones de ordenamiento


def sortVideos(catalog, size: int):

    if size <= lt.size(catalog['videos']):

        sub_list = lt.subList(catalog['videos'], 1, size)
        sub_list = sub_list.copy()

        start_time = time.process_time()

        sorted_list = mergesort.sort(sub_list, cmpVideosByViews)

        stop_time = time.process_time()

        elapsed_time_mseg = (stop_time - start_time)*1000

        return elapsed_time_mseg, sorted_list
    
    else:

        return None, None