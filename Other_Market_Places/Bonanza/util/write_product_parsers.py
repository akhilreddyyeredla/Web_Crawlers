source_path = '/home/eunimart-04/eunimart_dev_akhil/Bonanza/util/Product_details_parsers.py'

destination_path = '/home/eunimart-04/eunimart_dev_akhil/Bonanza/product_parsers'

CATEGORY_LIST = ['antiques', 'art', 'baby', 'books', 'business', 'cameras', 'cell_phones', \
                 'coins', 'collectibles', 'computers', 'consumer_electronics', 'crafts', \
                 'digital_goods', 'dolls', 'dvds_movies', 'entertainment', 'everything_else', \
                 'fashion', 'health_beauty', 'home_garden', 'jewellery', 'music', 'musical_instruments', \
                 'pet_supplies', 'pottery', 'speciality_services', 'sporting_goods', 'sports_mem', \
                 'stamps', 'tickets', 'toys', 'travel', 'video_games']

file_path = '{}/{}_parser_collector.py'


for category in CATEGORY_LIST:
    file = open(source_path, 'rt')
    lines = []

    for line in file:

            lines.append(line)
    write_file =open(file_path.format(destination_path, category),'w')

    for line in lines:
        write_file.write(line.encode('utf-8'))