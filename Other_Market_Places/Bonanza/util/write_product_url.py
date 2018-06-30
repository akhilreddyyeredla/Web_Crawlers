source_path = '/home/eunimart-04/eunimart_dev_akhil/Bonanza/util/Art_Product_URL.py'

destination_path = '/home/eunimart-04/eunimart_dev_akhil/Bonanza/product_url_collectors'

CATEGORY_LIST = ['antiques', 'art', 'baby', 'books', 'business', 'cameras', 'cell_phones', \
                 'coins', 'collectibles', 'computers', 'consumer_electronics', 'crafts', \
                 'digital_goods', 'dolls', 'dvds_movies', 'entertainment', 'everything_else', \
                 'fashion', 'health_beauty', 'home_garden', 'jewellery', 'music', 'musical_instruments', \
                 'pet_supplies', 'pottery', 'speciality_services', 'sporting_goods', 'sports_mem', \
                 'stamps', 'tickets', 'toys', 'travel', 'video_games']

file_path = '{}/{}_url_collector.py'

line1 = '("started Art urls collection")'

changed_line1 = '("started {} urls collection")'

line2 = 'ANTIQUES urls'

changed_line2 = '{} urls :'

for category in CATEGORY_LIST:
    file = open(source_path,'rt')
    lines = []
    for line in file:
        if line1 in line:
            lines.append(line.replace(line1, changed_line1.format(category.upper())))
        elif line2 in lines:
            lines.append(line.replace(line1, changed_line2.format(category.upper())))
        else:
            lines.append(line)
    path = file_path.format(destination_path, category)
    file = open(path, 'w')
    for line in lines:
        file.write(line)
