import os

path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_Mexico/url_collectors'

sample_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_Mexico/util_files/url_collector.py'

category_list = ['Automotriz_y_Motocicletas', 'Bebe_', 'Co_mputo_y_Tablets', 'Deportes_y_Aire_Libre', 'Electro_nicos',
                 'Handmade', 'Herramientas_y_Mejoras_del_Hogar', 'Hogar_y_Cocina', 'Industria_Empresas_y_Ciencia',
                 'Juegos_y_Juguetes', 'Libros', 'Mascotas_y_Accesorios', 'Peli_culas_Series_de_TV_y_Mu_sica',
                 'Ropa_Zapatos_y_Accesorios', 'Salud_Belleza_y_Cuidado_Personal', 'Software', 'Videojuegos']


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


