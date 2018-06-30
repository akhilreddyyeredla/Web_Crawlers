# coding=utf-8
import os

source_path = '/home/eunimart-04/eunimart_dev_akhil/Linio/utils/product_parser.py'

destination_path = '/home/eunimart-04/eunimart_dev_akhil/Linio/product_parsers'

category_list = ['Salud_y_Bienestar', 'Hogar', 'Celulares', 'Moda', 'Deportes', 'Electrodomesticos', 'TV_Audio_y_Video', 'Consolas_y_Videojuegos', 'Juguetes_ninos_y_bebes', 'Belleza', 'Computacion']


file_path = '{}/{}_get_product_info.py'
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
# #
#     print 'from Linio.product_parsers.{}_get_product_info import ProductDetails as {}_get_details'.format(category.lower(), category.lower())
# print os.listdir('/home/eunimart/Documents/eunimart_dev_pavan/Amazon_FRANCE/AMAZON_FRANCE_1')