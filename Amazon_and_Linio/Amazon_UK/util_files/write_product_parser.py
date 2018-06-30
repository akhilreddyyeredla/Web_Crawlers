source_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_UK/util_files/product_parser_1.py'

destination_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_UK/product_parsers'

category_list = ['Amazon_Pantry', 'Books_and_Audible', 'Business_Industry_and_Science', 'Car_and_Motorbike',
                 'Clothes_Shoes_and_Watches', 'Electronics_and_Computers', 'Handmade', 'Health_and_Beauty',
                 'Home_Garden_Pets_and_DIY', 'Movies_TV_Music_and_Games', 'Sports_and_Outdoors', 'Toys_Children_and_Baby']


file_path = '{}/{}_get_product_info.py'

for category in category_list:
    file_ = open(source_path, 'rt')
    lines = []
    for line in file_:
        lines.append(line)
    write_file = open(file_path.format(destination_path, category.lower()), 'w')

    for line in lines:
        write_file.write(line.encode('utf-8'))
    # line = "{} = '{}'".format(category.upper(),category.lower())
    # print line