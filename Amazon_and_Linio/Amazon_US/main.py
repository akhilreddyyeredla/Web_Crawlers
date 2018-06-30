import sys
sys.path.insert(0, r'/usr/datacollector')

from url_collectors import amazon_global_url_collector, books_url_collector, home_garden_and_tools_url_collector, \
    beauty_and_health_url_collector, toys_and_games_url_collector, sports_and_outdoor_url_collector, \
    clothing_url_collector, electronics_url_collector, handmade_url_collector
from hierarchy_collectors import amazon_global_hierarchy, books_hierarchy, home_garden_and_tools_hierarchy, \
    beauty_and_health_hierarchy, toys_and_games_hierarchy, sports_and_outdoors, clothing_hierarchy, \
    electronics_hierarchy, handmade_hierarchy
from product_info_collectors import amazon_global_info_collector, books_info_collector, \
    home_garden_and_tools_info_collector, beauty_and_health_info_collector, toys_and_games_info_collector, \
    sports_and_outdoor_info_collector, clothing_info_collector, electronics_info_collector, handmade_info_collector
from CONSTANTS import *
from DataCollectors_Configuration import AMAZON_US_CATEGORY_LIST, START_HIERARCHY_COLLECTION, START_URL_COLLECTION, \
    START_INFO_COLLECTION
from multiprocessing import Process

category_list = '|'.join(AMAZON_US_CATEGORY_LIST)


def start_info_collection():
    jobs = []
    if AMAZON_GLOBAL in category_list:
        process_1 = Process(target=amazon_global_info_collector.start_info_collection, args=(AMAZON_GLOBAL,))

        process_1.daemon = True

        jobs.append(process_1)

    if BOOKS in category_list:
        process_2 = Process(target=books_info_collector.start_info_collection, args=(BOOKS,))

        process_2.daemon = True

        jobs.append(process_2)

    if HOME_GARDEN_AND_TOOLS in category_list:
        process_3 = Process(target=home_garden_and_tools_info_collector.start_info_collection,
                            args=(HOME_GARDEN_AND_TOOLS,))

        process_3.daemon = True

        jobs.append(process_3)

    if BEAUTY_AND_HEALTH in category_list:
        process_4 = Process(target=beauty_and_health_info_collector.start_info_collection, args=(BEAUTY_AND_HEALTH,))

        process_4.daemon = True

        jobs.append(process_4)

    if TOYS_AND_GAMES in category_list:
        process_5 = Process(target=toys_and_games_info_collector.start_info_collection, args=(TOYS_AND_GAMES,))

        process_5.daemon = True

        jobs.append(process_5)

    if SPORTS_AND_OUTDOOR in category_list:
        process_6 = Process(target=sports_and_outdoor_info_collector.start_info_collection, args=(SPORTS_AND_OUTDOOR,))

        process_6.daemon = True

        jobs.append(process_6)

    if CLOTHING in category_list:
        process_7 = Process(target=clothing_info_collector.start_info_collection, args=(CLOTHING,))

        process_7.daemon = True

        jobs.append(process_7)

    if ELECTRONICS in category_list:
        process_8 = Process(target=electronics_info_collector.start_info_collection, args=(ELECTRONICS,))

        process_8.daemon = True

        jobs.append(process_8)

    if HANDMADE in category_list:
        process_9 = Process(target=handmade_info_collector.start_info_collection, args=(HANDMADE,))

        process_9.daemon = True

        jobs.append(process_9)

    for job in jobs:
        job.start()
    for job in jobs:
        if job.is_alive():
            job.join()


def start_url_collection():
    jobs = []
    if AMAZON_GLOBAL in category_list:
        process_1 = Process(target=amazon_global_url_collector.start_program, args=(AMAZON_GLOBAL,))

        process_1.daemon = True

        jobs.append(process_1)

    if BOOKS in category_list:
        process_2 = Process(target=books_url_collector.start_program, args=(BOOKS,))

        process_2.daemon = True

        jobs.append(process_2)

    if HOME_GARDEN_AND_TOOLS in category_list:
        process_3 = Process(target=home_garden_and_tools_url_collector.start_program, args=(HOME_GARDEN_AND_TOOLS,))

        process_3.daemon = True

        jobs.append(process_3)

    if BEAUTY_AND_HEALTH in category_list:
        process_4 = Process(target=beauty_and_health_url_collector.start_program, args=(BEAUTY_AND_HEALTH,))

        process_4.daemon = True

        jobs.append(process_4)

    if TOYS_AND_GAMES in category_list:
        process_5 = Process(target=toys_and_games_url_collector.start_program, args=(TOYS_AND_GAMES,))

        process_5.daemon = True

        jobs.append(process_5)

    if SPORTS_AND_OUTDOOR in category_list:
        process_6 = Process(target=sports_and_outdoor_url_collector.start_program, args=(SPORTS_AND_OUTDOOR,))

        process_6.daemon = True

        jobs.append(process_6)

    if CLOTHING in category_list:
        process_7 = Process(target=clothing_url_collector.start_program, args=(CLOTHING,))

        process_7.daemon = True

        jobs.append(process_7)

    if ELECTRONICS in category_list:
        process_8 = Process(target=electronics_url_collector.start_program, args=(ELECTRONICS,))

        process_8.daemon = True

        jobs.append(process_8)

    if HANDMADE in category_list:
        process_9 = Process(target=handmade_url_collector.start_program, args=(HANDMADE,))

        process_9.daemon = True

        jobs.append(process_9)

    for job in jobs:
        job.start()
    for job in jobs:
        if job.is_alive():
            job.join()


def start_hierarchy_collection():
    jobs = []
    if AMAZON_GLOBAL in category_list:
        process_1 = Process(target=amazon_global_hierarchy.start_program)

        process_1.daemon = True

        jobs.append(process_1)

    if BOOKS in category_list:
        process_2 = Process(target=books_hierarchy.start_program)

        process_2.daemon = True

        jobs.append(process_2)

    if HOME_GARDEN_AND_TOOLS in category_list:
        process_3 = Process(target=home_garden_and_tools_hierarchy.start_program)

        process_3.daemon = True

        jobs.append(process_3)

    if BEAUTY_AND_HEALTH in category_list:
        process_4 = Process(target=beauty_and_health_hierarchy.start_program)

        process_4.daemon = True

        jobs.append(process_4)

    if TOYS_AND_GAMES in category_list:
        process_5 = Process(target=toys_and_games_hierarchy.start_program)

        process_5.daemon = True

        jobs.append(process_5)

    if SPORTS_AND_OUTDOOR in category_list:
        process_6 = Process(target=sports_and_outdoors.start_program)

        process_6.daemon = True

        jobs.append(process_6)

    if CLOTHING in category_list:
        process_7 = Process(target=clothing_hierarchy.start_program)

        process_7.daemon = True

        jobs.append(process_7)

    if ELECTRONICS in category_list:
        process_8 = Process(target=electronics_hierarchy.start_program)

        process_8.daemon = True

        jobs.append(process_8)

    if HANDMADE in category_list:
        process_9 = Process(target=handmade_hierarchy.start_program)

        process_9.daemon = True

        jobs.append(process_9)

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
