import os

path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_FRANCE/url_collectors'

sample_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_FRANCE/util_files/url_collector.py'

category_list = ['Beaute__Sante__E_picerie', 'Jouets_Enfants_et_Be_be_s', 'Ve_tements_Chaussures_Bijoux',
                 'Maison_Bricolage_Animalerie', 'High_Tech_et_Informatique', 'Auto_et_Moto', 'Musique_DVD_et_Blu_ray',
                 'Livres_and_Audible', 'Jeux_vide_o_et_Consoles', 'Commerce_Industrie_et_Science', 'Sports_et_Loisirs',
                 'Handmade']

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


