import os

source_path = '/home/eunimart/Documents/eunimart_dev_pavan/Amazon_Spain/main.py'


category_list = ['Informa_tica_y_Oficina', 'Videojuegos', 'Deportes_y_aire_libre', 'Electro_nica',
                 'Industria_empresas_y_ciencia', 'Coche_y_moto', 'Hogar_Jardi_n_Bricolaje_y_Mascotas',
                 'Alimentacio_n_y_bebidas', 'Juguetes_y_Bebe_', 'Libros', 'Belleza_y_Salud',
                 'Cine_TV_y_Mu_sica', 'Handmade', 'Moda']

#
line = 'from url_collectors import'
line_1 = '{}_url_collector,'
line_3 = '{}_hierarchy,'
line_2 = ''
line_4 = ''
for category in category_list:
    line_2 = line_2+line_1.format(category.lower())
    line_4 = line_4 + line_3.format(category.lower())
print(line_2)
print line_4
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
#
#
#
