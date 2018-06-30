from response_getter import get_content
from helpers import string_format, url_format
from file_operations import create_directory_and_hierarchy_files
from threading import Thread
from Queue import Queue
from DataCollectors_Configuration import NO_OF_THEARDS
from CONSTANTS import *

# this queue is used to store urls and this queue is given as Threadpool queue
urls_queue = Queue()

# This is list to store hierarchy|urls
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
                    if sub_category_name in IGNORE_LIST:
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


# print(response.prettify())


def find_left_nav_hierarchy(hierarchy, page_soup):
    category_container = page_soup
    toggle = True
    if category_container:
        category_list = category_container.findAll('ul')
        if len(category_list) != 0:
            for category in category_list:
                if toggle:
                    toggle = False
                else:
                    category_tag = category.find('a')
                    if category_tag:
                        category_name = string_format(category_tag)
                        category_url = url_format(category_tag['href'])

                        hierarchy_name = '{}|{}'.format(hierarchy, category_name)
                        line = '{}|{}'.format(hierarchy_name, category_url)

                        # add links to the queue
                        urls_queue.put(line)


def find_box_grid_hierarchy(hierarchy, page_soup):
    response = page_soup
    if response:
        category_container_1 = response.findAll('div', {'class': SMALL_BOX_GRID_CLASS})
        category_container_2 = response.findAll('div', {'class': LARGE_BOX_GRID_CLASS})

        if len(category_container_1) != 0:
            for category in category_container_1:
                anchor_tag = category.find('a')
                if anchor_tag:
                    category_name = string_format(anchor_tag)
                    category_url = url_format(anchor_tag['href'])

                    hierarchy_name = '{}|{}'.format(hierarchy, category_name)

                    line = '{}|{}'.format(hierarchy_name, category_url)

                    # add links to the queue
                    urls_queue.put(line)

        if len(category_container_2) != 0:
            for category in category_container_1:
                anchor_tag = category.find('a')
                if anchor_tag:
                    category_name = string_format(anchor_tag)
                    category_url = url_format(anchor_tag['href'])

                    hierarchy_name = '{}|{}'.format(hierarchy, category_name)

                    line = '{}|{}'.format(hierarchy_name, category_url)

                    # add links to the queue
                    urls_queue.put(line)


def find_level_1_hierarchy(hierarchy, page_soup):
    category_container = page_soup
    if category_container:
        sub_category_container = category_container.find("span", {'class': 'a-list-item'})
        if sub_category_container:
            sub_category_list = sub_category_container.findAll('a', {'class': NORMAL_ANCHOR_TAG_CLASS})
            for sub_category in sub_category_list:
                sub_category_name = string_format(sub_category)
                hierarchy_name = '{}|{}'.format(hierarchy, sub_category_name)
                hierarchy_url = url_format(sub_category['href'])

                line = '{}|{}'.format(hierarchy_name, hierarchy_url)
                # add links to the queue
                urls_queue.put(line)


def get_tree_hierarchy(hierarchy, url):
    """

    :param hierarchy: Hierarchy name
    :param url: current page url
    :return: NOne
    """
    response = get_content(url)
    if response:
        container = response.find('div', {'class': BOX_GRID_CONTAINER_CLASS})
        if container:
            category_containers = container.findAll('div', {'class': SMALL_BOX_GRID_CLASS})
            if len(category_containers) != 0:
                for category in category_containers:
                    category_name = string_format(category.img['alt'])
                    category_url = url_format(category.find('a')['href'])

                    hierarchy_name = '{}|{}'.format(hierarchy, category_name)

                    category_response = get_content(category_url)
                    """
                    :logic - At first we will find all possible class names from response 
                    and we will check which type of class got response and call that 
                    specific function to proceed further
                    """
                    if category_response:

                        category_response_type_1 = category_response.find("ul", {'class': INDENT_ONE_CLASS})
                        category_response_type_2 = category_response.findAll('div', {'class': SMALL_BOX_GRID_CLASS})
                        category_response_type_3 = category_response.find('div', {'class': LEFT_NAV_CLASS})
                        category_response_type_4 = category_response.find('ol', {'class': CAROUSAL_CLASS})

                        if category_response_type_1:
                            find_level_1_hierarchy(hierarchy_name, category_response_type_1)

                        elif len(category_response_type_2) != 0:
                            find_box_grid_hierarchy(hierarchy_name, category_response)

                        elif category_response_type_3:
                            find_left_nav_hierarchy(hierarchy_name, category_response_type_3)

                        elif category_response_type_4:
                            find_carousel_hierarchy(hierarchy_name, category_response)

                        else:
                            line = '{}|{}'.format(hierarchy_name, category_url)
                            urls_queue.put(line)

                urls_queue.join()



def start_program(link):
    link_list = link.split('|')
    name = '|'.join(link_list[0:-1])
    url = link_list[-1]
    create_workers()
    get_tree_hierarchy(name, url)
