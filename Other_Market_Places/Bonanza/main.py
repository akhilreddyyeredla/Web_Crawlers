import sys

sys.path.insert(0, r'/usr/datacollector')

from hierarchy_collectors import antiques_hierarchy_collector, art_hierarchy_collector, baby_hierarchy_collector \
    , books_hierarchy_collector, business_hierarchy_collector, cameras_hierarchy_collector, \
    cell_phones_hierarchy_collector \
    , coins_hierarchy_collector, collectibles_hierarchy_collector, computers_hierarchy_collector, \
    consumer_electronics_hierarchy_collector \
    , crafts_hierarchy_collector, digital_goods_hierarchy_collector, dolls_hierarchy_collector, \
    dvds_movies_hierarchy_collector \
    , entertainment_hierarchy_collector, everything_else_hierarchy_collector, fashion_hierarchy_collector, \
    health_beauty_hierarchy_collector \
    , home_garden_hierarchy_collector, jewellery_hierarchy_collector, music_hierarchy_collector, \
    musical_instruments_hierarchy_collector \
    , pet_supplies_hierarchy_collector, pottery_hierarchy_collector, speciality_services_hierarchy_collector, \
    sporting_goods_hierarchy_collector \
    , sports_mem_hierarchy_collector, stamps_hierarchy_collector, tickets_hierarchy_collector, toys_hierarchy_collector, \
    travel_hierarchy_collector, \
    video_games_hierarchy_collector

from product_url_collectors import antiques_url_collector, art_url_collector, baby_url_collector \
    , books_url_collector, business_url_collector, cameras_url_collector, cell_phones_url_collector \
    , coins_url_collector, collectibles_url_collector, computers_url_collector, consumer_electronics_url_collector \
    , crafts_url_collector, digital_goods_url_collector, dolls_url_collector, dvds_movies_url_collector \
    , entertainment_url_collector, everything_else_url_collector, fashion_url_collector, health_beauty_url_collector \
    , home_garden_url_collector, jewellery_url_collector, music_url_collector, musical_instruments_url_collector \
    , pet_supplies_url_collector, pottery_url_collector, speciality_services_url_collector, sporting_goods_url_collector \
    , sports_mem_url_collector, stamps_url_collector, tickets_url_collector, toys_url_collector, travel_url_collector, \
    video_games_url_collector
from product_info_collectors import antiques_info_collector, art_info_collector, baby_info_collector \
    , books_info_collector, business_info_collector, cameras_info_collector, cell_phones_info_collector \
    , coins_info_collector, collectibles_info_collector, computers_info_collector, consumer_electronics_info_collector \
    , crafts_info_collector, digital_goods_info_collector, dolls_info_collector, dvds_movies_info_collector \
    , entertainment_info_collector, everything_else_info_collector, fashion_info_collector, health_beauty_info_collector \
    , home_garden_info_collector, jewellery_info_collector, music_info_collector, musical_instruments_info_collector \
    , pet_supplies_info_collector, pottery_info_collector, speciality_services_info_collector, \
    sporting_goods_info_collector \
    , sports_mem_info_collector, stamps_info_collector, tickets_info_collector, toys_info_collector, \
    travel_info_collector, video_games_info_collector
from threading import Thread
from CONSTANTS import *

from DataCollectors_Configuration import BONANZA_CATEGORY_LIST, START_URL_COLLECTION, START_INFO_COLLECTION, \
    START_HIERARCHY_COLLECTION

category_list = '|'.join(BONANZA_CATEGORY_LIST)


