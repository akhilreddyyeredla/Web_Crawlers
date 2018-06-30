from response_getter import get_content
from helpers import string_format, url_format
from file_operations import create_directory_and_hierarchy_files
from threading import Thread
from Queue import Queue
from DataCollectors_Configuration import NO_OF_THEARDS
from CONSTANTS import *

urls_queue = Queue()

urls_list = Queue()


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
    then pass that url to find_hierarchy(hierarchy_name, page_url) this function will
    travel recurcivesly and find hierarchy
    :return: None
    """
    while True:
        value = urls_queue.get().split('|')
        name = '|'.join(value[0:-1])

        url = value[-1]
        find_hierarchy(name, url)  # to call scrapper method which collects all products urls
        urls_queue.task_done()


def store_last_level_of_hierarchy(hierarchy, page_soup, url):
    response = page_soup
    if response:
        h4_tag = response.find('h4', {'class': H4_TAG_CLASS})
        if h4_tag:
            category_name = string_format(h4_tag)

            category_url_tag = response.find('a', {'title': LAYOUT_PICKER})

            # To get tiles view url
            if category_url_tag:
                category_url = url_format(category_url_tag['href'])
            else:
                category_url = url

            # Get hierarchy name
            if category_name in hierarchy:
                hierarchy_name = hierarchy
            else:
                hierarchy_name = '{}|{}'.format(hierarchy, category_name)

            line = '{}|{}'.format(hierarchy_name, category_url)

            line_1 ='completed|{}'.format(line)
            urls_list.put(line_1)
            print line

            # store the line in a file and create hierarchy directory
            create_directory_and_hierarchy_files(hierarchy_name, line)


def find_hierarchy(hierarchy, url):
    """

    :param hierarchy: category_hierarchy name
    :param url: current_page_url
    :return: None
    :working: recurssion function to find the hierarchy, last_page and products_page_url
    """
    response = get_content(url)
    if response:
        sub_categories_container = response.find('ul',
                                                 {'class': INDENT_TWO_CLASS})

        if sub_categories_container:
            anchor_tags = sub_categories_container.findAll('a', {'class': NORMAL_ANCHOR_TAG_CLASS})

            # If length of anchor tags is not zero then it contains more categories
            if len(anchor_tags) != 0:
                # Now for each category_url again call find_hierarchy function
                for anchor_tag in anchor_tags:
                    category_name = string_format(anchor_tag)
                    category_url = url_format(anchor_tag['href'])

                    hierarchy_name = '{}|{}'.format(hierarchy, category_name)

                    line = '{}|{}'.format(hierarchy_name, category_url)

                    urls_list.put(line)

                    find_hierarchy(hierarchy_name, category_url)


            # If length of anchor tags is zero then it is the last level of hierarchy
            # Now create directory and save hierarchy and url in a file in that directory
            else:
                store_last_level_of_hierarchy(hierarchy, response, url)


def get_indent_two_hierarchy(hierarchy, page_soup, url):
    """

    :param url: Current Page Url
    :param hierarchy: hierarchy_name
    :param page_soup: BeautifulSoup response
    :return: None
    """
    response = page_soup
    if response:
        sub_categories_container = response.find('ul',
                                                 {'class': INDENT_TWO_CLASS})

        if sub_categories_container:
            anchor_tags = sub_categories_container.findAll('a', {'class': NORMAL_ANCHOR_TAG_CLASS})

            # If length of anchor tags is not zero then it contains more categories
            if len(anchor_tags) != 0:
                # Now for each category_url again call find_hierarchy function
                for anchor_tag in anchor_tags:
                    category_name = string_format(anchor_tag)
                    category_url = url_format(anchor_tag['href'])

                    hierarchy_name = '{}|{}'.format(hierarchy, category_name)

                    line = '{}|{}'.format(hierarchy_name, category_url)
                    urls_queue.put(line)

                    # to store it in file before that we store it in queue
                    line_1 = 'completed|{}'.format(line)
                    urls_list.put(line_1)

                urls_queue.join()
            # If length of anchor tags is zero then it is the last level of hierarchy
            # Now create directory and save hierarchy and url in a file in that directory
            else:
                store_last_level_of_hierarchy(hierarchy, response, url)

def start_program():
    links = [
        'Amazon_Pantry|Baby_and_Child_Care|https://www.amazon.co.uk/b/ref=sd_allcat_prime_pantry_bc/262-6468249-9592357?ie=UTF8&node=8479375031',
        'Amazon_Pantry|Beer_Wine_and_Spirits|https://www.amazon.co.uk/b/ref=sd_allcat_prime_pantry_bws/262-6468249-9592357?ie=UTF8&node=8464529031',
        'Amazon_Pantry|Beverages|https://www.amazon.co.uk/b/ref=sd_allcat_prime_pantry_bv/262-6468249-9592357?ie=UTF8&node=5782664031',
        'Amazon_Pantry|Food_Cupboard|https://www.amazon.co.uk/b/ref=sd_allcat_prime_pantry_fc/262-6468249-9592357?ie=UTF8&node=5782663031',
        'Amazon_Pantry|Health_and_Beauty|https://www.amazon.co.uk/b/ref=sd_allcat_prime_pantry_hb/262-6468249-9592357?ie=UTF8&node=5790355031',
        'Amazon_Pantry|Household_Supplies|https://www.amazon.co.uk/b/ref=sd_allcat_prime_pantry_hs/262-6468249-9592357?ie=UTF8&node=5790354031',
        'Amazon_Pantry|Past_Purchases|https://www.amazon.co.uk/gp/pantry/past-purchases/ref=sd_allcat_prime_pantry_pp/262-6468249-9592357'
    ]

    for link in links:
        link_list = link.split('|')
        name = '|'.join(link_list[0:-1])
        url = link_list[-1]
        create_workers()
        resposne = get_content(url)
        if resposne:
            get_indent_two_hierarchy(name, resposne, url)


