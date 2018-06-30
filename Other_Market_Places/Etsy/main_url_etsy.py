import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = '/'.join(dir_path.split('/')[0:-1])
sys.path.insert(0, dir_path)
from Common.Etsy_common_imports import *

project = DataCollectors_Configuration.ETSY_PROJECT_NAME

PATH_STYLE = DataCollectors_Configuration.PATH_STYLE
ROOT_FOLDER = DataCollectors_Configuration.ROOT_FOLDER


def files_path(name):
    """

    :param name: category_name as a input
    :return: project_name , category_queue_file path name, sub_category_queue path, sub_sub_category_queue path and
            category_name
    """
    category_queue = ROOT_FOLDER + PATH_STYLE + project + PATH_STYLE + name + DataCollectors_Configuration.CATEGORY_QUEUE.format(
        name)
    sub_category_queue = ROOT_FOLDER + PATH_STYLE + project + PATH_STYLE + name + DataCollectors_Configuration.SUB_CATEGORY_QUEUE.format(
        name)
    sub_sub_category_queue = ROOT_FOLDER + PATH_STYLE + project + PATH_STYLE + name + DataCollectors_Configuration.SUB_SUB_CATEGORY_QUEUE.format(
        name)
    return ROOT_FOLDER + PATH_STYLE + project + PATH_STYLE + name, category_queue, sub_category_queue, sub_sub_category_queue, name


'''
this 'def function_name()' is function which passes project name, that category main url, category queue path,
sub category queue path, sub sub category queue path and category name to category_name_scrapper.Workers this function
will start scrapping process    
'''


def accesories():
    project_name, category_queue, sub_category_queue, sub_sub_category_queue, category_name = files_path(
        DataCollectors_Configuration.ACCESSORIES)
    accessories_scrapper.Workers(project_name, DataCollectors_Configuration.ACCESSORIES_URL,
                                 category_queue,
                                 sub_category_queue, sub_sub_category_queue, category_name)


def art_and_collectables():
    project_name, category_queue, sub_category_queue, sub_sub_category_queue, category_name = files_path(
        DataCollectors_Configuration.ART_AND_COLLECTIBLES)
    art_and_collectibles_scrapper.Workers(project_name,
                                          DataCollectors_Configuration.ART_AND_COLLECTIBLES_URL,
                                          category_queue,
                                          sub_category_queue, sub_sub_category_queue, category_name)


def bags_and_purses():
    project_name, category_queue, sub_category_queue, sub_sub_category_queue, category_name = files_path(
        DataCollectors_Configuration.BAGS_AND_PURSES)
    bags_and_purses_scrapper.Workers(project_name,
                                     DataCollectors_Configuration.BAGS_AND_PURSES_URL,
                                     category_queue,
                                     sub_category_queue, sub_sub_category_queue, category_name)


def bath_and_beauty():
    project_name, category_queue, sub_category_queue, sub_sub_category_queue, category_name = files_path(
        DataCollectors_Configuration.BATH_AND_BEAUTY)
    bath_and_beauty_scrapper.Workers(project_name,
                                     DataCollectors_Configuration.BATH_AND_BEAUTY_URL,
                                     category_queue,
                                     sub_category_queue, sub_sub_category_queue, category_name)


def books_movies_and_music():
    project_name, category_queue, sub_category_queue, sub_sub_category_queue, category_name = files_path(
        DataCollectors_Configuration.BOOKS_MOVIES_AND_MUSIC)
    books_movies_and_music_scrapper.Workers(project_name,
                                            DataCollectors_Configuration.BOOKS_MOVIES_AND_MUSIC_URL,
                                            category_queue, sub_category_queue, sub_sub_category_queue,
                                            category_name)


def clothing():
    project_name, category_queue, sub_category_queue, sub_sub_category_queue, category_name = files_path(
        DataCollectors_Configuration.CLOTHING)
    clothing_scrapper.Workers(project_name, DataCollectors_Configuration.CLOTHING_URL,
                              category_queue,
                              sub_category_queue, sub_sub_category_queue, category_name)


