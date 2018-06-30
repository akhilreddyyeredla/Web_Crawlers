destination_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Etsy/scrappers'

source_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Etsy/util/scrapper.py'

line_1 = "print('Total_time to collect ' + str(total_time))"
Changed_line_1  = "print('Total_time to collect {} Hierarchy ' + str(total_time) + ' sec' )"

line_2 = "print('starting accessores')"
Changed_line_2 = "print('starting {}')"

line_3 = "accessories hierarchy"
Changed_line_3 = "{} hierarchy"

category_list = ['accessories', 'art_and_collectibles', 'bags_and_purses', 'bath_and_beauty', 'books_movies_and_music', 'clothing', 'craft_supplies_and_tools', 'electronics_and_accessories', 'home_and_living', 'jewelry', 'paper_and_party_supplies', 'pet_supplies', 'shoes', 'toys_and_games', 'weddings']

file_path = '{}/{}_scrapper.py'
for category in category_list:
    file = open(source_path,'rt')
    lines = []
    for line in file:
        if line_1 in line:
            lines.append(line.replace(line_1, Changed_line_1.format(category)))
        elif line_2 in line:
            lines.append(line.replace(line_2, Changed_line_2.format(category)))
        elif line_3 in line:
            lines.append(line.replace(line_3, Changed_line_3.format(category)))
        else:

            lines.append(line)
    write_file =open(file_path.format(destination_path, category),'w')

    for line in lines:
        write_file.write(line.encode('utf-8'))
