import sys
sys.path.insert(0, r'/usr/datacollector')
from url_collectors import music_url_collector, home_kitchen_and_pets_url_collector, \
    clothing_shoes_and_jewelry_url_collector, software_url_collector, health_beauty_and_grocery_url_collector, \
    books_and_audible_url_collector, tools_patio_and_garden_url_collector, toys_and_baby_url_collector, \
    video_games_url_collector, automotive_and_industrial_url_collector, sports_and_outdoors_url_collector, \
    handmade_url_collector, electronics_url_collector
from info_collectors import music_info_collector, home_kitchen_and_pets_info_collector, \
    clothing_shoes_and_jewelry_info_collector, software_info_collector, health_beauty_and_grocery_info_collector, \
    books_and_audible_info_collector, tools_patio_and_garden_info_collector, toys_and_baby_info_collector, \
    video_games_info_collector, automotive_and_industrial_info_collector, sports_and_outdoors_info_collector, \
    handmade_info_collector, electronics_info_collector
from hierarchy_collectors import music_hierarchy, home_kitchen_and_pets_hierarchy, clothing_shoes_and_jewelry_hierarchy, \
    software_hierarchy, health_beauty_and_grocery_hierarchy, books_and_audible_hierarchy, \
    tools_patio_and_garden_hierarchy, toys_and_baby_hierarchy, video_games_hierarchy, \
    automotive_and_industrial_hierarchy, sports_and_outdoors_hierarchy, handmade_hierarchy, electronics_hierarchy
from CONSTANTS import *
from multiprocessing import Process
from DataCollectors_Configuration import AMAZON_CANADA_CATEGORY_LIST, START_HIERARCHY_COLLECTION, START_URL_COLLECTION, \
    START_INFO_COLLECTION

category_list = '|'.join(AMAZON_CANADA_CATEGORY_LIST)


def start_info_collection():
    jobs = []
    if MUSIC in category_list:
        process_1 = Process(target=music_info_collector.start_info_collection, args=(MUSIC,))
        process_1.daemon = True
        jobs.append(process_1)

    if HOME_KITCHEN_AND_PETS in category_list:
        process_2 = Process(target=home_kitchen_and_pets_info_collector.start_info_collection,
                            args=(HOME_KITCHEN_AND_PETS,))
        process_2.daemon = True
        jobs.append(process_2)

    if CLOTHING_SHOES_AND_JEWELRY in category_list:
        process_3 = Process(target=clothing_shoes_and_jewelry_info_collector.start_info_collection,
                            args=(CLOTHING_SHOES_AND_JEWELRY,))
        process_3.daemon = True
        jobs.append(process_3)

    if SOFTWARE in category_list:
        process_4 = Process(target=software_info_collector.start_info_collection, args=(SOFTWARE,))
        process_4.daemon = True
        jobs.append(process_4)

    if HEALTH_BEAUTY_AND_GROCERY in category_list:
        process_5 = Process(target=health_beauty_and_grocery_info_collector.start_info_collection,
                            args=(HEALTH_BEAUTY_AND_GROCERY,))
        process_5.daemon = True
        jobs.append(process_5)

    if BOOKS_AND_AUDIBLE in category_list:
        process_6 = Process(target=books_and_audible_info_collector.start_info_collection, args=(BOOKS_AND_AUDIBLE,))
        process_6.daemon = True
        jobs.append(process_6)

    if TOOLS_PATIO_AND_GARDEN in category_list:
        process_7 = Process(target=tools_patio_and_garden_info_collector.start_info_collection,
                            args=(TOOLS_PATIO_AND_GARDEN,))
        process_7.daemon = True
        jobs.append(process_7)

    if TOYS_AND_BABY in category_list:
        process_8 = Process(target=toys_and_baby_info_collector.start_info_collection, args=(TOYS_AND_BABY,))
        process_8.daemon = True
        jobs.append(process_8)

    if VIDEO_GAMES in category_list:
        process_9 = Process(target=video_games_info_collector.start_info_collection, args=(VIDEO_GAMES,))
        process_9.daemon = True
        jobs.append(process_9)

    if AUTOMOTIVE_AND_INDUSTRIAL in category_list:
        process_10 = Process(target=automotive_and_industrial_info_collector.start_info_collection,
                             args=(AUTOMOTIVE_AND_INDUSTRIAL,))
        process_10.daemon = True
        jobs.append(process_10)

    if SPORTS_AND_OUTDOORS in category_list:
        process_11 = Process(target=sports_and_outdoors_info_collector.start_info_collection,
                             args=(SPORTS_AND_OUTDOORS,))
        process_11.daemon = True
        jobs.append(process_11)

    if HANDMADE in category_list:
        process_12 = Process(target=handmade_info_collector.start_info_collection, args=(HANDMADE,))
        process_12.daemon = True
        jobs.append(process_12)

    if ELECTRONICS in category_list:
        process_13 = Process(target=electronics_info_collector.start_info_collection, args=(ELECTRONICS,))
        process_13.daemon = True
        jobs.append(process_13)

    for job in jobs:
        job.start()
    for job in jobs:
        if job.is_alive():
            job.join()


