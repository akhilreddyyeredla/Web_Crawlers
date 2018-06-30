# coding=utf-8
##
## Global Configurations
##

PATH_STYLE = '/'

## Max number of threads you want to spwan
NO_OF_THEARDS = 20


## Which_part_to_collect

START_HIERARCHY_COLLECTION = False
START_URL_COLLECTION = False
START_INFO_COLLECTION = True


ROOT_FOLDER = '/home/eunimart/datacollector/Data_store_1'

# 1 to write into  sql_db
# 2 to write into file
# 3 to write into cassandra
# 4 to write into multiple file
# 5 to write into BigQuery
WRITE_TO = 4

# Flag is used to collect sample data or all data
# 1 to collect sample data
# 2 to collect all the data

PRODUCT_INFO_FLAG = 2
PRODUCT_URL_FLAG = 2

## No of sample products you want to collect
NO_OF_PRODUCT_INFO_TO_COLLECT = 2

## No of product urls tou want to collect for each sub_sub_category
NO_OF_PRODUCT_URL_TO_COLLECT = 2

## this pattern is used to find all the text files mathching with that path
PATTERN_1 = '*_page_links.txt'
PATTERN_2 = '*_page_completed.txt'
PATTERN_3 = '*_info_links.txt'
PATTERN_4 = '*_info_completed.txt'
SOUQ_PATTERN = '*_links.txt'

DEBUG = True


LINIO_MEX_HIERARCHY_ROOT = ROOT_FOLDER +'/Linio_MEX/hierarchy'
LINIO_MEX_URL_ROOT = ROOT_FOLDER + '/Linio_MEX/url'
LINIO_MEX_INFO_ROOT = ROOT_FOLDER +'/Linio_MEX/info'
'''
['Salud_y_Bienestar', 'Hogar', 'Celulares', 'Moda',
'Deportes', 'Electrodomésticos', 'TV_Audio_y_Video',
'Consolas_y_Videojuegos', 'Juguetes_niños_y_bebés','Belleza', 'Computación']
'''

LINIO_MEX_CATEGORIES = ['Celulares', 'Computación']

'''***************************CONSTANTS********************************'''
# coding=utf-8

# This is the path where data of products will be stored IF
# configured to store each product's detail in individual file
#
# Change this as per the requirements
# This is tested on Windows File System



SALUD_Y_BIENESTAR                   = "Salud_y_Bienestar"
HOGAR                               = "Hogar"
CELULARES                           = "Celulares"
MODA                                = "Moda"
DEPORTES                            = "Deportes"
ELECTRODOMESTICOS                   = "Electrodomésticos"
TV_AUDIO_Y_VIDEO                    = "TV_Audio_y_Video"
CONSOLAS_Y_VIDEOJUEGOS              = "Consolas_y_Videojuegos"
JUGUETES_NINOS_Y_BEBES              = "Juguetes_niños_y_bebés"
BELLEZA                             = "Belleza"
COMPUTACION                         = "Computación"



PRODUCTS_PAGE = 'products_page_links.txt'
COMPLETED_PAGE = 'products_page_completed.txt'


# To store product urls links
PRODUCTS_INFO_FILE = 'products_info_links.txt'
COMPLETED_INFO_FILE = 'products_info_completed.txt'


# To store hierarchy queue files
QUEUE_FILE = '_file_queue.txt'
COMPLETED_QUEUE_FILE = '_file_completed.txt'


# path = DataCollectors_Configuration.ROOT_FOLDER + "/" +  DataCollectors_Configuration.LINIO_PROJECT_NAME

MARKETPLACE = "Linio_Mexico"

MAIN_URL = "https://www.linio.com.mx"

WRITE_TO_SINGLE_FILE = 2

WRITE_TO_DATABASE = 1

WRITE_TO_INDIVIDUAL_FILE = 4

WRITE_TO_CASSANDRA = 3

FEW_PRODUCTS = 1

ALL_PRODUCTS = 2

ON = "ON"

OFF = "OFF"

CURRENCY = "MXN"

