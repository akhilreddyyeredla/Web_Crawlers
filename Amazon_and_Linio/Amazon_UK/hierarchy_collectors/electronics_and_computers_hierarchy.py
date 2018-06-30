from response_getter import get_content
from helpers import string_format, url_format
from file_operations import create_directory_and_hierarchy_files
from threading import Thread
from Queue import Queue
from DataCollectors_Configuration import NO_OF_THEARDS
from CONSTANTS import *
from bs4 import BeautifulSoup

urls_queue = Queue()

urls_list = []


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


def find_nav_hierarchy(hierarchy, page_soup):
    """

    :param hierarchy:hierarchy name
    :param page_soup: current url
    :return: None
    """
    response = page_soup
    if response:
        nav_container = response.find('div', {'class': LEFT_NAV_CLASS})
        if nav_container:
            nav_string = str(nav_container).split('<h3>')
            # for all nav_string find see more tag and hirarachy name and
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
                            if 'All_Electronics|Accessories|Computer_Accessories|Accessories|Accessories|' in hierarchy_name or 'All_Electronics|Computers_Components_and_Accessories|Accessories|Accessories|' in hierarchy_name:
                                pass
                            else:
                                # for current url find the traverse style as it was
                                find_traverse_type(hierarchy_name, category_url, False)


def get_indent_two_hierarchy(hierarchy, page_soup, url,flag):
    """

    :param url: Current Page Url
    :param flag: true or flase if true it is first time traverse if false then it is second time traverse
    :param hierarchy: hierarchy_name
    :param page_soup: BeautifulSoup response
    :return: None
    """
    response = page_soup
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

                    if flag:
                        find_traverse_type(hierarchy_name, category_url,flag=False)
                    else:
                        urls_queue.put(line)

            # If length of anchor tags is zero then it is the last level of hierarchy
            # Now create directory and save hierarchy and url in a file in that directory
            else:
                store_last_level_of_hierarchy(hierarchy, response, url)


def find_traverse_type(hierarchy, url, flag):
    """

    :param hierarchy: category hierarchy
    :param url: current page utl
    :param flag: true or false  if it is true then the function was called for 1st time  if not then it is second time
    :return: None
    """
    response = get_content(url)
    if response:
        category_response_type_1 = response.find('div', {'class': LEFT_NAV_CLASS})
        category_response_type_3 = response.find('ul', {'class': INDENT_TWO_CLASS})

        if category_response_type_3:

            get_indent_two_hierarchy(hierarchy, response, url,flag=flag)

        elif category_response_type_1:

            find_nav_hierarchy(hierarchy, response)


def get_tree_hierarchy(hierarchy, url):
    """

    :param hierarchy: category_hierarchy name
    :param url: current_page_url
    :return: None
    :working: this function will find out 1st level of hierarchy  and calls  find_traverse_type(hierarchy_name, category_url)
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
                find_traverse_type(hierarchy_name, category_url, flag=True)
                # print(line)
            urls_queue.join()


def start_program():
    link = 'Electronics_and_Computers|All_Electronics|https://www.amazon.co.uk/electronics-camera-mp3-ipod-tv/b/ref=sd_allcat_el/262-6468249-9592357?ie=UTF8&node=560798'

    link_list = link.split('|')
    name = '|'.join(link_list[0:-1])
    url = link_list[-1]
    create_workers()
    get_tree_hierarchy(name, url)






