from bs4 import BeautifulSoup

from response_getter import get_content
from helpers import string_format, url_format
from file_operations import create_directory_and_hierarchy_files
from threading import Thread
from Queue import Queue
from DataCollectors_Configuration import NO_OF_THEARDS
from CONSTANTS import *

# this queue is used to store urls and this queue is given as Threadpool queue
urls_queue = Queue()


def create_workers():
    """
    Creates threadpool and with max number of threads mentioned in cinfig file and targets work fucntion
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
    then pass that url to get_level_1_hierarchy(hierarchy_name, page_url) this function will
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


def find_carousal_sub_categories(hierarchy, page_soup, anchor_tag):
    """

    :param hierarchy: Hierarchy name
    :param page_soup: BeautifulSoup response
    :param anchor_tag: anchor tag to get category name and url
    :return: none
    :working: It wll find all the sub categories under carousal division and add them to url list
    """
    category_name = string_format(anchor_tag)
    category_id = anchor_tag['id']
    if category_name in IGNORE_LIST:
        pass
    else:
        sub_cat_id = 'sub{}'.format(category_id)
        sub_category_container = page_soup.find('div', {'id': sub_cat_id})
        if sub_category_container:
            sub_category_list = sub_category_container.findAll('a', {'class': SUB_CATEGORY_LIST_ANCHOR_TAG_CLASS})
            if len(sub_category_list) != 0:
                for sub_category in sub_category_list:
                    sub_category_name = string_format(sub_category)
                    sub_category_url = url_format(sub_category['href'])
                    if sub_category_name.replace(category_name, '') in IGNORE_LIST:
                        # If it is in ignore list skip that link
                        pass
                    else:
                        hierarchy_name = '{}|{}|{}'.format(hierarchy, category_name, sub_category_name)
                        line = '{}|{}'.format(hierarchy_name, sub_category_url)

                        # add links to the queue
                        print(line)
                        urls_queue.put(line)


        else:

            sub_category_url = url_format(anchor_tag['href'])
            hierarchy_name = '{}|{}'.format(hierarchy, category_name)
            line = '{}|{}'.format(hierarchy_name, sub_category_url)

            # add links to the queue
            urls_queue.put(line)


def find_carousel_hierarchy(hierarchy, page_soup):
    """

    :param hierarchy: Hierarchy_name
    :param page_soup: Beautifulsoup resposne
    :return: None
    :working : This will find 1st level of hierarchy and calls
    find_carousal_sub_categories(hierarchy, page_soup, anchor_tag) to find sub_categories
    """
    category_container = page_soup
    if category_container:
        category_tags = category_container.findAll('a', {'class': CATEGORY_LIST_ANCHOR_TAG_CLASS})
        if category_tags:
            for category_tag in category_tags:
                find_carousal_sub_categories(hierarchy, page_soup, category_tag)
                # print(category_tag.text)


def get_indent_two_hierarchy(hierarchy, page_soup, url):
    """

    :param url: Current Page Url
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
                    urls_queue.put(line)

            # If length of anchor tags is zero then it is the last level of hierarchy
            # Now create directory and save hierarchy and url in a file in that directory
            else:
                store_last_level_of_hierarchy(hierarchy, response, url)


def get_level_1_see_more_hierarchy(hierarchy, page_soup):
    response = page_soup
    if response:
        see_more_tags = response.findAll("p", {"class": SEE_MORE_CLASS})
        if len(see_more_tags) != 0:
            for see_more_tag in see_more_tags:
                category_name = string_format(str(see_more_tag.text[7:]))

                category_url = url_format(see_more_tag.a["href"])

                hierarchy_name = '{}|{}'.format(hierarchy, category_name)
                if category_name in "Billiards_and_Pool":
                    continue
                else:
                    find_traverse_type(hierarchy_name, category_url)


def find_traverse_type(hierarchy, url):
    response = get_content(url)
    if response:
        category_response_type_1 = response.find('div', {'class': LEFT_NAV_CLASS})
        category_response_type_2 = response.find('ol', {'class': CAROUSAL_CLASS})
        category_response_type_3 = response.find('ul', {'class': INDENT_TWO_CLASS})

        if category_response_type_3:

            get_indent_two_hierarchy(hierarchy, response, url)


        elif category_response_type_1:

            get_level_1_see_more_hierarchy(hierarchy, response)

        elif category_response_type_2:

            find_carousel_hierarchy(hierarchy, response)


def find_nav_hierarchy(hierarchy, page_soup):
    response = page_soup
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

                        if 'Featured_Stores' in main_category_name:
                            anchor_tags = nav_html.find_all('a')
                            if len(anchor_tags) != 0:
                                for anchor_tag in anchor_tags:
                                    category_name = string_format(anchor_tag)
                                    if category_name in IGNORE_LIST:
                                        continue
                                    else:
                                        category_url = url_format(anchor_tag['href'])

                                        hierarchy_name = '{}|{}'.format(hierarchy, category_name)


                                        find_traverse_type(hierarchy_name, category_url)


def get_tree_hierarchy(hierarchy, url):
    """

    :param hierarchy: last level hierarchy name
    :param url: current page url
    :return: None
    """

    response = get_content(url)
    if response:
        category_container = response.findAll('a', {'class': 'nav-a'})
        if len(category_container) != 0:
            for anchor_tag in category_container:
                # if anchor_tag.get('tabindex') == '66' or anchor_tag.get('tabindex') =='67':
                category_name = string_format(anchor_tag)
                if category_name in SELECTED_LIST:
                    category_url = url_format(anchor_tag['href'])

                    hierarchy_name = '{}|{}'.format(hierarchy, category_name)
                    response = get_content(category_url)
                    category_response_type_1 = response.find('div', {'class': LEFT_NAV_CLASS})
                    category_response_type_2 = response.find('ol', {'class': CAROUSAL_CLASS})
                    if category_response_type_1:

                        find_nav_hierarchy(hierarchy_name, response)
                    elif category_response_type_2:

                        find_carousel_hierarchy(hierarchy_name, response)
            urls_queue.join()


def start_program(link):
    link_list = link.split('|')
    name = '|'.join(link_list[0:-1])
    url = link_list[-1]
    create_workers()
    get_tree_hierarchy(name, url)