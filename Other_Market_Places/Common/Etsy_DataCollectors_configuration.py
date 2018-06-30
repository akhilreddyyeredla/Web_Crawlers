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
ETSY_ROOT_FOLDER = ROOT_FOLDER + '/ETSY'
ETSY_HIERARCHY_ROOT_FOLDER = ETSY_ROOT_FOLDER + '/HIERARCHY'
ETSY_URL_ROOT_FOLDER = ETSY_ROOT_FOLDER + '/URL'
ETSY_INFO_ROOT_FOLDER = ETSY_ROOT_FOLDER + '/INFO'
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

# Root folder where you want to save all files
ETSY_PROJECT_NAME = "ETSY_TEST_15"

# Category list is used to collect specific category urls
'''
category_list = ['accessories', 'art_and_collectabls', 'art_and_collectibles', 'bags_and_purses', 'bath_and_beauty',
                 'books_movies_and_music', 'clothing', 'craft_supplies_and_tools', 'electronics_and_accessories',
                 'home_and_living', 'jewelry', 'paper_and_party_supplies', 'pet_supplies', 'shoes', 'toys_and_games',
                 'weddings']
'''

ETSY_CATEGORY_LIST = ['accessories', 'art_and_collectabls', 'art_and_collectibles', 'bags_and_purses', 'bath_and_beauty',
                 'books_movies_and_music', 'clothing', 'craft_supplies_and_tools', 'electronics_and_accessories',
                 'home_and_living', 'jewelry', 'paper_and_party_supplies', 'pet_supplies', 'shoes', 'toys_and_games',
                 'weddings']

#ETSY_CATEGORY_LIST = ['accessories', 'art_and_collectabls', 'art_and_collectibles', 'bags_and_purses', 'bath_and_beauty',
                 #'books_movies_and_music', 'clothing', 'craft_supplies_and_tools', 'electronics_and_accessories',
                 #'home_and_living', 'jewelry', 'paper_and_party_supplies', 'pet_supplies', 'shoes', 'toys_and_games',
                 #'weddings']

'''*****************************CONSTANTS****************************************'''
# Main website name
MARKET_PLACE_NAME = "Etsy"

# Domain name of website
DOMAIN_NAME = 'www.etsy.com'

# max retires that are allowed
MAX_RETRIES = 5

# GOOD status resposne 200
GOOD_STATUS = 200

# BAD status response 503 it means amazon has blocked us
BAD_STATUS = 503

# Page not found response 404
PAGE_NOT_FOUND = 404

# to write into MySql
WRITE_TO_DB = 1

# to write into file
WRITE_TO_FILE = 2

# to Write into Cassandra
WRITE_TO_CASSANDRA = 3

# to compare with config.url_flag value
URL_FLAG = 1

# to compare with config.info_flag value
PRODUCT_FlAG = 1

# Categories List
ACCESSORIES = 'accessories'
ART_AND_COLLECTIBLES = 'art_and_collectibles'
BAGS_AND_PURSES = 'bags_and_purses'
BATH_AND_BEAUTY = 'bath_and_beauty'
BOOKS_MOVIES_AND_MUSIC = 'books_movies_and_music'
CLOTHING = 'clothing'
CRAFT_SUPPLIES_AND_TOOLS = 'craft_supplies_and_tools'
ELECTRONICS_AND_ACCESSORIES = 'electronics_and_accessories'
HOME_AND_LIVING = 'home_and_living'
JEWELRY = 'jewelry'
PAPER_AND_PARTY_SUPPLIES = 'paper_and_party_supplies'
PET_SUPPLIES = 'pet_supplies'
SHOES = 'shoes'
TOYS_AND_GAMES = 'toys_and_games'
WEDDINGS = 'weddings'

