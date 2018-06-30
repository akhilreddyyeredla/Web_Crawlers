import os

path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_cad/url_collectors'

sample_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_cad/util_files/url_collector.py'

category_list = ['Music', 'Home_Kitchen_and_Pets', 'Clothing_Shoes_and_Jewelry', 'Software',
                 'Health_Beauty_and_Grocery', 'Books_and_Audible', 'Tools_Patio_and_Garden', 'Toys_and_Baby',
                 'Video_Games', 'Automotive_and_Industrial', 'Sports_and_Outdoors', 'Handmade',
                 'Electronics']

file_path = '{}/{}_url_collector.py'

line_1 = 'Electronics_url_collection'
Changed_line_1 = '{}_url_collection'


for category in category_list:
    file = open(sample_path,'rt')
    lines = []
    for line in file:
        if line_1 in line:
            lines.append(line.replace(line_1, Changed_line_1.format(category)))
        else:

            lines.append(line)
    write_file = open(file_path.format(path, category.lower()),'w')

    for line in lines:
        write_file.write(line.encode('utf-8'))


