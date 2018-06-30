from bs4 import BeautifulSoup

from response_getter import get_content
from helpers import string_format, url_format
from file_operations import create_directory_and_hierarchy_files
from threading import Thread
from Queue import Queue
from DataCollectors_Configuration import NO_OF_THEARDS
from CONSTANTS import *

urls_queue = Queue()


# site = 'https://www.amazon.com/International-Shipping-Direct/b/ref=sd_allcat_full_store_dir_VisitAg?ie=UTF8&node=230659011'


def create_workers():
    """
    Creates threadpool and with max number of threads mentioned in config file and targets work fucntion
    :return: none
    """
    for _ in range(NO_OF_THEARDS):
        thread = Thread(target=work)
        # make the thread daemon to stop the thread when main program exits
        thread.daemon = False
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

                    find_hierarchy(hierarchy_name, category_url)

            # If length of anchor tags is zero then it is the last level of hierarchy
            # Now create directory and save hierarchy and url in a file in that directory
            else:
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
                    print line

                    # store the line in a file and create hierarchy directory
                    create_directory_and_hierarchy_files(hierarchy_name, line)


def get_tree_hierarchy(hierarchy, url):
    """

    :param hierarchy: category_hierarchy name
    :param url: current_page_url
    :return: None
    :working: this function will find out 1st level of hierarchy  and calls  find_hierarchy(hierarchy_name, category_url)
    """
    response = get_content(url)

    if response:
        sub_categories_container = response.find('ul',
                                                 {'class': INDENT_ONE_CLASS})
        if sub_categories_container:
            anchor_tags = sub_categories_container.findAll('a', {'class': NORMAL_ANCHOR_TAG_CLASS})
            for anchor_tag in anchor_tags:
                category_name = string_format(anchor_tag)
                category_url = url_format(anchor_tag['href'])

                hierarchy_name = '{}|{}'.format(hierarchy, category_name)
                line = '{}|{}'.format(hierarchy_name, category_url)

                urls_queue.put(line)
                # print(line)
            urls_queue.join()


def find_nav_hierarchy(hierarchy, url):
    """

    :param hierarchy:hierarchy name
    :param url: current url
    :return: None
    """
    response = get_content(url)
    if response:
        nav_container = response.find('div', {'class': LEFT_NAV_CLASS})
        if nav_container:
            nav_string = str(nav_container).split('<h3>')
            # for all nav_string find see more tag and hirarachy name and
            for nav in nav_string:
                nav_html = BeautifulSoup(nav, 'lxml')
                if nav_html:
                    category_container = nav_html.find('p')
                    if category_container:
                        main_category_name = string_format(category_container)
                        see_more_tag = nav_html.find("p", {"class": SEE_MORE_CLASS})
                        if see_more_tag:
                            category_url = url_format(see_more_tag.a["href"])
                            hierarchy_name = '{}|{}'.format(hierarchy, main_category_name)
                            line = '{}|{}'.format(hierarchy_name, category_url)

                            # add the link into queue
                            urls_queue.put(line)


def start_program():
    link_1 = 'Home_Garden_Pets_and_DIY|Kitchen_and_Home_Appliances|https://www.amazon.co.uk/Kitchen-Appliances-Home/b/ref=sd_allcat_khapp_t2/262-6468249-9592357?ie=UTF8&node=391784011'
    links = [
        'Home_Garden_Pets_and_DIY|Large_Appliances|https://www.amazon.co.uk/Washing-Machines-Fridges-Freezers-Ovens-Tumble-Dryers/b/ref=amb_link_99?ie=UTF8&node=908798031&pf_rd_m=A3P5ROKL5A1OLE&pf_rd_s=merchandised-search-leftnav&pf_rd_r=DTAFZG508PZ70284E4R2&pf_rd_r=DTAFZG508PZ70284E4R2&pf_rd_t=101&pf_rd_p=a564509d-20f4-454f-886d-3c645031070b&pf_rd_p=a564509d-20f4-454f-886d-3c645031070b&pf_rd_i=11052681',
        'Home_Garden_Pets_and_DIY|All_DIY_and_Tools|https://www.amazon.co.uk/diy-and-tools/b/ref=sd_allcat_diyhi_t2/262-6468249-9592357?ie=UTF8&node=79903031',
        'Home_Garden_Pets_and_DIY|Garden_and_Outdoors|https://www.amazon.co.uk/Garden-Outdoors-Home/b/ref=sd_allcat_lg_t2/262-6468249-9592357?ie=UTF8&node=11052671',
        'Home_Garden_Pets_and_DIY|Lighting|https://www.amazon.co.uk/Lighting-LED-bulbs-lamps-energy-saving/b/ref=sd_allcat_light_t2/262-6468249-9592357?ie=UTF8&node=213077031',
        'Home_Garden_Pets_and_DIY|Pet_Supplies|https://www.amazon.co.uk/Pet-Supplies-Food-Animals/b/ref=sd_allcat_ps_t2/262-6468249-9592357?ie=UTF8&node=340840031'
    ]
    # first call find_nav to collect hierarchy for that traverse style only for kitchen_and_home_appliances category
    link_list = link_1.split('|')
    name = '|'.join(link_list[0:-1])
    url = link_list[-1]
    find_nav_hierarchy(name, url)

    # for links call get_tree_hierarchy to collect hierarchy
    for link in links:
        link_list = link.split('|')
        name = '|'.join(link_list[0:-1])
        url = link_list[-1]
        create_workers()
        get_tree_hierarchy(name, url)
    urls_queue.join()



