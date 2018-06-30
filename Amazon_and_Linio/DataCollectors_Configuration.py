# coding=utf-8
##
## Global Configurations
##

PATH_STYLE = '/'

## Max number of threads you want to spwan
NO_OF_THEARDS = 4


## Which_part_to_collect

START_HIERARCHY_COLLECTION = False
START_URL_COLLECTION = False
START_INFO_COLLECTION = True


## MySQL database configuration file
MYSQL_USER_NAME = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_HOST = 'localhost'
MYSQL_DB_name = 'amazon_uk'

## Cassandra database configuration file
Cassandra_USER_NAME = 'root'
Cassandra_PASSWORD = 'root'
Cassandra_HOST = '127.0.0.1'
Cassandra_DB_name = 'market_place_data'

# BigQuery key path
key_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/My_key.json'
dataset_id = 'test_dataset'
table_id = 'test_table'



## Root folder where you want to save all files

ROOT_FOLDER = '/usr/datacollector/Data_store'

DEBUG = 'ON'

ROOT_FOLDER = '/usr/datacollector/Data_store'

LINIO_MEX_HIERARCHY_ROOT = '/home/eunimart/Work/Amazon_data/Linio_test/hierarchy'
LINIO_MEX_URL_ROOT = '/home/eunimart/Work/Amazon_data/Linio_test/url'
LINIO_MEX_INFO_ROOT = '/home/eunimart/Work/Amazon_data/Linio_test/info'

# 1 to write into  sql_db
# 2 to write into file
# 3 to write into cassandra
# 4 to wrtie into bigQuery
WRITE_TO = 4

# Flag is used to collect sample data or all data
# 1 to collect sample data
# 2 to collect all the data

PRODUCT_INFO_FLAG = 1
PRODUCT_URL_FLAG = 1

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

# Proxy_on is a controller which controls the usage of proxy if
# True then it will send request through proxy if flase it will send through our ip address

PROXY_ON = True

##
## Project / Data Collector specific configurations
##

AMAZON_AUS_PROJECT_NAME = 'AMAZON_AUSTRALIA_1'
# possible categories
'''
category_list = ['Health_and_Beauty', 'Electronics_Computers_and_Office', 'Home_Improvement',
                 'Sports_Fitness_and_Outdoors', 'Books_and_Audible', 'Toys_Kids_and_Baby', 'Home_and_Kitchen', 'Fashion']
'''
AMAZON_AUS_CATEGORY_LIST = ['Sports_Fitness_and_Outdoors']

###

AMAZON_CANADA_PROJECT_NAME = 'AMAZON_CANADA_1'

# possible categories
'''
category_list = ['Music', 'Home_Kitchen_and_Pets', 'Clothing_Shoes_and_Jewelry', 'Software',
                 'Health_Beauty_and_Grocery', 'Books_and_Audible', 'Tools_Patio_and_Garden', 'Toys_and_Baby',
                 'Video_Games', 'Automotive_and_Industrial', 'Sports_and_Outdoors', 'Handmade',
                 'Electronics']
'''

AMAZON_CANADA_CATEGORY_LIST = ['Clothing_Shoes_and_Jewelry']

###

AMAZON_FRANCE_PROJECT_NAME = 'AMAZON_FRANCE_1'

# possible categories
'''
category_list = ['Beaute__Sante__E_picerie', 'Jouets_Enfants_et_Be_be_s', 'Ve_tements_Chaussures_Bijoux',
                 'Maison_Bricolage_Animalerie', 'High_Tech_et_Informatique', 'Auto_et_Moto', 'Musique_DVD_et_Blu_ray',
                 'Livres_and_Audible', 'Jeux_vide_o_et_Consoles', 'Commerce_Industrie_et_Science', 'Sports_et_Loisirs',
                 'Handmade']
'''

AMAZON_FRANCE_CATEGORY_LIST = ['Ve_tements_Chaussures_Bijoux']

###

AMAZON_GERMANY_PROJECT_NAME = 'AMAZON_GERMANY_1'

