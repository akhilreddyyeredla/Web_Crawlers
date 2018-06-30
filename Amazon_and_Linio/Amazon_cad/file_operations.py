import os

import CONSTANTS
import DataCollectors_Configuration


def file_to_dictionary(file_name):
    '''

    :param file_name: path of input file
    :return: directionary with category_hirerachy(key): urls(values)
    '''
    results = {}
    with open(file_name, 'rt') as f:
        for line in f:
            line_split = line.split('|')
            key_value = '|'.join(line_split[0:-1])
            if key_value in results.keys():
                results[key_value].append(line_split[-1].replace('\n', ''))
            else:
                results[key_value] = [line_split[-1].replace('\n', '')]
    return results


def dictionary_to_file(path, url_list):
    '''

    :param path: location or path in which you want to save the file
    :param url_list: data_list which you want to write into file
    :return: nothing
    '''
    with open(path, 'w') as f:
        for url in sorted(url_list):
            f.write(url.encode('utf-8'))


def create_project_dir(directory):
    if not os.path.exists(directory):
        # print('Creating directory ' + directory)
        os.makedirs(directory)


def file_to_list(file_name):
    results = []
    with open(file_name, 'rt') as f:
        for line in f:
            results.append(line.replace('\n', ''))
    return results


def list_to_file(file_name, links):
    with open(file_name, "w") as f:
        for link in sorted(links):
            f.write(link + "\n")


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Create a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
        f.close()
    return results


# create hierarchy directory structure and write hierarchy links into a file
def create_text_store_file(project_path, file_name, data):
    txt_path = os.path.join(project_path, '{}'.format(file_name))
    append_to_file(txt_path, data)


def create_directory_and_hierarchy_files(hiearchy, line):
    file_name = CONSTANTS.PODUCTS_PAGE
    completed_file_name = CONSTANTS.COMPLETED_PAGE

    path = '{}{}{}{}{}'.format(DataCollectors_Configuration.ROOT_FOLDER, DataCollectors_Configuration.PATH_STYLE, DataCollectors_Configuration.AMAZON_CANADA_PROJECT_NAME, DataCollectors_Configuration.PATH_STYLE,
                               hiearchy.replace('|', DataCollectors_Configuration.PATH_STYLE))

    # create directory structure
    create_project_dir(os.path.join(path))

    # create text file which contains
    create_text_store_file(path, file_name, line)
    create_text_store_file(path, completed_file_name, '')


def update_files(hierarchy_name, urls_list, page_url, queue_file_name, completed_file_name):
    queue_path = '{}{}{}{}{}{}{}'.format(DataCollectors_Configuration.ROOT_FOLDER, DataCollectors_Configuration.PATH_STYLE, DataCollectors_Configuration.AMAZON_CANADA_PROJECT_NAME,
                                         DataCollectors_Configuration.PATH_STYLE,
                                         hierarchy_name.replace('|', DataCollectors_Configuration.PATH_STYLE),
                                         DataCollectors_Configuration.PATH_STYLE, queue_file_name)
    list_to_file(queue_path, urls_list)
    completed_path = '{}{}{}{}{}{}{}'.format(DataCollectors_Configuration.ROOT_FOLDER, DataCollectors_Configuration.PATH_STYLE,
                                             DataCollectors_Configuration.AMAZON_CANADA_PROJECT_NAME,
                                             DataCollectors_Configuration.PATH_STYLE,
                                             hierarchy_name.replace('|', DataCollectors_Configuration.PATH_STYLE),
                                             DataCollectors_Configuration.PATH_STYLE, completed_file_name)
    data = '{}|{}'.format(hierarchy_name, page_url)
    append_to_file(completed_path, data)
