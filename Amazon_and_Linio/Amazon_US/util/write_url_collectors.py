path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_US/url_collectors'

sample_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_US/util/url_collector.py'

category_list = ['amazon_global', 'books', 'home_garden_and_tools', 'beauty_and_health', 'toys_and_games', 'sports_and_outdoor', 'clothing', 'electronics', 'handmade']

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
    write_file =open(file_path.format(path, category),'w')

    for line in lines:
        write_file.write(line.encode('utf-8'))