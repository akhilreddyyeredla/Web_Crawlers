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
    Creates threadpool and with max number of threads mentioned in config file and targets work fucntion
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


def get_tree_hierarchy(hierarchy, url):
    """

    :param hierarchy: category_hierarchy name
    :param url: current_page_url
    :return: None
    :working: this function will find out 1st level of hierarchy  and adds link to the queue
    """
    response = get_content(url)

    if response:
        sub_categories_container = response.find('ul',
                                                 {'class': INDENT_ONE_CLASS})
        if sub_categories_container:
            anchor_tags = sub_categories_container.findAll('a', {'class': NORMAL_ANCHOR_TAG_CLASS})
            for anchor_tag in anchor_tags:
                category_name = string_format(anchor_tag)
                category_url = url_format(anchor_tag['href'])

                hierarchy_name = '{}|{}'.format(hierarchy, category_name)
                line = '{}|{}'.format(hierarchy_name, category_url)

                urls_queue.put(line)
                # print(line)
            urls_queue.join()


def start_program():
    links = [
            'Electronics|All_Electronics|https://www.amazon.ca/electronics-tv-pc-xbmc-gopro-bose/b/ref=sd_allcat_mj_all_electronics/143-4227003-6144506?ie=UTF8&node=667823011',
            'Electronics|Office_Electronics_and_Supplies|https://www.amazon.ca/office-products/b/ref=sd_allcat_mj_ce_office/143-4227003-6144506?ie=UTF8&node=6205511011',
            'Electronics|Car_Electronics|https://www.amazon.ca/b/ref=sd_allcat_mj_ce_gps/143-4227003-6144506?ie=UTF8&node=12638334011',
            'Electronics|Musical_Instruments|https://www.amazon.ca/musical-instruments-stage-studio/b/ref=sd_allcat_mj_ce_musicalins/143-4227003-6144506?ie=UTF8&node=6916844011'
            ]
    for link in links:
        link_list = link.split('|')
        name = '|'.join(link_list[0:-1])
        url = link_list[-1]
        create_workers()
        get_tree_hierarchy(name, url)

