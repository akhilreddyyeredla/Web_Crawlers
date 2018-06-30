'''
How to Run:

python statistics_analysis.py /usr/datacollector/Data_Store/Amazon_us info (or) url (or) all

'''

import fnmatch
import os
import sys
import DataCollectors_Configuration


def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
        f.close()
    return results


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
    queue_links_count = 0
    completed_links_count = 0
    for files in queue_files:
        for url in file_to_set(files):
            queue_set.add(url)
            queue_links_count = queue_links_count + 1

    for files in completed_files:
        for url in file_to_set(files):
            competed_set.add(url)
            completed_links_count = completed_links_count + 1

    return queue_links_count, completed_links_count


def get_info_data(path):
    """"
    :param: category is the present working category or folder
        This method is starting point of program It collects all the paths of products urls and iterate over each
        path and collect product info from each url
    """
    # path = '{}{}{}{}{}'.format(
    #                            DataCollectors_Configuration.ROOT_FOLDER,
    #                            DataCollectors_Configuration.PATH_STYLE,
    #                            DataCollectors_Configuration.AMAZON_AUS_PROJECT_NAME,
    #                            DataCollectors_Configuration.PATH_STYLE,
    #                            folder_name
    #                            )

    category_list = os.listdir(path)

    for category in category_list:
        path_to_compare = path.lower()
        category_path = '{}/{}'.format(path, category)
        if 'souq' in path_to_compare:
            queue_files     = get_all_files(root=category_path, pattern=DataCollectors_Configuration.SOUQ_PATTERN)
            competed_files  = get_all_files(root=category_path, pattern=DataCollectors_Configuration.PATTERN_2)
        else :
            queue_files     = get_all_files(root=category_path, pattern=DataCollectors_Configuration.PATTERN_3)
            competed_files  = get_all_files(root=category_path, pattern=DataCollectors_Configuration.PATTERN_4)

        queue_count, completed_count = get_updated_links(queue_files, competed_files)
        print '---------------------------------------------------------------------------------------------'
        print "In {}_info \n Queue_links count {} | Completed_links count {}".format(category, queue_count, completed_count)
        print '--------------------------------------------------------------------------------------------\n'

def get_url_data(path):
    """"
    :param: category is the present working category or folder
        This method is starting point of program It collects all the paths of products urls and iterate over each
        path and collect product info from each url
    """
    # path = '{}{}{}{}{}'.format(
    #                            DataCollectors_Configuration.ROOT_FOLDER,
    #                            DataCollectors_Configuration.PATH_STYLE,
    #                            DataCollectors_Configuration.AMAZON_AUS_PROJECT_NAME,
    #                            DataCollectors_Configuration.PATH_STYLE,
    #                            folder_name
    #                            )

    category_list = os.listdir(path)

    for category in category_list:
        path_to_compare = path.lower()
        category_path = '{}/{}'.format(path, category)
        if 'souq' in path_to_compare:
            queue_files     = get_all_files(root=category_path, pattern='*_queue.txt')
            competed_files  = get_all_files(root=category_path, pattern='*_completed.txt')

        else:
            queue_files    = get_all_files(root=category_path, pattern=DataCollectors_Configuration.PATTERN_1)
            competed_files = get_all_files(root=category_path, pattern=DataCollectors_Configuration.PATTERN_2)

        queue_count, completed_count = get_updated_links(queue_files, competed_files)

        print '---------------------------------------------------------------------------------------------'
        print "In {}_url \n Queue_links count {} | Completed_links count {}".format(category, queue_count, completed_count)
        print '--------------------------------------------------------------------------------------------\n'


if __name__ == '__main__':
    path = sys.argv[1]

    search_type = sys.argv[2].lower()

    # print os.listdir(path)

    if search_type == 'hierarchy':
        pass
    elif search_type == 'url':
        get_url_data(path)

    elif search_type == 'info':
        get_info_data(path)

    elif search_type == 'all':
        get_url_data(path)
        get_info_data(path)
