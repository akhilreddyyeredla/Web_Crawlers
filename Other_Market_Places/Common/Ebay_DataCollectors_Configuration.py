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
ROOT_FOLDER_EBAY = ROOT_FOLDER + '/EBAY'
ROOT_FOLDER_EBAY_HIERARCHY = ROOT_FOLDER_EBAY + '/HIERARCHY'
ROOT_FOLDER_EBAY_URL = ROOT_FOLDER_EBAY + '/URL'
ROOT_FOLDER_EBAY_INFO = ROOT_FOLDER_EBAY + '/INFO'
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

EBAY_PROJECT_NAME = "EBay"
EBAY_CATEGORY_LIST = ['Music']
#'Fashion', 'Electronics', 'Collectibles_AND_Art', 'Home_AND_Garden', 'Sporting_Goods', 'Toys_AND_Hobbies', 'Business_AND_Industrial', 'Music' ];

'''******************************CONSTANTS******************************'''

#Main Website name
PROJECT_NAME = "EBAY"
main_url = 'https://www.ebay.com/v/allcategories'

# Domain name of website
PROJECT_DOMAIN = 'www.ebay.com'

# max retires that are allowed
MAX_RETRIES = 5

# GOOD status resposne 200
GOOD_STATUS = 200

# BAD status response 503 it means amazon has blocked us
BAD_STATUS = 503

# to compare with config.write_to value
WRITE_TO_MYSQL = 1

# to compare with config.write_to value
WRITE_TO_FILE = 2

WRITE_TO_CASSANDRA = 3

WRITE_TO_BIG_QUERY = 5

# to compare with config.url_flag value
URL_FLAG = 1

#to compare with config.info_flag value

PRODUCT_FlAG = 1
HEADERS_LIST = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.140 Chrome/64.0.3282.140 Safari/537.36' ]

PROXY_LIST = []

PROXY = {"https": ""}

HEADERS = {
    "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9", "Connection": "keep-alive",
    "Content-Type" : "application/json;charset=UTF-8",
    "User-Agent": ''
}


# Categories List
MOTORS = 'Motors'
FASHION = 'Fashion'
ELECTRONICS = 'Electronics'
COLLECTIBLES = 'Collectibles_AND_Art'
HOME = 'Home_AND_Garden'
SPORT = 'Sporting_Goods'
TOYS = 'Toys_AND_Hobbies'
BUSINESS = 'Business_AND_Industrial'
MUSIC = 'Music'


# constants used name files in that directory  in place of {} category name will written while running
CATEGORY_COMPLETED = '/category_completed_{}.txt'
CATEGORY_QUEUE = '/category_queue_{}.txt'
SKIPPED_COMPLETD = '/skipped_completed_{}.txt'
SKIPPED_QUEUE = '/skipped_queue_{}.txt'
SUB_CATEGORY_COMPLETED = '/sub_category_completed_{}.txt'
SUB_CATEGORY_QUEUE = '/sub_category_queue_{}.txt'
SUB_SUB_CATEGORY_COMPLETED = '\sub_sub_category_completed_{}.txt'
SUB_SUB_CATEGORY_QUEUE = '/sub_sub_category_queue_{}.txt'

# This is the file name which will searched recursivly in a category folder while product info collection
PODUCTS_PAGE = 'products_page_links.txt'


COMPLETED_FILE = "COMPLETED.txt"


#Main urls
Motors = '{}/Motors/Motors.txt'
Fashion = '{}/Fashion/Fashion.txt'
Electronics = '{}/Electronics/Electronics.txt'
Collectibles_arts = '{}/Collectibles_AND_Art/Collectibles_AND_Art.txt'
Home_Garden = '{}/Home_AND_Garden/Home_AND_Garden.txt'
Sports_Goods = '{}/Sporting_Goods/Sporting_Goods.txt'
Toys_Hobbies = '{}/Toys_AND_Hobbies/Toys_AND_Hobbies.txt'
Business = '{}/Business_AND_Industrial/Business_AND_Industrial.txt'
Music = '{}/Music/Music.txt'

#completed main urls
motors_completed = '{}/Motors/Motors_COMPLETED.txt'
fashion_completed = '{}/Fashion/Fashion_COMPLETED.txt'
electronics_completed = '{}/Electronics/Electronics_COMPLETED.txt'
collectibles_completed = '{}/Collectibles_AND_Art/Collectibles_AND_Art_COMPLETED.txt'
home_completed = '{}/Home_AND_Garden/Home_AND_Garden_COMPLETED.txt'
sport_completed = '{}/Sporting_Goods/Sporting_Goods_COMPLETED.txt'
toys_completed = '{}/Toys_AND_Hobbies/Toys_AND_Hobbies_COMPLETED.txt'
business_completed = '{}/Business_AND_Industrial/Business_AND_Industrial_COMPLETED.txt'
music_completed = '{}/Music/Music_COMPLETED.txt'


#product_leaf_collection
motor_leaf = '{}/Motors/Motors_product_leaf.txt'
fashion_leaf = '{}/Fashion/Fashion_product_leaf.txt'
electronics_leaf = '{}/Electronics/Electronics_product_leaf.txt'
collectibles_leaf = '{}/Collectibles_AND_Art/Collectibles_AND_Art_product_leaf.txt'
home_leaf = '{}/Home_AND_Garden/Home_AND_Garden_product_leaf.txt'
sport_leaf = '{}/Sporting_Goods/Sporting_Goods_product_leaf.txt'
toy_leaf = '{}/Toys_AND_Hobbies/Toys_AND_Hobbies_product_leaf.txt'
music_leaf = '{}/Music/Music_product_leaf.txt'
Business_leaf = '{}/Business_AND_Industrial/Business_AND_Industrial.txt'


#completed pages
motor_pages = '{}/Motors/Motors_completed_pages.txt'
fashion_pages = '{}/Fashion/Fashion_completed_pages.txt'
electronics_pages = '{}/Electronics/Electronics_completed_pages.txt'
collectibles_pages = '{}/Collectibles_AND_Art/Collectibles_AND_Art_completed_pages.txt'
home_pages = '{}/Home_AND_Garden/Home_AND_Garden_completed_pages.txt'
sport_pages = '{}/Sporting_Goods/Sporting_Goods_completed_pages.txt'
toy_pages = '{}/Toys_AND_Hobbies/Toys_AND_Hobbies_completed_pages.txt'
bussiness_pages = '{}/Business_AND_Industrial/Business_AND_Industrial_completed_pages.txt'
music_pages = '{}/Music/Music_completed_pages.txt'

#product info paths
motor_info = '{}/Motors'
fashion_info = '{}/Fashion'
electronics_info = '{}/Electronics'
collectibles_info = '{}/Collectibles_AND_Art'
home_info = '{}/Home_AND_Garden'
sport_info = '{}/Sporting_Goods'
toy_info = '{}/Toys_AND_Hobbies'
business_info = '{}/Business_AND_Industrial'
music_info = '{}/Music'