# possible categories
'''
category_list = [ 'Kleidung_Schuhe_and_Uhren', 'Haushalt_Garten_Baumarkt',
                 'Auto_Motorrad_and_Gewerbe', 'Handmade_and_Amazon_Launchpad', 'Spielzeug_and_Baby',
                 'Sport_and_Freizeit', 'Filme_Serien_Musik_and_Games', 'Elektronik_and_Computer',
                 'Beauty_Drogerie_and_Lebensmittel']
'''

AMAZON_GERMANY_CATEGORY_LIST = ['Spielzeug_and_Baby']

###

AMAZON_ITALY_PROJECT_NAME = 'AMAZON_ITALY_1'

# possible categories
'''
category_list = ['Musica_Film_e_TV', 'Videogiochi_e_Console', 'Alimentari_e_Cura_della_casa',
                 'Elettronica_e_Informatica', 'Commercio_Industria_e_Scienza', 'Sport_e_tempo_libero',
                 'Libri_e_Audible', 'Casa_Giardino_Fai_da_te_e_Animali', 'Giochi_e_Prima_infanzia',
                 'Bellezza_e_Salute', 'Abbigliamento_Scarpe_e_Gioielli', 'Auto_e_Moto',
                 'Handmade']
'''

AMAZON_ITALY_CATEGORY_LIST = ['Videogiochi_e_Console']

###

AMAZON_MEXICO_PROJECT_NAME = 'AMAZON_Mexico_1'

# possible categories
'''
category_list = ['Automotriz_y_Motocicletas', 'Bebe_', 'Co_mputo_y_Tablets', 'Deportes_y_Aire_Libre', 'Electro_nicos',
                 'Handmade', '', 'Hogar_y_Cocina', 'Industria_Empresas_y_Ciencia',
                 'Juegos_y_Juguetes', 'Libros', 'Mascotas_y_Accesorios', 'Peli_culas_Series_de_TV_y_Mu_sica',
                 'Ropa_Zapatos_y_Accesorios', 'Salud_Belleza_y_Cuidado_Personal', 'Software', 'Videojuegos']
'''

AMAZON_MEXICO_CATEGORY_LIST = ['Salud_Belleza_y_Cuidado_Personal']

###

AMAZON_SPAIN_PROJECT_NAME = 'AMAZON_SPAIN_1'

# possible categories
'''
category_list = ['Informa_tica_y_Oficina', 'Videojuegos', 'Deportes_y_aire_libre', 'Electro_nica',
                 'Industria_empresas_y_ciencia', 'Coche_y_moto', 'Hogar_Jardi_n_Bricolaje_y_Mascotas',
                 'Alimentacio_n_y_bebidas', 'Juguetes_y_Bebe_', 'Libros', 'Belleza_y_Salud',
                 'Cine_TV_y_Mu_sica', 'Handmade', 'Moda']
'''

AMAZON_SPAIN_CATEGORY_LIST = ['Handmade']

###

AMAZON_UK_PROJECT_NAME = 'AMAZON_Uk_1'

# possible categories
'''
category_list = ['Amazon_Pantry', 'Books_and_Audible', 'Business_Industry_and_Science', 'Car_and_Motorbike',
                 'Clothes_Shoes_and_Watches', 'Electronics_and_Computers', 'Handmade', 'Health_and_Beauty',
                 'Home_Garden_Pets_and_DIY', 'Movies_TV_Music_and_Games', 'Sports_and_Outdoors', 'Toys_Children_and_Baby']
'''

AMAZON_UK_CATEGORY_LIST = ['Home_Garden_Pets_and_DIY']

###

AMAZON_US_PROJECT_NAME = 'AMAZON_US_1'

# possible categories
'''
category_list = ['amazon_global', 'books', 'home_garden_and_tools', 'beauty_and_health', 
                'toys_and_games', 'sports_and_outdoor', 'clothing', 'electronics', 'handmade']
'''

AMAZON_US_CATEGORY_LIST = ['clothing']

###

# Root folder where you want to save all files
ETSY_PROJECT_NAME = "ETSY_TEST_15"

# Category list is used to collect specific category urls
'''
category_list = ['accessories', 'art_and_collectabls', 'art_and_collectibles', 'bags_and_purses', 'bath_and_beauty',
                 'books_movies_and_music', 'clothing', 'craft_supplies_and_tools', 'electronics_and_accessories',
                 'home_and_living', 'jewelry', 'paper_and_party_supplies', 'pet_supplies', 'shoes', 'toys_and_games',
                 'weddings']
'''

