
source_path = '/home/eunimart-04/eunimart_dev_akhil/Etsy/util/product_parser.py'

destination_path = '/home/eunimart-04/eunimart_dev_akhil/Etsy/product_parsers'

category_list = ['accessories','art_and_collectibles', 'bags_and_purses', 'bath_and_beauty',
                 'books_movies_and_music', 'clothing', 'craft_supplies_and_tools', 'electronics_and_accessories',
                 'home_and_living', 'jewelry', 'paper_and_party_supplies', 'pet_supplies', 'shoes', 'toys_and_games',
                 'weddings']


file_path = '{}/{}_get_product_info.py'


for category in category_list:
    file = open(source_path,'rt')
    lines = []
    for line in file:

            lines.append(line)
    write_file =open(file_path.format(destination_path, category),'w')

    for line in lines:
        write_file.write(line.encode('utf-8'))
