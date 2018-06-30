import Queue
import fnmatch
import threading
import time
import os
from datetime import date
from file_operations import file_to_set, append_to_file
from product_parsers.giochi_e_prima_infanzia_get_product_info import *
import CONSTANTS
import response_getter
import DataCollectors_Configuration
from product_info_storage import store


class Workers:
    NUMBER_OF_THREADS = DataCollectors_Configuration.NO_OF_THEARDS
    categories_queue = Queue.Queue()
    starting_time = 0
    ending_time = 0

    def __init__(self, ):
        Workers.starting_time = time.time()
        self.create_workers()

    # Create worker threads (will die when main exits)
    def create_workers(self):
        for _ in range(Workers.NUMBER_OF_THREADS):
            t = threading.Thread(target=Workers.work)
            t.daemon = True
            t.start()

    # Do the next job in the queue
    @staticmethod
    def work():
        while True:
            url = Workers.categories_queue.get()
            # If we split it by '|' then 0:-1 is hierarchy and -1 is a url
            # product_page_url
            url_split = url.split('|')
            hierarchy = '|'.join(url_split[0:-1])
            product_page_url = url_split[-1]
            # save_date is method which parsers the url and store it into db so that each thread access different object
            save_data(threading.current_thread().name, hierarchy, product_page_url)
            Workers.categories_queue.task_done()

    # Put all urls into queue and data is collected from all the urls
    @staticmethod
    def collect_all_data(urls_list):
        for link in urls_list:
            Workers.categories_queue.put(link)
        Workers.categories_queue.join()

    # Check if there are items in the queue, if so crawl them
    @staticmethod
    def crawl(urls_list):
        """
        :param flag: flag value is which DataCollectors_Configurationured in DataCollectors_Configuration file
        :param urls_list: file loaction of product_urls.txt
        :return: none
        """
        queued_links = urls_list

        if len(queued_links) > 0:
            # print(str(len(queued_links)) + ' links in the queue')
            Workers.collect_all_data(urls_list)


retries = 0


def get_correct_data(hierarchy, url):
    """
    :param hierarchy: category hierarchy
    :param url: Current page Url
    :return: valid product details as a tuple
    """

    data = None
    for retires in range(0, CONSTANTS.MAX_RETRIES):
        raw_data = response_getter.get_content(url)
        # Raw_data is beautifulSoup object and it is passed through "get_data" to collect data
        if raw_data:
            # get product information as tuple
            data = get_data(raw_data, hierarchy, url)
            if data:
                break
            else:
                continue
    return data

    # global retries
    # if retries > CONSTANTS.MAX_RETRIES:
    #     return None
    #     # Raw_data is beautifulSoup object and it is passed through "get_data" to collect data
    # else:
    #     raw_data = response_getter.get_content(url)
    #     if raw_data:
    #         # get product information as tuple
    #         data = get_data(raw_data, hierarchy, url)
    #         if data is None:
    #             retries = retries + 1
    #             get_correct_data(hierarchy, url)
    #         else:
    #             retries = 0
    #             return data


def save_data(thread_name, hierarchy, url):
    """
    :param thread_name: name of current thread
    :param hierarchy: hierarchy of category
    :param url: product url which is parsed and save data in either file or database based on DataCollectors_Configurationuration
    :return: none
    """
    starting_time = time.time()

    data = get_correct_data(hierarchy, url)
    if data:
        hierarchy_name = hierarchy.split('|')
        hierarchy_path = DataCollectors_Configuration.PATH_STYLE.join(hierarchy_name)

        today_date = date.today()
        present_time = time.time()

        # Store the data externally
        store(market_place=CONSTANTS.MARKET_PLACE_NAME, date=today_date, time=present_time, info_dictionary=data,
              hirarchy=hierarchy)

        ending_time = time.time()
        total_time = ending_time - starting_time

        completed_path = '{}{}{}{}{}{}{}'.format(DataCollectors_Configuration.ROOT_FOLDER,
                                                 DataCollectors_Configuration.PATH_STYLE,
                                                 DataCollectors_Configuration.AMAZON_CANADA_PROJECT_NAME,
                                                 DataCollectors_Configuration.PATH_STYLE,
                                                 hierarchy_path,
                                                 DataCollectors_Configuration.PATH_STYLE,
                                                 CONSTANTS.COMPLETED_PAGE
                                                 )

        append_to_file(completed_path, '{}|{}'.format(hierarchy, url))
        print('{} has completed {}|{}|thread_staring_time:{}|thread_ending_time:{}|total_time:{}sec'.format(
            thread_name,
            hierarchy,
            url,
            starting_time,
            ending_time,
            total_time))


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


def get_updated_links(queue_files, completed_files):
    queue_set = set()
    competed_set = set()

    for files in queue_files:

        count = 1
        for url in file_to_set(files):
            if DataCollectors_Configuration.PRODUCT_INFO_FLAG == CONSTANTS.PRODUCT_FlAG:
                # load only sample urls mentioned in DataCollectors_Configuration file
                if count <= DataCollectors_Configuration.NO_OF_PRODUCT_INFO_TO_COLLECT:
                    queue_set.add(url)
                    count = count + 1
                else:

                    break
            else:
                queue_set.add(url)

    for files in completed_files:
        count = 1
        for url in file_to_set(files):
            if DataCollectors_Configuration.PRODUCT_INFO_FLAG == CONSTANTS.PRODUCT_FlAG:
                # load only sample urls mentioned in DataCollectors_Configuration file
                if count <= DataCollectors_Configuration.NO_OF_PRODUCT_INFO_TO_COLLECT:
                    competed_set.add(url)
                    count = count + 1
                else:

                    break
            else:
                competed_set.add(url)

    final_set = queue_set - competed_set
    return final_set


def get_page_data(folder_name):
    """"
    :param: category is the present working category or folder
        This method is starting point of program It collects all the paths of products urls and iterate over each
        path and collect product info from each url
    """
    path = '{}{}{}{}{}'.format(DataCollectors_Configuration.ROOT_FOLDER, DataCollectors_Configuration.PATH_STYLE, DataCollectors_Configuration.AMAZON_CANADA_PROJECT_NAME, DataCollectors_Configuration.PATH_STYLE,
                               folder_name)
    queue_files = get_all_files(root=path, pattern=DataCollectors_Configuration.PATTERN_3)
    competed_files = get_all_files(root=path, pattern=DataCollectors_Configuration.PATTERN_4)

    urls_list = get_updated_links(queue_files, competed_files)

    workers_obj = Workers()
    workers_obj.crawl(urls_list)


def start_info_collection(folder_name):
    print('started info collection')
    start_time = time.time()
    get_page_data(folder_name)
    end_time = time.time()
    total_time = end_time - start_time
    print 'Giochi_e_Prima_infanzia_info_collection|started-{}|ended-{}|total_time_taken-{} '.format(start_time, end_time, total_time)
