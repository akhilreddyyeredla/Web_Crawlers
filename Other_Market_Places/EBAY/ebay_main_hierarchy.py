import sys
import os
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


def start_prodcut_leaf_collection_new():
    jobs = []
    start = time.time()
    #if constant.MOTORS in DataCollectors_Configuration.EBAY_CATEGORY_LIST:
    for t_Category in DataCollectors_Configuration.EBAY_CATEGORY_LIST :
        if ( t_Category == DataCollectors_Configuration.MOTORS ):
            work_obj_motor = motors.workers()
            thread1 = threading.Thread(target=work_obj_motor.mus, args=(DataCollectors_Configuration.Motors.format(ROOT_FOLDER),))
            print("leaf collections started: " + DataCollectors_Configuration.MOTORS)
        elif ( t_Category == DataCollectors_Configuration.FASHION ):
            work_obj_fashion = fashion.workers()
            thread1 = threading.Thread(target=work_obj_fashion.mus, args=(DataCollectors_Configuration.Fashion.format(ROOT_FOLDER),))
            print("leaf collections started: " + DataCollectors_Configuration.FASHION)
        elif ( t_Category == DataCollectors_Configuration.ELECTRONICS ):
            work_obj_electronics = electronics.workers()
            thread1 = threading.Thread(target=work_obj_electronics.mus, args=(DataCollectors_Configuration.Electronics.format(ROOT_FOLDER),))
            print("leaf collections started: " + DataCollectors_Configuration.ELECTRONICS)
        elif ( t_Category == DataCollectors_Configuration.COLLECTIBLES ):
            work_obj_collectibles = collectibles_arts.workers()
            thread1 = threading.Thread(target=work_obj_collectibles.mus, args=(DataCollectors_Configuration.Collectibles_arts.format(ROOT_FOLDER),))
            print("leaf collections started: " + DataCollectors_Configuration.COLLECTIBLES)
        elif ( t_Category == DataCollectors_Configuration.HOME ):
            work_obj_home = home_garden.workers()
            thread1 = threading.Thread(target=work_obj_home.mus, args=(DataCollectors_Configuration.Home_Garden.format(ROOT_FOLDER),))
            print("leaf collections started: " + DataCollectors_Configuration.HOME)
        elif ( t_Category == DataCollectors_Configuration.SPORT ):
            work_obj_sport = sporting_goods.workers()
            thread1 = threading.Thread(target=work_obj_sport.mus, args=(DataCollectors_Configuration.Sports_Goods.format(ROOT_FOLDER),))
            print("leaf collections started: " + DataCollectors_Configuration.SPORT)
        elif ( t_Category == DataCollectors_Configuration.TOYS ):
            work_obj_toys = toys_hobbies.workers()
            thread1 = threading.Thread(target=work_obj_toys.mus, args=(DataCollectors_Configuration.Toys_Hobbies.format(ROOT_FOLDER),))
            print("leaf collections started: " + DataCollectors_Configuration.TOYS)
        elif ( t_Category == DataCollectors_Configuration.MUSIC ):
            work_obj_music = music.workers()

            thread1 = threading.Thread(target=work_obj_music.mus, args=(DataCollectors_Configuration.Music.format(ROOT_FOLDER),))
            print("leaf collections started: " + DataCollectors_Configuration.MUSIC)
        elif ( t_Category == DataCollectors_Configuration.BUSINESS ):
            work_obj_bussiness = bussiness.workers()
            thread1 = threading.Thread(target=work_obj_bussiness.mus, args=(DataCollectors_Configuration.Business.format(ROOT_FOLDER),))
            print("leaf collections started: " + DataCollectors_Configuration.BUSINESS)
        else:
            print ("*** ERROR: Unsupported category. ***")

        # Starting of threads
        thread1.daemon = True
        thread1.start ()
        thread1.join ()
        #jobs.append(thread1)




url = DataCollectors_Configuration.main_url
page_soup = page(url)

