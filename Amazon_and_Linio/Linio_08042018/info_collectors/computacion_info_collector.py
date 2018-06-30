import fnmatch
import os
from Queue import Queue
from threading import Thread
import time
from file_operation import file_to_set, update_files, create_project_dir,append_to_file
from response_getter import get_content
from CONSTANTS import *
from product_parsers.computacion_get_product_info import get_details
from product_info_storage import store
import DataCollectors_Configuration

urls_queue = Queue()


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
        get_product_info(value)  # to call get_products method which collects all products urls
        urls_queue.task_done()


def get_product_info(hierarchy_url):
    """

    :param hierarchy_url: string in this format 'hierarchy|page_url"
    :return: None
    :working : requsts the url and then find last page and call's traverse_page function
    """
    name_list = hierarchy_url.split('|')
    hierarchy_name = '|'.join(name_list[0:-1])

    page_url = name_list[-1]

    # urls_list = []

    hierarchy_path = '/'.join(name_list[2:-1])
    completed_path = '{}{}{}'.format(DataCollectors_Configuration.LINIO_MEX_INFO_ROOT,
                                     DataCollectors_Configuration.PATH_STYLE, hierarchy_path)

    response = get_content(page_url)

    if response:
        data, date, time = get_details(hierarchy_url, response)

        if data:
            store(MARKETPLACE, date, hierarchy_name, time, data)
            file_path = '{}/{}'.format(completed_path, COMPLETED_INFO_FILE)
            # print file_path
            append_to_file(file_path, hierarchy_url)





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


def start_info_collection(folder_name):
    """

    :param folder_name: category_folder name
    :return: None
    """
    queue_path = '{}{}{}'.format(DataCollectors_Configuration.LINIO_MEX_URL_ROOT,
                                 DataCollectors_Configuration.PATH_STYLE, folder_name)
    queue_files = get_all_files(queue_path, DataCollectors_Configuration.PATTERN_3)

    completed_path = '{}{}{}'.format(DataCollectors_Configuration.LINIO_MEX_INFO_ROOT,
                                     DataCollectors_Configuration.PATH_STYLE, folder_name)
    completed_files = get_all_files(completed_path, DataCollectors_Configuration.PATTERN_4)

    completed_set = set()
    for files in completed_files:
        if os.path.exists(files):
            links = file_to_set(files)
            for link in links:
                completed_set.add(link)
                # print link

    for files in queue_files:
        if os.path.exists(files):
            for url in file_to_set(files):
                # print(url)
                url_split = url.split('|')
                hierarchy_path = '/'.join(url_split[2:-1])
                if url in completed_set:
                    # print url
                    pass
                else:

                    completed_path = '{}{}{}'.format(DataCollectors_Configuration.LINIO_MEX_INFO_ROOT,
                                                     DataCollectors_Configuration.PATH_STYLE, hierarchy_path)

                    if os.path.exists(completed_path):

                        pass

                    else:
                        create_project_dir(completed_path)
                    urls_queue.put(url)

                        # get_product_urls(line)
    urls_queue.join()


def start_program(folder_name):
    """
    :param folder_name: category_folder name
    :return
    """

    print('started {} info collection').format(folder_name)
    start_time = time.time()

    # creates threadpool
    create_workers()

    # call this function to start url collection
    start_info_collection(folder_name)

    end_time = time.time()
    total_time = end_time - start_time
    print '{}_info_collection|started-{}|ended-{}|total_time_taken-{} '.format(folder_name, start_time, end_time, total_time)


