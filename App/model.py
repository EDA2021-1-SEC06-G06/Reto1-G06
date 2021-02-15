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
    """

    catalog = {
        'videos': None,
        'category_id': None,
        }
    
    catalog['videos'] = lt.newList()

    catalog['category_id'] = lt.newList('SINGLE_LINKED', cmpfunction=None)  #TODO: Cambiar cmpfunction

    return catalog


# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    #Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)


def addVideoId(catalog, id_category, video):
    """
    """
    todos_category_ids = catalog['category_id']

    posID = lt.isPresent(todos_category_ids, id_category)

    if posID > 0:
        cat_id = lt.getElement(todos_category_ids, posID)
    
    else:
        cat_id = newCategoryId(id_category)
        lt.addLast(todos_category_ids, cat_id)
    
    lt.addLast(cat_id['videos'], video)


# Funciones para creacion de datos


def newCategoryId(new_id):
    """
    """

    category = {'name': '', 'videos': None, 'id': new_id} #TODO: De pronto toca agregar algo, newAuthor

    category['id'] = new_id
    




# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento