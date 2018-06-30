import sys
sys.path.insert(0, r'/usr/datacollector')

from info_collectors import health_and_beauty_info_collector, electronics_computers_and_office_info_collector, \
    home_improvement_info_collector, sports_fitness_and_outdoors_info_collector, books_and_audible_info_collector, \
    toys_kids_and_baby_info_collector, home_and_kitchen_info_collector, fashion_info_collector
from url_collectors import health_and_beauty_url_collector, electronics_computers_and_office_url_collector, \
    home_improvement_url_collector, sports_fitness_and_outdoors_url_collector, books_and_audible_url_collector, \
    toys_kids_and_baby_url_collector, home_and_kitchen_url_collector, fashion_url_collector
from hierarchy_collectors import health_and_beauty_hierarchy, electronics_computers_and_office_hierarchy, \
    home_improvement_hierarchy, sports_fitness_and_outdoors_hierarchy, books_and_audible_hierarchy, \
    toys_kids_and_baby_hierarchy, home_and_kitchen_hierarchy, fashion_hierarchy

from CONSTANTS import *
from multiprocessing import Process
from DataCollectors_Configuration import AMAZON_AUS_CATEGORY_LIST, START_HIERARCHY_COLLECTION, START_URL_COLLECTION, \
    START_INFO_COLLECTION

category_list = '|'.join(AMAZON_AUS_CATEGORY_LIST)


def start_info_collection():
    jobs = []
    if HEALTH_AND_BEAUTY in category_list:
        process_1 = Process(target=health_and_beauty_info_collector.start_info_collection, args=(HEALTH_AND_BEAUTY,))
        process_1.daemon = True
        jobs.append(process_1)

    if ELECTRONICS_COMPUTERS_AND_OFFICE in category_list:
        process_2 = Process(target=electronics_computers_and_office_info_collector.start_info_collection,
                            args=(ELECTRONICS_COMPUTERS_AND_OFFICE,))
        process_2.daemon = True
        jobs.append(process_2)

    if HOME_IMPROVEMENT in category_list:
        process_3 = Process(target=home_improvement_info_collector.start_info_collection, args=(HOME_IMPROVEMENT,))
        process_3.daemon = True
        jobs.append(process_3)

    if SPORTS_FITNESS_AND_OUTDOORS in category_list:
        process_4 = Process(target=sports_fitness_and_outdoors_info_collector.start_info_collection,
                            args=(SPORTS_FITNESS_AND_OUTDOORS,))
        process_4.daemon = True
        jobs.append(process_4)

    if BOOKS_AND_AUDIBLE in category_list:
        process_5 = Process(target=books_and_audible_info_collector.start_info_collection, args=(BOOKS_AND_AUDIBLE,))
        process_5.daemon = True
        jobs.append(process_5)

    if TOYS_KIDS_AND_BABY in category_list:
        process_6 = Process(target=toys_kids_and_baby_info_collector.start_info_collection, args=(TOYS_KIDS_AND_BABY,))
        process_6.daemon = True
        jobs.append(process_6)

    if HOME_AND_KITCHEN in category_list:
        process_7 = Process(target=home_and_kitchen_info_collector.start_info_collection, args=(HOME_AND_KITCHEN,))
        process_7.daemon = True
        jobs.append(process_7)

    if FASHION in category_list:
        process_8 = Process(target=fashion_info_collector.start_info_collection, args=(FASHION,))
        process_8.daemon = True
        jobs.append(process_8)

    for job in jobs:
        job.start()
    for job in jobs:
        if job.is_alive():
            job.join()


def start_url_collection():
    jobs = []
    if HEALTH_AND_BEAUTY in category_list:
        process_1 = Process(target=health_and_beauty_url_collector.start_program, args=(HEALTH_AND_BEAUTY,))
        process_1.daemon = True
        jobs.append(process_1)
    if ELECTRONICS_COMPUTERS_AND_OFFICE in category_list:
        process_2 = Process(target=electronics_computers_and_office_url_collector.start_program,
                            args=(ELECTRONICS_COMPUTERS_AND_OFFICE,))
        process_2.daemon = True
        jobs.append(process_2)

    if HOME_IMPROVEMENT in category_list:
        process_3 = Process(target=home_improvement_url_collector.start_program, args=(HOME_IMPROVEMENT,))
        process_3.daemon = True
        jobs.append(process_3)

    if SPORTS_FITNESS_AND_OUTDOORS in category_list:
        process_4 = Process(target=sports_fitness_and_outdoors_url_collector.start_program,
                            args=(SPORTS_FITNESS_AND_OUTDOORS,))
        process_4.daemon = True
        jobs.append(process_4)

    if BOOKS_AND_AUDIBLE in category_list:
        process_5 = Process(target=books_and_audible_url_collector.start_program, args=(BOOKS_AND_AUDIBLE,))
        process_5.daemon = True
        jobs.append(process_5)

    if TOYS_KIDS_AND_BABY in category_list:
        process_6 = Process(target=toys_kids_and_baby_url_collector.start_program, args=(TOYS_KIDS_AND_BABY,))
        process_6.daemon = True
        jobs.append(process_6)

    if HOME_AND_KITCHEN in category_list:
        process_7 = Process(target=home_and_kitchen_url_collector.start_program, args=(HOME_AND_KITCHEN,))
        process_7.daemon = True
        jobs.append(process_7)

    if FASHION in category_list:
        process_8 = Process(target=fashion_url_collector.start_program, args=(FASHION,))
        process_8.daemon = True
        jobs.append(process_8)

    for job in jobs:
        job.start()
    for job in jobs:
        if job.is_alive():
            job.join()


def start_hierarchy_collection():
    jobs = []
    if HEALTH_AND_BEAUTY in category_list:
        process_1 = Process(target=health_and_beauty_hierarchy.start_program)
        process_1.daemon = True

        jobs.append(process_1)

    if ELECTRONICS_COMPUTERS_AND_OFFICE in category_list:
        process_2 = Process(target=electronics_computers_and_office_hierarchy.start_program)
        process_2.daemon = True

        jobs.append(process_2)

    if HOME_IMPROVEMENT in category_list:
        process_3 = Process(target=home_improvement_hierarchy.start_program)
        process_3.daemon = True

        jobs.append(process_3)

    if SPORTS_FITNESS_AND_OUTDOORS in category_list:
        process_4 = Process(target=sports_fitness_and_outdoors_hierarchy.start_program)
        process_4.daemon = True

        jobs.append(process_4)

    if BOOKS_AND_AUDIBLE in category_list:
        process_5 = Process(target=books_and_audible_hierarchy.start_program)
        process_5.daemon = True

        jobs.append(process_5)

    if TOYS_KIDS_AND_BABY in category_list:
        process_6 = Process(target=toys_kids_and_baby_hierarchy.start_program)
        process_6.daemon = True

        jobs.append(process_6)

    if HOME_AND_KITCHEN in category_list:
        process_7 = Process(target=home_and_kitchen_hierarchy.start_program)
        process_7.daemon = True

        jobs.append(process_7)

    if FASHION in category_list:
        process_8 = Process(target=fashion_hierarchy.start_program)
        process_8.daemon = True

        jobs.append(process_8)

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
