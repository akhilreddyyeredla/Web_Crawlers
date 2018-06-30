##
## Global Configurations
##

PATH_STYLE = '/'

## Max number of threads you want to spwan
NO_OF_THEARDS = 10


## Which_part_to_collect

START_HIERARCHY_COLLECTION = False
START_URL_COLLECTION = False
START_INFO_COLLECTION = True

## Redis_output  path 

REDIS_OUTPUT_PATH = '/usr/datacollector/Data_store/Souq_Product_Details_Json/{}_details.txt'
REDIS_DELAY = 60


## Big Query Configuration file
key_path = "/usr/datacollector/CBEC-Insights-91fbc0a4af35.json"
dataset_id = 'eu_cbec_bi_data'
table_id = 'marketplaces'


## MySQL database configuration file
MYSQL_USER_NAME = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_HOST = 'localhost'
MYSQL_DB_name = 'amazon_uk'

## Cassandra database configuration file
Cassandra_USER_NAME = 'root'
Cassandra_PASSWORD = 'Root@123456'
Cassandra_HOST = '35.200.145.21'
Cassandra_DB_name = 'marketplaces'


## Root folder where you want to save all files
ROOT_FOLDER = '/home/eunimart-04/eunimart_dev_akhil'
ROOT_FOLDER_BONANZA = ROOT_FOLDER + '/BONANZA'
ROOT_FOLDER_BONANZA_HIERARCHY = ROOT_FOLDER + '/HIERARCHY'
ROOT_FOLDER_BONANZA_URL = ROOT_FOLDER + '/URL'
ROOT_FOLDER_BONANZA_INFO = ROOT_FOLDER + '/INFO'

DEBUG = 'ON'

# 1 to write into  sql_db
# 2 to write into file
# 3 to write into cassandra
# 4 to write into multiple file
# 5 to write into BigQuery
# 6 to write into kafka
# 7 to write into redis
WRITE_TO = 7

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

# Proxy_on is a controller which controls the usage of proxy if
# True then it will send request through proxy if flase it will send through our ip address

PROXY_ON = False 

##
## Project / Data Collector specific configurations
##
URL_SUFFIX = '&q[gallery_style]=1&q[page]=1&q[per_page]=48&q[sort_by]=relevancy'

MAX_RETRIES = 2

BONANZA_MAIN_URL = "https://www.Bonanza.com/booths/browse_categories"

BONANZA_PROJECT_NAME = 'Bonanza_test_3'

DOMAIN_NAME = 'https://www.Bonanza.com'

'''
 CATEGORY_LIST = ['antiques','art','baby','books','business','cameras','cell_phones',\
 'coins','collectibles','computers','consumer_electronics','crafts',\
 'digital_goods','dolls','dvds_movies','entertainment','everything_else',\
 'fashion','health_beauty','home_garden','jewellery','music','musical_instruments',\
 'pet_supplies','pottery','speciality_services','sporting_goods','sports_mem',\
 'stamps','tickets','toys','travel','video_games']
'''

BONANZA_CATEGORY_LIST = ['antiques','art','baby','books','business',\
'cameras','cell_phones', 'coins','collectibles','computers',\
'consumer_electronics','crafts', 'digital_goods','dolls','dvds_movies',\
'entertainment','everything_else', 'fashion','health_beauty','home_garden',\
'jewellery','music','musical_instruments', 'pet_supplies','pottery',\
'speciality_services','sporting_goods','sports_mem', 'stamps','tickets',\
'toys','travel','video_games']


BONANZA_PATTERN_3 = '*_url_link.txt'
BONANZA_PATTERN_4 = '*_url_completed.txt'

'''**********CONSTANTS***************'''
# Main website name
PROJECT_NAME = "Bonanza_US"

# Domain name of website
PROJECT_DOMAIN = 'www.souq.com'

MAX_RETRIES = 5

# response status code if 200 then we got good response
GOOD_STATUS = 200

# response status code if 404 then that page does not exists
BAD_STATUS = 404

# to compare with config.write_to value
WRITE_TO_DB = 1

# to compare with config.write_to value
WRITE_TO_FILE = 2

# to compare with config.write_to value
WRITE_TO_CASSANDRA = 3

# to compare with config.write_to value
WRITE_TO_MULTIPLE_FILE = 4

# to compare with config.url_flag value
URL_FLAG = 1

# to compare with config.info_flag value
PRODUCT_FlAG = 1

CURRENCY = "USD"

ON = "ON"

# Main-category indices in browse-all categories page
ANTIQUES_INDEX = 0

ART_INDEX = 1

BABY_INDEX = 2

BOOKS_INDEX = 3

BUSINESS_INDEX = 4

CAMERAS_INDEX = 5

CELL_PHONES_INDEX = 6

COINS_INDEX = 7

COLLECTIBLES_INDEX = 8

COMPUTERS_INDEX = 9

CONSUMER_ELECTRONICS_INDEX = 10

