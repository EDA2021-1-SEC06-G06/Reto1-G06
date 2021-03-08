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
from DISClib.Algorithms.Sorting import mergesort
assert cf
import datetime  # Se importa para que al imprimir información de los vídeos aparezca como una fecha legible.


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las 
categorias de los mismos.
"""


# Construccion de modelos



def newCatalog():
    """
    Inicializa el catálogo de videos. Crea una lista vacía para guardar
    todos los videos. Adicionalmente, crea una lista vacía para las categorías.

    Retorna el catálogo inicializado
    """

    catalog = {'videos': None, 'category_id': None, 'country': None}

    # Se crean las listas bajo esas llaves
    catalog['videos'] = lt.newList(datastructure='ARRAY_LIST', cmpfunction=cmpVideosByViews)

    # Se puede cambiar el cmpfunction
    catalog['category_id'] = lt.newList(datastructure='ARRAY_LIST', cmpfunction=cmpCategoriasByName)  

    catalog['country'] = lt.newList(datastructure='ARRAY_LIST', cmpfunction=cmpByCountry)

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

    paises = catalog['country']  # paises es un dict que tiene como llaves los países

    poscountry = lt.isPresent(paises, countryName)  # posición del país en paises

    if poscountry > 0:
        country = lt.getElement(paises, poscountry)  # si ya existe, retorna el array del dict
    else:
        country = newCountry(countryName)  # Si no existe, lo crea
        lt.addLast(paises, country)  # lo agrega al final de paises

    lt.addLast(country['videos'], video)  # agrega el vídeo en el país



# Funciones para creacion de datos



def newCategoryID(name, id_):
    """
    Esta estructura almacena las categorías utilizadas para marcar videos.
    """

    category = {'name': '', 'category_id': ''}

    category['name'] = name
    category['category_id'] = int(id_)


    return category




def newCountry(countryName):

    country = {'name': '', 'videos': None}
    country['name'] = countryName
    country['videos'] = lt.newList('ARRAY_LIST', cmpfunction=cmpVideosByViews)
    return country



# Funciones de consulta



def primerVideo(catalog):

    video1 = lt.getElement(catalog["videos"], 1)
    return video1




def getVideosByCountry(catalog, countryName: str):

    posCountry = lt.isPresent(catalog['country'], countryName)  # recibo la posición del país en el catálogo
    if posCountry > 0:
        country = lt.getElement(catalog['country'], posCountry)  # recibe el array del país que contiene el name y videos
        return country
    return None




def getVideosByCategory(catalog, categoryName: str, categoryCatalog):
    """
    Args:
        catalog: Catálogo del país
        categoryName: Nombre del país
        categoryCatalog: Catálogo principal que contiene los category_id
    """

    id_, name = categoryNameToID(categoryCatalog, categoryName)  # del catálogo principal, cambia categoryName por su id

    catalogo_filtrado = {'name': name, 'videos': None}
    catalogo_filtrado['videos'] = lt.newList('ARRAY_LIST', cmpfunction=cmpVideosByViews)


    for video in lt.iterator(catalog['videos']):  # Ciclo para iterar por cada video del catálogo
   
        if video['category_id'] == id_:

            lt.addLast(catalogo_filtrado['videos'], video)  # se agrega al catálogo filtrado

    return catalogo_filtrado




def masDiasTrending(ord_videos):
    """
    Args:
        catalog: Catálogo ordenado según los Títulos

    Return:
        video_mayor_dias: Video que ha tenido más días de tendencia.
    """
    size = lt.size(ord_videos)

    video_con_mas_dias = None
    mas_dias = 1

    i = 1  # Índice 1
    ii = 2  # Índice 2

    while i <= size and ii <= size:
        
        video = lt.getElement(ord_videos, i)

        if video['title'] == lt.getElement(ord_videos, ii)['title']:  # Si video tiene el mismo título que el siguiente vídeo.
        
            while ii <= size and (video['title'] == lt.getElement(ord_videos, ii)['title']):  # Mientras el siguiente vídeo tenga el mismo título.
                video['dias_t'] += 1
                ii += 1  # El índice 2 va aumentando.

            # Cuando termine el ciclo
            i = ii + 1
            ii += 2

        else:  # Si no tienen el mismo título
            i += 1
            ii += 1

        # Compara los días trending con más días
        if video['dias_t'] > mas_dias:
            mas_dias = video['dias_t']
            video_con_mas_dias = video

    return video_con_mas_dias




# Funciones utilizadas para comparar elementos dentro de una lista



def categoryNameToID(catalog, name: str):

    id_ = None

    for category in lt.iterator(catalog['category_id']):  # iteramos por las categorías del catálogo princpal

        if category['name'].lower() == name.lower():

            id_ = int(category['category_id'])
            name = category['name']

            return (id_, name)




def cmpVideosByViews(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son mayores que los del video2
    Args:
        video1: informacion del primer video que incluye su valor 'views'
        video2: informacion del segundo video que incluye su valor 'views'
    """

    return (float(video1['views']) > float(video2['views']))




def cmpByCountry(countryName1, countryname):
    """
    Devuelve cero (0) si...
    """
    if (countryName1.lower() in countryname['name'].lower()):
        return 0
    return -1




def cmpCategoriasByName(name, category):
    return (name == category['name'])




def cmpVideosByTitle(video1, video2):
    return (video1['title'] >= video2['title'])




def cmpDiasTrending(video1, video2):
    return (video1['dias_t'] > video2['dias_t'])




def cmpVideosByLikes(video1, video2):
    return (video1['likes'] > video2['likes'])


# Funciones de ordenamiento



def sortVideos(catalog, size: int):

    if size <= lt.size(catalog['videos']):

        sub_list = lt.subList(catalog['videos'], 1, size)
        sub_list = sub_list.copy()

        start_time = time.process_time()

        sorted_list = mergesort.sort(sub_list, cmpVideosByViews)

        stop_time = time.process_time()

        elapsed_time_mseg = (stop_time - start_time) * 1000

        return elapsed_time_mseg, sorted_list

    else:

        return None, None


def sortByTitle(catalog):
  
    sub_list = lt.subList(catalog['videos'], 1, lt.size(catalog['videos']))

    sub_list = sub_list.copy()

    sorted_list = mergesort.sort(lst=sub_list, lessfunction=cmpVideosByTitle)

    return sorted_list


def sortByLikes(catalog):

    sub_list = lt.subList(catalog['videos'], 1, lt.size(catalog['videos']))

    sub_list = sub_list.copy()

    sorted_list = mergesort.sort(lst=sub_list, lessfunction=cmpVideosByLikes)

    return sorted_list
