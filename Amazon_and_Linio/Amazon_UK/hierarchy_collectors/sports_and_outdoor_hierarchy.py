from response_getter import get_content
from helpers import string_format, url_format
from file_operations import create_directory_and_hierarchy_files
from threading import Thread
from Queue import Queue
from DataCollectors_Configuration import NO_OF_THEARDS
from CONSTANTS import *

urls_queue = Queue()

urls_list = Queue()


def create_workers():
    """
    Creates threadpool and with max number of threads mentioned in config file and targets work fucntion
    :return: none
    """
    for _ in range(NO_OF_THEARDS):
        thread = Thread(target=work)
        # make the thread daemon to stop the thread when main program exits
        thread.daemon = True
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

            line_1 = 'completed|{}'.format(line)
            urls_list.put(line_1)
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

                    line = '{}|{}'.format(hierarchy_name, category_url)

                    urls_list.put(line)

                    find_hierarchy(hierarchy_name, category_url)


            # If length of anchor tags is zero then it is the last level of hierarchy
            # Now create directory and save hierarchy and url in a file in that directory
            else:
                store_last_level_of_hierarchy(hierarchy, response, url)


def collect_urls(hierarchy, raw_data):
    category_container = raw_data
    if category_container:
        category_name_tag = category_container.find('div', {'class': 'acs-category-tile-header'})
        category_url_tag = category_container.find('div', {'class': 'acs-category-tile-shopall '})
        category_urls_list = category_container.findAll('li')
        if category_name_tag:
            category_name = string_format(category_name_tag)
            hierarchy_name = '{}|{}'.format(hierarchy, category_name)
            if category_url_tag:
                category_url = url_format(category_url_tag.a['href'])
                line = '{}|{}'.format(hierarchy_name, category_url)
                urls_queue.put(line)
            else:
                for category_url_tag in category_urls_list:
                    category_url = url_format(category_url_tag.a['href'])
                    line = '{}|{}'.format(hierarchy_name, category_url)
                    urls_queue.put(line)


def get_tree_hierarchy(hierarchy, url):
    """

    :param hierarchy: hierarchy name
    :param url: current page url
    :return: none
    """

    resposne = get_content(url)
    if resposne:
        category_container_1 = resposne.find_all('div', {'class': 'acs-ux-innerc1 acs-category-tile-links '})
        category_container_2 = resposne.find_all('div', {'class': 'acs-ux-innerc2 acs-category-tile-links '})
        category_container_3 = resposne.find_all('div', {'class': 'acs-ux-innerc3 acs-category-tile-links '})

        for category_container in category_container_1:
            collect_urls(hierarchy, category_container)

        for category_container in category_container_2:
            collect_urls(hierarchy, category_container)

        for category_container in category_container_3:
            collect_urls(hierarchy, category_container)

        # wait till all the urls complete in queue
        urls_queue.join()


def start_program():
    link = 'Sports_and_Outdoors|All_Sports_and_Outdoors|https://www.amazon.co.uk/Sports-Exercise-Fitness-Bikes-Camping/b/ref=sd_allcat_allsp/262-6468249-9592357?ie=UTF8&node=318949011'

    link_list = link.split('|')
    name = '|'.join(link_list[0:-1])
    url = link_list[-1]
    create_workers()
    get_tree_hierarchy(name, url)


