from Common.Souq_common_imports import *
import os

def file_to_dictionary(file_name):
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
   with open(os.path.join(config.SOUQ_URL_ROOT_FOLDER, '/'.join(path)), 'w') as f:
        for url in sorted(url_list):
            f.write(url.encode('utf-8'))


def create_project_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory.replace('\\','/'))


def file_to_list(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


def list_to_file(links, file_name):
    with open(file_name, "w") as f:
        for l in sorted(links):
            f.write(l + "\n")

# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results
