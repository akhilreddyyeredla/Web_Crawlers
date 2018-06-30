import sys
sys.path.insert(0, r'/usr/datacollector')

import requests
import time
from bs4 import BeautifulSoup as soup
import DataCollectors_Configuration
import threading
import os
import constant

# from product_url_collection import Music_product_url_collection
from product_leaf_collector import music, bussiness, motors, collectibles_arts, electronics, fashion, home_garden, \
    toys_hobbies, sporting_goods
from product_info_collector import bussiness_info_collector, collectibles_info_collector, electronics_info_collector, \
    fashion_info_collector, home_info_collector, motor_info_collector, music_info_collector, sport_info_collector, \
    toy_info_collector
from product_url_collection import bussiness_product_url_collection, collectibles_product_url_collection, \
    electronics_product_url_collection, fashion_product_url_collection, home_product_url_collection, \
    motor_product_url_collection, Music_product_url_collection, sport_product_url_collection, toy_product_url_collection

# Returns page_soup

ROOT_FOLDER = DataCollectors_Configuration.ROOT_FOLDER


def page(url):

    uClient = requests.get(url)
    page_html = uClient.content
    uClient.close()
    page_soup = soup(page_html, "lxml")
    return page_soup


def start_prodcut_leaf_collection_new():
    jobs = []
    start = time.time()
    #if constant.MOTORS in DataCollectors_Configuration.EBAY_CATEGORY_LIST:
    for t_Category in DataCollectors_Configuration.EBAY_CATEGORY_LIST :
        if ( t_Category == constant.MOTORS ):
            thread1 = threading.Thread(target=motors.mus, args=(constant.Motors.format(ROOT_FOLDER),))
            print("leaf collections started: " + constant.MOTORS)
        elif ( t_Category == constant.FASHION ):
            thread1 = threading.Thread(target=fashion.mus, args=(constant.Fashion.format(ROOT_FOLDER),))
            print("leaf collections started: " + constant.FASHION)
        elif ( t_Category == constant.ELECTRONICS ):
            thread1 = threading.Thread(target=electronics.mus, args=(constant.Electronics.format(ROOT_FOLDER),))
            print("leaf collections started: " + constant.ELECTRONICS)
        elif ( t_Category == constant.COLLECTIBLES ):
            thread1 = threading.Thread(target=collectibles_arts.mus, args=(constant.Collectibles_arts.format(ROOT_FOLDER),))
            print("leaf collections started: " + constant.COLLECTIBLES)
        elif ( t_Category == constant.HOME ):
            thread1 = threading.Thread(target=home_garden.mus, args=(constant.Home_Garden.format(ROOT_FOLDER),))
            print("leaf collections started: " + constant.HOME)
        elif ( t_Category == constant.SPORT ):
            thread1 = threading.Thread(target=sporting_goods.mus, args=(constant.Sports_Goods.format(ROOT_FOLDER),))
            print("leaf collections started: " + constant.SPORT)
        elif ( t_Category == constant.TOYS ):
            thread1 = threading.Thread(target=toys_hobbies.mus, args=(constant.Toys_Hobbies.format(ROOT_FOLDER),))
            print("leaf collections started: " + constant.TOYS)
        elif ( t_Category == constant.MUSIC ):
            thread1 = threading.Thread(target=music.mus, args=(constant.Music.format(ROOT_FOLDER),))
            print("leaf collections started: " + constant.MUSIC)
        elif ( t_Category == constant.BUSINESS ):
            thread1 = threading.Thread(target=bussiness.mus, args=(constant.Business.format(ROOT_FOLDER),))
            print("leaf collections started: " + constant.BUSINESS)
        else:
            print ( "*** ERROR: Unsupported category. ***" );

        # Starting of threads
        thread1.daemon = True
        thread1.start ();
        thread1.join ();
        #jobs.append(thread1)