def craft_supplies_and_tools():
    project_name, category_queue, sub_category_queue, sub_sub_category_queue, category_name = files_path(
        DataCollectors_Configuration.CRAFT_SUPPLIES_AND_TOOLS)
    craft_supplies_and_tools_scrapper.Workers(project_name,
                                              DataCollectors_Configuration.CRAFT_SUPPLIES_AND_TOOLS_URL,
                                              category_queue, sub_category_queue, sub_sub_category_queue,
                                              category_name)


def electronics_and_accessories():
    project_name, category_queue, sub_category_queue, sub_sub_category_queue, category_name = files_path(
        DataCollectors_Configuration.ELECTRONICS_AND_ACCESSORIES)
    electronics_and_accessories_scrapper.Workers(project_name,
                                                 DataCollectors_Configuration.ELECTRONICS_AND_ACCESSORIES_URL,
                                                 category_queue, sub_category_queue, sub_sub_category_queue,
                                                 category_name)


def home_and_living():
    project_name, category_queue, sub_category_queue, sub_sub_category_queue, category_name = files_path(
        DataCollectors_Configuration.HOME_AND_LIVING)
    home_and_living_scrapper.Workers(project_name,
                                     DataCollectors_Configuration.HOME_AND_LIVING_URL,
                                     category_queue,
                                     sub_category_queue, sub_sub_category_queue, category_name)


def jewelry():
    project_name, category_queue, sub_category_queue, sub_sub_category_queue, category_name = files_path(
        DataCollectors_Configuration.JEWELRY)
    jewelry_scrapper.Workers(project_name, DataCollectors_Configuration.JEWELRY_URL,
                             category_queue,
                             sub_category_queue, sub_sub_category_queue, category_name)


def paper_and_party_supplies():
    project_name, category_queue, sub_category_queue, sub_sub_category_queue, category_name = files_path(
        DataCollectors_Configuration.PAPER_AND_PARTY_SUPPLIES)
    paper_and_party_supplies_scrapper.Workers(project_name,
                                              DataCollectors_Configuration.PAPER_AND_PARTY_SUPPLIES_URL,
                                              category_queue, sub_category_queue, sub_sub_category_queue,
                                              category_name)


def pet_supplies():
    project_name, category_queue, sub_category_queue, sub_sub_category_queue, category_name = files_path(
        DataCollectors_Configuration.PET_SUPPLIES)
    pet_supplies_scrapper.Workers(project_name,
                                  DataCollectors_Configuration.PET_SUPPLIES_URL,
                                  category_queue,
                                  sub_category_queue, sub_sub_category_queue, category_name)


def shoes():
    project_name, category_queue, sub_category_queue, sub_sub_category_queue, category_name = files_path(
        DataCollectors_Configuration.SHOES)
    shoes_scrapper.Workers(project_name, DataCollectors_Configuration.SHOES_URL,
                           category_queue,
                           sub_category_queue, sub_sub_category_queue, category_name)


def toys_and_games():
    project_name, category_queue, sub_category_queue, sub_sub_category_queue, category_name = files_path(
        DataCollectors_Configuration.TOYS_AND_GAMES)
    toys_and_games_scrapper.Workers(project_name,
                                    DataCollectors_Configuration.TOYS_AND_GAMES_URL,
                                    category_queue,
                                    sub_category_queue, sub_sub_category_queue, category_name)


def weddings():
    project_name, category_queue, sub_category_queue, sub_sub_category_queue, category_name = files_path(
        DataCollectors_Configuration.WEDDINGS)
    weddings_scrapper.Workers(project_name, DataCollectors_Configuration.WEDDINGS_URL,
                              category_queue,
                              sub_category_queue, sub_sub_category_queue, category_name)


category = set(DataCollectors_Configuration.ETSY_CATEGORY_LIST)


