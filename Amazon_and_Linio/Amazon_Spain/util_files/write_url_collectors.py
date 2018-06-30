import os

path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_Spain/url_collectors'

sample_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_Spain/util_files/url_collector.py'

category_list = ['Informa_tica_y_Oficina', 'Videojuegos', 'Deportes_y_aire_libre', 'Electro_nica',
                 'Industria_empresas_y_ciencia', 'Coche_y_moto', 'Hogar_Jardi_n_Bricolaje_y_Mascotas',
                 'Alimentacio_n_y_bebidas', 'Juguetes_y_Bebe_', 'Libros', 'Belleza_y_Salud',
                 'Cine_TV_y_Mu_sica', 'Handmade', 'Moda']

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


