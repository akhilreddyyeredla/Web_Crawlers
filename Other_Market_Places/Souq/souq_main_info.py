import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = '/'.join(dir_path.split('/')[0:-1])
sys.path.insert(0, dir_path)
from Common.Souq_common_imports import *


def start_info_collection():
    jobs = []

    if DataCollectors_Configuration.APPAREL_SHOES_AND_ACCESSORIES in SOUQ_CATEGORY_LIST:
        thread_1 = multiprocessing.Process(target=Apparel_Shoes_and_Accessories_info_collector.start_info_collection)
        thread_1.daemon = True
        jobs.append(thread_1)

    if DataCollectors_Configuration.ART_CRAFTS_AND_COLLECTIBLES in SOUQ_CATEGORY_LIST:
        thread_2 = multiprocessing.Process(target=Art_Crafts_and_Collectibles_info_collector.start_info_collection)
        thread_2.daemon = True
        jobs.append(thread_2)

    if DataCollectors_Configuration.BABY in SOUQ_CATEGORY_LIST:
        thread_3 = multiprocessing.Process(target=Baby_info_collector.start_info_collection)
        thread_3.daemon = True
        jobs.append(thread_3)

    if DataCollectors_Configuration.BEAUTY in SOUQ_CATEGORY_LIST:
        thread_4 = multiprocessing.Process(target=Beauty_info_collector.start_info_collection)
        thread_4.daemon = True
        jobs.append(thread_4)

    if DataCollectors_Configuration.BED_AND_BATH in SOUQ_CATEGORY_LIST:
        thread_5 = multiprocessing.Process(target=Bed_and_Bath_info_collector.start_info_collection)
        thread_5.daemon = True
        jobs.append(thread_5)

    if DataCollectors_Configuration.BOOKS in SOUQ_CATEGORY_LIST:
        thread_6 = multiprocessing.Process(target=Books_info_collector.start_info_collection)
        thread_6.daemon = True
        jobs.append(thread_6)

    if DataCollectors_Configuration.CAMERAS in SOUQ_CATEGORY_LIST:
        thread_7 = multiprocessing.Process(target=Cameras_info_collector.start_info_collection)
        thread_7.daemon = True
        jobs.append(thread_7)

    if DataCollectors_Configuration.COINS_STAMPS_AND_PAPER_MONEY in SOUQ_CATEGORY_LIST:
        thread_8 = multiprocessing.Process(target=Coins_Stamps_and_Paper_money_info_collector.start_info_collection)
        thread_8.daemon = True
        jobs.append(thread_8)

    if DataCollectors_Configuration.COMPUTERS_IT_AND_NETWORKING in SOUQ_CATEGORY_LIST:
        thread_9 = multiprocessing.Process(target=Computers_IT_and_Networking_info_collector.start_info_collection)
        thread_9.daemon = True
        jobs.append(thread_9)

    if DataCollectors_Configuration.ELECTRONICS in SOUQ_CATEGORY_LIST:
        thread_10 = multiprocessing.Process(target=Electronics_info_collector.start_info_collection)
        thread_10.daemon = True
        jobs.append(thread_10)

    if DataCollectors_Configuration.EYEWEAR_AND_OPTICS in SOUQ_CATEGORY_LIST:
        thread_11 = multiprocessing.Process(target=Eyewear_and_Optics_info_collector.start_info_collection)
        thread_11.daemon = True
        jobs.append(thread_11)

    if DataCollectors_Configuration.FURNITURE in SOUQ_CATEGORY_LIST:
        thread_12 = multiprocessing.Process(target=Furniture_info_collector.start_info_collection)
        thread_12.daemon = True
        jobs.append(thread_12)

    if DataCollectors_Configuration.GAMING in SOUQ_CATEGORY_LIST:
        thread_13 = multiprocessing.Process(target=Gaming_info_collector.start_info_collection)
        thread_13.daemon = True
        jobs.append(thread_13)

    if DataCollectors_Configuration.GARDEN_AND_OUTDOOR in SOUQ_CATEGORY_LIST:
        thread_14 = multiprocessing.Process(target=Garden_and_Outdoor_info_collector.start_info_collection)
        thread_14.daemon = True
        jobs.append(thread_14)

    if DataCollectors_Configuration.GROCERY_FOOD_AND_BEVERAGES in SOUQ_CATEGORY_LIST:
        thread_15 = multiprocessing.Process(target=Grocery_Food_and_Beverages_info_collector.start_info_collection)
        thread_15.daemon = True
        jobs.append(thread_15)

    if DataCollectors_Configuration.HEALTH_AND_PERSONAL_CARE in SOUQ_CATEGORY_LIST:
        thread_16 = multiprocessing.Process(target=Health_and_Personal_Care_info_collector.start_info_collection)
        thread_16.daemon = True
        jobs.append(thread_16)

    if DataCollectors_Configuration.HOME_APPLIANCES in SOUQ_CATEGORY_LIST:
        thread_17 = multiprocessing.Process(target=Home_Appliances_info_collector.start_info_collection)
        thread_17.daemon = True
        jobs.append(thread_17)

    if DataCollectors_Configuration.HOME_DECOR_AND_FURNITURE in SOUQ_CATEGORY_LIST:
        thread_18 = multiprocessing.Process(target=Home_Decor_and_Furniture_info_collector.start_info_collection)
        thread_18.daemon = True
        jobs.append(thread_18)

    if DataCollectors_Configuration.JEWELRY_AND_ACCESSORIES in SOUQ_CATEGORY_LIST:
        thread_19 = multiprocessing.Process(target=Jewelry_and_Accessories_info_collector.start_info_collection)
        thread_19.daemon = True
        jobs.append(thread_19)

    if DataCollectors_Configuration.KITCHEN_AND_HOME_SUPPLIES in SOUQ_CATEGORY_LIST:
        thread_20 = multiprocessing.Process(target=Kitchen_and_Home_Supplies_info_collector.start_info_collection)
        thread_20.daemon = True
        jobs.append(thread_20)

    if DataCollectors_Configuration.KITCHEN_APPLIANCES in SOUQ_CATEGORY_LIST:
        thread_21 = multiprocessing.Process(target=Kitchen_Appliances_info_collector.start_info_collection)
        thread_21.daemon = True
        jobs.append(thread_21)

    if DataCollectors_Configuration.MOBILE_PHONES_TABLETS_AND_ACCESSORIES in SOUQ_CATEGORY_LIST:
        thread_22 = multiprocessing.Process(
            target=Mobile_Phones_Tablets_and_Accessories_info_collector.start_info_collection)
        thread_22.daemon = True
        jobs.append(thread_22)

    if DataCollectors_Configuration.MUSIC_AND_MOVIES in SOUQ_CATEGORY_LIST:
        thread_23 = multiprocessing.Process(target=Music_and_Movies_info_collector.start_info_collection)
        thread_23.daemon = True
        jobs.append(thread_23)

    if DataCollectors_Configuration.OFFICE_PRODUCTS_AND_SUPPLIES in SOUQ_CATEGORY_LIST:
        thread_24 = multiprocessing.Process(target=Office_Products_and_Supplies_info_collector.start_info_collection)
        thread_24.daemon = True
        jobs.append(thread_24)

    if DataCollectors_Configuration.PERFUMES_AND_FRAGRANCES in SOUQ_CATEGORY_LIST:
        thread_25 = multiprocessing.Process(target=Perfumes_and_Fragrances_info_collector.start_info_collection)
        thread_25.daemon = True
        jobs.append(thread_25)

    if DataCollectors_Configuration.PET_FOOD_AND_SUPPLIES in SOUQ_CATEGORY_LIST:
        thread_26 = multiprocessing.Process(target=Pet_Food_and_Supplies_info_collector.start_info_collection)
        thread_26.daemon = True
        jobs.append(thread_26)

    if DataCollectors_Configuration.SPORTS_AND_FITNESS in SOUQ_CATEGORY_LIST:
        thread_27 = multiprocessing.Process(target=Sports_and_Fitness_info_collector.start_info_collection)
        thread_27.daemon = True
        jobs.append(thread_27)

    if DataCollectors_Configuration.TOOLS_AND_HOME_IMPROVEMENTS in SOUQ_CATEGORY_LIST:
        thread_28 = multiprocessing.Process(target=Tools_and_Home_Improvements_info_collector.start_info_collection)
        thread_28.daemon = True
        jobs.append(thread_28)

    if DataCollectors_Configuration.TOYS in SOUQ_CATEGORY_LIST:
        thread_29 = multiprocessing.Process(target=Toys_info_collector.start_info_collection)
        thread_29.daemon = True
        jobs.append(thread_29)

    if DataCollectors_Configuration.VEHICLE_PARTS_AND_ACCESSORIES in SOUQ_CATEGORY_LIST:
        thread_30 = multiprocessing.Process(target=Vehicle_Parts_and_Accessories_info_collector.start_info_collection)
        thread_30.daemon = True
        jobs.append(thread_30)

    if DataCollectors_Configuration.VOUCHERS_AND_TICKETS in SOUQ_CATEGORY_LIST:
        thread_31 = multiprocessing.Process(target=Vouchers_and_Tickets_info_collector.start_info_collection)
        thread_31.daemon = True
        jobs.append(thread_31)

    if DataCollectors_Configuration.WEARABLE_TECHNOLOGY_DEVICES in SOUQ_CATEGORY_LIST:
        thread_32 = multiprocessing.Process(target=Wearable_Technology_Devices_info_collector.start_info_collection)
        thread_32.daemon = True
        jobs.append(thread_32)

    for job in jobs:
        job.start()
        # job.join ();

    for job in jobs:
        if (job.is_alive()):
            job.join()


if __name__ == '__main__':
    start_info_collection()