# main category links
ACCESSORIES_URL = 'https://www.etsy.com/in-en/search/accessories?explicit=1&use_mmx=1'
ART_AND_COLLECTIBLES_URL = 'https://www.etsy.com/in-en/search/art-and-collectibles?explicit=1&use_mmx=1'
BAGS_AND_PURSES_URL = 'https://www.etsy.com/in-en/search/bags-and-purses?explicit=1&use_mmx=1'
BATH_AND_BEAUTY_URL = 'https://www.etsy.com/in-en/search/bath-and-beauty?explicit=1&use_mmx=1'
BOOKS_MOVIES_AND_MUSIC_URL = 'https://www.etsy.com/in-en/search/books-movies-and-music?explicit=1&use_mmx=1'
CLOTHING_URL = 'https://www.etsy.com/in-en/search/clothing?explicit=1&use_mmx=1'
CRAFT_SUPPLIES_AND_TOOLS_URL = 'https://www.etsy.com/in-en/search/craft-supplies-and-tools?explicit=1&use_mmx=1'
ELECTRONICS_AND_ACCESSORIES_URL = 'https://www.etsy.com/in-en/search/electronics-and-accessories?explicit=1&use_mmx=1'
HOME_AND_LIVING_URL = 'https://www.etsy.com/in-en/search/home-and-living?explicit=1&use_mmx=1'
JEWELRY_URL = 'https://www.etsy.com/in-en/search/jewelry?explicit=1&use_mmx=1'
PAPER_AND_PARTY_SUPPLIES_URL = 'https://www.etsy.com/in-en/search/paper-and-party-supplies?explicit=1&use_mmx=1'
PET_SUPPLIES_URL = 'https://www.etsy.com/in-en/search/pet-supplies?explicit=1&use_mmx=1'
SHOES_URL = 'https://www.etsy.com/in-en/search/shoes?explicit=1&use_mmx=1'
TOYS_AND_GAMES_URL = 'https://www.etsy.com/in-en/search/toys-and-games?explicit=1&use_mmx=1'
WEDDINGS_URL = 'https://www.etsy.com/in-en/search/weddings?explicit=1&use_mmx=1'

# constants used name files in that directory  in place of {} category name will written while running
CATEGORY_COMPLETED = '/category_completed_{}.txt'
CATEGORY_QUEUE = '/category_queue_{}.txt'
SKIPPED_COMPLETD = '/skipped_completed_{}.txt'
SKIPPED_QUEUE = '/skipped_queue_{}.txt'
SUB_CATEGORY_COMPLETED = '/sub_category_completed_{}.txt'
SUB_CATEGORY_QUEUE = '/sub_category_queue_{}.txt'
SUB_SUB_CATEGORY_COMPLETED = '/sub_sub_category_completed_{}.txt'
SUB_SUB_CATEGORY_QUEUE = '/sub_sub_category_queue_{}.txt'

# This is the file name which will searched recursivly in a category folder while product info collection
PODUCTS_PAGE = 'products_page_links.txt'
COMPLETED_PAGE = 'products_page_completed.txt'

PROXY = {"http": ""}

# Superset filed names
HEADERS = "(`ProductSKU`,           `ProductDate` ,           `ProductTime`,               `ProductMarketplace`," \
          " `ProductDomain`,        `ProductCategory`,        `ProductSubCategory1`,       `ProductSubCategory2`," \
          " `ProductSubCategory3`,  `ProductSubCategory4`,    `ProductSubCategory5`,       `ProductSubCategory6`," \
          " `ProductSubCategory7`,  `ProductSubCategory8`,    `ProductSubCategory9`,       `ProductCondition`," \
          " `ProductSavedPrice`,    `ProductAddedDate`,       `ProductAdditionalPolicies`, `ProductAvailability`," \
          " `ProductBrand`,         `ProductDescription`,     `ProductDiscountPercentage`, `ProductSellingPrice`, " \
          " `ProductEAN`,           `ProductHighlights`,      `ProductId`,                 `ProductImageUrl`," \
          " `ProductISBN`,          `ProductLikes`,           `ProductMPN`,                 `ProductName`," \
          " `ProductNoOfReviews`,   `ProductOriginalPrice`,   `Productrating`,              `ProductShippingPrice`," \
          " `ProductSize`,          `ProductSpecifications`,  `ProductUPC`,                 `ProductUrl`," \
          " `ProductsAvailable`,    `ProductsSold`,           `ProductReturnPolicies`,      `SellerCode`," \
          " `SellerLocation`,       `SellerName`,             `SellerNegativeRating`,       `SellerNeutralRating`, " \
          " `SellerPositiveRating`, `SellerOverallRating`,    `SellerRank`,                 `SellerYearOfJoining`," \
          " `ShippingAvailableCountries`, `ShippingLocation`, `ShippingLogisticName`,       `ShippingPrice`," \
          " `ShopLocation`,         `ShopName`,               `ShopNoOfSales`,              `ShopRating`," \
          "`TaxInformation`,        `ProductVisibility`,      `ProductWarranty`,            `ProductCurrency`,    " \
          "`ProductShippingPolicies`".replace(',', '|')

# REquest headers to pass them in request.get arguments to look like request is comming from browser instead of script
REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",

    "User-Agent": "",
}

HEADERS_LIST = [
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.140 Chrome/64.0.3282.140 Safari/537.36']