def start_url_collection():
    jobs = []
    if MUSIC in category_list:
        process_1 = Process(target=music_url_collector.start_program, args=(MUSIC,))
        process_1.daemon = True
        jobs.append(process_1)

    if HOME_KITCHEN_AND_PETS in category_list:
        process_2 = Process(target=home_kitchen_and_pets_url_collector.start_program, args=(HOME_KITCHEN_AND_PETS,))
        process_2.daemon = True
        jobs.append(process_2)

    if CLOTHING_SHOES_AND_JEWELRY in category_list:
        process_3 = Process(target=clothing_shoes_and_jewelry_url_collector.start_program,
                            args=(CLOTHING_SHOES_AND_JEWELRY,))
        process_3.daemon = True
        jobs.append(process_3)

    if SOFTWARE in category_list:
        process_4 = Process(target=software_url_collector.start_program, args=(SOFTWARE,))
        process_4.daemon = True
        jobs.append(process_4)

    if HEALTH_BEAUTY_AND_GROCERY in category_list:
        process_5 = Process(target=health_beauty_and_grocery_url_collector.start_program,
                            args=(HEALTH_BEAUTY_AND_GROCERY,))
        process_5.daemon = True
        jobs.append(process_5)

    if BOOKS_AND_AUDIBLE in category_list:
        process_6 = Process(target=books_and_audible_url_collector.start_program, args=(BOOKS_AND_AUDIBLE,))
        process_6.daemon = True
        jobs.append(process_6)

    if TOOLS_PATIO_AND_GARDEN in category_list:
        process_7 = Process(target=tools_patio_and_garden_url_collector.start_program, args=(TOOLS_PATIO_AND_GARDEN,))
        process_7.daemon = True
        jobs.append(process_7)

    if TOYS_AND_BABY in category_list:
        process_8 = Process(target=toys_and_baby_url_collector.start_program, args=(TOYS_AND_BABY,))
        process_8.daemon = True
        jobs.append(process_8)

    if VIDEO_GAMES in category_list:
        process_9 = Process(target=video_games_url_collector.start_program, args=(VIDEO_GAMES,))
        process_9.daemon = True
        jobs.append(process_9)

    if AUTOMOTIVE_AND_INDUSTRIAL in category_list:
        process_10 = Process(target=automotive_and_industrial_url_collector.start_program,
                             args=(AUTOMOTIVE_AND_INDUSTRIAL,))
        process_10.daemon = True
        jobs.append(process_10)

    if SPORTS_AND_OUTDOORS in category_list:
        process_11 = Process(target=sports_and_outdoors_url_collector.start_program, args=(SPORTS_AND_OUTDOORS,))
        process_11.daemon = True
        jobs.append(process_11)

    if HANDMADE in category_list:
        process_12 = Process(target=handmade_url_collector.start_program, args=(HANDMADE,))
        process_12.daemon = True
        jobs.append(process_12)

    if ELECTRONICS in category_list:
        process_13 = Process(target=electronics_url_collector.start_program, args=(ELECTRONICS,))
        process_13.daemon = True
        jobs.append(process_13)

    for job in jobs:
        job.start()
    for job in jobs:
        if job.is_alive():
            job.join()


def start_hierarchy_collection():
    jobs = []
    if MUSIC in category_list:
        process_1 = Process(target=music_hierarchy.start_program)
        process_1.daemon = True
        print 'in'
        jobs.append(process_1)

    if HOME_KITCHEN_AND_PETS in category_list:
        process_2 = Process(target=home_kitchen_and_pets_hierarchy.start_program)
        process_2.daemon = True

        jobs.append(process_2)

    if CLOTHING_SHOES_AND_JEWELRY in category_list:
        process_3 = Process(target=clothing_shoes_and_jewelry_hierarchy.start_program)
        process_3.daemon = True

        jobs.append(process_3)

    if SOFTWARE in category_list:
        process_4 = Process(target=software_hierarchy.start_program)
        process_4.daemon = True

        jobs.append(process_4)

    if HEALTH_BEAUTY_AND_GROCERY in category_list:
        process_5 = Process(target=health_beauty_and_grocery_hierarchy.start_program)
        process_5.daemon = True

        jobs.append(process_5)

    if BOOKS_AND_AUDIBLE in category_list:
        process_6 = Process(target=books_and_audible_hierarchy.start_program)
        process_6.daemon = True

        jobs.append(process_6)

    if TOOLS_PATIO_AND_GARDEN in category_list:
        process_7 = Process(target=tools_patio_and_garden_hierarchy.start_program)
        process_7.daemon = True

        jobs.append(process_7)

    if TOYS_AND_BABY in category_list:
        process_8 = Process(target=toys_and_baby_hierarchy.start_program)
        process_8.daemon = True

        jobs.append(process_8)

    if VIDEO_GAMES in category_list:
        process_9 = Process(target=video_games_hierarchy.start_program)
        process_9.daemon = True

        jobs.append(process_9)

    if AUTOMOTIVE_AND_INDUSTRIAL in category_list:
        process_10 = Process(target=automotive_and_industrial_hierarchy.start_program)
        process_10.daemon = True

        jobs.append(process_10)

    if SPORTS_AND_OUTDOORS in category_list:
        process_11 = Process(target=sports_and_outdoors_hierarchy.start_program)
        process_11.daemon = True

        jobs.append(process_11)

    if HANDMADE in category_list:
        process_12 = Process(target=handmade_hierarchy.start_program)
        process_12.daemon = True

        jobs.append(process_12)

    if ELECTRONICS in category_list:
        process_13 = Process(target=electronics_hierarchy.start_program)
        process_13.daemon = True

        jobs.append(process_13)

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
