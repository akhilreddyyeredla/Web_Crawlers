import fnmatch
import os
from Queue import Queue
from threading import Thread
import time
import DataCollectors_Configuration
from file_operations import file_to_set, update_files
from response_getter import get_content
from helpers import string_format, url_format
from CONSTANTS import *

urls_queue = Queue()


# site = 'https://www.amazon.com/International-Shipping-Direct/b/ref=sd_allcat_full_store_dir_VisitAg?ie=UTF8&node=230659011'


def create_workers():
    """
    Creates threadpool and with max number of threads mentioned in DataCollectors_Configuration file and targets work function
    :return: none
    """
    for _ in range(DataCollectors_Configuration.NO_OF_THEARDS):
        thread = Thread(target=work)
        # make the thread daemon to stop the thread when main program exits
        thread.daemon = True
        thread.start()


def work():
    """
    Work is function which get urls from queue and calls get_products_urls(hierarchy|url)
    :return: None
    """
    while True:
        value = urls_queue.get()
        get_product_urls(value)  # to call get_products method which collects all products urls
        urls_queue.task_done()


def find_last_page(page_soup):
    response = page_soup
    try:
        last_page_tag = response.find('span', {'class': LAST_PAGE_CLASS})
        if last_page_tag:
            last_page = string_format(last_page_tag)
            return last_page
        else:
            last_page_tag = response.findAll('span', {'class': 'pagnLink'})[-1]
            if last_page_tag:
                last_page = string_format(last_page_tag)
                return last_page
    except IndexError:
        return '1'


def in_completed_urls(current_page, urls_set):
    flag = False
    for urls in urls_set:
        if current_page in urls:
            flag = True
            break
    return flag


def collect_sample_data(hierarchy, url, last_page, completed_set):
    """

    :param hierarchy: hierarchy name
    :param url: current page url
    :param last_page: last page number
    :param completed_set: completed url sets to compare
    :return: None
    :working: collects products url the sample pages mentioned in DataCollectors_Configuration file
    """
    url_list = []
    for pageNo in range(2, last_page):
        if pageNo <= DataCollectors_Configuration.NO_OF_PRODUCT_URL_TO_COLLECT:
            current_page = '{}&page={}'.format(url, pageNo)
            if in_completed_urls(current_page, completed_set):
                continue
            else:

                response = get_content(current_page)
                if response:
                    product_url_tags = response.findAll('a', {
                        'class': 'a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal'})
                    if len(product_url_tags) != 0:
                        for product_url_tag in product_url_tags:
                            product_url = url_format(product_url_tag['href'])
                            line = '{}|{}'.format(hierarchy, product_url)
                            url_list.append(line)

                        print('{}|{}'.format(hierarchy, current_page))
                        update_files(hierarchy, url_list, current_page, PRODUCTS_INFO_FILE, COMPLETED_PAGE)
        else:
            break


def collect_all_data(hierarchy, url, last_page, completed_set):
    """

       :param hierarchy: hierarchy name
       :param url: current page url
       :param last_page: last page number
       :param completed_set: completed url sets to compare
       :return: None
       :working: collects products url from all pages
       """
    url_list = []
    for pageNo in range(2, last_page):
        current_page = '{}&page={}'.format(url, pageNo)
        if in_completed_urls(current_page, completed_set):
            continue
        else:

            response = get_content(current_page)
            if response:
                product_url_tags = response.findAll('a', {
                    'class': 'a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal'})
                if len(product_url_tags) != 0:
                    for product_url_tag in product_url_tags:
                        product_url = url_format(product_url_tag['href'])
                        line = '{}|{}'.format(hierarchy, product_url)
                        url_list.append(line)

                    print('{}|{}'.format(hierarchy, current_page))
                    update_files(hierarchy, url_list, current_page, PRODUCTS_INFO_FILE, COMPLETED_PAGE)


def traverse_pages(hierarchy, url, last_page, completed_set):
    """

    :param hierarchy: hierarchy name
    :param url: current page url
    :param last_page: last page number
    :param completed_set: completed urls set
    :return: None
    :working; as per url flag in DataCollectors_Configuration flag it will collect sample urls or all urls
    """
    last_page_no = int(last_page) + 1
    if DataCollectors_Configuration.PRODUCT_URL_FLAG == URL_FLAG:

        collect_sample_data(hierarchy, url, last_page_no, completed_set)
    else:

        collect_all_data(hierarchy, url, last_page_no, completed_set)


def get_product_urls(hierarchy_url):
    """

    :param hierarchy_url: string in this format 'hierarchy|page_url"
    :return: None
    :working : requsts the url and then find last page and call's traverse_page function
    """
    name_list = hierarchy_url.split('|')
    hierarchy_name = '|'.join(name_list[0:-1])
    page_url = name_list[-1]

    urls_list = []
    completed_path = '{}{}{}{}{}{}{}'.format(DataCollectors_Configuration.ROOT_FOLDER, DataCollectors_Configuration.PATH_STYLE, DataCollectors_Configuration.AMAZON_CANADA_PROJECT_NAME,
                                             DataCollectors_Configuration.PATH_STYLE, hierarchy_name.replace('|', DataCollectors_Configuration.PATH_STYLE),
                                             DataCollectors_Configuration.PATH_STYLE, COMPLETED_PAGE)
    completed_set = file_to_set(completed_path)
    if in_completed_urls(page_url, completed_set):
        pass
    else:
        response = get_content(page_url)
        if response:

            product_url_tags = response.findAll('a', {
                'class': 'a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal'})
            if len(product_url_tags) != 0:
                for product_url_tag in product_url_tags:
                    product_url = url_format(product_url_tag['href'])
                    line = '{}|{}'.format(hierarchy_name, product_url)
                    urls_list.append(line)

                update_files(hierarchy_name, urls_list, page_url, PRODUCTS_INFO_FILE, COMPLETED_PAGE)

                last_page = find_last_page(response)
                traverse_pages(hierarchy_name, page_url, last_page, completed_set)


def get_all_files(root, pattern):
    """

    :param root: Root folder location
    :param pattern: pattern of file name which to be searched ex: '*_links.txt' is pattern
    :return: list of paths that matches with pattern
    """
    links_files = []

    # The below lines perform recurvise search of directories in the root folder and returns paths of file which
    # matches the pattern

    for root, dirs, files in os.walk(root):  # os.walk is python library to collect all directories
        for filename in fnmatch.filter(files, pattern):
            links_files.append(os.path.join(root, filename))
    return links_files


def start_url_collection(folder_name):
    """

    :param folder_name: category_folder name
    :return: None
    """
    path = '{}{}{}{}{}'.format(DataCollectors_Configuration.ROOT_FOLDER, DataCollectors_Configuration.PATH_STYLE, DataCollectors_Configuration.AMAZON_CANADA_PROJECT_NAME, DataCollectors_Configuration.PATH_STYLE,
                               folder_name)
    all_files = get_all_files(path, DataCollectors_Configuration.PATTERN_1)
    for files in all_files:
        if os.path.exists(files):
            for url in file_to_set(files):
                urls_queue.put(url)
    urls_queue.join()


def start_program(folder_name):
    """
    :param folder_name: category_folder name
    :return
    """
    print('started url collection')
    start_time = time.time()

    # creates threadpool
    create_workers()

    # call this function to start url collection
    start_url_collection(folder_name)

    end_time = time.time()
    total_time = end_time - start_time
    print 'Industria_Empresas_y_Ciencia_url_collection|started-{}|ended-{}|total_time_taken-{} '.format(start_time, end_time, total_time)