def start_prodcut_url_collection():
    jobs = []
    start = time.time()
    for t_category in DataCollectors_Configuration.EBAY_CATEGORY_LIST:
    	if (t_category == constant.MOTORS):
        	thread2 = threading.Thread(target=motor_product_url_collection.Buss_url,args=(constant.motor_leaf.format(ROOT_FOLDER),))
       		print("urls collections started: " + constant.MOTORS)

        elif (t_category == constant.FASHION):
       	        thread2 = threading.Thread(target=fashion_product_url_collection.Buss_url, args=(constant.fashion_leaf.format(ROOT_FOLDER),))
                print("urls collections started: " + constant.FASHION)

   	elif (t_category == constant.ELECTRONICS):
	        thread2 = threading.Thread(target=electronics_product_url_collection.Buss_url, args=(constant.electronics_leaf.format(ROOT_FOLDER),))
                print("urls collections started: " + constant.ELECTRONICS)

   	elif (t_coategory == constant.COLLECTIBLES):
	        thread2 = threading.Thread(target=collectibles_product_url_collection.Buss_url,args=(constant.collectibles_leaf.format(ROOT_FOLDER),))
                print("urls collections started: " + constant.COLLECTIBLES)

        elif (t_category == constant.HOME):
        	thread2 = threading.Thread(target=home_product_url_collection.Buss_url, args=(constant.home_leaf.format(ROOT_FOLDER),))
                print("urls collections started: " + constant.HOME)

        elif (t_category == constant.SPORT):
       	        thread2 = threading.Thread(target=sport_product_url_collection.Buss_url, args=(constant.sport_leaf.format(ROOT_FOLDER),))
                print("urls collections started: " + constant.SPORT)

        elif (t_category == constant.TOYS):
        	thread2 = threading.Thread(target=toy_product_url_collection.Buss_url, args=(constant.toy_leaf.format(ROOT_FOLDER),))
                print("urls collections started: " + constant.TOYS)

    	elif (t_category == constant.MUSIC):
	        thread2 = threading.Thread(target=Music_product_url_collection.Buss_url, args=(constant.music_leaf.format(ROOT_FOLDER),))
                print("urls collections started: " + constant.MUSIC)

        elif (t_category == constant.BUSINESS):
        	thread2 = threading.Thread(target=bussiness_product_url_collection.Buss_url, args=(constant.Business_leaf.format(ROOT_FOLDER),))
                print("urls collections started: " + constant.BUSINESS)

        else:
		print("*** ERROR: Invalid Category")
        # Starting of threads
        thread2.daemon = True
        thread2.start ();
        thread2.join ();
        #jobs.append(thread1)


def start_prodcut_info_collection():
    jobs = []
    start = time.time()
    for t_category in DataCollectors_Configuration.EBAY_CATEGORY_LIST:
    	if t_category == constant.MOTORS:
        	thread3 = threading.Thread(target=motor_info_collector.collection_start,args=(constant.motor_info.format(ROOT_FOLDER),))
      		print("info collections started: " + constant.MOTORS)

    	elif t_category == constant.FASHION:
        	thread3 = threading.Thread(target=fashion_info_collector.collection_start,args=(constant.fashion_info.format(ROOT_FOLDER),))
                print("info collections started: " + constant.FASHION)

    	elif t_category == constant.ELECTRONICS:
        	thread3 = threading.Thread(target=electronics_info_collector.collection_start,args=(constant.electronics_info.format(ROOT_FOLDER),)) 
       		print("info collections started: " + constant.ELECTRONICS)

    	elif t_category == constant.COLLECTIBLES:
        	thread3 = threading.Thread(target=collectibles_info_collector.collection_start,args=(constant.collectibles_info.format(ROOT_FOLDER),))
        
        	print("info collections started: " + constant.COLLECTIBLES)

    	elif t_category == constant.HOME:
        	thread3 = threading.Thread(target=home_info_collector.collection_start,args=(constant.home_info.format(ROOT_FOLDER),))
        
        	print("info collections started: " + constant.HOME)

    	elif t_category == constant.SPORT:
        	thread3 = threading.Thread(target=sport_info_collector.collection_start,args=(constant.sport_info.format(ROOT_FOLDER),))
        	print("info collections started: " + constant.SPORT)

    	elif t_category == constant.TOYS:
        	thread3 = threading.Thread(target=toy_info_collector.collection_start,args=(constant.toy_info.format(ROOT_FOLDER),))
        
        	print("info collections started: " + constant.TOYS)

    	elif t_category == constant.MUSIC:
        	thread3 = threading.Thread(target=music_info_collector.collection_start,args=(constant.music_info.format(ROOT_FOLDER),))
        
        	print("info collections started: " + constant.MUSIC)

    	elif t_category == constant.BUSINESS:
        	thread3 = threading.Thread(target=bussiness_info_collector.collection_start, args=(constant.business_info.format(ROOT_FOLDER),))
        
              	print("info collections started: " + constant.BUSINESS)
  	# Starting of threads
        thread3.daemon = True
        thread3.start ();
        thread3.join ();
        #jobs.append(thread1)
url = constant.main_url
page_soup = page(url)

