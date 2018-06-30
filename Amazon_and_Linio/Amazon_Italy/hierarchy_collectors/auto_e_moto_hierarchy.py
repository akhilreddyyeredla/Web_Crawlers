from response_getter import get_content
from helpers import string_format, url_format
from file_operations import create_directory_and_hierarchy_files
from threading import Thread
from Queue import Queue
from DataCollectors_Configuration import NO_OF_THEARDS
from CONSTANTS import *

urls_queue = Queue()


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


def store_last_level_of_hierarchy(hierarchy, page_soup, url):
    response = page_soup
    if response:
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
                store_last_level_of_hierarchy(hierarchy, response, url)



def find_acs_nav_section(hierarchy, url):
    """

    :param hierarchy: hierarchy name
    :param url: current page url
    :return: None
    :Working: it will find out 1st level of hierarchy after that adds link into queue

    """
    response = get_content(url)
    if response:
        category_container = response.find('div', {'class': 'a-section a-spacing-base'})
        if category_container:
            category_list = category_container.findAll('div', {'class': ACS_SECTION_CLASS})
            if len(category_list) != 0:
                for category in category_list:
                    category_tag = category.find('div', {'class': 'acs-ln-links'})
                    if category_tag:
                        category_name = string_format(category_tag)
                        if category_name in IGNORE_LIST:
                            continue
                        else:
                            sub_category_links = category.findAll('a')
                            if len(sub_category_links) != 0:
                                for sub_category_link in sub_category_links:
                                    sub_category_name = string_format(sub_category_link)
                                    sub_category_url = url_format(sub_category_link['href'])

                                    hierarchy_name = '{}|{}|{}'.format(hierarchy, category_name, sub_category_name)

                                    line = '{}|{}'.format(hierarchy_name, sub_category_url)
                                    if 'Tutto' in hierarchy_name:
                                        urls_queue.put(line)
                                    else:
                                        pass


def start_program():
    links = [
        'Auto_e_Moto|Accessori_e_parti_per_auto|https://www.amazon.it/Auto-e-Moto/b/ref=sd_allcat_car_acc_parts/259-2339394-2872550?ie=UTF8&node=1571280031',
        'Auto_e_Moto|Accessori_e_parti_per_moto|https://www.amazon.it/Moto-accessoricomponenti/b/ref=sd_allcat_moto_acc_parts/259-2339394-2872550?ie=UTF8&node=2420930031'

    ]
    for link in links:
        link_list = link.split('|')
        name = '|'.join(link_list[0:-1])
        url = link_list[-1]
        create_workers()
        find_acs_nav_section(name, url)
    urls_queue.join()

# find_acs_nav_section('p','https://www.amazon.it/s/ref=lp_2420687031_ex_n_1?rh=n%3A1571280031&bbn=1571280031&ie=UTF8&qid=1519125471')
