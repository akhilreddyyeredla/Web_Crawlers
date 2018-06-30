##
## Global Configurations
##

PATH_STYLE = '/'

## Max number of threads you want to spwan
NO_OF_THEARDS = 40


## Which_part_to_collect

START_HIERARCHY_COLLECTION = False
START_URL_COLLECTION = False
START_INFO_COLLECTION = True

## Redis_output  path 

REDIS_OUTPUT_PATH = '/usr/datacollector/Data_store/Souq_Product_Details_Json/{}_details.txt'
REDIS_DELAY = 1800


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
SOUQ_HIRERACHY_ROOT_FOLDER = ROOT_FOLDER+'/SOUQ_NEW'+'/hierarchy'
SOUQ_URL_ROOT_FOLDER = ROOT_FOLDER +'/SOUQ_NEW'+ '/url'
SOUQ_INFO_ROOT_FOLDER = ROOT_FOLDER +'/SOUQ_NEW'+ '/info'

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
###
SOUQ_MAIN_URL = "https://uae.souq.com/ae-en/shop-all-categories/c/?ref=nav"

SOUQ_PROJECT_NAME = 'Souq_test_1'

#SOUQ_CATEGORY_LIST = ['Electronics'];
#, 'Cameras', 'Coins_Stamps_and_Paper_money', 'Computers_IT_and_Networking', 'Electronics', 'Eyewear_and_Optics', 'Furniture', 'Gaming', 'Garden_and_Outdoor', 'Grocery_Food_and_Beverages', 'Health_and_Personal_Care', 'Home_Appliances', 'Home_Decor_and_Furniture', 'Jewelry_and_Accessories', 'Beauty','Baby', 'Bed_and_Bath','Books', 'Apparel_Shoes_and_Accessories','Art_Crafts_and_Collectibles']

#SOUQ_CATEGORY_LIST  = ['Kitchen_and_Home_Supplies', 'Kitchen_Appliances', 'Mobile_Phones_Tablets_and_Accessories', 'Music_and_Movies', 'Office_Products_and_Supplies']

SOUQ_CATEGORY_LIST = ['Garden_and_Outdoor']
#, 'Pet_Food_and_Supplies', 'Sports_and_Fitness', 'Tools_and_Home_Improvements', 'Toys', 'Vehicle_Parts_and_Accessories', 'Vouchers_and_Tickets', 'Wearable_Technology_Devices']

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
###

'''Constants '''



# categories names
APPAREL_SHOES_AND_ACCESSORIES = 'Apparel_Shoes_and_Accessories'
ART_CRAFTS_AND_COLLECTIBLES = 'Art_Crafts_and_Collectibles'
BABY = 'Baby'
BEAUTY = 'Beauty'
BED_AND_BATH = 'Bed_and_Bath'
BOOKS = 'Books'
CAMERAS = 'Cameras'
COINS_STAMPS_AND_PAPER_MONEY = 'Coins_Stamps_and_Paper_money'
COMPUTERS_IT_AND_NETWORKING = 'Computers_IT_and_Networking'
ELECTRONICS = 'Electronics'
EYEWEAR_AND_OPTICS = 'Eyewear_and_Optics'
FURNITURE = 'Furniture'
GAMING = 'Gaming'
GARDEN_AND_OUTDOOR = 'Garden_and_Outdoor'
GROCERY_FOOD_AND_BEVERAGES = 'Grocery_Food_and_Beverages'
HEALTH_AND_PERSONAL_CARE = 'Health_and_Personal_Care'
HOME_APPLIANCES = 'Home_Appliances'
HOME_DECOR_AND_FURNITURE = 'Home_Decor_and_Furniture'
JEWELRY_AND_ACCESSORIES = 'Jewelry_and_Accessories'
KITCHEN_AND_HOME_SUPPLIES = 'Kitchen_and_Home_Supplies'
KITCHEN_APPLIANCES = 'Kitchen_Appliances'
MOBILE_PHONES_TABLETS_AND_ACCESSORIES = 'Mobile_Phones_Tablets_and_Accessories'
MUSIC_AND_MOVIES = 'Music_and_Movies'
OFFICE_PRODUCTS_AND_SUPPLIES = 'Office_Products_and_Supplies'
PERFUMES_AND_FRAGRANCES = 'Perfumes_and_Fragrances'
PET_FOOD_AND_SUPPLIES = 'Pet_Food_and_Supplies'
SPORTS_AND_FITNESS = 'Sports_and_Fitness'
TOOLS_AND_HOME_IMPROVEMENTS = 'Tools_and_Home_Improvements'
TOYS = 'Toys'
VEHICLE_PARTS_AND_ACCESSORIES = 'Vehicle_Parts_and_Accessories'
VOUCHERS_AND_TICKETS = 'Vouchers_and_Tickets'
WEARABLE_TECHNOLOGY_DEVICES = 'Wearable_Technology_Devices'

# Main website name
PROJECT_NAME = "Souq_UAE"

# Domain name of website
PROJECT_DOMAIN = 'www.souq.com'


# response status code if 200 then we got good response
GOOD_STATUS = 200

# response status code if 404 then that page does not exists
BAD_STATUS = 404

# to compare with config.write_to value
WRITE_TO_DB = 1

# to compare with config.write_to value
WRITE_TO_FILE = 2

# Write to cassandra
WRITE_TO_CASSANDRA = 3

# Write to Multiple_file
WRITE_TO_MULTIPLE_FILE = 4

# to compare with config.url_flag value
URL_FLAG = 1

#to compare with config.info_flag value
PRODUCT_FlAG = 1


COMPLETED_PAGE = 'products_page_completed.txt'

MAX_RETRIES = 5

HEADERS_LIST = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.140 Chrome/64.0.3282.140 Safari/537.36' ]

PROXY_LIST = []

PROXY = {"https": ""}

HEADERS = {
    "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9", "Connection": "keep-alive",
    "Content-Type" : "application/json;charset=UTF-8",
    "User-Agent": ''
    }
