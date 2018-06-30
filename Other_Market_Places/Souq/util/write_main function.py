
source_path = '/home/pavan/PycharmProjects/Souq_1/main.py'


category_list = ['Apparel_Shoes_and_Accessories', 'Art_Crafts_and_Collectibles', 'Baby', 'Beauty', 'Bed_and_Bath',
                 'Books',
                 'Cameras', 'Coins_Stamps_and_Paper_money', 'Computers_IT_and_Networking', 'Electronics',
                 'Eyewear_and_Optics', 'Furniture', 'Gaming', 'Garden_and_Outdoor', 'Grocery_Food_and_Beverages',
                 'Health_and_Personal_Care', 'Home_Appliances', 'Home_Decor_and_Furniture', 'Jewelry_and_Accessories',
                 'Kitchen_and_Home_Supplies', 'Kitchen_Appliances', 'Mobile_Phones_Tablets_and_Accessories',
                 'Music_and_Movies', 'Office_Products_and_Supplies', 'Perfumes_and_Fragrances', 'Pet_Food_and_Supplies',
                 'Sports_and_Fitness', 'Tools_and_Home_Improvements', 'Toys', 'Vehicle_Parts_and_Accessories',
                 'Vouchers_and_Tickets', 'Wearable_Technology_Devices']


import Souq.CONSTANTS
from Souq.config import CATEGORY_LIST
import_line = 'from scrappers '
line_1 = ' {}_scrape_urls,'
line_2 = '{}_info_collector,'

writing_line_1 = 'from scrappers import'
writing_line_2 = 'from product_info_collectors import '

file = open(source_path,'w')
for category in category_list:
    writing_line_1 = writing_line_1 + line_1.format(category)
    writing_line_2 = writing_line_2 + line_2.format(category)
file.write(writing_line_1 + '\n')
file.write(writing_line_2+'\n')
file.write('import config')

count = 1
for category in category_list:
    line_3 = '    if CONSTANTS.{} in CATEGORY_LIST:\n'.format(category.upper())
    line_4 = "                                     \n"
    line_5 = "        thread_{} = multiprocessing.Process(target = {}_info_collector. start_info_collection)\n".format(count,
                                                                                                                  category)
    line_6 = "        thread_{}.daemon = True\n".format(count)
    line_7 = "        jobs.append(thread_{})\n\n".format(count)
    count = count + 1
    file.write(line_3)
    file.write(line_4)
    file.write(line_5)
    file.write(line_6)
    file.write(line_7)


count = 1
for category in category_list:

    line_3 = '    if CONSTANTS.{} in CATEGORY_LIST:\n'.format(category.upper())
    line_4 = "                                     \n"
    line_5 = "        thread_{} = multiprocessing.Process(target = {}_scrape_urls.start_url_collection)\n".format(count,category)
    line_6 = "        thread_{}.daemon = True\n".format(count)
    line_7 = "        jobs.append(thread_{})\n\n".format(count)
    count = count + 1
    file.write(line_3)
    file.write(line_4)
    file.write(line_5)
    file.write(line_6)
    file.write(line_7)

"""

import CONSTANTS
from config import CATEGORY_LIST
import multiprocessing


def start_product_url_collection():
    category_list = '|'.join(CATEGORY_LIST)
    jobs = []
"""
