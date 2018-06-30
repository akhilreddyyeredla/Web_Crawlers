# coding=utf-8
path = '/home/eunimart-04/eunimart_dev_akhil/Linio/info_collectors'

sample_path = '/home/eunimart-04/eunimart_dev_akhil/Linio/utils/info_collection.py'

category_list = ['Salud_y_Bienestar', 'Hogar', 'Celulares', 'Moda', 'Deportes', 'Electrodomesticos', 'TV_Audio_y_Video', 'Consolas_y_Videojuegos', 'Juguetes_ninos_y_bebes', 'Belleza', 'Computacion']

file_path = '{}/{}_info_collector.py'

line_1 = 'belleza_get_details'
Changed_line_1 = '{}_get_details'

for category in category_list:
    file = open(sample_path,'rt')
    lines = []
    for line in file:
        if line_1 in line:
            lines.append(line.replace(line_1, Changed_line_1.format(category.lower())))
        else:

            lines.append(line)
    write_file =open(file_path.format(path, category.lower()),'w')

    for line in lines:
        write_file.write(line)

    print 'from Linio.product_parsers.{}_get_product_info import ProductDetails  as {}_get_details'.format(category.lower(), category.lower())