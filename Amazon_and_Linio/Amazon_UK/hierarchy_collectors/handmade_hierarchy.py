from response_getter import get_content
from helpers import string_format, url_format
from file_operations import create_directory_and_hierarchy_files
from threading import Thread
from Queue import Queue
from DataCollectors_Configuration import NO_OF_THEARDS
from CONSTANTS import *

urls_queue = Queue()


# site = 'https://www.amazon.com/International-Shipping-Direct/b/ref=sd_allcat_full_store_dir_VisitAg?ie=UTF8&node=230659011'


def create_workers():
    """
    Creates threadpool and with max number of threads mentioned in cinfig file and targets work fucntion
    :return: none
    """
    for _ in range(NO_OF_THEARDS):
        thread = Thread(target=work)
        # make the thread daemon to stop the thread when main program exits
        thread.daemon = False
        thread.start()


def work():
    """
    Work is function which gets url from queue and slipt it into hierarchy name and page url
    then pass that url to find_hierarchy(hierarchy_name, page_url) this function will
    travel recurcivesly and find hierarchy
    :return: None
    """
    while True:
        value = urls_queue.get().split('|')
        name = '|'.join(value[0:-1])
        url = value[-1]
        find_hierarchy(name, url)  # to call scrapper method which collects all products urls
        urls_queue.task_done()


def find_hierarchy(hierarchy, url):
    """

    :param hierarchy: category_hierarchy name
    :param url: current_page_url
    :return: None
    :working: recurssion function to find the hierarchy, last_page and products_page_url
    """
    response = get_content(url)
    if response:
        sub_categories_container = response.find('ul',
                                                 {'class': INDENT_TWO_CLASS})

        if sub_categories_container:
            anchor_tags = sub_categories_container.findAll('a', {'class': NORMAL_ANCHOR_TAG_CLASS})

            # If length of anchor tags is not zero then it contains more categories
            if len(anchor_tags) != 0:
                # Now for each category_url again call find_hierarchy function
                for anchor_tag in anchor_tags:
                    category_name = string_format(anchor_tag)
                    category_url = url_format(anchor_tag['href'])

                    hierarchy_name = '{}|{}'.format(hierarchy, category_name)

                    find_hierarchy(hierarchy_name, category_url)

            # If length of anchor tags is zero then it is the last level of hierarchy
            # Now create directory and save hierarchy and url in a file in that directory
            else:
                h4_tag = response.find('h4', {'class': H4_TAG_CLASS})
                if h4_tag:
                    category_name = string_format(h4_tag)

                    category_url_tag = response.find('a', {'title': LAYOUT_PICKER})

                    # To get tiles view url
                    if category_url_tag:
                        category_url = url_format(category_url_tag['href'])
                    else:
                        category_url = url

                    # Get hierarchy name
                    if category_name in hierarchy:
                        hierarchy_name = hierarchy
                    else:
                        hierarchy_name = '{}|{}'.format(hierarchy, category_name)

                    line = '{}|{}'.format(hierarchy_name, category_url)
                    print line

                    # store the line in a file and create hierarchy directory
                    create_directory_and_hierarchy_files(hierarchy_name, line)

def start_program():
    links = [
        'Handmade|Baby|https://www.amazon.co.uk/b/ref=sd_allcat_HM_baby/262-6468249-9592357?ie=UTF8&node=10293736031',
        'Handmade|Clothing_Shoes_and_Accessories|https://www.amazon.co.uk/b/ref=sd_allcat_HM_clothingaccessories/262-6468249-9592357?ie=UTF8&node=10293738031',
        'Handmade|Gifts|https://www.amazon.co.uk/b/ref=sd_allcat_HM_Gifts/262-6468249-9592357?ie=UTF8&node=14075837031',
        'Handmade|Home_and_Kitchen|https://www.amazon.co.uk/b/ref=sd_allcat_HM_homekitchen/262-6468249-9592357?ie=UTF8&node=10293740031',
        'Handmade|Jewellery|https://www.amazon.co.uk/b/ref=sd_allcat_HM_Jewelry/262-6468249-9592357?ie=UTF8&node=10293741031',
        'Handmade|Made_in_Italy|https://www.amazon.co.uk/b/ref=sd_allcat_HM_mii/262-6468249-9592357?ie=UTF8&node=12440600031',
        'Handmade|Stationery_and_Party_Supplies|https://www.amazon.co.uk/b/ref=sd_allcat_HM_stationery/262-6468249-9592357?ie=UTF8&node=10293745031',
        'Handmade|Toys_and_Games|https://www.amazon.co.uk/b/ref=sd_allcat_HM_toysgames/262-6468249-9592357?ie=UTF8&node=10293746031'

    ]
    create_workers()
    for link in links:
        urls_queue.put(link)
    urls_queue.join()













