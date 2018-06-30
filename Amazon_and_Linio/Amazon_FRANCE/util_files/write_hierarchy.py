import os

source_path = '/home/eunimart/Documents/eunimart_dev_pavan/Amazon_FRANCE/util_files/hierarchy.py'

destination_path = '/home/eunimart/Documents/eunimart_dev_pavan/Amazon_FRANCE/hierarchy_collectors'

category_list = ['Beaute__Sante__E_picerie', 'Jouets_Enfants_et_Be_be_s', 'Ve_tements_Chaussures_Bijoux',
                 'Maison_Bricolage_Animalerie', 'High_Tech_et_Informatique', 'Auto_et_Moto', 'Musique_DVD_et_Blu_ray',
                 'Livres_and_Audible', 'Jeux_vide_o_et_Consoles', 'Commerce_Industrie_et_Science', 'Sports_et_Loisirs',
                 'Handmade']


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