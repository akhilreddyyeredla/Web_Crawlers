import os

source_path = '/home/eunimart/Documents/eunimart_dev_pavan/Amazon_Germany/util_files/hierarchy.py'

destination_path = '/home/eunimart/Documents/eunimart_dev_pavan/Amazon_Germany/hierarchy_collectors'

category_list = [ 'Kleidung_Schuhe_and_Uhren', 'Haushalt_Garten_Baumarkt',
                 'Auto_Motorrad_and_Gewerbe', 'Handmade_and_Amazon_Launchpad', 'Spielzeug_and_Baby',
                 'Sport_and_Freizeit', 'Filme_Serien_Musik_and_Games', 'Elektronik_and_Computer',
                 'Beauty_Drogerie_and_Lebensmittel']

file_path = '{}/{}_hierarchy.py'
#
for category in category_list:
    file_ = open(source_path, 'rt')
    lines = []
    for line in file_:
        lines.append(line)
    write_file = open(file_path.format(destination_path, category.lower()), 'w')

    for line in lines:
        write_file.write(line.encode('utf-8'))
    # line = "{} = '{}'".format(category.upper(),category)
    # print line
#
# print os.listdir('/home/eunimart/Documents/eunimart_dev_pavan/Amazon_aus/AMAZON_AUSTRALIA_1')