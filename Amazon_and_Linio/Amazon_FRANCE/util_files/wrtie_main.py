import os

source_path = '/home/eunimart/Documents/eunimart_dev_pavan/Amazon_FRANCE/main.py'


category_list = ['Beaute__Sante__E_picerie', 'Jouets_Enfants_et_Be_be_s', 'Ve_tements_Chaussures_Bijoux',
                 'Maison_Bricolage_Animalerie', 'High_Tech_et_Informatique', 'Auto_et_Moto', 'Musique_DVD_et_Blu_ray',
                 'Livres_and_Audible', 'Jeux_vide_o_et_Consoles', 'Commerce_Industrie_et_Science', 'Sports_et_Loisirs',
                 'Handmade']


line = 'from url_collectors import'
line_1 = '{}_info_collector,'
line_2 = ''
for category in category_list:
    line_2 = line_2+line_1.format(category.lower())

print(line_2)
# file = open(source_path,'w')
# count =1
# for category in category_list:
#     line_2 ='   if {} in category_list:\n'.format(category.upper())
#     line_3 ='       thread_{} = Thread(target={}_info_collector.start_info_collection, args=({},))\n'.format(count, category.lower(),category.upper())
#     line_4 ='       thread_{}.daemon = True\n'.format(count)
#     line_5 ='       jobs.append(thread_{})\n\n'.format(count)
#     count = count+1
#     file.write(line_2)
#     file.write(line_3)
#     file.write(line_4)
#     file.write(line_5)
# count =1
# for category in category_list:
#     line_2 ='     if {} in category_list:\n'.format(category.upper())
#     line_3 ='         thread_{} = Thread(target={}_url_collector.start_program, args=({},))\n'.format(count,category.lower(),category.upper())
#     line_4 ='         thread_{}.daemon = True\n'.format(count)
#     line_5 ='         jobs.append(thread_{})\n\n'.format(count)
#     count = count +1
#     file.write(line_2)
#     file.write(line_3)
#     file.write(line_4)
#     file.write(line_5)
#
# count =1
# for category in category_list:
#     line_2 ='   if {} in category_list:\n'.format(category.upper())
#     line_3 ='       thread_{} = Thread(target={}_hierarchy.start_program)\n'.format(count,category.lower())
#     line_4 ='       thread_{}.daemon = True\n\n'.format(count)
#     line_5 ='       jobs.append(thread_{})\n\n'.format(count)
#     count = count + 1
#     file.write(line_2)
#     file.write(line_3)
#     file.write(line_4)
#     file.write(line_5)



