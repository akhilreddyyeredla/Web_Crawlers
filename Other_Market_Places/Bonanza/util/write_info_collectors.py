source_path = '/home/eunimart-04/eunimart_dev_akhil/Bonanza/util/info_collector.py'

destination_path = '/home/eunimart-04/eunimart_dev_akhil/Bonanza/product_info_collectors'

CATEGORY_LIST = ['antiques', 'art', 'baby', 'books', 'business', 'cameras', 'cell_phones', \
                 'coins', 'collectibles', 'computers', 'consumer_electronics', 'crafts', \
                 'digital_goods', 'dolls', 'dvds_movies', 'entertainment', 'everything_else', \
                 'fashion', 'health_beauty', 'home_garden', 'jewellery', 'music', 'musical_instruments', \
                 'pet_supplies', 'pottery', 'speciality_services', 'sporting_goods', 'sports_mem', \
                 'stamps', 'tickets', 'toys', 'travel', 'video_games']

file_path = '{}/{}_info_collector.py'

line1 = 'starting ANTIQUES information collection'

changed_line1 = 'starting {} information collection'

line2 = "CONSTANTS.ANTIQUES_INFO"

changed_line2 = 'CONSTANTS.{}_INFO'

line3 = "Antiques_info_completed"

changed_line3 = '{}_info_completed'

for category in CATEGORY_LIST:
    file = open(source_path,'rt')
    lines = []
    for line in file:
        if line1 in line:
            lines.append(line.replace(line1, changed_line1.format(category.upper())))
        elif line2 in line:
            lines.append(line.replace(line2, changed_line2.format(category.upper())))

        elif line3 in line:
            lines.append(line.replace(line3,changed_line3.format(category.upper())))
        else:
            lines.append(line)

        path = file_path.format(destination_path, category)
        file = open(path, 'w')
        for line in lines:
            file.write(line)