path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_cad/info_collectors'

sample_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_cad/util_files/info_collector.py'

category_list = ['Music', 'Home_Kitchen_and_Pets', 'Clothing_Shoes_and_Jewelry', 'Software',
                 'Health_Beauty_and_Grocery', 'Books_and_Audible', 'Tools_Patio_and_Garden', 'Toys_and_Baby',
                 'Video_Games', 'Automotive_and_Industrial', 'Sports_and_Outdoors', 'Handmade',
                 'Electronics']

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

            lines.append(line.replace(line_3, Changed_line_3.format(category.lower())))
        elif line_4 in line:

            lines.append(line.replace(line_4, Changed_line_4.format(category)))
        else:

            lines.append(line)
    write_file =open(file_path.format(path, category.lower()),'w')

    for line in lines:
        write_file.write(line.encode('utf-8'))