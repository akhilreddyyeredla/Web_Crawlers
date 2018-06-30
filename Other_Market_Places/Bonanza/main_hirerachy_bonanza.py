import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = '/'.join(dir_path.split('/')[0:-1])
sys.path.insert(0, dir_path)
from Common.Bonanza_common_imports import *

category_list = '|'.join(BONANZA_CATEGORY_LIST)


def start_hierarchy_collection():
    if DataCollectors_Configuration.ANTIQUES in category_list:
        thread_1 = Thread(target=antiques_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.ART in category_list:
        thread_1 = Thread(target=art_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.BABY in category_list:
        thread_1 = Thread(target=baby_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.BOOKS in category_list:
        thread_1 = Thread(target=books_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.BUSINESS in category_list:
        thread_1 = Thread(target=business_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.CAMERAS in category_list:
        thread_1 = Thread(target=cameras_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.CELL_PHONES in category_list:
        thread_1 = Thread(target=cell_phones_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.COINS in category_list:
        thread_1 = Thread(target=coins_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.COLLECTIBLES in category_list:
        thread_1 = Thread(target=collectibles_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.COMPUTERS in category_list:
        thread_1 = Thread(target=computers_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.CONSUMER_ELECTRONICS in category_list:
        thread_1 = Thread(target=consumer_electronics_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.CRAFTS in category_list:
        thread_1 = Thread(target=crafts_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.DIGITAL_GOODS in category_list:
        thread_1 = Thread(target=digital_goods_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.DOLLS in category_list:
        thread_1 = Thread(target=dolls_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.DVDS_MOVIES in category_list:
        thread_1 = Thread(target=dvds_movies_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.ENTERTAINMENT in category_list:
        thread_1 = Thread(target=entertainment_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.EVERYTHING_ELSE in category_list:
        thread_1 = Thread(target=everything_else_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.FASHION in category_list:
        thread_1 = Thread(target=fashion_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.HEALTH_BEAUTY in category_list:
        thread_1 = Thread(target=health_beauty_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.HOME_GARDEN in category_list:
        thread_1 = Thread(target=home_garden_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.JEWELLERY in category_list:
        thread_1 = Thread(target=jewellery_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.MUSIC in category_list:
        thread_1 = Thread(target=music_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.MUSICAL_INSTRUMENTS in category_list:
        thread_1 = Thread(target=musical_instruments_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.PET_SUPPLIES in category_list:
        thread_1 = Thread(target=pet_supplies_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.POTTERY in category_list:
        thread_1 = Thread(target=pottery_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.SPECIALITY_SERVICES in category_list:
        thread_1 = Thread(target=speciality_services_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.SPORTING_GOODS in category_list:
        thread_1 = Thread(target=sporting_goods_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.SPORTS_MEM in category_list:
        thread_1 = Thread(target=sports_mem_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.STAMPS in category_list:
        thread_1 = Thread(target=stamps_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.TICKETS in category_list:
        thread_1 = Thread(target=tickets_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.TOYS in category_list:
        thread_1 = Thread(target=toys_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.TRAVEL in category_list:
        thread_1 = Thread(target=travel_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()
    if DataCollectors_Configuration.VIDEO_GAMES in category_list:
        thread_1 = Thread(target=video_games_hierarchy_collector.start_hierarchy)
        thread_1.daemon = True
        thread_1.start()
        thread_1.join()


if __name__ == '__main__':
    start_hierarchy_collection()
