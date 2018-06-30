import os

path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_AUS/url_collectors'

sample_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_AUS/util_files/url_collector.py'

category_list = ['Health_and_Beauty', 'Electronics_Computers_and_Office', 'Home_Improvement',
                 'Sports_Fitness_and_Outdoors', 'Books_and_Audible', 'Toys_Kids_and_Baby', 'Home_and_Kitchen', 'Fashion']

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


