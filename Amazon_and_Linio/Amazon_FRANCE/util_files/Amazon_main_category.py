from response_getter import get_content
from CONSTANTS import DOMAIN_NAME
from file_operations import create_project_dir, list_to_file
from helpers import string_format
from config import PROJECT_NAME, ROOT_FOLDER


# This function collects all the urls and hierarchy in amazon full directory page


def collect_main_page_urls(main_url):
    """
    :param main_url: Home page url
    :return: dictionary with category_names as key and urls as values
    """

    '''
    get_content is function which takes url as input then parse it and returns html response back
    '''
    raw_data = get_content(main_url)
    category_name_and_url = {}  # Dictionary to store category names and urls
    if raw_data:
        category_containers = raw_data.findAll('div', {'class': 'popover-grouping'})
        for category in category_containers:
            category_name_tag = category.find('h2', {'class': 'popover-category-name'})
            category_name = string_format(category_name_tag)
            urls_tag = category.findAll('a')
            for url in urls_tag:
                sub_category_1 = string_format(url)
                name_key = '{}|{}'.format(category_name, sub_category_1)
                url_value = url['href']
                # The url which we get does not contain domain name so we should concat the domain name
                url = '{}{}'.format(DOMAIN_NAME, url_value)
                category_name_and_url[name_key] = url

        return category_name_and_url
    else:
        print('got none')


def create_hirerachy(starting_url):
    """

    :param starting_url: Give staring url
    :working: It will collect all urls with hierarchy and creates directories as present on website and writ into files
    :return: does not return anything
    """
    create_project_dir(PROJECT_NAME)
    category_hierarchy_and_urls = collect_main_page_urls(starting_url)
    urls_list = []

    # To create directories with hierarchy
    for category_name in sorted(category_hierarchy_and_urls.keys()):
        category_path = '{}/{}/{}'.format(ROOT_FOLDER, PROJECT_NAME, category_name.replace('|', '/'))
        create_project_dir(category_path)

    # This will add dictionary elements into a list
    for key in category_hierarchy_and_urls.keys():
        line = '{}|{}'.format(key, category_hierarchy_and_urls[key])

        urls_list.append(line)
    # This function will write urls present in list to file
    list_to_file('queue_links', urls_list)


create_hirerachy('https://www.amazon.fr/gp/site-directory/ref=nav_shopall_btn/258-7331116-6165932')
# create_hirerachy('https://www.amazon.fr/handmade/b/ref=sd_allcat_HM_Home?ie=UTF8&node=9699368031')
# create_hirerachy('https://www.amazon.fr/handmade/b/ref=sd_allcat_HM_Home?ie=UTF8&node=9699368031')
