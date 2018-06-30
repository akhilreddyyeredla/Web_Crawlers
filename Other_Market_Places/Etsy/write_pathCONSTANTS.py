
from Common.Etsy_common_imports import *

def write_path():
    line_1 = "{}_QUEUE_PATH = '{}{}{}{}{}{}products_page_links.txt'\n"

    line_2 = "{}_COMPLETED_PATH = '{}{}{}{}{}{}sub_sub_category_completed_{}.txt '\n"

    line_3 = "{}_SKIPPED_PATH = '{}{}{}{}{}{}skipped_queue_{}.txt'\n\n"

    category_list = ['accessories', 'art_and_collectibles', 'bags_and_purses', 'bath_and_beauty',
                     'books_movies_and_music', 'clothing', 'craft_supplies_and_tools', 'electronics_and_accessories',
                     'home_and_living', 'jewelry', 'paper_and_party_supplies', 'pet_supplies', 'shoes', 'toys_and_games',
                     'weddings']

    path = 'path_CONSTANTS.py'

    file = open(path, "w")

    for category in category_list:
        line = "{} = '{}'".format(category.upper(),category)

        CATEGORY = category.upper()
        file.write(line_1.format(CATEGORY,
                                 DataCollectors_Configuration.ROOT_FOLDER,
                                 DataCollectors_Configuration.PATH_STYLE,
                                 DataCollectors_Configuration.ETSY_PROJECT_NAME,
                                 DataCollectors_Configuration.PATH_STYLE,
                                 category,
                                 DataCollectors_Configuration.PATH_STYLE,
                                 category))
        file.write(line_2.format(CATEGORY,
                                 DataCollectors_Configuration.ROOT_FOLDER,
                                 DataCollectors_Configuration.PATH_STYLE,
                                 DataCollectors_Configuration.ETSY_PROJECT_NAME,
                                 DataCollectors_Configuration.PATH_STYLE,
                                 category,
                                 DataCollectors_Configuration.PATH_STYLE,
                                 category))
        file.write(line_3.format(CATEGORY,
                                 DataCollectors_Configuration.ROOT_FOLDER,
                                 DataCollectors_Configuration.PATH_STYLE,
                                 DataCollectors_Configuration.ETSY_PROJECT_NAME,
                                 DataCollectors_Configuration.PATH_STYLE,
                                 category,
                                 DataCollectors_Configuration.PATH_STYLE,
                                 category))