CRAFTS_INDEX = 11

DIGITAL_GOODS_INDEX = 12

DOLLS_INDEX = 13

DVDS_MOVIES_INDEX = 14

ENTERTAINMENT_INDEX = 15

EVERYTHING_ELSE_INDEX = 16

FASHION_INDEX = 17

HEALTH_BEAUTY_INDEX = 18

HOME_GARDEN_INDEX = 19

JEWELLERY_INDEX = 20

MUSIC_INDEX = 21

MUSICAL_INSTRUMENTS_INDEX = 22

PARTS_ACCESORIES_INDEX = 23

PET_SUPPLIES_INDEX = 24

POTTERY_INDEX = 25

SPECIALITY_SERVICES_INDEX = 26

SPORTING_GOODS_INDEX = 27

SPORTS_MEM_INDEX = 28

STAMPS_INDEX = 29

TICKETS_INDEX = 30

TOYS_INDEX = 31

TRAVEL_INDEX = 32

VIDEO_GAMES_INDEX = 33

COMPLETED_INFO_FILE = 'product_url_completed.txt'

# Main-category names
ANTIQUES = 'antiques'

ART = 'art'

BABY = 'baby'

BOOKS = 'books'

BUSINESS = 'business'

CAMERAS = 'cameras'

CELL_PHONES = 'cell_phones'

COINS = 'coins'

COLLECTIBLES = 'collectibles'

COMPUTERS = 'computers'

CONSUMER_ELECTRONICS = 'consumer_electronics'

CRAFTS = 'crafts'

DIGITAL_GOODS = 'digital_goods'

DOLLS = 'dolls'

DVDS_MOVIES = 'dvds_movies'

ENTERTAINMENT = 'entertainment'

EVERYTHING_ELSE = 'everything_else'

FASHION = 'fashion'

HEALTH_BEAUTY = 'health_beauty'

HOME_GARDEN = 'home_garden'

JEWELLERY = 'jewellery'

MUSIC = 'music'

MUSICAL_INSTRUMENTS = 'musical_instruments'

PET_SUPPLIES = 'pet_supplies'

POTTERY = 'pottery'

SPECIALITY_SERVICES = 'speciality_services'

SPORTING_GOODS = 'sporting_goods'

SPORTS_MEM = 'sports_mem'

STAMPS = 'stamps'

TICKETS = 'tickets'

TOYS = 'toys'

TRAVEL = 'travel'

VIDEO_GAMES = 'video_games'

# product_info

ANTIQUES_INFO = 'Antiques'

ARTS_INFO = 'Art'

BABY_INFO = 'Baby'

BOOKS_INFO = 'Books'

BUSINESS_INFO = 'Business_and_Industrial'

CAMERAS_INFO = 'Cameras_and_Photo'

CELL_PHONES_INFO = 'Cell_Phones_and_Accessories'

COINS_INFO = 'Coins_and_Paper_Money'

COLLECTIBLES_INFO = 'Collectibles'

COMPUTERS_INFO = 'Computers_Tablets_and_Networking'

CONSUMER_ELECTRONICS_INFO = 'Consumer_Electronics'

CRAFTS_INFO = 'Crafts'

DIGITAL_GOODS_INFO = 'Digital_Goods'

DOLLS_INFO = 'Dolls_and_Bears'

DVDS_MOVIES_INFO = 'DVDs_and_Movies'

ENTERTAINMENT_INFO = 'Entertainment_Memorabilia'

EVERYTHING_ELSE_INFO = 'Everything Else'

FASHION_INFO = 'Fashion'

HEALTH_BEAUTY_INFO = 'Health_and_Beauty'

HOME_GARDEN_INFO = 'Home_and_Garden'

JEWELLERY_INFO = 'Jewelry_and_Watches'

MUSIC_INFO = 'Music'

MUSICAL_INSTRUMENTS_INFO = 'Musical_Instruments_and_Gear'

PARTS_ACCESORIES_INFO = 'Parts_and_Accessories'

PET_SUPPLIES_INFO = 'Pet_Supplies'

POTTERY_INFO = 'Pottery_and_Glass'

SPECIALITY_SERVICES_INFO = 'Specialty_Services'

SPORTING_GOODS_INFO = 'Sporting_Goods'

SPORTS_MEM_INFO = 'Sports Mem__Cards_and_Fan_Shop'

STAMPS_INFO = 'Stamps'

TICKETS_INFO = 'Tickets_and_Experiences'

TOYS_INFO = 'Toys & Hobbies'

TRAVEL_INFO = 'Travel'

VIDEO_GAMES_INFO = 'Video_Games_and_Consoles'


PROXY = {"http": ""}

# REquest headers to pass them in request.get arguments to look like request is comming from browser instead of script
REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",

    "User-Agent": "",
}

HEADERS_LIST = [
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.140 Chrome/64.0.3282.140 Safari/537.36']

