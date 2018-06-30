path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_Spain/info_collectors'

sample_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_Spain/util_files/info_collector.py'

category_list = ['Informa_tica_y_Oficina', 'Videojuegos', 'Deportes_y_aire_libre', 'Electro_nica',
                 'Industria_empresas_y_ciencia', 'Coche_y_moto', 'Hogar_Jardi_n_Bricolaje_y_Mascotas',
                 'Alimentacio_n_y_bebidas', 'Juguetes_y_Bebe_', 'Libros', 'Belleza_y_Salud',
                 'Cine_TV_y_Mu_sica', 'Handmade', 'Moda']

file_path = '{}/{}_info_collector.py'

line_1 = "print('Total_time taken to collect:' + str(total_time))"
Changed_line_1 = "print('Total_time taken to collect {} category products:' + str(total_time) + ' sec') "

line_2 = "CONSTANTS.ACCESSORIES"
Changed_line_2 ="CONSTANTS.{}"

line_3 = 'from product_parsers.accessories_get_product_info import *'
Changed_line_3 = 'from product_parsers.{}_get_product_info import *'

line_4 = "Electronics_url_collection"
Changed_line_4 = '{}_info_collection'

for category in category_list:
    file = open(sample_path,'rt')
    lines = []
    for line in file:
        if line_1 in line:
            lines.append(line.replace(line_1, Changed_line_1.format(category)))
        elif line_2 in line:

            lines.append(line.replace(line_2, Changed_line_2.format(category.upper())))
        elif line_3 in line:

            lines.append(line.replace(line_3, Changed_line_3.format(category.lower())))
        elif line_4 in line:

            lines.append(line.replace(line_4, Changed_line_4.format(category)))
        else:

            lines.append(line)
    write_file =open(file_path.format(path, category.lower()),'w')

    for line in lines:
        write_file.write(line.encode('utf-8'))