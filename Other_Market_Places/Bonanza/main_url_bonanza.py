import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = '/'.join(dir_path.split('/')[0:-1])
sys.path.insert(0, dir_path)
from Common.Bonanza_common_imports import *

category_list = '|'.join(BONANZA_CATEGORY_LIST)


def start_url_collection():
    jobs = []
    if DataCollectors_Configuration.ANTIQUES in category_list:
        thread_1 = Thread(target=antiques_url_collector.start_url_collection)
        thread_1.daemon = True
        jobs.append(thread_1)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.ART in category_list:
        thread_2 = Thread(target=art_url_collector.start_url_collection)
        thread_2.daemon = True
        jobs.append(thread_2)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.BABY in category_list:
        thread_3 = Thread(target=baby_url_collector.start_url_collection)
        thread_3.daemon = True
        jobs.append(thread_3)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.BOOKS in category_list:
        thread_4 = Thread(target=books_url_collector.start_url_collection)
        thread_4.daemon = True
        jobs.append(thread_4)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.BUSINESS in category_list:
        thread_5 = Thread(target=business_url_collector.start_url_collection)
        thread_5.daemon = True
        jobs.append(thread_5)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.CAMERAS in category_list:
        thread_6 = Thread(target=cameras_url_collector.start_url_collection)
        thread_6.daemon = True
        jobs.append(thread_6)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.CELL_PHONES in category_list:
        thread_7 = Thread(target=cell_phones_url_collector.start_url_collection)
        thread_7.daemon = True
        jobs.append(thread_7)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.COINS in category_list:
        thread_8 = Thread(target=coins_url_collector.start_url_collection)
        thread_8.daemon = True
        jobs.append(thread_8)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.COLLECTIBLES in category_list:
        thread_9 = Thread(target=collectibles_url_collector.start_url_collection)
        thread_9.daemon = True
        jobs.append(thread_9)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.COMPUTERS in category_list:
        thread_10 = Thread(target=computers_url_collector.start_url_collection)
        thread_10.daemon = True
        jobs.append(thread_10)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.CONSUMER_ELECTRONICS in category_list:
        thread_11 = Thread(target=consumer_electronics_url_collector.start_url_collection)
        thread_11.daemon = True
        jobs.append(thread_11)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.CRAFTS in category_list:
        thread_12 = Thread(target=crafts_url_collector.start_url_collection)
        thread_12.daemon = True
        jobs.append(thread_12)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.DIGITAL_GOODS in category_list:
        thread_13 = Thread(target=digital_goods_url_collector.start_url_collection)
        thread_13.daemon = True
        jobs.append(thread_13)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.DOLLS in category_list:
        thread_14 = Thread(target=dolls_url_collector.start_url_collection)
        thread_14.daemon = True
        jobs.append(thread_14)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.DVDS_MOVIES in category_list:
        thread_15 = Thread(target=dvds_movies_url_collector.start_url_collection)
        thread_15.daemon = True
        jobs.append(thread_15)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.ENTERTAINMENT in category_list:
        thread_16 = Thread(target=entertainment_url_collector.start_url_collection)
        thread_16.daemon = True
        jobs.append(thread_16)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.EVERYTHING_ELSE in category_list:
        thread_17 = Thread(target=everything_else_url_collector.start_url_collection)
        thread_17.daemon = True
        jobs.append(thread_17)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.FASHION in category_list:
        thread_18 = Thread(target=fashion_url_collector.start_url_collection)
        thread_18.daemon = True
        jobs.append(thread_18)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.HEALTH_BEAUTY in category_list:
        thread_19 = Thread(target=health_beauty_url_collector.start_url_collection)
        thread_19.daemon = True
        jobs.append(thread_19)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.HOME_GARDEN in category_list:
        thread_20 = Thread(target=home_garden_url_collector.start_url_collection)
        thread_20.daemon = True
        jobs.append(thread_20)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.JEWELLERY in category_list:
        thread_21 = Thread(target=jewellery_url_collector.start_url_collection)
        thread_21.daemon = True
        jobs.append(thread_21)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.MUSIC in category_list:
        thread_22 = Thread(target=music_url_collector.start_url_collection)
        thread_22.daemon = True
        jobs.append(thread_22)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.MUSICAL_INSTRUMENTS in category_list:
        thread_23 = Thread(target=musical_instruments_url_collector.start_url_collection)
        thread_23.daemon = True
        jobs.append(thread_23)
        # thread_1.start(23
        # thread_1.join()
    if DataCollectors_Configuration.PET_SUPPLIES in category_list:
        thread_24 = Thread(target=pet_supplies_url_collector.start_url_collection)
        thread_24.daemon = True
        jobs.append(thread_24)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.POTTERY in category_list:
        thread_25 = Thread(target=pottery_url_collector.start_url_collection)
        thread_25.daemon = True
        jobs.append(thread_25)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.SPECIALITY_SERVICES in category_list:
        thread_26 = Thread(target=speciality_services_url_collector.start_url_collection)
        thread_26.daemon = True
        jobs.append(thread_26)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.SPORTING_GOODS in category_list:
        thread_27 = Thread(target=sporting_goods_url_collector.start_url_collection)
        thread_27.daemon = True
        jobs.append(thread_27)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.SPORTS_MEM in category_list:
        thread_28 = Thread(target=sports_mem_url_collector.start_url_collection)
        thread_28.daemon = True
        jobs.append(thread_28)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.STAMPS in category_list:
        thread_29 = Thread(target=stamps_url_collector.start_url_collection)
        thread_29.daemon = True
        jobs.append(thread_29)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.TICKETS in category_list:
        thread_30 = Thread(target=tickets_url_collector.start_url_collection)
        thread_30.daemon = True
        jobs.append(thread_30)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.TOYS in category_list:
        thread_31 = Thread(target=toys_url_collector.start_url_collection)
        thread_31.daemon = True
        jobs.append(thread_31)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.TRAVEL in category_list:
        thread_32 = Thread(target=travel_url_collector.start_url_collection)
        thread_32.daemon = True
        jobs.append(thread_32)
        # thread_1.start()
        # thread_1.join()
    if DataCollectors_Configuration.VIDEO_GAMES in category_list:
        thread_33 = Thread(target=video_games_url_collector.start_url_collection)
        thread_33.daemon = True
        jobs.append(thread_33)
        # thread_1.start()
        # thread_1.join()
    for job in jobs:
        job.start()
    for job in jobs:
        if (job.is_alive()):
            job.join()


if __name__ == '__main__':
    start_url_collection()
