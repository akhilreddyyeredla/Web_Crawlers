import os

source_path = '/home/eunimart/Documents/eunimart_dev_pavan/Amazon_Italy/util_files/hierarchy.py'

destination_path = '/home/eunimart/Documents/eunimart_dev_pavan/Amazon_Italy/hierarchy_collectors'

category_list = ['Musica_Film_e_TV', 'Videogiochi_e_Console', 'Alimentari_e_Cura_della_casa',
                 'Elettronica_e_Informatica', 'Commercio_Industria_e_Scienza', 'Sport_e_tempo_libero',
                 'Libri_e_Audible', 'Casa_Giardino_Fai_da_te_e_Animali', 'Giochi_e_Prima_infanzia',
                 'Bellezza_e_Salute', 'Abbigliamento_Scarpe_e_Gioielli', 'Auto_e_Moto',
                 'Handmade']


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