main_containers = page_soup.findAll("div", {"class": "category-section"})
for main_category in main_containers:

    category_name = main_category.h2.text.replace(" ", "_").replace("&", "AND").replace(",", "_").encode('utf-8')

    sub_container = main_category.findAll("div", {"class": "sub-categories-container side-cntr"})

    # Creating directroy path for each category
    directory_path = "{}/{}/{}".format(ROOT_FOLDER, 'EBAY', category_name)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    file_name = '{}.txt'.format(category_name)
    file_path = '{}/{}/{}/{}'.format(ROOT_FOLDER, 'EBAY', category_name, file_name)

    # creating completed file
    completed_file_name = '{}_{}'.format(category_name, constant.COMPLETED_FILE)
    completed_file_path = '{}/{}/{}/{}'.format(ROOT_FOLDER, 'EBAY', category_name, completed_file_name)

    # SubCategory
    for sub_category in sub_container:
        sub_category_name = sub_category.h3.text.split("-")[0].replace(" ", "_").replace("&", "AND").replace(",",
                                                                                                             "_").encode(
            'utf-8')
        # print(sub_category_name)
        sub_sub_container = sub_category.findAll("li", {"class": "sub-category"})

        # Sub-Sub-Category
        for sub_sub_category in sub_sub_container:
            sub_sub_url = sub_sub_category.a['href']
            sub_sub_name = sub_sub_category.text.split("-")[0].replace(" ", "_").replace("&", "AND").replace(",",
                                                                                                             "_").encode(
                'utf-8')

            name = str(category_name) + "|" + str(sub_category_name) + "|" + str(sub_sub_name).replace(",", "_")

            # print(name)
            with open(completed_file_path, 'a') as file1:

                if (category_name == constant.MOTORS):
                    motor_list = set()
                    """completed file to list"""
                    motor_list = open(constant.motors_completed.format(ROOT_FOLDER, )).read().splitlines()
                    if not sub_sub_url in motor_list:
                        # urls into file
                        with open(file_path, 'a') as file:
                            line = '{},{}\n'.format(name, sub_sub_url)
                            file.write(line)
                        # ulrs into completed file
                        file1.write(sub_sub_url + "\n")

                if (category_name == constant.FASHION):
                    fashion_list = list()
                    # completed file to list
                    fashion_list = open(constant.fashion_completed.format(ROOT_FOLDER)).read().splitlines()
                    if sub_sub_url not in fashion_list:
                        with open(file_path, 'a') as file:
                            line = '{},{}\n'.format(name, sub_sub_url)
                            file.write(line)
                        # ulrs into completed file
                        file1.write(sub_sub_url + "\n")

                if (category_name == constant.ELECTRONICS):
                    elec_list = list()
                    # completed file to list
                    elec_list = open(constant.electronics_completed.format(ROOT_FOLDER)).read().splitlines()
                    if sub_sub_url not in elec_list:
                        # urls into file
                        with open(file_path, 'a') as file:
                            line = '{},{}\n'.format(name, sub_sub_url)
                            file.write(line)
                        # ulrs into completed file
                        file1.write(sub_sub_url + "\n")

                if (category_name == constant.COLLECTIBLES):
                    coll_list = list()
                    # completed file to list
                    coll_list = open(constant.collectibles_completed.format(ROOT_FOLDER)).read().splitlines()
                    if sub_sub_url not in coll_list:
                        # urls into file
                        with open(file_path, 'a') as file:
                            line = '{},{}\n'.format(name, sub_sub_url)
                            file.write(line)
                        # ulrs into completed file
                        file1.write(sub_sub_url + "\n")

                if (category_name == constant.HOME):
                    home_list = list()
                    # completed file to list
                    home_list = open(constant.home_completed.format(ROOT_FOLDER)).read().splitlines()
                    if sub_sub_url not in home_list:
                        # urls into file
                        with open(file_path, 'a') as file:
                            line = '{},{}\n'.format(name, sub_sub_url)
                            file.write(line)
                        # ulrs into completed file
                        file1.write(sub_sub_url + "\n")

                if (category_name == constant.SPORT):
                    sport_list = list()
                    # completed file to list
                    sport_list = open(constant.sport_completed.format(ROOT_FOLDER)).read().splitlines()
                    if sub_sub_url not in sport_list:
                        # urls into file
                        with open(file_path, 'a') as file:
                            line = '{},{}\n'.format(name, sub_sub_url)
                            file.write(line)
                        # ulrs into completed file
                        file1.write(sub_sub_url + "\n")

                if (category_name == constant.TOYS):
                    toy_list = list()
                    # completed file to list
                    toy_list = open(constant.toys_completed.format(ROOT_FOLDER)).read().splitlines()
                    if sub_sub_url not in toy_list:
                        # urls into file
                        with open(file_path, 'a') as file:
                            line = '{},{}\n'.format(name, sub_sub_url)
                            file.write(line)
                        # ulrs into completed file
                        file1.write(sub_sub_url + "\n")

                if (category_name == constant.BUSINESS):
                    business_list = list()
                    # completed file to list
                    business_list = open(constant.business_completed.format(ROOT_FOLDER)).read().splitlines()
                    if sub_sub_url not in business_list:
                        # urls into file
                        with open(file_path, 'a') as file:
                            line = '{},{}\n'.format(name, sub_sub_url)
                            file.write(line)
                        # ulrs into completed file
                        file1.write(sub_sub_url + "\n")

                if (category_name == constant.MUSIC):
                    music_list = list()
                    # completed file to list
                    music_list = open(constant.music_completed.format(ROOT_FOLDER)).read().splitlines()
                    if sub_sub_url not in music_list:
                        # urls into file
                        with open(file_path, 'a') as file:
                            line = '{},{}\n'.format(name, sub_sub_url)
                            file.write(line)
                        # ulrs into completed file
                        file1.write(sub_sub_url + "\n")
if __name__ == "__main__":
	if DataCollectors_Configuration.START_HIERARCHY_COLLECTION:
		start_prodcut_leaf_collection_new()
	if DataCollectors_Configuration.START_URL_COLLECTION:
		start_prodcut_url_collection()
	if DataCollectors_Configuration.START_INFO_COLLECTION:
		start_prodcut_info_collection()
