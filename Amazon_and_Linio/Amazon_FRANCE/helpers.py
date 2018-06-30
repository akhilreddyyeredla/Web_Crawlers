import re

import unicodedata

from CONSTANTS import DOMAIN_NAME


def url_format(url):
    """

    :param url: input is unformmated url and it does not contain domain name
    :return: formatted url in domain name is added and removed unnecesesary text from url
    """
    if DOMAIN_NAME in url:
        formated_url = url.replace('amp;', '')
        return formated_url
    else:
        formated_url = url.replace('amp;', '')
        working_url = '{}{}'.format(DOMAIN_NAME, formated_url)
        return working_url


def string_format(input_string):
    """
    :param input_string:html tag
    function takes tag as a input and extract text from tags and using regular expression
    replace '&' with 'and', replace 'space' with '_'
    :return: clean string without any special characters
    """

    if type(input_string) is str:
        string_text = input_string.replace(',','')
    else:
        string_text = input_string.text.strip()

    '''
    re.sub is a rugular expression method which takes list of characters and matches with pattern and replaces
    it with desired character 
    '''

    formatted_string = re.sub('[^a-zA-Z0-9&%@/\-,:.]', '_', string_text).replace('&', 'and').replace(',', '')

    return formatted_string


def text_format(input_string):
    """
    :param input_string:html tag
    function takes tag as a input and extract text from tags and using regular expression
    replace '&' with 'and', replace 'space' with '_'
    :return: clean string without any special characters
    """

    if type(input_string) is str:
        string_text = input_string.replace(',','')
    else:
        string_text = input_string.text.strip()

    '''
    re.sub is a rugular expression method which takes list of characters and matches with pattern and replaces
    it with desired character 
    '''
    normal_text = unicodedata.normalize('NFD',string_text)
    formatted_string = re.sub('[^a-zA-Z0-9&%()@/\-,: .]', '_', normal_text).replace('&', 'and').replace(',', '')

    return formatted_string


