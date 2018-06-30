import os

path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_Italy/url_collectors'

sample_path = '/home/eunimart/Work/eunimart_dev_pavan/Data_collector/Amazon_Italy/util_files/url_collector.py'

category_list = ['Musica_Film_e_TV', 'Videogiochi_e_Console', 'Alimentari_e_Cura_della_casa',
                 'Elettronica_e_Informatica', 'Commercio_Industria_e_Scienza', 'Sport_e_tempo_libero',
                 'Libri_e_Audible', 'Casa_Giardino_Fai_da_te_e_Animali', 'Giochi_e_Prima_infanzia',
                 'Bellezza_e_Salute', 'Abbigliamento_Scarpe_e_Gioielli', 'Auto_e_Moto',
                 'Handmade']

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


