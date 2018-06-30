import os

line_1 = 'products_page_url_queue_file = path_CONSTANTS.ACCESSORIES_QUEUE_PATH'
Changed_line_1 = 'products_page_url_queue_file = path_CONSTANTS.{}_QUEUE_PATH'

line_2 = 'products_page_url_completed_file = path_CONSTANTS.ACCESSORIES_COMPLETED_PATH'
Changed_line_2 = 'products_page_url_completed_file = path_CONSTANTS.{}_COMPLETED_PATH'

line_3 = 'products_page_url_skipped_file = path_CONSTANTS.ACCESSORIES_SKIPPED_PATH'
Changed_line_3 = 'products_page_url_skipped_file = path_CONSTANTS.{}_SKIPPED_PATH'

line_4 = 'products_page_url_skipped_file = path_CONSTANTS.ACESSORIES_SKIPPED_PATH'
Changed_line_4 = 'products_page_url_skipped_file = path_CONSTANTS.{}_SKIPPED_PATH'

line_5 = "Total_time taken to collect ACCESSORIES category urls"
Changed_line_5 = "Total_time taken to collect {} category urls"

line_6 = "starting ACCESSORIES product url collection"
Changed_line_6 = "starting {} product url collection"

category_list = ['accessories', 'art_and_collectibles', 'bags_and_purses', 'bath_and_beauty', 'books_movies_and_music', 'clothing', 'craft_supplies_and_tools', 'electronics_and_accessories', 'home_and_living', 'jewelry', 'paper_and_party_supplies', 'pet_supplies', 'shoes', 'toys_and_games', 'weddings']

path = '/home/eunimart-04/eunimart_dev_akhil/Etsy/product_urls_collectors'

sample_file_path = '/home/eunimart-04/eunimart_dev_akhil/Etsy/util/products_url_collector.py'

file_name = '{}_products_url_collector.py'

for category in category_list:
    file = open(sample_file_path,'rt')
    lines = []
    for line in file:
        if line_1 in line:
            lines.append(line.replace(line_1,Changed_line_1.format(category.upper())))
        elif line_2 in line:
            lines.append(line.replace(line_2, Changed_line_2.format(category.upper())))
        elif line_3 in line:
            lines.append(line.replace(line_3, Changed_line_3.format(category.upper())))
        elif line_4 in line:
            lines.append(line.replace(line_4, Changed_line_4.format(category.upper())))
        elif line_5 in line:
            lines.append(line.replace(line_5, Changed_line_5.format(category.upper())))
        elif line_6 in line:
            lines.append(line.replace(line_6, Changed_line_6.format(category.upper())))
        else:
            lines.append(line)
    write_file = open('{}/{}'.format(path, file_name.format(category)), 'w')
    for line in lines:
        write_file.write(line.encode('utf-8'))


