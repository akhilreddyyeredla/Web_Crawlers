import sys
sys.path.insert(0, r'/usr/datacollector')

import re
from response_getter import get_page_soup
from collections import OrderedDict
from bs4 import BeautifulSoup, NavigableString
from file_operations import create_project_dir
import DataCollectors_Configuration
#import config

url_dict = {}  # dictionary to store category name and url
hierarchy_dict = dict() # dictionary to store hierarchy and product page url
level_Dictionary = OrderedDict()  # To store the level and category name
project_name = DataCollectors_Configuration.SOUQ_HIRERACHY_ROOT_FOLDER


# To form categories hirerachy and to create directories in the form of hirerachy

def collect_hirerachy_details():
    create_project_dir(project_name)
    page_soup, recivied_url = get_page_soup(DataCollectors_Configuration.SOUQ_MAIN_URL)
    columns_container = page_soup.find_all("div", {'class': 'large-4 columns'})

    # To split html page into different blocks so that we can get main category name
    categories_container = []
    for columns in columns_container:
        category_data = str(columns).split('<h3 class="shop-all-title">')
        for data in category_data:
            data = '<h3>' + data
            categories_container.append(data)

    # This method forms dictionary of last level sub_category as a key and its url
    form_url_dict(page_soup)

    # pasrse the categories container and perform depth first search then form hirerachy
    for i in categories_container:
        categories_block_container = BeautifulSoup(i, "html.parser")
        dfs(categories_block_container, 0, level_Dictionary)

    # Store hirerachy ditionary into file
    write_hirerachy_file(hierarchy_dict)


def form_url_dict(page_soup):
    sub_categories_container = page_soup.find_all('div', {'class': 'grouped-list'})

    # To store the key-value pair of sub_category name and url
    for sub in sub_categories_container:
        links = sub.find_all('li')
        for x in links:
            demo = x.find_all('a')
            for y in demo:
                try:
                    link = (y['href'])
                    name = y.text.strip()
                    url_dict[name] = link
                except:
                    continue


# TO perform depth first search(dfs) and store level(key) and category_name(value)
def dfs(tree, level, level_Dictionary):
    for node in tree.children:
        if isinstance(node,
                      NavigableString):  # NavigablString is beautifulsoup method it will say wheter the tag contains another tag
            if not node.string == '':
                if level in level_Dictionary.keys():
                    level_Dictionary[level].append(node.string)
                else:
                    level_Dictionary[level] = [node.string]
                form_hierarchy(level)
            return
        dfs(node, level + 1, level_Dictionary)
    return


# TO store hierarchy into hierarchy dictionary and form hierarchy  and strore url
def form_hierarchy(level):
    if level == 1:
        li = level_Dictionary[1][-1]
        name_ = li
        category_name = name_.replace('&', 'and').strip()
        category_name = re.sub('[^a-zA-Z|]', '_', category_name).replace('__', '').strip()
        create_project_dir(project_name + '/' + category_name)
       
    elif level == 4:
        li = level_Dictionary[1][-1]
        li2 = level_Dictionary[4][-1]
        if li2 in url_dict.keys():
            name_ = li + '|' + li2
            category_name = name_.replace('&', 'and').strip()
            category_name = re.sub('[^a-zA-Z|]', '_', category_name).replace('__', '').strip()
            hierarchy_dict[category_name] = url_dict[li2]
            create_project_dir(project_name + '/' + category_name.replace('|', '/'))
       
    elif level == 6:
        li = level_Dictionary[1][-1]
        li2 = level_Dictionary[4][-1]
        li3 = level_Dictionary[6][-1]
        if li3 in url_dict.keys():
            name_ = li + '|' + li2 + '|' + li3
            category_name = name_.replace('&', 'and').strip()
            category_name = re.sub('[^a-zA-Z|]', '_', category_name).replace('__', '').strip()
            hierarchy_dict[category_name] = url_dict[li3]
            create_project_dir(project_name + '/' + category_name.replace('|', '/'))
     
    elif level == 7:
        li = level_Dictionary[1][-1]
        li2 = level_Dictionary[4][-1]
        li3 = level_Dictionary[7][-1]
        if li3 in url_dict.keys():
            name_ = li + '|' + li2 + '|' + li3
            category_name = name_.replace('&', 'and').strip()
            category_name = re.sub('[^a-zA-Z|]', '_', category_name).replace('__', '').strip()
            hierarchy_dict[category_name] = url_dict[li3]
            create_project_dir(project_name + '/' + category_name.replace('|', '/'))
      
    elif level == 8:
        li = level_Dictionary[1][-1]
        li2 = level_Dictionary[4][-1]
        li3 = level_Dictionary[6][-1]
        li4 = level_Dictionary[8][-1]
        if li4 in url_dict.keys():
            name_ = li + '|' + li2 + '|' + li3 + '|' + li4
            category_name = name_.replace('&', 'and').strip()
            category_name = re.sub('[^a-zA-Z|]', '_', category_name).replace('__', '').strip()
            hierarchy_dict[category_name] = url_dict[li4]
            create_project_dir(project_name + '/' + category_name.replace('|', '/'))

     


# write ditionary to file and create other files
def write_hirerachy_file(dictionary):
    for keys in dictionary.keys():
        category_name = keys.split('|')[0]
        path = project_name + '/' + category_name
        file_1 = open(path + '/{}_link_queue.txt'.format(category_name), 'a')
        file_2 = open(path + '/{}_link_completed.txt'.format(category_name), 'a')
        file_2.close()
        file_3 = open(path + '/{}_link_skipped.txt'.format(category_name), 'a')
        file_3.close()
        # file_1 = open('link_queue.txt', 'a', encoding='utf-8')
        # file_2 = open('link_completed.txt', 'a', encoding='utf-8')
        # file_2.close()
        # file_3 = open('link_skipped.txt', 'a', encoding='utf-8')
        # file_3.close()

        file_1.write(keys + '|' + hierarchy_dict[keys].replace(" ", "%") + "\n")


collect_hirerachy_details()
