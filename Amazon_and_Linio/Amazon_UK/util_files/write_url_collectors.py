import os

path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_UK/url_collectors'

sample_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_UK/util_files/url_collector.py'

category_list = ['Amazon_Pantry', 'Books_and_Audible', 'Business_Industry_and_Science', 'Car_and_Motorbike',
                 'Clothes_Shoes_and_Watches', 'Electronics_and_Computers', 'Handmade', 'Health_and_Beauty',
                 'Home_Garden_Pets_and_DIY', 'Movies_TV_Music_and_Games', 'Sports_and_Outdoors', 'Toys_Children_and_Baby']

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


