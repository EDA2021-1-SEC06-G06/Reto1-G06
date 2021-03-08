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
 """

import config as cf
import model
import csv
import datetime as dt


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Inicialización del Catálogo de vídeos



def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog



# Funciones para la carga de datos



def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadCategoryID(catalog)
    loadVideos(catalog)




def loadCategoryID(catalog):
    """
    Carga las categorías del archivo.
    """
    categoryfile = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(categoryfile, encoding='utf-8'), delimiter="\t")
    for category in input_file:
        filtered_category = {
            'id': category['id'],
            'name': (category['name']).replace(" ", '')  # quitar los espacios
        }

        model.addCategoryID(catalog, filtered_category)




def loadVideos(catalog):
    """
    Carga todos los vídeos del archivo y los agrega a la lista de vídeos
    """
    videosfile = cf.data_dir + 'videos/videos-large.csv'  # videos-large para la entrega
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        
        filtered_video = {
            'video_id': video['video_id'],
            'trending_date': dt.datetime.strptime(video['trending_date'], '%y.%d.%m').date(),
            'title': video['title'],
            'channel_title': video['channel_title'],
            'category_id': int(video['category_id']),
            'publish_time': dt.datetime.strptime(video['publish_time'], "%Y-%m-%dT%H:%M:%S.%fZ"),
            'tags': video['tags'],
            'views': int(video['views']),
            'likes': int(video['likes']),
            'dislikes': int(video['dislikes']),
            'country': video['country'],
            'dias_t': 1
        }

       
        model.addVideo(catalog, filtered_video)
        model.addVideoCountry(catalog, filtered_video['country'], filtered_video)



# Funciones de ordenamiento



def sortVideos(catalog, size: int):
    """
    Ordena los vídeos según sus views.
    """
    return model.sortVideos(catalog, size)




def sortByTitle(catalog):
    """
    Ordena los vídeos según sus títulos.
    """
    return model.sortByTitle(catalog)




def sortByLikes(catalog):
    """
    Ordena los vídeos según el número de likes.
    """
    return model.sortByLikes(catalog)



# Funciones de consulta sobre el catálogo



def primerVideo(catalog):
    video1 = model.primerVideo(catalog)
    return video1




def getVideosByCountry(catalog, countryName):
    country = model.getVideosByCountry(catalog, countryName)
    return country




def getVideosByCategory(catalog, categoryName, categoryCatalog):
    """
    Args:
        catalog: Catálogo del país
        categoryName: Nombre del país
        categoryCatalog: Catálogo principal que contiene los category_id
    """  
    category = model.getVideosByCategory(catalog, categoryName, categoryCatalog)
    return category



def getVideosByTag(catalog, tag):

    tag = model.getVideosByTag(catalog, tag)
    return tag

# Funciones de operaciones sobre el catálogo



def masDiasTrending(catalog):
    """
    Args:
        catalog: Catálogo ordenado según los Títulos

    Return:
        video_mayor_dias: Video que ha tenido más días de tendencia.
    """
    catalog = model.masDiasTrending(catalog)
    return catalog
