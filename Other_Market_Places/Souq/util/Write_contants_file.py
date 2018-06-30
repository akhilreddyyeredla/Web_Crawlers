import fnmatch
import os

import DataCollectors_Configuration

category_list = ['Apparel_Shoes_and_Accessories', 'Art_Crafts_and_Collectibles', 'Baby', 'Beauty', 'Bed_and_Bath',
                 'Books',
                 'Cameras', 'Coins_Stamps_and_Paper_money', 'Computers_IT_and_Networking', 'Electronics',
                 'Eyewear_and_Optics', 'Furniture', 'Gaming', 'Garden_and_Outdoor', 'Grocery_Food_and_Beverages',
                 'Health_and_Personal_Care', 'Home_Appliances', 'Home_Decor_and_Furniture', 'Jewelry_and_Accessories',
                 'Kitchen_and_Home_Supplies', 'Kitchen_Appliances', 'Mobile_Phones_Tablets_and_Accessories',
                 'Music_and_Movies', 'Office_Products_and_Supplies', 'Perfumes_and_Fragrances', 'Pet_Food_and_Supplies',
                 'Sports_and_Fitness', 'Tools_and_Home_Improvements', 'Toys', 'Vehicle_Parts_and_Accessories',
                 'Vouchers_and_Tickets', 'Wearable_Technology_Devices']


def write_path():
    line_1 = "{}_QUEUE_PATH = '{}{}{}{}{}{}products_page_links.txt'\n"

    line_2 = "{}_COMPLETED_PATH = '{}{}{}{}{}{}sub_sub_category_completed_{}.txt '\n"

    line_3 = "{}_SKIPPED_PATH = '{}{}{}{}{}{}skipped_queue_{}.txt'\n\n"

    path = 'path_CONSTANTS.py'

    file = open(path, "w")

    for category in category_list:
        line = "{} = '{}'".format(category.upper(),category)

        CATEGORY = category.upper()
        file.write(line_1.format(CATEGORY,
                                 DataCollectors_Configuration.ROOT_FOLDER,
                                 DataCollectors_Configuration.PATH_STYLE,
                                 DataCollectors_Configuration.SOUQ_PROJECT_NAME,
                                 DataCollectors_Configuration.PATH_STYLE,
                                 category,
                                 DataCollectors_Configuration.PATH_STYLE,
                                 category))
        file.write(line_2.format(CATEGORY,
                                 DataCollectors_Configuration.ROOT_FOLDER,
                                 DataCollectors_Configuration.PATH_STYLE,
                                 DataCollectors_Configuration.SOUQ_PROJECT_NAME,
                                 DataCollectors_Configuration.PATH_STYLE,
                                 category,
                                 DataCollectors_Configuration.PATH_STYLE,
                                 category))
        file.write(line_3.format(CATEGORY,
                                 DataCollectors_Configuration.ROOT_FOLDER,
                                 DataCollectors_Configuration.PATH_STYLE,
                                 DataCollectors_Configuration.SOUQ_PROJECT_NAME,
                                 DataCollectors_Configuration.PATH_STYLE,
                                 category,
                                 DataCollectors_Configuration.PATH_STYLE,
                                 category))

write_path()