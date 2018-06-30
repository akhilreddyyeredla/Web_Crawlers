from response_getter import get_content
from helpers import string_format, url_format
from file_operations import create_directory_and_hierarchy_files
from threading import Thread
from Queue import Queue
from DataCollectors_Configuration import NO_OF_THEARDS
from CONSTANTS import *

sub_category_urls = []

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

def find_sub_category_container(html_tags):
    """

    :param html_tags: beautifulsoup response is given as input then we will do deapth first search
    :return: last level of tag and its contents
    """
    container = html_tags.find('ul', {'class': INDENT_ONE_CLASS})
    if container:
        return find_sub_category_container(container)
    else:
        return html_tags


def find_hierarchy(hierarchy_name, url):
    """

    :param hierarchy_name:  hierachy names with pipe_delimited format
    :param url: current page url
    :return: None
    """
    response = get_content(url)
    if response:
        sub_category_container = find_sub_category_container(response)

        if sub_category_container:
            h4_tag = sub_category_container.find('h4', {'class': H4_TAG_CLASS})

            # If it contains <h4> tag then it is last level of hierarchy
            if h4_tag:
                anchor_tag = h4_tag.find('a')

                category_url = url_format(anchor_tag['href'])
                line = '{}|{}'.format(hierarchy_name, category_url)
                print(line)

                # stote the line in a file and create hierarchy directory
                create_directory_and_hierarchy_files(hierarchy_name, line)

            # else it contains more categories then find urls and again call this function
            else:
                anchor_tags = sub_category_container.findAll('a', {'class': NORMAL_ANCHOR_TAG_CLASS})
                for anchor_tag in anchor_tags:
                    category_name = string_format(anchor_tag)
                    category_url = url_format(anchor_tag['href'])
                    hierarchy = '{}|{}'.format(hierarchy_name, category_name)

                    # recurvisely calling this function
                    find_hierarchy(hierarchy, category_url)

                    sub_category_urls.append(url_format(anchor_tag['href']))


def get_tree_hierarchy(main_category_name, url):
    '''

    :param main_category_name: Hierarchy name
    :param url: current_page_url
    :return:
    '''

    """
    This is the staring of the category hierarchy collection 
    for each category it will go recurvisely and find all sub_sub_categories
    and stores it in a hierarchy directory structure 
    """
    response = get_content(url)
    if response:
        category_container = response.find("ul", {'class': INDENT_NONE_CLASS})
        if category_container:
            sub_category_container = category_container.find("span", {'class': 'a-list-item'})
            if sub_category_container:
                sub_category_list = sub_category_container.findAll('a', {'class': NORMAL_ANCHOR_TAG_CLASS})
                for sub_category in sub_category_list:
                    sub_sub_category_name = string_format(sub_category)
                    hierarchy_name = '{}|{}'.format(main_category_name, sub_sub_category_name)
                    hierarchy_url = url_format(sub_category['href'])

                    line = '{}|{}'.format(hierarchy_name, hierarchy_url)

                    urls_queue.put(line)
                urls_queue.join()

def start_program():
    link  = "Clothing_Shoes_and_Jewelry|Baby|https://www.amazon.com/Baby-Clothing-Shoes/b/ref=sd_allcat_sft_baby?ie=UTF8&node=7147444011"
    link_list = link.split('|')
    name = '|'.join(link_list[0:-1])
    url = link_list[-1]
    print('startted Clothing hierarchy')
    create_workers()
    get_tree_hierarchy(name, url)
