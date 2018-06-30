import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = '/'.join(dir_path.split('/')[0:-1])
sys.path.insert(0, dir_path)
from Common.Etsy_common_imports import *
ROOT_FOLDER = DataCollectors_Configuration.ROOT_FOLDER
PATH_STYLE = DataCollectors_Configuration.PATH_STYLE


def create_project_dir(directory):

    if not os.path.exists(directory):
        os.makedirs(directory)


# Create queue and completed files (if not created)
def create_data_files(project_name, base_url, name):
    category_queue = os.path.join(project_name, 'category_queue_{}.txt'.format(name))
    category_completed = os.path.join(project_name, "category_completed_{}.txt".format(name))
    sub_category_queue = os.path.join(project_name, 'sub_category_queue_{}.txt'.format(name))
    sub_category_completed = os.path.join(project_name, 'sub_category_completed_{}.txt'.format(name))
    sub_sub_category_queue = os.path.join(project_name, 'sub_sub_category_queue_{}.txt'.format(name))
    sub_sub_category_completed = os.path.join(project_name, 'sub_sub_category_completed_{}.txt'.format(name))
    product_queue = os.path.join(project_name, 'skipped_queue_{}.txt'.format(name))
    product_completed = os.path.join(project_name, 'skipped_completed_{}.txt'.format(name))

    if not os.path.isfile(category_queue):
        write_file(category_queue, base_url)
    if not os.path.isfile(category_completed):
        write_file(category_completed, '')

    if not os.path.isfile(sub_category_queue):
        write_file(sub_category_queue, '')
    if not os.path.isfile(sub_category_completed):
        write_file(sub_category_completed, '')

    if not os.path.isfile(sub_sub_category_queue):
        write_file(sub_sub_category_queue, '')
    if not os.path.isfile(sub_sub_category_completed):
        write_file(sub_sub_category_completed, '')

    if not os.path.isfile(product_queue):
        write_file(product_queue, '')
    if not os.path.isfile(product_completed):
        write_file(product_completed, '')


# create a file to store product details in csv file
def create_data_store_file(project_name, file_name, data):
    csv = os.path.join(project_name, '{}.csv'.format(file_name))
    if not os.path.isfile(csv):
        write_file(csv, data)


# create hierarchy directory structure and write hierarchy links into a file
def create_text_store_file(project_path, file_name, data):
    txt_path = os.path.join(project_path, '{}'.format(file_name))
    append_to_file(txt_path, data)


# Create a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Delete the contents of a file
def delete_file_contents(path):
    open(path, 'w').close()


# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Iterate through a set, each item will be a line in a file
def set_to_file(file_name, links):
    with open(file_name, "w") as f:
        for l in sorted(links):
            f.write(l + "\n")


# Iterate through a list, each item will be a line in a file
def list_to_file(file_name, links):
    with open(file_name, "a") as f:
        for l in sorted(links):
            f.write(l + "\n")


def create_directory_and_hierarchy_files(project_name, path, total_pages, product_page_url):
    file_name = CONSTANTS.PODUCTS_PAGE
    completed_file_name = CONSTANTS.COMPLETED_PAGE
    project_name_ = project_name.split(PATH_STYLE)
    line = '{}|{}|{}|{}|{}|{}'.format(CONSTANTS.MARKET_PLACE_NAME,
                                      CONSTANTS.DOMAIN_NAME,
                                      project_name_[-1],
                                      path.replace(PATH_STYLE, '|'),
                                      str(total_pages),
                                      product_page_url
                                      )
    create_project_dir(os.path.join(project_name, path))
    create_text_store_file(project_name, file_name, line)
    create_text_store_file(project_name, completed_file_name, '')