main_containers = page_soup.findAll("div", {"class": "category-section"})
for main_category in main_containers:

    category_name = main_category.h2.text.replace(" ", "_").replace("&", "AND").replace(",", "_").encode('utf-8')

    sub_container = main_category.findAll("div", {"class": "sub-categories-container side-cntr"})

    # Creating directroy path for each category
    directory_path = "{}/{}".format(ROOT_FOLDER, category_name)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    file_name = '{}.txt'.format(category_name)
    file_path = '{}/{}/{}'.format(ROOT_FOLDER, category_name, file_name)

    # creating completed file
    completed_file_name = '{}_{}'.format(category_name, DataCollectors_Configuration.COMPLETED_FILE)
    completed_file_path = '{}/{}/{}'.format(ROOT_FOLDER, category_name, completed_file_name)

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

                if (category_name == DataCollectors_Configuration.MOTORS):
                    motor_list = set()
                    """completed file to list"""
                    motor_list = open(DataCollectors_Configuration.motors_completed.format(ROOT_FOLDER, )).read().splitlines()
                    if not sub_sub_url in motor_list:
                        # urls into file
                        with open(file_path, 'a') as file:
                            line = '{},{}\n'.format(name, sub_sub_url)
                            file.write(line)
                        # ulrs into completed file
                        file1.write(sub_sub_url + "\n")

                if (category_name == DataCollectors_Configuration.FASHION):
                    fashion_list = list()
                    # completed file to list
                    fashion_list = open(DataCollectors_Configuration.fashion_completed.format(ROOT_FOLDER)).read().splitlines()
                    if sub_sub_url not in fashion_list:
                        with open(file_path, 'a') as file:
                            line = '{},{}\n'.format(name, sub_sub_url)
                            file.write(line)
                        # ulrs into completed file
                        file1.write(sub_sub_url + "\n")

                if (category_name == DataCollectors_Configuration.ELECTRONICS):
                    elec_list = list()
                    # completed file to list
                    elec_list = open(DataCollectors_Configuration.electronics_completed.format(ROOT_FOLDER)).read().splitlines()
                    if sub_sub_url not in elec_list:
                        # urls into file
                        with open(file_path, 'a') as file:
                            line = '{},{}\n'.format(name, sub_sub_url)
                            file.write(line)
                        # ulrs into completed file
                        file1.write(sub_sub_url + "\n")

                if (category_name == DataCollectors_Configuration.COLLECTIBLES):
                    coll_list = list()
                    # completed file to list
                    coll_list = open(DataCollectors_Configuration.collectibles_completed.format(ROOT_FOLDER)).read().splitlines()
                    if sub_sub_url not in coll_list:
                        # urls into file
                        with open(file_path, 'a') as file:
                            line = '{},{}\n'.format(name, sub_sub_url)
                            file.write(line)
                        # ulrs into completed file
                        file1.write(sub_sub_url + "\n")

                if (category_name == DataCollectors_Configuration.HOME):
                    home_list = list()
                    # completed file to list
                    home_list = open(DataCollectors_Configuration.home_completed.format(ROOT_FOLDER)).read().splitlines()
                    if sub_sub_url not in home_list:
                        # urls into file
                        with open(file_path, 'a') as file:
                            line = '{},{}\n'.format(name, sub_sub_url)
                            file.write(line)
                        # ulrs into completed file
                        file1.write(sub_sub_url + "\n")

                if (category_name == DataCollectors_Configuration.SPORT):
                    sport_list = list()
                    # completed file to list
                    sport_list = open(DataCollectors_Configuration.sport_completed.format(ROOT_FOLDER)).read().splitlines()
                    if sub_sub_url not in sport_list:
                        # urls into file
                        with open(file_path, 'a') as file:
                            line = '{},{}\n'.format(name, sub_sub_url)
                            file.write(line)
                        # ulrs into completed file
                        file1.write(sub_sub_url + "\n")

                if category_name == DataCollectors_Configuration.TOYS:
                    toy_list = list()
                    # completed file to list
                    toy_list = open(DataCollectors_Configuration.toys_completed.format(ROOT_FOLDER)).read().splitlines()
                    if sub_sub_url not in toy_list:
                        # urls into file
                        with open(file_path, 'a') as file:
                            line = '{},{}\n'.format(name, sub_sub_url)
                            file.write(line)
                        # ulrs into completed file
                        file1.write(sub_sub_url + "\n")

                if category_name == DataCollectors_Configuration.BUSINESS:
                    business_list = list()
                    # completed file to list
                    business_list = open(DataCollectors_Configuration.business_completed.format(ROOT_FOLDER)).read().splitlines()
                    if sub_sub_url not in business_list:
                        # urls into file
                        with open(file_path, 'a') as file:
                            line = '{},{}\n'.format(name, sub_sub_url)
                            file.write(line)
                        # ulrs into completed file
                        file1.write(sub_sub_url + "\n")

                if category_name == DataCollectors_Configuration.MUSIC:
                    music_list = list()
                    # completed file to list
                    music_list = open(DataCollectors_Configuration.music_completed.format(ROOT_FOLDER)).read().splitlines()
                    if sub_sub_url not in music_list:
                        # urls into file
                        with open(file_path, 'a') as file:
                            line = '{},{}\n'.format(name, sub_sub_url)
                            file.write(line)
                        # ulrs into completed file
                        file1.write(sub_sub_url + "\n")


start_prodcut_leaf_collection_new()

