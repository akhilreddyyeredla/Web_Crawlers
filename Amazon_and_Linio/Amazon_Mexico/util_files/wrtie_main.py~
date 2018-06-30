import os

source_path = '/home/eunimart/Documents/eunimart_dev_pavan/Amazon_Mexico/main.py'


category_list = ['Automotriz_y_Motocicletas', 'Bebe_', 'Co_mputo_y_Tablets', 'Deportes_y_Aire_Libre', 'Electro_nicos',
                 'Handmade', 'Herramientas_y_Mejoras_del_Hogar', 'Hogar_y_Cocina', 'Industria_Empresas_y_Ciencia',
                 'Juegos_y_Juguetes', 'Libros', 'Mascotas_y_Accesorios', 'Peli_culas_Series_de_TV_y_Mu_sica',
                 'Ropa_Zapatos_y_Accesorios', 'Salud_Belleza_y_Cuidado_Personal', 'Software', 'Videojuegos']


line = 'from url_collectors import'
line_1 = '{}_url_collector,'
line_2 = ''
for category in category_list:
    line_2 = line_2+line_1.format(category.lower())

print(line_2)

line = 'from info_collectors import'
line_1 = '{}_info_collector,'
line_2 = ''
for category in category_list:
    line_2 = line_2+line_1.format(category.lower())

print(line_2)

line = 'from hierarchy_collectors import'
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



