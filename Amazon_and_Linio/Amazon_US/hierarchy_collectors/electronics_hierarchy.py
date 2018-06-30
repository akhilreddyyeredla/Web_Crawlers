import time

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


def find_acs_nav_section(hierarchy, page_soup):
    response = page_soup
    if response:
        category_container = response.find('div', {'class': ACS_WIDGET_LEFT_NAV_CLASS})
        if category_container:
            category_list = category_container.findAll('div', {'class': ACS_SECTION_CLASS})
            if len(category_list) != 0:
                for category in category_list:
                    category_tag = category.find('button', {'class': ACS_HEADER_CLASS})
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
                                    find_traverse_type(hierarchy_name, sub_category_url)


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
                        see_more_tag = nav_html.find("p", {"class": SEE_MORE_CLASS})
                        if see_more_tag:
                            category_url = url_format(see_more_tag.a["href"])
                            hierarchy_name = '{}|{}'.format(hierarchy, main_category_name)
                            line = '{}|{}'.format(hierarchy_name, category_url)
                            urls_queue.put(line)


def find_traverse_type(hierarchy, url):
    response = get_content(url)
    if response:
        category_response_type_1 = response.find('div', {'class': LEFT_NAV_CLASS})
        category_response_type_2 = response.find('ol', {'class': CAROUSAL_CLASS})
        category_response_type_3 = response.find('ul', {'class': INDENT_TWO_CLASS})
        category_response_type_4 = response.find('div', {'class': ACS_WIDGET_LEFT_NAV_CLASS})

        if category_response_type_3:

            get_indent_two_hierarchy(hierarchy, response, url)

        elif category_response_type_4:

            find_acs_nav_section(hierarchy, response)

        elif category_response_type_1:

            find_nav_hierarchy(hierarchy, response)

        elif category_response_type_2:

            find_carousel_hierarchy(hierarchy, response)


def get_level_1_see_more_hierarchy(hierarchy, page_soup):
    response = page_soup
    if response:
        see_more_tags = response.findAll("p", {"class": SEE_MORE_CLASS})
        if len(see_more_tags) != 0:
            for see_more_tag in see_more_tags:
                category_name = string_format(str(see_more_tag.text[7:]))

                category_url = url_format(see_more_tag.a["href"])

                hierarchy_name = '{}|{}'.format(hierarchy, category_name)
                find_traverse_type(hierarchy_name, category_url)


def get_level_1_hierarchy(hierarchy, page_soup):
    response = page_soup
    if response:
        category_name = response.find('p')
        if category_name:
            main_category_name = string_format(category_name)
            anchor_tags = response.findAll('a')
            if len(anchor_tags) != 0:
                for anchor_tag in anchor_tags:
                    sub_category_name = string_format(anchor_tag)
                    if sub_category_name.replace(main_category_name, '') in IGNORE_LIST:
                        continue
                    else:
                        sub_category_url = url_format(anchor_tag['href'])

                        hierarchy_name = '{}|{}|{}'.format(hierarchy, main_category_name, sub_category_name)

                        find_traverse_type(hierarchy_name, sub_category_url)


def get_tree_hierarchy(hierarchy, url):
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
                        if main_category_name in IGNORE_LIST:
                            pass
                        elif main_category_name in SELECTED_LIST:
                            get_level_1_see_more_hierarchy(hierarchy, nav_html)
                            # print(main_category_name)
                        else:
                            get_level_1_hierarchy(hierarchy, nav_html)

            urls_queue.join()


def start_program():
    link = 'Electronics__Computers_and_Office|https://www.amazon.com/s/ref=lp_1266092011_ex_n_1?rh=n%3A172282&bbn=172282&ie=UTF8&qid=1518267013'
    link_list = link.split('|')
    name = '|'.join(link_list[0:-1])
    url = link_list[-1]
    print('started hierarchy collection')
    start_time = time.time()
    create_workers()
    get_tree_hierarchy(name, url)
    end_time = time.time()
    total_time = end_time - start_time
    print('Electronics|started-{}|ended-{}|total_time_taken-{} ').format(start_time, end_time, total_time)