ETSY_CATEGORY_LIST = ['clothing']

###

SOUQ_PROJECT_NAME = 'Souq_test_1'

SOUQ_CATEGORY_LIST = ['Grocery_Food_and_Beverages']
'''
 ['Beauty','Baby', 'Bed_and_Bath','Books', 'Apparel_Shoes_and_Accessories','Art_Crafts_and_Collectibles','Electronics'
 'Cameras', 'Coins_Stamps_and_Paper_money', 'Computers_IT_and_Networking', 'Electronics', 'Eyewear_and_Optics',
 'Furniture', 'Gaming', 'Garden_and_Outdoor', 'Grocery_Food_and_Beverages', 'Health_and_Personal_Care',
 'Home_Appliances', 'Home_Decor_and_Furniture', 'Jewelry_and_Accessories', 'Kitchen_and_Home_Supplies',
 'Kitchen_Appliances', 'Mobile_Phones_Tablets_and_Accessories', 'Music_and_Movies', 'Office_Products_and_Supplies',
 'Perfumes_and_Fragrances', 'Pet_Food_and_Supplies', 'Sports_and_Fitness', 'Tools_and_Home_Improvements', 'Toys',
 'Vehicle_Parts_and_Accessories', 'Vouchers_and_Tickets', 'Wearable_Technology_Devices']
'''
###

EBAY_PROJECT_NAME = "EBay"
EBAY_CATEGORY_LIST = ['Motors']

# 'Motors'
# 'Fashion'
# 'Electronics'
# 'Collectibles_AND_Art'
# 'Home_AND_Garden'
# 'Sporting_Goods'
# 'Toys_AND_Hobbies'
# 'Business_AND_Industrial'
# 'Music''
###

URL_SUFFIX = '&q[gallery_style]=1&q[page]=1&q[per_page]=48&q[sort_by]=relevancy'

MAX_RETRIES = 2

BONANZA_MAIN_URL = "https://www.Bonanza.com/booths/browse_categories"

BONANZA_PROJECT_NAME = 'Bonanza_test_3'

DOMAIN_NAME = 'https://www.Bonanza.com'

# CATEGORY_LIST = ['antiques','art','baby','books','business','cameras','cell_phones',\
# 'coins','collectibles','computers','consumer_electronics','crafts',\
# 'digital_goods','dolls','dvds_movies','entertainment','everything_else',\
# 'fashion','health_beauty','home_garden','jewellery','music','musical_instruments',\
# 'pet_supplies','pottery','speciality_services','sporting_goods','sports_mem',\
# 'stamps','tickets','toys','travel','video_games']


BONANZA_CATEGORY_LIST = ['antiques']

BONANZA_PATTERN_3 = '*_url_link.txt'
BONANZA_PATTERN_4 = '*_url_completed.txt'

###

LINIO_MAX_RETRIES = 2

LINIO_NO_OF_PRODUCTS = 50

# 1 to configurable number of PRODUCTS' details
# 2 to collect ALL PRODUCTS' details
LINIO_PRODUCTS_FLAG = 1

# 1 to write to single FILE
# 2 to write to DATABASE
# 3 to write to INDIVIDUAL FILES
LINIO_STORAGE_FLAG = 1

LINIO_SLEEP_TIME = 4

LINIO_PROJECT_NAME = 'LINIO_TEST'

LINIO_MEX_PROJECT_NAME = "Linio_Mex"



'''
['Salud_y_Bienestar', 'Hogar', 'Celulares', 'Moda',
 'Deportes', 'Electrodomésticos', 'TV_Audio_y_Video',
  'Consolas_y_Videojuegos', 'Juguetes_niños_y_bebés',
   'Belleza', 'Computación']
'''
LINIO_MEX_CATEGORIES = ['Salud_y_Bienestar'] #, 'Hogar', 'Celulares', 'Moda',
#  'Deportes', 'Electrodomésticos', 'TV_Audio_y_Video',
#   'Consolas_y_Videojuegos', 'Juguetes_niños_y_bebés',
#    'Belleza', 'Computación']

###


###
