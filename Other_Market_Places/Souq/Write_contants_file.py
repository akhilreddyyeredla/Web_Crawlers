from Common.Souq_common_imports import *

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
    line_1 = "{}_QUEUE_FILE = '{}{}{}{}{}{}{}_link_queue.txt'\n"

    line_2 = "{}_COMPLETED_FILE = '{}{}{}{}{}{}{}_link_completed.txt'\n"

    line_3 = "{}_SKIPPED_FILE = '{}{}{}{}{}{}{}_link_completed.txt'\n\n"

    path = '/usr/datacollector/Souq/path_CONSTANTS.py'

    file = open(path, "w")

    for category in category_list:
        line = "{} = '{}'".format(category.upper(),category)

        CATEGORY = category
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

