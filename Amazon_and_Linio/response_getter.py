import random
import requests
from bs4 import BeautifulSoup
import time
from Global_Constants import MAX_RETRIES, HEADERS, GOOD_STATUS, BAD_STATUS, PROXY, HEADERS_LIST, PAGE_NOT_FOUND
from DataCollectors_Configuration import PROXY_ON

PROXY["http"] = 'http://{}'.format("127.0.0.1:8118")
PROXY["https"] = 'https://{}'.format("127.0.0.1:8118")


def get_user_agent():
    '''

    :return: random user agent from headers list
    '''
    num = random.randint(0, len(HEADERS_LIST) - 1)

    return HEADERS_LIST[num]


HEADERS["User-Agent"] = get_user_agent()


def get_content(url,data=None):
    """

    :param url: page_url
    :return: Beautifulsoup object
    """
    try:
        response = get_request(url)
        # check if we got response then parse that response with beautifulsoup
        if response is None:
            return None
        else:
            # print(BeautifulSoup(response.content, 'lxml'))
            return BeautifulSoup(response.content, 'lxml')

    except Exception as e:
        print (e)
        get_content(url)


def get_request(url):
    response = None
    for count in range(MAX_RETRIES):
        try:
            # time.sleep(30)
            if PROXY_ON:
                req = requests.get(url, headers=HEADERS, proxies=PROXY, timeout=60)
            else:
                req = requests.get(url, headers=HEADERS, timeout=60)

            if req.status_code == GOOD_STATUS:
                response = req
                break
            elif req.status_code == BAD_STATUS:
                print('blocked')
                time.sleep(50)
            else:
                print(url)
                time.sleep(50)
                print ("got invalid response")
        except Exception as e:
            time.sleep(50)
            print('Exception')
    return response


########################################## for souq #########################################
def get_page_soup(url):
    """

        :param url: page_url
        :return: Beautifulsoup object
        """
    try:
        response = get_request_souq(url)
        # check if we got response then parse that response with beautifulsoup
        if response is None:
            return None, None
        elif response == BAD_STATUS:
            return response, None

        else:
            return BeautifulSoup(response.content, "lxml"), response.url
    except Exception as e:
        # print('in be')
        print(e)
        get_page_soup(url)


# parse the url and return request content

def get_request_souq(url):
    response = None
    for count in range(MAX_RETRIES):
        try:
            # time.sleep(30)
            if PROXY_ON:
                req = requests.get(url, headers=HEADERS, proxies=PROXY, timeout=60)
            else:
                req = requests.get(url, headers=HEADERS, timeout=60)

            if req.status_code == GOOD_STATUS:
                return req
            elif req.status_code == PAGE_NOT_FOUND:
                return req.status_code
            else:
                print(url)
                time.sleep(50)
                print ("got invalid response")
        except Exception as e:
            time.sleep(50)
            print('Exception')
    return response

##########################################################################################################