import sys
sys.path.insert(0, r'/usr/datacollector')

#import Write_contants_file
#Write_contants_file.write_path()
from scrappers import Apparel_Shoes_and_Accessories_scrape_urls, Art_Crafts_and_Collectibles_scrape_urls, \
    Baby_scrape_urls, Beauty_scrape_urls, Bed_and_Bath_scrape_urls, Books_scrape_urls, Cameras_scrape_urls, \
    Coins_Stamps_and_Paper_money_scrape_urls, Computers_IT_and_Networking_scrape_urls, Electronics_scrape_urls, \
    Eyewear_and_Optics_scrape_urls, Furniture_scrape_urls, Gaming_scrape_urls, Garden_and_Outdoor_scrape_urls, \
    Grocery_Food_and_Beverages_scrape_urls, Health_and_Personal_Care_scrape_urls, Home_Appliances_scrape_urls, \
    Home_Decor_and_Furniture_scrape_urls, Jewelry_and_Accessories_scrape_urls, Kitchen_and_Home_Supplies_scrape_urls, \
    Kitchen_Appliances_scrape_urls, Mobile_Phones_Tablets_and_Accessories_scrape_urls, Music_and_Movies_scrape_urls, \
    Office_Products_and_Supplies_scrape_urls, Perfumes_and_Fragrances_scrape_urls, Pet_Food_and_Supplies_scrape_urls, \
    Sports_and_Fitness_scrape_urls, Tools_and_Home_Improvements_scrape_urls, Toys_scrape_urls, \
    Vehicle_Parts_and_Accessories_scrape_urls, Vouchers_and_Tickets_scrape_urls, Wearable_Technology_Devices_scrape_urls
from product_info_collectors import Apparel_Shoes_and_Accessories_info_collector, \
    Art_Crafts_and_Collectibles_info_collector, Baby_info_collector, Beauty_info_collector, Bed_and_Bath_info_collector, \
    Books_info_collector, Cameras_info_collector, Coins_Stamps_and_Paper_money_info_collector, \
    Computers_IT_and_Networking_info_collector, Electronics_info_collector, Eyewear_and_Optics_info_collector, \
    Furniture_info_collector, Gaming_info_collector, Garden_and_Outdoor_info_collector, \
    Grocery_Food_and_Beverages_info_collector, Health_and_Personal_Care_info_collector, Home_Appliances_info_collector, \
    Home_Decor_and_Furniture_info_collector, Jewelry_and_Accessories_info_collector, \
    Kitchen_and_Home_Supplies_info_collector, Kitchen_Appliances_info_collector, \
    Mobile_Phones_Tablets_and_Accessories_info_collector, Music_and_Movies_info_collector, \
    Office_Products_and_Supplies_info_collector, Perfumes_and_Fragrances_info_collector, \
    Pet_Food_and_Supplies_info_collector, Sports_and_Fitness_info_collector, Tools_and_Home_Improvements_info_collector, \
    Toys_info_collector, Vehicle_Parts_and_Accessories_info_collector, Vouchers_and_Tickets_info_collector, \
    Wearable_Technology_Devices_info_collector
from DataCollectors_Configuration import SOUQ_CATEGORY_LIST, START_URL_COLLECTION, START_INFO_COLLECTION
import CONSTANTS
import multiprocessing


