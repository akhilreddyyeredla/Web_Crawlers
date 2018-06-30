import random
import requests
from bs4 import BeautifulSoup
import time
from Global_Constants import MAX_RETRIES, HEADERS, GOOD_STATUS, BAD_STATUS, HEADERS_LIST, PAGE_NOT_FOUND


class Response:

    def __init__(self):
        self.PROXY = dict()
        self.PROXY["http"] = 'http://{}'.format("127.0.0.1:8118")
        self.PROXY["https"] = 'https://{}'.format("127.0.0.1:8118")

    def get_user_agent(self):
        '''
        :return: random user agent from headers list
        '''
        num = random.randint(0, len(HEADERS_LIST) - 1)

        return HEADERS_LIST[num]

    def get_content(self,url,data=None, proxy=False):
        """
        :param url: page_url
        :return: Beautifulsoup object
        """
        try:
            response = self.get_request(url, proxy=proxy)
            # check if we got response then parse that response with beautifulsoup
            if response is None:
                return None
            else:
                # print(BeautifulSoup(response.content, 'lxml'))
                return BeautifulSoup(response.content, 'lxml')

        except Exception as e:
            print (e)
            return self.get_content(url, proxy)

    def get_request(self, url, proxy=False):
        response = None
        HEADERS["User-Agent"] = self.get_user_agent()
        for count in range(MAX_RETRIES):
            try:
                # time.sleep(30)
                if proxy:
                    req = requests.get(url, headers=HEADERS, proxies=self.PROXY, timeout=60)
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
                print url
        return response

    ########################################## for souq #########################################
    def get_page_soup(self, url, proxy=False):
        """
            :param proxy: default flase if you want to send request through proxy pass parameter as proxy=True
            :param url: page_url
            :return: Beautifulsoup object
            """
        try:
            response = self.get_request_souq(url,proxy=proxy)
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
            return self.get_page_soup(url, proxy=proxy)

    # parse the url and return request content

    def get_request_souq(self, url, proxy=False):
        response = None
        HEADERS["User-Agent"] = self.get_user_agent()
        for count in range(MAX_RETRIES):
            try:
                # time.sleep(30)
                if proxy:
                    req = requests.get(url, headers=HEADERS, proxies=self.PROXY, timeout=60)
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
                time.sleep(2)
                print('Exception')
                print e

