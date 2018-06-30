import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = '/'.join(dir_path.split('/')[0:-1])
sys.path.insert(0, dir_path)
from Common.Ebay_common_imports import *

ROOT_FOLDER = DataCollectors_Configuration.ROOT_FOLDER_EBAY_URL


def page(url):
    uClient = requests.get(url)
    page_html = uClient.content
    uClient.close()
    page_soup = soup(page_html, "lxml")
    return page_soup


def start_prodcut_info_collection():
    jobs = []
    start = time.time()
    for t_category in DataCollectors_Configuration.EBAY_CATEGORY_LIST:
        if t_category == DataCollectors_Configuration.MOTORS:
            motor_obj = motor_info_collector.workers()
            thread3 = threading.Thread(target=motor_obj.collection_start,
                                       args=(DataCollectors_Configuration.motor_info.format(ROOT_FOLDER),))
            print("info collections started: " + DataCollectors_Configuration.MOTORS)

        elif t_category == DataCollectors_Configuration.FASHION:
            fashion_obj = fashion_info_collector.workers()
            thread3 = threading.Thread(target=fashion_obj.collection_start,
                                       args=(DataCollectors_Configuration.fashion_info.format(ROOT_FOLDER),))
            print("info collections started: " + DataCollectors_Configuration.FASHION)

        elif t_category == DataCollectors_Configuration.ELECTRONICS:
            electronics_obj = electronics_info_collector.workers()
            thread3 = threading.Thread(target=electronics_obj.collection_start,
                                       args=(DataCollectors_Configuration.electronics_info.format(ROOT_FOLDER),))
            print("info collections started: " + DataCollectors_Configuration.ELECTRONICS)

        elif t_category == DataCollectors_Configuration.COLLECTIBLES:
            colletibles_obj = collectibles_info_collector.workers()
            thread3 = threading.Thread(target=colletibles_obj.collection_start,
                                       args=(DataCollectors_Configuration.collectibles_info.format(ROOT_FOLDER),))

            print("info collections started: " + DataCollectors_Configuration.COLLECTIBLES)

        elif t_category == DataCollectors_Configuration.HOME:
            home_obj = home_info_collector.workers()
            thread3 = threading.Thread(target=home_obj.collection_start,
                                       args=(DataCollectors_Configuration.home_info.format(ROOT_FOLDER),))

            print("info collections started: " + DataCollectors_Configuration.HOME)

        elif t_category == DataCollectors_Configuration.SPORT:
            sport_obj = sport_info_collector.workers()
            thread3 = threading.Thread(target=sport_obj.collection_start,
                                       args=(DataCollectors_Configuration.sport_info.format(ROOT_FOLDER),))
            print("info collections started: " + DataCollectors_Configuration.SPORT)

        elif t_category == DataCollectors_Configuration.TOYS:
            toys_obj = toy_info_collector.workers()
            thread3 = threading.Thread(target=toys_obj.collection_start,
                                       args=(DataCollectors_Configuration.toy_info.format(ROOT_FOLDER),))

            print("info collections started: " + DataCollectors_Configuration.TOYS)

        elif t_category == DataCollectors_Configuration.MUSIC:
            music_obj = music_info_collector.workers()
            thread3 = threading.Thread(target=music_obj.collection_start,
                                       args=(DataCollectors_Configuration.music_info.format(ROOT_FOLDER),))

            print("info collections started: " + DataCollectors_Configuration.MUSIC)

        elif t_category == DataCollectors_Configuration.BUSINESS:
            bussiness_obj = bussiness_info_collector.workers()
            thread3 = threading.Thread(target=bussiness_obj.collection_start,
                                       args=(DataCollectors_Configuration.business_info.format(ROOT_FOLDER),))

            print("info collections started: " + DataCollectors_Configuration.BUSINESS)
        # Starting of threads
        thread3.daemon = True
        thread3.start()
        thread3.join()
        # jobs.append(thread1)

if __name__ == "__main__":
    start_prodcut_info_collection()
