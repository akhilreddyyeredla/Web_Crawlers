import os

source_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_cad/util_files/product_parser_1.py'

destination_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_cad/product_parsers'

category_list = ['Music', 'Home_Kitchen_and_Pets', 'Clothing_Shoes_and_Jewelry', 'Software',
                 'Health_Beauty_and_Grocery', 'Books_and_Audible', 'Tools_Patio_and_Garden', 'Toys_and_Baby',
                 'Video_Games', 'Automotive_and_Industrial', 'Sports_and_Outdoors', 'Handmade',
                 'Electronics']


file_path = '{}/{}_get_product_info.py'

for category in category_list:
    file_ = open(source_path, 'rt')
    lines = []
    for line in file_:
        lines.append(line)
    write_file = open(file_path.format(destination_path, category.lower()), 'w')

    for line in lines:
        write_file.write(line.encode('utf-8'))
    # line = "{} = '{}'".format(category.upper(),category)
    # print line

# print os.listdir('/home/eunimart/Documents/eunimart_dev_pavan/Amazon_canada/AMAZON_CANADA_1')