import os

path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_Germany/url_collectors'

sample_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_Germany/util_files/url_collector.py'

category_list = [ 'Kleidung_Schuhe_and_Uhren', 'Haushalt_Garten_Baumarkt',
                 'Auto_Motorrad_and_Gewerbe', 'Handmade_and_Amazon_Launchpad', 'Spielzeug_and_Baby',
                 'Sport_and_Freizeit', 'Filme_Serien_Musik_and_Games', 'Elektronik_and_Computer',
                 'Beauty_Drogerie_and_Lebensmittel']
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


