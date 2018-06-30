source_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_US/util/product_parser_1.py'

destination_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_US/product_parsers'

category_list = ['amazon_global', 'books', 'home_garden_and_tools', 'beauty_and_health', 'toys_and_games',
                 'sports_and_outdoor', 'clothing', 'electronics', 'handmade']

file_path = '{}/{}_get_product_info.py'

for category in category_list:
    file_ = open(source_path, 'rt')
    lines = []
    for line in file_:
        lines.append(line)
    write_file = open(file_path.format(destination_path, category), 'w')

    for line in lines:
        write_file.write(line.encode('utf-8'))