def start_info_collection():
    jobs = []

    if CONSTANTS.APPAREL_SHOES_AND_ACCESSORIES in SOUQ_CATEGORY_LIST:
        thread_1 = multiprocessing.Process(target=Apparel_Shoes_and_Accessories_info_collector.start_info_collection)
        thread_1.daemon = True
        jobs.append(thread_1)

    if CONSTANTS.ART_CRAFTS_AND_COLLECTIBLES in SOUQ_CATEGORY_LIST:
        thread_2 = multiprocessing.Process(target=Art_Crafts_and_Collectibles_info_collector.start_info_collection)
        thread_2.daemon = True
        jobs.append(thread_2)

    if CONSTANTS.BABY in SOUQ_CATEGORY_LIST:
        thread_3 = multiprocessing.Process(target=Baby_info_collector.start_info_collection)
        thread_3.daemon = True
        jobs.append(thread_3)

    if CONSTANTS.BEAUTY in SOUQ_CATEGORY_LIST:
        thread_4 = multiprocessing.Process(target=Beauty_info_collector.start_info_collection)
        thread_4.daemon = True
        jobs.append(thread_4)

    if CONSTANTS.BED_AND_BATH in SOUQ_CATEGORY_LIST:
        thread_5 = multiprocessing.Process(target=Bed_and_Bath_info_collector.start_info_collection)
        thread_5.daemon = True
        jobs.append(thread_5)

    if CONSTANTS.BOOKS in SOUQ_CATEGORY_LIST:
        thread_6 = multiprocessing.Process(target=Books_info_collector.start_info_collection)
        thread_6.daemon = True
        jobs.append(thread_6)

    if CONSTANTS.CAMERAS in SOUQ_CATEGORY_LIST:
        thread_7 = multiprocessing.Process(target=Cameras_info_collector.start_info_collection)
        thread_7.daemon = True
        jobs.append(thread_7)

    if CONSTANTS.COINS_STAMPS_AND_PAPER_MONEY in SOUQ_CATEGORY_LIST:
        thread_8 = multiprocessing.Process(target=Coins_Stamps_and_Paper_money_info_collector.start_info_collection)
        thread_8.daemon = True
        jobs.append(thread_8)

    if CONSTANTS.COMPUTERS_IT_AND_NETWORKING in SOUQ_CATEGORY_LIST:
        thread_9 = multiprocessing.Process(target=Computers_IT_and_Networking_info_collector.start_info_collection)
        thread_9.daemon = True
        jobs.append(thread_9)

    if CONSTANTS.ELECTRONICS in SOUQ_CATEGORY_LIST:
        thread_10 = multiprocessing.Process(target=Electronics_info_collector.start_info_collection)
        thread_10.daemon = True
        jobs.append(thread_10)

    if CONSTANTS.EYEWEAR_AND_OPTICS in SOUQ_CATEGORY_LIST:
        thread_11 = multiprocessing.Process(target=Eyewear_and_Optics_info_collector.start_info_collection)
        thread_11.daemon = True
        jobs.append(thread_11)

    if CONSTANTS.FURNITURE in SOUQ_CATEGORY_LIST:
        thread_12 = multiprocessing.Process(target=Furniture_info_collector.start_info_collection)
        thread_12.daemon = True
        jobs.append(thread_12)

    if CONSTANTS.GAMING in SOUQ_CATEGORY_LIST:
        thread_13 = multiprocessing.Process(target=Gaming_info_collector.start_info_collection)
        thread_13.daemon = True
        jobs.append(thread_13)

    if CONSTANTS.GARDEN_AND_OUTDOOR in SOUQ_CATEGORY_LIST:
        thread_14 = multiprocessing.Process(target=Garden_and_Outdoor_info_collector.start_info_collection)
        thread_14.daemon = True
        jobs.append(thread_14)

    if CONSTANTS.GROCERY_FOOD_AND_BEVERAGES in SOUQ_CATEGORY_LIST:
        thread_15 = multiprocessing.Process(target=Grocery_Food_and_Beverages_info_collector.start_info_collection)
        thread_15.daemon = True
        jobs.append(thread_15)

    if CONSTANTS.HEALTH_AND_PERSONAL_CARE in SOUQ_CATEGORY_LIST:
        thread_16 = multiprocessing.Process(target=Health_and_Personal_Care_info_collector.start_info_collection)
        thread_16.daemon = True
        jobs.append(thread_16)

    if CONSTANTS.HOME_APPLIANCES in SOUQ_CATEGORY_LIST:
        thread_17 = multiprocessing.Process(target=Home_Appliances_info_collector.start_info_collection)
        thread_17.daemon = True
        jobs.append(thread_17)

    if CONSTANTS.HOME_DECOR_AND_FURNITURE in SOUQ_CATEGORY_LIST:
        thread_18 = multiprocessing.Process(target=Home_Decor_and_Furniture_info_collector.start_info_collection)
        thread_18.daemon = True
        jobs.append(thread_18)

    if CONSTANTS.JEWELRY_AND_ACCESSORIES in SOUQ_CATEGORY_LIST:
        thread_19 = multiprocessing.Process(target=Jewelry_and_Accessories_info_collector.start_info_collection)
        thread_19.daemon = True
        jobs.append(thread_19)

    if CONSTANTS.KITCHEN_AND_HOME_SUPPLIES in SOUQ_CATEGORY_LIST:
        thread_20 = multiprocessing.Process(target=Kitchen_and_Home_Supplies_info_collector.start_info_collection)
        thread_20.daemon = True
        jobs.append(thread_20)

    if CONSTANTS.KITCHEN_APPLIANCES in SOUQ_CATEGORY_LIST:
        thread_21 = multiprocessing.Process(target=Kitchen_Appliances_info_collector.start_info_collection)
        thread_21.daemon = True
        jobs.append(thread_21)

    if CONSTANTS.MOBILE_PHONES_TABLETS_AND_ACCESSORIES in SOUQ_CATEGORY_LIST:
        thread_22 = multiprocessing.Process(
            target=Mobile_Phones_Tablets_and_Accessories_info_collector.start_info_collection)
        thread_22.daemon = True
        jobs.append(thread_22)

    if CONSTANTS.MUSIC_AND_MOVIES in SOUQ_CATEGORY_LIST:
        thread_23 = multiprocessing.Process(target=Music_and_Movies_info_collector.start_info_collection)
        thread_23.daemon = True
        jobs.append(thread_23)

    if CONSTANTS.OFFICE_PRODUCTS_AND_SUPPLIES in SOUQ_CATEGORY_LIST:
        thread_24 = multiprocessing.Process(target=Office_Products_and_Supplies_info_collector.start_info_collection)
        thread_24.daemon = True
        jobs.append(thread_24)

    if CONSTANTS.PERFUMES_AND_FRAGRANCES in SOUQ_CATEGORY_LIST:
        thread_25 = multiprocessing.Process(target=Perfumes_and_Fragrances_info_collector.start_info_collection)
        thread_25.daemon = True
        jobs.append(thread_25)

    if CONSTANTS.PET_FOOD_AND_SUPPLIES in SOUQ_CATEGORY_LIST:
        thread_26 = multiprocessing.Process(target=Pet_Food_and_Supplies_info_collector.start_info_collection)
        thread_26.daemon = True
        jobs.append(thread_26)

    if CONSTANTS.SPORTS_AND_FITNESS in SOUQ_CATEGORY_LIST:
        thread_27 = multiprocessing.Process(target=Sports_and_Fitness_info_collector.start_info_collection)
        thread_27.daemon = True
        jobs.append(thread_27)

    if CONSTANTS.TOOLS_AND_HOME_IMPROVEMENTS in SOUQ_CATEGORY_LIST:
        thread_28 = multiprocessing.Process(target=Tools_and_Home_Improvements_info_collector.start_info_collection)
        thread_28.daemon = True
        jobs.append(thread_28)

    if CONSTANTS.TOYS in SOUQ_CATEGORY_LIST:
        thread_29 = multiprocessing.Process(target=Toys_info_collector.start_info_collection)
        thread_29.daemon = True
        jobs.append(thread_29)

    if CONSTANTS.VEHICLE_PARTS_AND_ACCESSORIES in SOUQ_CATEGORY_LIST:
        thread_30 = multiprocessing.Process(target=Vehicle_Parts_and_Accessories_info_collector.start_info_collection)
        thread_30.daemon = True
        jobs.append(thread_30)

    if CONSTANTS.VOUCHERS_AND_TICKETS in SOUQ_CATEGORY_LIST:
        thread_31 = multiprocessing.Process(target=Vouchers_and_Tickets_info_collector.start_info_collection)
        thread_31.daemon = True
        jobs.append(thread_31)

    if CONSTANTS.WEARABLE_TECHNOLOGY_DEVICES in SOUQ_CATEGORY_LIST:
        thread_32 = multiprocessing.Process(target=Wearable_Technology_Devices_info_collector.start_info_collection)
        thread_32.daemon = True
        jobs.append(thread_32)

    for job in jobs:
        job.start()
        job.join()



