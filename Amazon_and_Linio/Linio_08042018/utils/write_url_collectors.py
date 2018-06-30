# coding=utf-8
import os

path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Linio/url_collectors'

sample_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Linio/utils/url_collector.py'

category_list = category_list = ['Salud_y_Bienestar', 'Hogar', 'Celulares', 'Moda', 'Deportes', 'Electrodomesticos', 'TV_Audio_y_Video', 'Consolas_y_Videojuegos', 'Juguetes_ninos_y_bebes', 'Belleza', 'Computacion']

file_path = '{}/{}_url_collector.py'


for category in category_list:
    file = open(sample_path,'rt')
    lines = []
    for line in file:
        lines.append(line)
    write_file = open(file_path.format(path, category.lower()),'w')

    for line in lines:
        write_file.write(line.encode('utf-8'))


