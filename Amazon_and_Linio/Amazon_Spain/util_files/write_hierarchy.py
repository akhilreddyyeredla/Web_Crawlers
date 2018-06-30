import os

source_path = '/home/eunimart/Documents/eunimart_dev_pavan/Amazon_Spain/util_files/hierarchy.py'

destination_path = '/home/eunimart/Documents/eunimart_dev_pavan/Amazon_Spain/hierarchy_collectors'

category_list = ['Informa_tica_y_Oficina', 'Videojuegos', 'Deportes_y_aire_libre', 'Electro_nica',
                 'Industria_empresas_y_ciencia', 'Coche_y_moto', 'Hogar_Jardi_n_Bricolaje_y_Mascotas',
                 'Alimentacio_n_y_bebidas', 'Juguetes_y_Bebe_', 'Libros', 'Belleza_y_Salud',
                 'Cine_TV_y_Mu_sica', 'Handmade', 'Moda']

#
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
# print os.listdir('/home/eunimart/Documents/eunimart_dev_pavan/Amazon_Spain/AMAZON_SPAIN_1')