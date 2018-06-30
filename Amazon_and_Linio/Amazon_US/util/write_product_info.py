path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_US/product_info_collectors'

sample_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_US/util/info_collector.py'

category_list = ['amazon_global', 'books', 'home_garden_and_tools', 'beauty_and_health', 'toys_and_games', 'sports_and_outdoor', 'clothing', 'electronics', 'handmade']

file_path = '{}/{}_info_collector.py'

line_1 = "print('Total_time taken to collect:' + str(total_time))"
Changed_line_1 = "print('Total_time taken to collect {} category products:' + str(total_time) + ' sec') "

line_2 = "CONSTANTS.ACCESSORIES"
Changed_line_2 ="CONSTANTS.{}"

line_3 = 'from product_parsers.accessories_get_product_info import *'
Changed_line_3 = 'from product_parsers.{}_get_product_info import *'

line_4 = "Electronics_url_collection"
Changed_line_4 = '{}_info_collection'

for category in category_list:
    file = open(sample_path,'rt')
    lines = []
    for line in file:
        if line_1 in line:
            lines.append(line.replace(line_1, Changed_line_1.format(category)))
        elif line_2 in line:

            lines.append(line.replace(line_2, Changed_line_2.format(category.upper())))
        elif line_3 in line:

            lines.append(line.replace(line_3, Changed_line_3.format(category)))
        elif line_4 in line:

            lines.append(line.replace(line_4, Changed_line_4.format(category)))
        else:

            lines.append(line)
    write_file =open(file_path.format(path, category),'w')

    for line in lines:
        write_file.write(line.encode('utf-8'))