import os

source_path = '/home/eunimart/Documents/eunimart_dev_pavan/Amazon_Italy/main.py'


category_list = ['Musica_Film_e_TV', 'Videogiochi_e_Console', 'Alimentari_e_Cura_della_casa',
                 'Elettronica_e_Informatica', 'Commercio_Industria_e_Scienza', 'Sport_e_tempo_libero',
                 'Libri_e_Audible', 'Casa_Giardino_Fai_da_te_e_Animali', 'Giochi_e_Prima_infanzia',
                 'Bellezza_e_Salute', 'Abbigliamento_Scarpe_e_Gioielli', 'Auto_e_Moto',
                 'Handmade']


line = 'from url_collectors import'
line_1 = '{}_hierarchy,'
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



