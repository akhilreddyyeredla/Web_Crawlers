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
    :param url: current url
    :return: None
    :working : It will find the 1st level of hierarchy and add the links to the queue
    """
    response_container = get_content(url)
    if response_container:
        response = response_container.find('div', {'class': 'a-section a-spacing-base'})
        if response:

            nav_container = response.find('div', {'class': LEFT_NAV_CLASS})
            if nav_container:

                nav_string = str(nav_container).split('<h3>')
                # for all nav_string find see more tag and hirarachy name and  store sub category url
                for nav in nav_string:
                    nav_html = BeautifulSoup(nav, 'lxml')
                    if nav_html:
                        category_container = nav_html.find('p')
                        if category_container:
                            main_category_name = string_format(category_container)
                            see_more_tag = nav_html.find("p", {"class": SEE_MORE_CLASS})
                            if see_more_tag:
                                category_url = url_format(see_more_tag.a["href"])
                                hierarchy_name = '{}|{}'.format(hierarchy, main_category_name)
                                line = '{}|{}'.format(hierarchy_name, category_url)
                                urls_queue.put(line)
                                print line


def start_program():

    nav_links = [
            'Electro_nica|Fotografi_a_y_videoca_maras|https://www.amazon.es/fotografia-videocamaras/b/ref=sd_allcat_pcam/258-3512463-6364615?ie=UTF8&node=664660031',
            'Electro_nica|Mo_viles_y_telefoni_a|https://www.amazon.es/Moviles-Telefonia/b/ref=sd_allcat_tele/258-3512463-6364615?ie=UTF8&node=931491031',
            'Electro_nica|TV_Vi_deo_y_Home_Cinema|https://www.amazon.es/tv-video-home-cinema/b/ref=sd_allcat_tvv/258-3512463-6364615?ie=UTF8&node=664659031',
            'Electro_nica|Todo_en_Electro_nica|https://www.amazon.es/Electr%C3%B3nica/b/ref=sd_allcat_ele/258-3512463-6364615?ie=UTF8&node=599370031'
        ]
    # for all links the tree hierarchy links split that line into hierarchy name and url by '|'
    # after that call respective function to find hiearachy
    for link in nav_links:
        link_list = link.split('|')
        name = '|'.join(link_list[0:-1])
        url = link_list[-1]
        get_nav_hierarchy(name, url)

    # wait till all the links in the queue are finished
    urls_queue.join()
