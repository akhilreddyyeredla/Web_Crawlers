import os

import re

import uuid

import time

import fnmatch

import datetime

import response_getter
import Linio_Mex_config
import product_info_storage
import completed_queue
import json

from Queue import Queue

from  datetime import date

from threading import Thread

from multiprocessing import Process

from bs4 import BeautifulSoup

from Global_Constants import *

import Linio_Mex_config as DataCollectors_Configuration

from product_info_storage import store

from response_getter import Response

from class_not_found import ClassNotFound

from print_exception import print_exception

from Linio_Mex_config import *

from Common.Linio_Mex_config import MAIN_URL as linio_mex_main_url

#import Linio.CONSTANTS as linio_mex_constants

from Linio.product_parsers.salud_y_bienestar_get_product_info import ProductDetails  as salud_y_bienestar_get_details
from Linio.product_parsers.hogar_get_product_info import ProductDetails  as hogar_get_details
from Linio.product_parsers.celulares_get_product_info import ProductDetails  as celulares_get_details
from Linio.product_parsers.moda_get_product_info import ProductDetails  as moda_get_details
from Linio.product_parsers.deportes_get_product_info import ProductDetails  as deportes_get_details
from Linio.product_parsers.electrodomesticos_get_product_info import ProductDetails  as electrodomesticos_get_details
from Linio.product_parsers.tv_audio_y_video_get_product_info import ProductDetails  as tv_audio_y_video_get_details
from Linio.product_parsers.consolas_y_videojuegos_get_product_info import ProductDetails  as consolas_y_videojuegos_get_details
from Linio.product_parsers.juguetes_ninos_y_bebes_get_product_info import ProductDetails  as juguetes_ninos_y_bebes_get_details
from Linio.product_parsers.belleza_get_product_info import ProductDetails  as belleza_get_details
from Linio.product_parsers.computacion_get_product_info import ProductDetails  as computacion_get_details


from Linio.file_operation import create_directory_and_hierarchy_files as linio_mex_create_directory_and_hierarchy_files,file_to_set as linio_mex_file_to_set, update_files as linio_mex_update_files, create_project_dir as linio_mex_create_project_dir,append_to_file as linio_mex_append_to_file

from Linio.hirerachy_collectors import salud_y_bienestar_hierarchy,belleza_hierarchy,celulares_hierarchy,\
    computacion_hierarchy,consolas_y_videojuegos_hierarchy,deportes_hierarchy,\
    electrodomesticos_hierarchy,hogar_hierarchy,juguetes_ninos_y_bebes_hierarchy,\
    moda_hierarchy ,tv_audio_y_video_hierarchy

from Linio.info_collectors import belleza_info_collector,celulares_info_collector\
    ,computacion_info_collector,consolas_y_videojuegos_info_collector,deportes_info_collector\
    ,electrodomesticos_info_collector,hogar_info_collector\
    ,juguetes_ninos_y_bebes_info_collector,moda_info_collector,salud_y_bienestar_info_collector\
    ,tv_audio_y_video_info_collector

from Linio.url_collectors import belleza_url_collector,celulares_url_collector\
    ,computacion_url_collector,consolas_y_videojuegos_url_collector\
    ,deportes_url_collector,electrodomesticos_url_collector,hogar_url_collector\
    ,juguetes_ninos_y_bebes_url_collector,moda_url_collector\
    ,salud_y_bienestar_url_collector,tv_audio_y_video_url_collector