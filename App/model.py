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
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog():
    """
    Inicializa el catálogo de videos.
    """

    catalog = {
        'videos': None,
        'category_id': None,
        }
    
    catalog['videos'] = lt.newList()

    catalog['category_id'] = lt.newList('ARRAY_LIST', cmpfunction=None)  #TODO: Cambiar cmpfunction

    return catalog


# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):

    lt.addLast(catalog['videos'], video)



def addCategoryID(catalog, id_):
    """
    """

    i = newCategoryID(id_['category_id'])
    lt.addLast(catalog['category_id'], i)



# Funciones para creacion de datos


def newCategoryID(name, id_):
    """
    """

    category = {'name': '', 'category_id': ''}

    category['name'] = name
    category['category_id'] = id_


# Funciones de consulta


# Funciones utilizadas para comparar elementos dentro de una lista
def compareCategoryName(name, id_):
    return (name == id_['name'])

# Funciones de ordenamiento

def sortVideos(catalog):
    sa.sort(catalog['videos'], comparecategoryname)