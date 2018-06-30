from Queue import Queue
import Ebay_DataCollectors_Configuration as DataCollectors_Configuration
from print_exception import print_exception
import EBAY.database
import uuid
#import EBAY.constant as constant
import threading
import requests
import fnmatch
from datetime import date
import bigquery_insert
import sys
import EBAY.product_info_storage
from datetime import datetime
import EBAY.database
import product_info_storage
import completed_queue
from datetime import time

import os
import json
import pymysql
from bs4 import BeautifulSoup as soup
import re
import time
import insert_into_cassandra
from EBAY.product_info_collector import bussiness_info_collector, collectibles_info_collector, electronics_info_collector, fashion_info_collector, home_info_collector, motor_info_collector, music_info_collector, sport_info_collector, toy_info_collector


from EBAY.product_leaf_collector import music, bussiness, motors, collectibles_arts, electronics, fashion, home_garden, toys_hobbies, sporting_goods
from EBAY.product_url_collection import bussiness_product_url_collection, collectibles_product_url_collection, electronics_product_url_collection, fashion_product_url_collection, home_product_url_collection, motor_product_url_collection, Music_product_url_collection, sport_product_url_collection, toy_product_url_collection