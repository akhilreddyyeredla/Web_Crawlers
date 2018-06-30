import os

source_path = '/home/eunimart/Documents/eunimart_dev_pavan/Amazon_Mexico/util_files/hierarchy.py'

destination_path = '/home/eunimart/Documents/eunimart_dev_pavan/Amazon_Mexico/hierarchy_collectors'

category_list = ['Automotriz_y_Motocicletas', 'Bebe_', 'Co_mputo_y_Tablets', 'Deportes_y_Aire_Libre', 'Electro_nicos',
                 'Handmade', 'Herramientas_y_Mejoras_del_Hogar', 'Hogar_y_Cocina', 'Industria_Empresas_y_Ciencia',
                 'Juegos_y_Juguetes', 'Libros', 'Mascotas_y_Accesorios', 'Peli_culas_Series_de_TV_y_Mu_sica',
                 'Ropa_Zapatos_y_Accesorios', 'Salud_Belleza_y_Cuidado_Personal', 'Software', 'Videojuegos']



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