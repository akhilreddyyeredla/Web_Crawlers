from bs4 import BeautifulSoup

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

def get_nav_hierarchy(hierarchy, url):
    """

    :param hierarchy:hierarchy name
    :param url: current page url
    :return: none
    :working: Finds the 1st level of hierarchy which contains left_nav_class as a traverse style
              and then adds that links to queue
    """
    response = get_content(url)
    if response:
        nav_container = response.find('div', {'class': LEFT_NAV_CLASS})
        if nav_container:
            nav_string = str(nav_container).split('<h3>')
            for nav in nav_string:
                nav_html = BeautifulSoup(nav, 'lxml')
                if nav_html:

                    category_container = nav_html.find('p')

                    if category_container:
                        main_category_name = string_format(category_container)
                        see_more_tag = nav_html.find("p", {"class": SEE_MORE_CLASS})
                        if see_more_tag:
                            if main_category_name in 'Angebote_and_Aktionen|Kindle_Fire_and_Echo|Smartphones_and_mehr|Ratgeber_and_Services':
                                continue
                            else:
                                category_url = url_format(see_more_tag.a["href"])
                                hierarchy_name = '{}|{}'.format(hierarchy, main_category_name)

                                # for current url find the traverse style as it was
                                line = '{}|{}'.format(hierarchy_name, category_url)
                                urls_queue.put(line)
                                # print line
                        else:
                            anchor_tags = nav_html.findAll('a')
                            if len(anchor_tags) != 0:
                                for anchor_tag in anchor_tags:
                                    sub_category_name = string_format(anchor_tag)
                                    if main_category_name in 'Angebote_and_Aktionen|Kindle_Fire_and_Echo|Smartphones_and_mehr|Ratgeber_and_Services':
                                        continue
                                    else:
                                        hierarchy_name = '{}|{}|{}'.format(hierarchy, main_category_name, sub_category_name)
                                        sub_category_url = url_format(anchor_tag['href'])

                                        line = '{}|{}'.format(hierarchy_name, sub_category_url)
                                        urls_queue.put(line)
                                        # print line


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
        'Elektronik_and_Computer|Elektro_Gro_gera_te|https://www.amazon.de//Haushaltsger%C3%A4te-Hausger%C3%A4te/b/ref=sd_allcat_la/257-0336225-6363765?ie=UTF8&node=908823031',
        'Elektronik_and_Computer|Software|https://www.amazon.de//Software/b/ref=sd_allcat_soft/257-0336225-6363765?ie=UTF8&node=301927',
        'Elektronik_and_Computer|Computer_Zubeho_r|https://www.amazon.de/s/ref=lp_429874031_ex_n_1?rh=n%3A340843031&bbn=340843031&ie=UTF8&qid=1519031569'
    ]

    nav_links = [
                'Elektronik_and_Computer|Alle_Produkte|https://www.amazon.de//Elektronik-Foto/b/ref=sd_allcat_el/257-0336225-6363765?ie=UTF8&node=562066'
    ]
    for link in links:
        link_list = link.split('|')
        name = '|'.join(link_list[0:-1])
        url = link_list[-1]
        create_workers()
        get_tree_hierarchy(name, url)

    # for all links the tree hierarchy links split that line into hierarchy name and url by '|'
    # after that call respective function to find hiearachy
    for link in nav_links:
        link_list = link.split('|')
        name = '|'.join(link_list[0:-1])
        url = link_list[-1]
        get_nav_hierarchy(name, url)

    # wait till the links are finished in the queue
    urls_queue.join()