# This Dicttionary has 'Category' as key and corresponding dictionary
# has FILE_NAMES
#
# page - stores 'SUB_CATEGORY' URLs
# product - stores 'PRODUCT' URLs
# success - stores successfully completed 'SUB_CATEGORY' URLs
# output - stores respective OUTPUT file name
# file_names = {
#     "belleza": {
#         "page": path + "/belleza/belleza_page_urls.txt",
#         "product":path + "/belleza/belleza_prod_urls.txt",
#         "success": path + "/belleza/belleza_success.txt",
#         "output": path + "/belleza/belleza_products.json",
#         "completed_products": path + "/belleza/belleza_collected_products.txt"
#     },
#     "celulares": {
#         "page": path + "/celulares/celulares_page_urls.txt",
#         "product": path + "/celulares/celulares_prod_urls.txt",
#         "success": path + "/celulares/celulares_success.txt",
#         "output": path + "/celulares/celulares_products.json",
#         "completed_products": path + "/celulares/celulares_collected_products.txt"
#     },
#     "computacion": {
#         "page": path + "/computacion/computacion_page_urls.txt",
#         "product": path + "/computacion/computacion_prod_urls.txt",
#         "success": path + "/computacion/computacion_success.txt",
#         "output": path + "/computacion/computacion_products.json",
#         "completed_products": path + "/computacion/computacion_collected_products.txt"
#     },
#     "consolas": {
#         "page": path + "/consolas/consolas_page_urls.txt",
#         "product": path +"/consolas/consolas_prod_urls.txt",
#         "success": path + "/consolas/consolas_success.txt",
#         "output": path + "/consolas/consolas_products.json",
#         "completed_products": path + "/consolas/consolas_collected_products.txt"
#     },
#     "deportes": {
#         "page": path + "/deportes/deportes_page_urls.txt",
#         "product": path + "/deportes/deportes_prod_urls.txt",
#         "success": path + "/deportes/deportes_success.txt",
#         "output": path + "/deportes/deportes_products.json",
#         "completed_products": path + "/deportes/deportes_collected_products.txt"
#     },
#     "electrodomesticos": {
#         "page": path + "/electrodomesticos/electrodomesticos_page_urls.txt",
#         "product": path + "/electrodomesticos/electrodomesticos_prod_urls.txt",
#         "success": path + "/electrodomesticos/electrodomesticos_success.txt",
#         "output": path + "/electrodomesticos/electrodomesticos_products.json",
#         "completed_products": path + "/electrodomesticos/electrodomesticos_collected_products.txt"
#     },
#     "hogar": {
#         "page": path + "/hogar/hogar_page_urls.txt",
#         "product": path + "/hogar/hogar_prod_urls.txt",
#         "success": path + "/hogar/hogar_success.txt",
#         "output": path + "/hogar/hogar_products.json",
#         "completed_products": path + "/hogar/hogar_collected_products.txt"
#     },
#     "juguetes": {
#         "page": path + "/juguetes/juguetes_page_urls.txt",
#         "product":path + "/juguetes/juguetes_prod_urls.txt",
#         "success": path + "/juguetes/juguetes_success.txt",
#         "output": path + "/juguetes/juguetes_products.json",
#         "completed_products": path + "/juguetes/juguetes_collected_products.txt"
#     },
#     "moda": {
#         "page": path + "/moda/moda_page_urls.txt",
#         "product": path + "/moda/moda_prod_urls.txt",
#         "success": path + "/moda/moda_success.txt",
#         "output": path + "/moda/moda_products.json",
#         "completed_products": path + "/moda/moda_collected_products.txt"
#     },
#     "salud": {
#         "page": path + "/salud/salud_page_urls.txt",
#         "product": path + "/salud/salud_prod_urls.txt",
#         "success": path + "/salud/salud_success.txt",
#         "output": path + "/salud/salud_products.json",
#         "completed_products": path + "/salud/salud_collected_products.txt"
#     },
#     "tv": {
#         "page": path + "/tv/tv_page_urls.txt",
#         "product": path + "/tv/tv_prod_urls.txt",
#         "success": path + "/tv/tv_success.txt",
#         "output": path + "/tv/tv_products.json",
#         "completed_products": path + "/tv/tv_collected_products.txt"
#     },
# }


MAX_RETRIES = 5


# response status code if 200 then we got good response
GOOD_STATUS = 200

# response status code if 404 then that page does not exists
BAD_STATUS = 404


PROXY = {"http": ""}

# REquest headers to pass them in request.get arguments to look like request is comming from browser instead of script
REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",

    "User-Agent": "",
}

HEADERS_LIST = [
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.140 Chrome/64.0.3282.140 Safari/537.36']
