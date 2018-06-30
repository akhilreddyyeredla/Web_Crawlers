
path = '/home/eunimart-04/eunimart_dev_akhil/Etsy/product_info_collectors'

sample_path = '/home/eunimart-04/eunimart_dev_akhil/Etsy/util/products_info_collector.py'

category_list = ['accessories', 'art_and_collectibles', 'bags_and_purses', 'bath_and_beauty', 'books_movies_and_music', 'clothing', 'craft_supplies_and_tools', 'electronics_and_accessories', 'home_and_living', 'jewelry', 'paper_and_party_supplies', 'pet_supplies', 'shoes', 'toys_and_games', 'weddings']

file_path = '{}/{}_products_info_collector.py'

line_1 = 'accessories category products:'
Changed_line_1 = '{} category products:'

line_2 = "CONSTANTS.ACCESSORIES"
Changed_line_2 ="CONSTANTS.{}"

# line_3 = 'from product_parsers.jewelry_get_product_info import *'
# Changed_line_3 = 'from product_parsers.{}_get_product_info import *'
#
line_4 = "starting accessories information collection"
Changed_line_4 = "starting {} information collection"

for category in category_list:
    file = open(sample_path,'rt')
    lines = []
    for line in file:
        if line_1 in line:
            lines.append(line.replace(line_1, Changed_line_1.format(category)))
        elif line_2 in line:

            lines.append(line.replace(line_2, Changed_line_2.format(category.upper())))
        # elif line_3 in line:
        #
        #     lines.append(line.replace(line_3, Changed_line_3.format(category)))
        elif line_4 in line:

            lines.append(line.replace(line_4, Changed_line_4.format(category)))
        else:

            lines.append(line)
    write_file =open(file_path.format(path, category),'w')

    for line in lines:
        write_file.write(line.encode('utf-8'))
