import sys
sys.path.insert(0, r'/usr/datacollector')

from hierarchy_collectors import amazon_pantry_hierarchy, home_garden_and_diy_hierarchy, handmade_hierarchy, \
    movies_tv_music_and_games_hierarchy, clothes_shoes_and_watches_hierarchy, business_industry_and_science_hierarchy, \
    car_and_motorbike_hierarchy, health_and_beauty_hierarchy, sports_and_outdoor_hierarchy, books_and_audible_hierarchy, \
    electronics_and_computers_hierarchy, toys_children_and_baby_hierarchy
from info_collectors import home_garden_pets_and_diy_info_collector, clothes_shoes_and_watches_info_collector, \
    books_and_audible_info_collector, toys_children_and_baby_info_collector, electronics_and_computers_info_collector, \
    car_and_motorbike_info_collector, handmade_info_collector, sports_and_outdoors_info_collector, \
    amazon_pantry_info_collector, business_industry_and_science_info_collector, health_and_beauty_info_collector, \
    movies_tv_music_and_games_info_collector
from url_collectors import amazon_pantry_url_collector, car_and_motorbike_url_collector, \
    health_and_beauty_url_collector, movies_tv_music_and_games_url_collector, electronics_and_computers_url_collector, \
    home_garden_pets_and_diy_url_collector, business_industry_and_science_url_collector, \
    clothes_shoes_and_watches_url_collector, books_and_audible_url_collector, toys_children_and_baby_url_collector, \
    handmade_url_collector, sports_and_outdoors_url_collector
from CONSTANTS import *
from multiprocessing import Process
from DataCollectors_Configuration import AMAZON_UK_CATEGORY_LIST, START_HIERARCHY_COLLECTION, START_URL_COLLECTION, \
    START_INFO_COLLECTION

category_list = '|'.join(AMAZON_UK_CATEGORY_LIST)


def start_info_collection():
    jobs = []
    if AMAZON_PANTRY in category_list:
        thread_1 = Process(target=amazon_pantry_info_collector.start_info_collection, args=(AMAZON_PANTRY,))
        thread_1.daemon = True
        jobs.append(thread_1)

    if BOOKS_AND_AUDIBLE in category_list:
        thread_2 = Process(target=books_and_audible_info_collector.start_info_collection, args=(BOOKS_AND_AUDIBLE,))
        thread_2.daemon = True
        jobs.append(thread_2)

    if BUSINESS_INDUSTRY_AND_SCIENCE in category_list:
        thread_3 = Process(target=business_industry_and_science_info_collector.start_info_collection,
                           args=(BUSINESS_INDUSTRY_AND_SCIENCE,))
        thread_3.daemon = True
        jobs.append(thread_3)

    if CAR_AND_MOTORBIKE in category_list:
        thread_4 = Process(target=car_and_motorbike_info_collector.start_info_collection, args=(CAR_AND_MOTORBIKE,))
        thread_4.daemon = True
        jobs.append(thread_4)

    if CLOTHES_SHOES_AND_WATCHES in category_list:
        thread_5 = Process(target=clothes_shoes_and_watches_info_collector.start_info_collection,
                           args=(CLOTHES_SHOES_AND_WATCHES,))
        thread_5.daemon = True
        jobs.append(thread_5)

    if ELECTRONICS_AND_COMPUTERS in category_list:
        thread_6 = Process(target=electronics_and_computers_info_collector.start_info_collection,
                           args=(ELECTRONICS_AND_COMPUTERS,))
        thread_6.daemon = True
        jobs.append(thread_6)

    if HANDMADE in category_list:
        thread_7 = Process(target=handmade_info_collector.start_info_collection, args=(HANDMADE,))
        thread_7.daemon = True
        jobs.append(thread_7)

    if HEALTH_AND_BEAUTY in category_list:
        thread_8 = Process(target=health_and_beauty_info_collector.start_info_collection, args=(HEALTH_AND_BEAUTY,))
        thread_8.daemon = True
        jobs.append(thread_8)

    if HOME_GARDEN_PETS_AND_DIY in category_list:
        thread_9 = Process(target=home_garden_pets_and_diy_info_collector.start_info_collection,
                           args=(HOME_GARDEN_PETS_AND_DIY,))
        thread_9.daemon = True
        jobs.append(thread_9)

    if MOVIES_TV_MUSIC_AND_GAMES in category_list:
        thread_10 = Process(target=movies_tv_music_and_games_info_collector.start_info_collection,
                            args=(MOVIES_TV_MUSIC_AND_GAMES,))
        thread_10.daemon = True
        jobs.append(thread_10)

    if SPORTS_AND_OUTDOORS in category_list:
        thread_11 = Process(target=sports_and_outdoors_info_collector.start_info_collection,
                            args=(SPORTS_AND_OUTDOORS,))
        thread_11.daemon = True
        jobs.append(thread_11)

    if TOYS_CHILDREN_AND_BABY in category_list:
        thread_12 = Process(target=toys_children_and_baby_info_collector.start_info_collection,
                            args=(TOYS_CHILDREN_AND_BABY,))
        thread_12.daemon = True
        jobs.append(thread_12)

    for job in jobs:
        job.start()
    for job in jobs:
        if job.is_alive():
            job.join()


