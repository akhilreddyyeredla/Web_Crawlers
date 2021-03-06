from Queue import Queue

import Etsy_DataCollectors_configuration as DataCollectors_Configuration
from Etsy.product_info_collectors import accessories_products_info_collector, art_and_collectibles_products_info_collector, bags_and_purses_products_info_collector, bath_and_beauty_products_info_collector, books_movies_and_music_products_info_collector, clothing_products_info_collector, craft_supplies_and_tools_products_info_collector, electronics_and_accessories_products_info_collector, home_and_living_products_info_collector, jewelry_products_info_collector, paper_and_party_supplies_products_info_collector, pet_supplies_products_info_collector, shoes_products_info_collector, toys_and_games_products_info_collector, weddings_products_info_collector
import response_getter
import Etsy.CONSTANTS as CONSTANTS
import Etsy.path_CONSTANTS as path_CONSTANTS
import time
from Etsy.product_parsers.bags_and_purses_get_product_info import *
from Etsy.product_parsers.paper_and_party_supplies_get_product_info import *

import json
from datetime import date
from Etsy.product_parsers.electronics_and_accessories_get_product_info import *
import uuid
import os
import product_info_storage
import completed_queue
from print_exception import print_exception
from Etsy.product_parsers.pet_supplies_get_product_info import *
from Etsy.general import *
import sys
from Etsy.product_parsers import accessories_get_product_info
from Etsy.product_parsers import art_and_collectibles_get_product_info
from Etsy.product_parsers import bags_and_purses_get_product_info
from Etsy.product_parsers import bath_and_beauty_get_product_info
from Etsy.product_parsers import books_movies_and_music_get_product_info
from Etsy.product_parsers import clothing_get_product_info
from Etsy.product_parsers import craft_supplies_and_tools_get_product_info
from Etsy.product_parsers import electronics_and_accessories_get_product_info
from Etsy.product_parsers import home_and_living_get_product_info
from Etsy.product_parsers import jewelry_get_product_info
from Etsy.product_parsers import paper_and_party_supplies_get_product_info
from Etsy.product_parsers import pet_supplies_get_product_info
from Etsy.product_parsers import shoes_get_product_info
from Etsy.product_parsers import toys_and_games_get_product_info
from Etsy.product_parsers import weddings_get_product_info


from Etsy.product_parsers.jewelry_get_product_info import *
import datetime
from Etsy.scrappers import accessories_scrapper, art_and_collectibles_scrapper, bags_and_purses_scrapper, bath_and_beauty_scrapper, books_movies_and_music_scrapper, clothing_scrapper, craft_supplies_and_tools_scrapper, electronics_and_accessories_scrapper, home_and_living_scrapper, jewelry_scrapper, paper_and_party_supplies_scrapper, pet_supplies_scrapper, shoes_scrapper, toys_and_games_scrapper, weddings_scrapper
from Etsy.product_parsers.books_movies_and_music_get_product_info import *
import re
import threading

from Etsy.product_parsers.weddings_get_product_info import *
import sys
from Etsy.product_parsers.art_and_collectibles_get_product_info import *
from Etsy.product_parsers.clothing_get_product_info import *
from Etsy.general import file_to_set, append_to_file
from Etsy.product_parsers.accessories_get_product_info import *
from Etsy.product_parsers.shoes_get_product_info import *
import fnmatch
from bs4 import BeautifulSoup
import os
from Etsy.general import file_to_set, list_to_file, set_to_file,write_file
from Etsy.product_parsers.bath_and_beauty_get_product_info import *
import multiprocessing
from Etsy.product_urls_collectors import accessories_products_url_collector, art_and_collectibles_products_url_collector, bags_and_purses_products_url_collector, bath_and_beauty_products_url_collector, books_movies_and_music_products_url_collector, clothing_products_url_collector, craft_supplies_and_tools_products_url_collector, electronics_and_accessories_products_url_collector, home_and_living_products_url_collector, jewelry_products_url_collector, paper_and_party_supplies_products_url_collector, pet_supplies_products_url_collector, shoes_products_url_collector, toys_and_games_products_url_collector, weddings_products_url_collector

import time
from Etsy.product_parsers.craft_supplies_and_tools_get_product_info import *
from product_info_storage import store
from Etsy.product_parsers.home_and_living_get_product_info import *

from Etsy.product_parsers.toys_and_games_get_product_info import *
from print_exception import print_exception 