def start_program():
    jobs = []

    if CONSTANTS.APPAREL_SHOES_AND_ACCESSORIES in SOUQ_CATEGORY_LIST:
        thread_1 = multiprocessing.Process(target=Apparel_Shoes_and_Accessories_scrape_urls.start_url_collection)
        thread_1.daemon = True
        jobs.append(thread_1)

    if CONSTANTS.ART_CRAFTS_AND_COLLECTIBLES in SOUQ_CATEGORY_LIST:
        thread_2 = multiprocessing.Process(target=Art_Crafts_and_Collectibles_scrape_urls.start_url_collection)
        thread_2.daemon = True
        jobs.append(thread_2)

    if CONSTANTS.BABY in SOUQ_CATEGORY_LIST:
        thread_3 = multiprocessing.Process(target=Baby_scrape_urls.start_url_collection)
        thread_3.daemon = True
        jobs.append(thread_3)

    if CONSTANTS.BEAUTY in SOUQ_CATEGORY_LIST:
        thread_4 = multiprocessing.Process(target=Beauty_scrape_urls.start_url_collection)
        thread_4.daemon = True
        jobs.append(thread_4)

    if CONSTANTS.BED_AND_BATH in SOUQ_CATEGORY_LIST:
        thread_5 = multiprocessing.Process(target=Bed_and_Bath_scrape_urls.start_url_collection)
        thread_5.daemon = True
        jobs.append(thread_5)

    if CONSTANTS.BOOKS in SOUQ_CATEGORY_LIST:
        thread_6 = multiprocessing.Process(target=Books_scrape_urls.start_url_collection)
        thread_6.daemon = True
        jobs.append(thread_6)

    if CONSTANTS.CAMERAS in SOUQ_CATEGORY_LIST:
        thread_7 = multiprocessing.Process(target=Cameras_scrape_urls.start_url_collection)
        thread_7.daemon = True
        jobs.append(thread_7)

    if CONSTANTS.COINS_STAMPS_AND_PAPER_MONEY in SOUQ_CATEGORY_LIST:
        thread_8 = multiprocessing.Process(target=Coins_Stamps_and_Paper_money_scrape_urls.start_url_collection)
        thread_8.daemon = True
        jobs.append(thread_8)

    if CONSTANTS.COMPUTERS_IT_AND_NETWORKING in SOUQ_CATEGORY_LIST:
        thread_9 = multiprocessing.Process(target=Computers_IT_and_Networking_scrape_urls.start_url_collection)
        thread_9.daemon = True
        jobs.append(thread_9)

    if CONSTANTS.ELECTRONICS in SOUQ_CATEGORY_LIST:
        thread_10 = multiprocessing.Process(target=Electronics_scrape_urls.start_url_collection)
        thread_10.daemon = True
        jobs.append(thread_10)

    if CONSTANTS.EYEWEAR_AND_OPTICS in SOUQ_CATEGORY_LIST:
        thread_11 = multiprocessing.Process(target=Eyewear_and_Optics_scrape_urls.start_url_collection)
        thread_11.daemon = True
        jobs.append(thread_11)

    if CONSTANTS.FURNITURE in SOUQ_CATEGORY_LIST:
        thread_12 = multiprocessing.Process(target=Furniture_scrape_urls.start_url_collection)
        thread_12.daemon = True
        jobs.append(thread_12)

    if CONSTANTS.GAMING in SOUQ_CATEGORY_LIST:
        thread_13 = multiprocessing.Process(target=Gaming_scrape_urls.start_url_collection)
        thread_13.daemon = True
        jobs.append(thread_13)

    if CONSTANTS.GARDEN_AND_OUTDOOR in SOUQ_CATEGORY_LIST:
        thread_14 = multiprocessing.Process(target=Garden_and_Outdoor_scrape_urls.start_url_collection)
        thread_14.daemon = True
        jobs.append(thread_14)

    if CONSTANTS.GROCERY_FOOD_AND_BEVERAGES in SOUQ_CATEGORY_LIST:
        thread_15 = multiprocessing.Process(target=Grocery_Food_and_Beverages_scrape_urls.start_url_collection)
        thread_15.daemon = True
        jobs.append(thread_15)

    if CONSTANTS.HEALTH_AND_PERSONAL_CARE in SOUQ_CATEGORY_LIST:
        thread_16 = multiprocessing.Process(target=Health_and_Personal_Care_scrape_urls.start_url_collection)
        thread_16.daemon = True
        jobs.append(thread_16)

    if CONSTANTS.HOME_APPLIANCES in SOUQ_CATEGORY_LIST:
        thread_17 = multiprocessing.Process(target=Home_Appliances_scrape_urls.start_url_collection)
        thread_17.daemon = True
        jobs.append(thread_17)

    if CONSTANTS.HOME_DECOR_AND_FURNITURE in SOUQ_CATEGORY_LIST:
        thread_18 = multiprocessing.Process(target=Home_Decor_and_Furniture_scrape_urls.start_url_collection)
        thread_18.daemon = True
        jobs.append(thread_18)

    if CONSTANTS.JEWELRY_AND_ACCESSORIES in SOUQ_CATEGORY_LIST:
        thread_19 = multiprocessing.Process(target=Jewelry_and_Accessories_scrape_urls.start_url_collection)
        thread_19.daemon = True
        jobs.append(thread_19)

    if CONSTANTS.KITCHEN_AND_HOME_SUPPLIES in SOUQ_CATEGORY_LIST:
        thread_20 = multiprocessing.Process(target=Kitchen_and_Home_Supplies_scrape_urls.start_url_collection)
        thread_20.daemon = True
        jobs.append(thread_20)

    if CONSTANTS.KITCHEN_APPLIANCES in SOUQ_CATEGORY_LIST:
        thread_21 = multiprocessing.Process(target=Kitchen_Appliances_scrape_urls.start_url_collection)
        thread_21.daemon = True
        jobs.append(thread_21)

    if CONSTANTS.MOBILE_PHONES_TABLETS_AND_ACCESSORIES in SOUQ_CATEGORY_LIST:
        thread_22 = multiprocessing.Process(
            target=Mobile_Phones_Tablets_and_Accessories_scrape_urls.start_url_collection)
        thread_22.daemon = True
        jobs.append(thread_22)

    if CONSTANTS.MUSIC_AND_MOVIES in SOUQ_CATEGORY_LIST:
        thread_23 = multiprocessing.Process(target=Music_and_Movies_scrape_urls.start_url_collection)
        thread_23.daemon = True
        jobs.append(thread_23)

    if CONSTANTS.OFFICE_PRODUCTS_AND_SUPPLIES in SOUQ_CATEGORY_LIST:
        thread_24 = multiprocessing.Process(target=Office_Products_and_Supplies_scrape_urls.start_url_collection)
        thread_24.daemon = True
        jobs.append(thread_24)

    if CONSTANTS.PERFUMES_AND_FRAGRANCES in SOUQ_CATEGORY_LIST:
        thread_25 = multiprocessing.Process(target=Perfumes_and_Fragrances_scrape_urls.start_url_collection)
        thread_25.daemon = True
        jobs.append(thread_25)

    if CONSTANTS.PET_FOOD_AND_SUPPLIES in SOUQ_CATEGORY_LIST:
        thread_26 = multiprocessing.Process(target=Pet_Food_and_Supplies_scrape_urls.start_url_collection)
        thread_26.daemon = True
        jobs.append(thread_26)

    if CONSTANTS.SPORTS_AND_FITNESS in SOUQ_CATEGORY_LIST:
        thread_27 = multiprocessing.Process(target=Sports_and_Fitness_scrape_urls.start_url_collection)
        thread_27.daemon = True
        jobs.append(thread_27)

    if CONSTANTS.TOOLS_AND_HOME_IMPROVEMENTS in SOUQ_CATEGORY_LIST:
        thread_28 = multiprocessing.Process(target=Tools_and_Home_Improvements_scrape_urls.start_url_collection)
        thread_28.daemon = True
        jobs.append(thread_28)

    if CONSTANTS.TOYS in SOUQ_CATEGORY_LIST:
        thread_29 = multiprocessing.Process(target=Toys_scrape_urls.start_url_collection)
        thread_29.daemon = True
        jobs.append(thread_29)

    if CONSTANTS.VEHICLE_PARTS_AND_ACCESSORIES in SOUQ_CATEGORY_LIST:
        thread_30 = multiprocessing.Process(target=Vehicle_Parts_and_Accessories_scrape_urls.start_url_collection)
        thread_30.daemon = True
        jobs.append(thread_30)

    if CONSTANTS.VOUCHERS_AND_TICKETS in SOUQ_CATEGORY_LIST:
        thread_31 = multiprocessing.Process(target=Vouchers_and_Tickets_scrape_urls.start_url_collection)
        thread_31.daemon = True
        jobs.append(thread_31)

    if CONSTANTS.WEARABLE_TECHNOLOGY_DEVICES in SOUQ_CATEGORY_LIST:
        thread_32 = multiprocessing.Process(target=Wearable_Technology_Devices_scrape_urls.start_url_collection)
        thread_32.daemon = True
        jobs.append(thread_32)

    for job in jobs:
        job.start()
        #job.join()

    for job in jobs:
        if ( job.is_alive() ):
            job.join()

if __name__ == '__main__':

	start_program()