def start_info_collection():
    if ANTIQUES in category_list:
        thread_1 = Thread(target=antiques_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if ART in category_list:
        thread_1 = Thread(target=art_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if BABY in category_list:
        thread_1 = Thread(target=baby_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if BOOKS in category_list:
        thread_1 = Thread(target=books_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if BUSINESS in category_list:
        thread_1 = Thread(target=business_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if CAMERAS in category_list:
        thread_1 = Thread(target=cameras_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if CELL_PHONES in category_list:
        thread_1 = Thread(target=cell_phones_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if COINS in category_list:
        thread_1 = Thread(target=coins_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if COLLECTIBLES in category_list:
        thread_1 = Thread(target=collectibles_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if COMPUTERS in category_list:
        thread_1 = Thread(target=computers_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if CONSUMER_ELECTRONICS in category_list:
        thread_1 = Thread(target=consumer_electronics_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if CRAFTS in category_list:
        thread_1 = Thread(target=crafts_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DIGITAL_GOODS in category_list:
        thread_1 = Thread(target=digital_goods_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DOLLS in category_list:
        thread_1 = Thread(target=dolls_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DVDS_MOVIES in category_list:
        thread_1 = Thread(target=dvds_movies_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if ENTERTAINMENT in category_list:
        thread_1 = Thread(target=entertainment_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if EVERYTHING_ELSE in category_list:
        thread_1 = Thread(target=everything_else_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if FASHION in category_list:
        thread_1 = Thread(target=fashion_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if HEALTH_BEAUTY in category_list:
        thread_1 = Thread(target=health_beauty_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if HOME_GARDEN in category_list:
        thread_1 = Thread(target=home_garden_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if JEWELLERY in category_list:
        thread_1 = Thread(target=jewellery_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if MUSIC in category_list:
        thread_1 = Thread(target=music_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if MUSICAL_INSTRUMENTS in category_list:
        thread_1 = Thread(target=musical_instruments_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if PET_SUPPLIES in category_list:
        thread_1 = Thread(target=pet_supplies_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if POTTERY in category_list:
        thread_1 = Thread(target=pottery_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if SPECIALITY_SERVICES in category_list:
        thread_1 = Thread(target=speciality_services_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if SPORTING_GOODS in category_list:
        thread_1 = Thread(target=sporting_goods_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if SPORTS_MEM in category_list:
        thread_1 = Thread(target=sports_mem_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if STAMPS in category_list:
        thread_1 = Thread(target=stamps_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if TICKETS in category_list:
        thread_1 = Thread(target=tickets_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if TOYS in category_list:
        thread_1 = Thread(target=toys_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if TRAVEL in category_list:
        thread_1 = Thread(target=travel_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if VIDEO_GAMES in category_list:
        thread_1 = Thread(target=video_games_info_collector.start_info_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()


def start_url_collection():
    if ANTIQUES in category_list:
        thread_1 = Thread(target=antiques_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if ART in category_list:
        thread_1 = Thread(target=art_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if BABY in category_list:
        thread_1 = Thread(target=baby_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if BOOKS in category_list:
        thread_1 = Thread(target=books_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if BUSINESS in category_list:
        thread_1 = Thread(target=business_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if CAMERAS in category_list:
        thread_1 = Thread(target=cameras_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if CELL_PHONES in category_list:
        thread_1 = Thread(target=cell_phones_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if COINS in category_list:
        thread_1 = Thread(target=coins_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if COLLECTIBLES in category_list:
        thread_1 = Thread(target=collectibles_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if COMPUTERS in category_list:
        thread_1 = Thread(target=computers_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if CONSUMER_ELECTRONICS in category_list:
        thread_1 = Thread(target=consumer_electronics_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if CRAFTS in category_list:
        thread_1 = Thread(target=crafts_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DIGITAL_GOODS in category_list:
        thread_1 = Thread(target=digital_goods_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DOLLS in category_list:
        thread_1 = Thread(target=dolls_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DVDS_MOVIES in category_list:
        thread_1 = Thread(target=dvds_movies_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if ENTERTAINMENT in category_list:
        thread_1 = Thread(target=entertainment_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if EVERYTHING_ELSE in category_list:
        thread_1 = Thread(target=everything_else_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if FASHION in category_list:
        thread_1 = Thread(target=fashion_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if HEALTH_BEAUTY in category_list:
        thread_1 = Thread(target=health_beauty_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if HOME_GARDEN in category_list:
        thread_1 = Thread(target=home_garden_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if JEWELLERY in category_list:
        thread_1 = Thread(target=jewellery_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if MUSIC in category_list:
        thread_1 = Thread(target=music_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if MUSICAL_INSTRUMENTS in category_list:
        thread_1 = Thread(target=musical_instruments_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if PET_SUPPLIES in category_list:
        thread_1 = Thread(target=pet_supplies_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if POTTERY in category_list:
        thread_1 = Thread(target=pottery_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if SPECIALITY_SERVICES in category_list:
        thread_1 = Thread(target=speciality_services_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if SPORTING_GOODS in category_list:
        thread_1 = Thread(target=sporting_goods_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if SPORTS_MEM in category_list:
        thread_1 = Thread(target=sports_mem_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if STAMPS in category_list:
        thread_1 = Thread(target=stamps_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if TICKETS in category_list:
        thread_1 = Thread(target=tickets_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if TOYS in category_list:
        thread_1 = Thread(target=toys_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if TRAVEL in category_list:
        thread_1 = Thread(target=travel_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if VIDEO_GAMES in category_list:
        thread_1 = Thread(target=video_games_url_collector.start_url_collection)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()


def start_hierarchy_collection():
    if ANTIQUES in category_list:
        thread_1 = Thread(target=antiques_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if ART in category_list:
        thread_1 = Thread(target=art_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if BABY in category_list:
        thread_1 = Thread(target=baby_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if BOOKS in category_list:
        thread_1 = Thread(target=books_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if BUSINESS in category_list:
        thread_1 = Thread(target=business_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if CAMERAS in category_list:
        thread_1 = Thread(target=cameras_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if CELL_PHONES in category_list:
        thread_1 = Thread(target=cell_phones_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if COINS in category_list:
        thread_1 = Thread(target=coins_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if COLLECTIBLES in category_list:
        thread_1 = Thread(target=collectibles_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if COMPUTERS in category_list:
        thread_1 = Thread(target=computers_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if CONSUMER_ELECTRONICS in category_list:
        thread_1 = Thread(target=consumer_electronics_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if CRAFTS in category_list:
        thread_1 = Thread(target=crafts_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DIGITAL_GOODS in category_list:
        thread_1 = Thread(target=digital_goods_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DOLLS in category_list:
        thread_1 = Thread(target=dolls_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DVDS_MOVIES in category_list:
        thread_1 = Thread(target=dvds_movies_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if ENTERTAINMENT in category_list:
        thread_1 = Thread(target=entertainment_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if EVERYTHING_ELSE in category_list:
        thread_1 = Thread(target=everything_else_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if FASHION in category_list:
        thread_1 = Thread(target=fashion_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if HEALTH_BEAUTY in category_list:
        thread_1 = Thread(target=health_beauty_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if HOME_GARDEN in category_list:
        thread_1 = Thread(target=home_garden_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if JEWELLERY in category_list:
        thread_1 = Thread(target=jewellery_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if MUSIC in category_list:
        thread_1 = Thread(target=music_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if MUSICAL_INSTRUMENTS in category_list:
        thread_1 = Thread(target=musical_instruments_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if PET_SUPPLIES in category_list:
        thread_1 = Thread(target=pet_supplies_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if POTTERY in category_list:
        thread_1 = Thread(target=pottery_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if SPECIALITY_SERVICES in category_list:
        thread_1 = Thread(target=speciality_services_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if SPORTING_GOODS in category_list:
        thread_1 = Thread(target=sporting_goods_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if SPORTS_MEM in category_list:
        thread_1 = Thread(target=sports_mem_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if STAMPS in category_list:
        thread_1 = Thread(target=stamps_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if TICKETS in category_list:
        thread_1 = Thread(target=tickets_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if TOYS in category_list:
        thread_1 = Thread(target=toys_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if TRAVEL in category_list:
        thread_1 = Thread(target=travel_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if VIDEO_GAMES in category_list:
        thread_1 = Thread(target=video_games_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()


if __name__ == '__main__':
    if START_HIERARCHY_COLLECTION:
        start_hierarchy_collection()
    if START_URL_COLLECTION:
        start_url_collection()
    if START_INFO_COLLECTION:
        start_info_collection()

