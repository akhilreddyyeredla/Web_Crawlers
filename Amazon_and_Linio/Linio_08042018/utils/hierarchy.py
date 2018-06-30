import time

import response_getter
from CONSTANTS import *
import os

from file_operation import create_directory_and_hierarchy_files
from Queue import Queue
from DataCollectors_Configuration import NO_OF_THEARDS, LINIO_MEX_HIERARCHY_ROOT
from threading import Thread
urls_queue = Queue()


def create_workers():
    """
    Creates threadpool and with max number of threads mentioned in config file and targets work fucntion
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
    then pass that url to second_level_hierarchy(hierarchy_name, page_url) this function will
    travel recurcivesly and find hierarchy
    :return: None
    """
    while True:
        value = urls_queue.get().split('|')
        name = '|'.join(value[0:-1])
        url = value[-1]
        second_level_hierarchy(name, url)  # to call scrapper method which collects all products urls
        urls_queue.task_done()


def create_project_dir(directory):
    if not os.path.exists(directory):
        # print('Creating directory ' + directory)
        os.makedirs(directory)


def find_last_level(page_container):
    nav_container = page_container.find('li', {'class': 'active has-children'})
    if nav_container:
        return find_last_level(nav_container)
    else:
        return page_container



def find_last_page(page_container):
    page_tags = page_container.find_all('li', {'class': 'page-item'})

    try:
        return int(page_tags[-1].a['href'].split('page=')[-1])
    except Exception:
        return 1


def create_path(hierarchy):
    hierarchy_list = hierarchy.split('|')

    path = '{}/{}'.format(LINIO_MEX_HIERARCHY_ROOT, '/'.join(hierarchy_list[2:]))

    return path


def second_level_hierarchy(hierarchy, url):
    page_container = response_getter.get_content(url)
    if page_container:
        nav_container = page_container.find('li', {'class': 'active has-children'})

        if nav_container:
            # print nav_container.prettify()
            last_nav_container = find_last_level(nav_container)
            if last_nav_container:
                link_containers_1 = last_nav_container.find_all('li', {'class': 'has-children'})
                link_containers_2 = last_nav_container.find_all('li', {'class': ' '})
                if len(link_containers_1) > 0:

                    for link_container in link_containers_1:
                        url_tag = link_container.find('a')
                        page_url = '{}{}'.format(MAIN_URL, url_tag['href'])
                        category_name = url_tag.span.text.encode('utf-8').strip().replace(',', '').replace(' ', '_')
                        # hierarchy_list = hierarchy.split('|')
                        hierarchy_name = '{}|{}'.format(hierarchy, category_name)
                        # print hierarchy_name
                        second_level_hierarchy(hierarchy_name, page_url)


                elif len(link_containers_2) > 0:
                    for link_container in link_containers_2:
                        url_tag = link_container.find('a')
                        page_url = '{}{}'.format(MAIN_URL, url_tag['href'])
                        category_name = url_tag.span.text.encode('utf-8').strip().replace(',', '').replace(' ', '_')

                        hierarchy_name = '{}|{}'.format(hierarchy, category_name)

                        path = create_path(hierarchy_name)
                        if os.path.exists(path):
                            # print 'exits'
                            pass
                        else:
                            last_page = find_last_page(page_container)

                            last_level_line = '{}|{}|{}'.format(hierarchy_name, last_page, page_url)
                            # print last_level_line
                            create_directory_and_hierarchy_files(path, last_level_line)
                else:
                    hierarchy_name = '{}'.format(hierarchy)

                    path = create_path(hierarchy_name)
                    if os.path.exists(path):
                        # print 'exits'
                        pass
                    else:
                        last_page = find_last_page(page_container)

                        last_level_line = '{}|{}|{}'.format(hierarchy_name, last_page, url)
                        # print last_level_line
                        create_directory_and_hierarchy_files(path, last_level_line)


def first_level_hierarchy(hierarchy, content_containers):
    create_workers()
    for content_container in content_containers:

        dev_containers = content_container.find_all('div', recursive=False)

        for dev_container in dev_containers:
            anchor_tag = dev_container.find('a', {'class': 'canvas'})
            if anchor_tag:
                if MAIN_URL in anchor_tag['href']:
                    page_url = anchor_tag['href']
                else:
                    page_url = '{}{}'.format(MAIN_URL, anchor_tag['href'])

            category_container = dev_container.find('div', {'class': 'banner-menu'})
            img_container = dev_container.find('img')

            if category_container:
                category_name = category_container.h2.text.encode('utf-8').strip().replace(',', '').replace(' ', '_')

                sub_category_line = '{}|{}'.encode('utf-8').format(hierarchy, category_name)

            elif img_container:
                category_name = img_container['title'].encode('utf-8').strip().replace(',', '').replace(' ', '_')

                sub_category_line = '{}|{}'.encode('utf-8').format(hierarchy, category_name)

            line = '{}|{}'.format(sub_category_line, page_url)
            urls_queue.put(line)

    urls_queue.join()


def form_hierarchy(hierarchy, url):
    path = hierarchy.split('|')
    print 'Started {} Hierarchy Collection'.format(path[-1])
    start_time = time.time()
    page_container = response_getter.get_content(url)
    if page_container:
        content_containers_1 = page_container.find_all('div', {'class': 'banner-layout-5'})
        content_containers_2 = page_container.find_all('div', {'class': 'banner-layout-4'})
        content_containers_3 = page_container.find_all('div', {'class': 'banner-layout-8'})
        content_containers_4 = page_container.find_all('div', {'class': 'banner-layout-10'})

        if content_containers_1:
            first_level_hierarchy(hierarchy, content_containers_1)
        if content_containers_2:
            first_level_hierarchy(hierarchy, content_containers_2)
        if content_containers_3:
            first_level_hierarchy(hierarchy, content_containers_3)
        if content_containers_4:
            first_level_hierarchy(hierarchy, content_containers_4)

    end_time = time.time()

    total = end_time - start_time

    print '{} hierarchy collected |Started -> {} secs | Ended -> {} secs| Total -> {} secs '.format(path[-1], start_time, end_time, total)