def start_url_collection():
    jobs = []
    if AMAZON_PANTRY in category_list:
        thread_1 = Process(target=amazon_pantry_url_collector.start_program, args=(AMAZON_PANTRY,))
        thread_1.daemon = True
        jobs.append(thread_1)

    if BOOKS_AND_AUDIBLE in category_list:
        thread_2 = Process(target=books_and_audible_url_collector.start_program, args=(BOOKS_AND_AUDIBLE,))
        thread_2.daemon = True
        jobs.append(thread_2)

    if BUSINESS_INDUSTRY_AND_SCIENCE in category_list:
        thread_3 = Process(target=business_industry_and_science_url_collector.start_program,
                           args=(BUSINESS_INDUSTRY_AND_SCIENCE,))
        thread_3.daemon = True
        jobs.append(thread_3)

    if CAR_AND_MOTORBIKE in category_list:
        thread_4 = Process(target=car_and_motorbike_url_collector.start_program, args=(CAR_AND_MOTORBIKE,))
        thread_4.daemon = True
        jobs.append(thread_4)

    if CLOTHES_SHOES_AND_WATCHES in category_list:
        thread_5 = Process(target=clothes_shoes_and_watches_url_collector.start_program,
                           args=(CLOTHES_SHOES_AND_WATCHES,))
        thread_5.daemon = True
        jobs.append(thread_5)

    if ELECTRONICS_AND_COMPUTERS in category_list:
        thread_6 = Process(target=electronics_and_computers_url_collector.start_program,
                           args=(ELECTRONICS_AND_COMPUTERS,))
        thread_6.daemon = True
        jobs.append(thread_6)

    if HANDMADE in category_list:
        thread_7 = Process(target=handmade_url_collector.start_program, args=(HANDMADE,))
        thread_7.daemon = True
        jobs.append(thread_7)

    if HEALTH_AND_BEAUTY in category_list:
        thread_8 = Process(target=health_and_beauty_url_collector.start_program, args=(HEALTH_AND_BEAUTY,))
        thread_8.daemon = True
        jobs.append(thread_8)

    if HOME_GARDEN_PETS_AND_DIY in category_list:
        thread_9 = Process(target=home_garden_pets_and_diy_url_collector.start_program,
                           args=(HOME_GARDEN_PETS_AND_DIY,))
        thread_9.daemon = True
        jobs.append(thread_9)

    if MOVIES_TV_MUSIC_AND_GAMES in category_list:
        thread_10 = Process(target=movies_tv_music_and_games_url_collector.start_program,
                            args=(MOVIES_TV_MUSIC_AND_GAMES,))
        thread_10.daemon = True
        jobs.append(thread_10)

    if SPORTS_AND_OUTDOORS in category_list:
        thread_11 = Process(target=sports_and_outdoors_url_collector.start_program, args=(SPORTS_AND_OUTDOORS,))
        thread_11.daemon = True
        jobs.append(thread_11)

    if TOYS_CHILDREN_AND_BABY in category_list:
        thread_12 = Process(target=toys_children_and_baby_url_collector.start_program, args=(TOYS_CHILDREN_AND_BABY,))
        thread_12.daemon = True
        jobs.append(thread_12)

    for job in jobs:
        job.start()
    for job in jobs:
        if job.is_alive():
            job.join()


def start_hierarchy_collection():
    jobs = []
    if AMAZON_PANTRY in category_list:
        thread_1 = Process(target=amazon_pantry_hierarchy.start_program)
        thread_1.daemon = True

        jobs.append(thread_1)

    if BOOKS_AND_AUDIBLE in category_list:
        thread_2 = Process(target=books_and_audible_hierarchy.start_program)
        thread_2.daemon = True

        jobs.append(thread_2)

    if BUSINESS_INDUSTRY_AND_SCIENCE in category_list:
        thread_3 = Process(target=business_industry_and_science_hierarchy.start_program)
        thread_3.daemon = True

        jobs.append(thread_3)

    if CAR_AND_MOTORBIKE in category_list:
        thread_4 = Process(target=car_and_motorbike_hierarchy.start_program)
        thread_4.daemon = True

        jobs.append(thread_4)

    if CLOTHES_SHOES_AND_WATCHES in category_list:
        thread_5 = Process(target=clothes_shoes_and_watches_hierarchy.start_program)
        thread_5.daemon = True

        jobs.append(thread_5)

    if ELECTRONICS_AND_COMPUTERS in category_list:
        thread_6 = Process(target=electronics_and_computers_hierarchy.start_program)
        thread_6.daemon = True

        jobs.append(thread_6)

    if HANDMADE in category_list:
        thread_7 = Process(target=handmade_hierarchy.start_program)
        thread_7.daemon = True

        jobs.append(thread_7)

    if HEALTH_AND_BEAUTY in category_list:
        thread_8 = Process(target=health_and_beauty_hierarchy.start_program)
        thread_8.daemon = True

        jobs.append(thread_8)

    if HOME_GARDEN_PETS_AND_DIY in category_list:
        thread_9 = Process(target=home_garden_and_diy_hierarchy.start_program)
        thread_9.daemon = True

        jobs.append(thread_9)

    if MOVIES_TV_MUSIC_AND_GAMES in category_list:
        thread_10 = Process(target=movies_tv_music_and_games_hierarchy.start_program)
        thread_10.daemon = True

        jobs.append(thread_10)

    if SPORTS_AND_OUTDOORS in category_list:
        thread_11 = Process(target=sports_and_outdoor_hierarchy.start_program)
        thread_11.daemon = True

        jobs.append(thread_11)

    if TOYS_CHILDREN_AND_BABY in category_list:
        thread_12 = Process(target=toys_children_and_baby_hierarchy.start_program)
        thread_12.daemon = True

        jobs.append(thread_12)

    for job in jobs:
        job.start()
    for job in jobs:
        if job.is_alive():
            job.join()


if __name__ == '__main__':

    if START_HIERARCHY_COLLECTION:
        start_hierarchy_collection()

    if START_URL_COLLECTION:
        start_url_collection()

    if START_INFO_COLLECTION:
        start_info_collection()
