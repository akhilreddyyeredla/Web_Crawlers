import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = '/'.join(dir_path.split('/')[0:-1])
sys.path.insert(0, dir_path)
from Common.Ebay_common_imports import *

ROOT_FOLDER = DataCollectors_Configuration.ROOT_FOLDER_EBAY_HIERARCHY


def page(url):
    uClient = requests.get(url)
    page_html = uClient.content
    uClient.close()
    page_soup = soup(page_html, "lxml")
    return page_soup


def start_prodcut_url_collection():
    jobs = []
    start = time.time()
    for t_category in DataCollectors_Configuration.EBAY_CATEGORY_LIST:
        if (t_category == DataCollectors_Configuration.MOTORS):
            motors_obj = motor_product_url_collection.Workers()
            thread1 = threading.Thread(target=motors_obj.Buss_url,
                                       args=(DataCollectors_Configuration.motor_leaf.format(ROOT_FOLDER),))
            thread1.daemon = True
            jobs.append(thread1)
            print("urls collections started: " + DataCollectors_Configuration.MOTORS + " | " + str(start))

        if (t_category == DataCollectors_Configuration.FASHION):
            fashion_obj = fashion_product_url_collection.Workers()
            thread2 = threading.Thread(target=fashion_obj.Buss_url,
                                       args=(DataCollectors_Configuration.fashion_leaf.format(ROOT_FOLDER),))
            thread2.daemon = True
            jobs.append(thread2)
            print("urls collections started: " + DataCollectors_Configuration.FASHION)

        if (t_category == DataCollectors_Configuration.ELECTRONICS):
            electronics_obj = electronics_product_url_collection.Workers()
            thread3 = threading.Thread(target=electronics_obj.Buss_url,
                                       args=(DataCollectors_Configuration.electronics_leaf.format(ROOT_FOLDER),))
            thread3.daemon = True
            jobs.append(thread3)
            print("urls collections started: " + DataCollectors_Configuration.ELECTRONICS)

        if (t_category == DataCollectors_Configuration.COLLECTIBLES):
            collectibles_obj = collectibles_product_url_collection.Workers()
            thread4 = threading.Thread(target=collectibles_obj.Buss_url,
                                       args=(DataCollectors_Configuration.collectibles_leaf.format(ROOT_FOLDER),))
            thread4.daemon = True
            jobs.append(thread4)
            print("urls collections started: " + DataCollectors_Configuration.COLLECTIBLES)

        if (t_category == DataCollectors_Configuration.HOME):
            home_obj = home_product_url_collection.Workers()
            thread5 = threading.Thread(target=home_obj.Buss_url,
                                       args=(DataCollectors_Configuration.home_leaf.format(ROOT_FOLDER),))
            thread5.daemon = True
            jobs.append(thread5)
            print("urls collections started: " + DataCollectors_Configuration.HOME)

        if (t_category == DataCollectors_Configuration.SPORT):
            sport_obj = sport_product_url_collection.Workers()
            thread6 = threading.Thread(target=sport_obj.Buss_url,
                                       args=(DataCollectors_Configuration.sport_leaf.format(ROOT_FOLDER),))
            thread6.daemon = True
            jobs.append(thread6)
            print("urls collections started: " + DataCollectors_Configuration.SPORT)

        if (t_category == DataCollectors_Configuration.TOYS):
            toys_obj = toy_product_url_collection.Workers()
            thread7 = threading.Thread(target=toys_obj.Buss_url,
                                       args=(DataCollectors_Configuration.toy_leaf.format(ROOT_FOLDER),))
            thread7.daemon = True
            jobs.append(thread7)
            print("urls collections started: " + DataCollectors_Configuration.TOYS)

        if (t_category == DataCollectors_Configuration.MUSIC):
            music_obj = Music_product_url_collection.Workers()
            thread8 = threading.Thread(target=music_obj.Buss_url,
                                       args=(DataCollectors_Configuration.music_leaf.format(ROOT_FOLDER),))
            thread8.daemon = True
            jobs.append(thread8)
            print("urls collections started: " + DataCollectors_Configuration.MUSIC)

        if (t_category == DataCollectors_Configuration.BUSINESS):
            bussiness_obj = bussiness_product_url_collection.Workers()
            thread9 = threading.Thread(target=bussiness_obj.Buss_url,
                                       args=(DataCollectors_Configuration.Business_leaf.format(ROOT_FOLDER),))
            thread9.daemon = True
            jobs.append(thread9)
            print("urls collections started: " + DataCollectors_Configuration.BUSINESS)

        # Starting of threads

    for t_Job in jobs:
        t_Job.start()

    for t_Job in jobs:
        if (t_Job.is_alive()):
            stop = time.time()
            # print str(stop)
            t_Job.join()


if __name__ == "__main__":
    start_prodcut_url_collection()
