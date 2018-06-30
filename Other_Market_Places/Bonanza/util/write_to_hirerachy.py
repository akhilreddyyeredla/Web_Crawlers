source_path = '/home/eunimart-04/eunimart_dev_akhil/Bonanza/util/Music_get_hirerachy.py'

destination_path = '/home/eunimart-04/eunimart_dev_akhil/Bonanza/hierarchy_collectors'

CATEGORY_LIST = ['antiques','art','baby','books','business','cameras','cell_phones',\
'coins','collectibles','computers','consumer_electronics','crafts',\
'digital_goods','dolls','dvds_movies','entertainment','everything_else',\
'fashion','health_beauty','home_garden','jewellery','music','musical_instruments',\
'pet_supplies','pottery','speciality_services','sporting_goods','sports_mem',\
'stamps','tickets','toys','travel','video_games']

file_path = '{}/{}_hierarchy_collector.py'

line1 = '[CONSTANTS.ANTIQUES_INDEX]'

changed_line_1 = '[CONSTANTS.{}_INDEX]'

line2 = 'antiques Hierarchy Started'
changed_line_2 = '{} Hierarchy Started'

line3 = 'Antiques Hierarchy'
changed_line_3 = '{} Hierarchy'
for category in CATEGORY_LIST:
    file = open(source_path,'rt')
    lines = []
    for line in file:
        if line1 in line:
            lines.append(line.replace(line1, changed_line_1.format(category.upper())))
        else:
            lines.append(line)
    path = file_path.format(destination_path,category)
    file = open(path,'w')
    for line in lines:
        file.write(line)
