import os

source_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_AUS/util_files/product_parser_1.py'

destination_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_AUS/product_parsers'

category_list = ['Health_and_Beauty', 'Electronics_Computers_and_Office', 'Home_Improvement',
                 'Sports_Fitness_and_Outdoors', 'Books_and_Audible', 'Toys_Kids_and_Baby', 'Home_and_Kitchen', 'Fashion']


file_path = '{}/{}_get_product_info.py'
#
for category in category_list:
    file_ = open(source_path, 'rt')
    lines = []
    for line in file_:
        lines.append(line)
    write_file = open(file_path.format(destination_path, category.lower()), 'w')

    for line in lines:
        write_file.write(line.encode('utf-8'))
#     line = "{} = '{}'".format(category.upper(),category)
#     print line
#
# print os.listdir('/home/eunimart/Documents/eunimart_dev_pavan/Amazon_aus/AMAZON_AUSTRALIA_1')