def start_product_url_collection():
    """
    this function assign targets to each thread and launch them to collect product urls
    :return: none
    """
    jobs = []

    if DataCollectors_Configuration.ACCESSORIES in category:
        thread_1 = multiprocessing.Process(target=accessories_products_url_collector.start_collection)
        thread_1.daemon = True

        jobs.append(thread_1)

    if DataCollectors_Configuration.ART_AND_COLLECTIBLES in category:
        thread_2 = multiprocessing.Process(target=art_and_collectibles_products_url_collector.start_collection)
        thread_2.daemon = True
        jobs.append(thread_2)

    if DataCollectors_Configuration.BAGS_AND_PURSES in category:
        thread_3 = multiprocessing.Process(target=bags_and_purses_products_url_collector.start_collection)
        thread_3.daemon = True
        jobs.append(thread_3)

    if DataCollectors_Configuration.BOOKS_MOVIES_AND_MUSIC in category:
        thread_4 = multiprocessing.Process(target=books_movies_and_music_products_url_collector.start_collection)
        thread_4.daemon = True
        jobs.append(thread_4)
    if DataCollectors_Configuration.BATH_AND_BEAUTY in category:
        thread_5 = multiprocessing.Process(target=bath_and_beauty_products_url_collector.start_collection)
        thread_5.daemon = True
        jobs.append(thread_5)

    if DataCollectors_Configuration.CLOTHING in category:
        thread_6 = multiprocessing.Process(target=clothing_products_url_collector.start_collection)
        thread_6.daemon = True
        jobs.append(thread_6)

    if DataCollectors_Configuration.CRAFT_SUPPLIES_AND_TOOLS in category:
        thread_7 = multiprocessing.Process(target=craft_supplies_and_tools_products_url_collector.start_collection)
        thread_7.daemon = True
        jobs.append(thread_7)

    if DataCollectors_Configuration.ELECTRONICS_AND_ACCESSORIES in category:
        thread_8 = multiprocessing.Process(target=electronics_and_accessories_products_url_collector.start_collection)
        thread_8.daemon = True
        jobs.append(thread_8)

    if DataCollectors_Configuration.HOME_AND_LIVING in category:
        thread_9 = multiprocessing.Process(target=home_and_living_products_url_collector.start_collection)
        thread_9.daemon = True
        jobs.append(thread_9)

    if DataCollectors_Configuration.JEWELRY in category:
        thread_10 = multiprocessing.Process(target=jewelry_products_url_collector.start_collection)
        thread_10.daemon = True
        jobs.append(thread_10)

    if DataCollectors_Configuration.PAPER_AND_PARTY_SUPPLIES in category:
        thread_11 = multiprocessing.Process(target=paper_and_party_supplies_products_url_collector.start_collection)
        thread_11.daemon = True
        jobs.append(thread_11)

    if DataCollectors_Configuration.PET_SUPPLIES in category:
        thread_12 = multiprocessing.Process(target=pet_supplies_products_url_collector.start_collection)
        thread_12.daemon = True
        jobs.append(thread_12)

    if DataCollectors_Configuration.SHOES in category:
        thread_13 = multiprocessing.Process(target=shoes_products_url_collector.start_collection)
        thread_13.daemon = True
        jobs.append(thread_13)

    if DataCollectors_Configuration.TOYS_AND_GAMES in category:
        thread_14 = multiprocessing.Process(target=toys_and_games_products_url_collector.start_collection)
        thread_14.daemon = True
        jobs.append(thread_14)

    if DataCollectors_Configuration.WEDDINGS in category:
        thread_15 = multiprocessing.Process(target=weddings_products_url_collector.start_collection)
        thread_15.daemon = True

        jobs.append(thread_15)

    # Start the threads which are present in the list
    for job in jobs:
        job.start()
    for job in jobs:
        job.join()


if __name__ == '__main__':
    try:
        start_product_url_collection()


    except KeyboardInterrupt as e:
        # print e
        sys.exit('intrepted')
