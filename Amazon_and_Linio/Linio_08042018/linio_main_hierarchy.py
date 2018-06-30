# -*- encoding: utf-8 -*-

import sys
sys.path.insert(0, r'/home/eunimart-03/eunimart_dev_pavan/Data_collector/Linio_08042018')

import response_getter
import DataCollectors_Configuration
from CONSTANTS import *
from hirerachy_collectors import salud_y_bienestar_hierarchy,belleza_hierarchy,celulares_hierarchy,\
    computacion_hierarchy,consolas_y_videojuegos_hierarchy,deportes_hierarchy,\
    electrodomesticos_hierarchy,hogar_hierarchy,juguetes_ninos_y_bebes_hierarchy,\
    moda_hierarchy ,tv_audio_y_video_hierarchy
from multiprocessing import Process

def get_main_links():
    """

    :return: dictionary with category_name, url
    """
    main_hierarchy_container = response_getter.get_content(MAIN_URL)
    categories = {}
    if main_hierarchy_container:

        categories_container = main_hierarchy_container.find('ul',{'class': 'nav nav-pills nav-stacked menu'})

        if categories_container:
            category_urls = categories_container.find_all('li')
            for category_url in category_urls:
                url = '{}{}'.encode('utf-8').format(MAIN_URL,category_url.a['href'])
                category_name = category_url.a['title'].encode('utf-8').strip().replace(',','').replace(' ','_')
                urls_split = url.split('/')
                line = '{}|{}|{}|{}'.encode('utf-8').format(MARKETPLACE,MAIN_URL, category_name, url)
                if urls_split[-2] == 'c':
                    categories[category_name] = line
                else:
                    continue
    return categories


def start_program():
    category_list = DataCollectors_Configuration.LINIO_MEX_CATEGORIES
    get_main_urls = get_main_links()
    
    jobs = []
    if SALUD_Y_BIENESTAR in category_list:
        key_value = get_main_urls.get(SALUD_Y_BIENESTAR).split('|')
        hierarchy = '|'.join(key_value[0:-1])
        url = key_value[-1]
        process_1 = Process(target=salud_y_bienestar_hierarchy.form_hierarchy,args=(hierarchy, url))
        jobs.append(process_1)
        
    if HOGAR in category_list:
        key_value = get_main_urls.get(HOGAR).split('|')
        hierarchy = '|'.join(key_value[0:-1])
        url = key_value[-1]
        process_2 = Process(target=hogar_hierarchy.form_hierarchy,args=(hierarchy, url))
        jobs.append(process_2)

    if CELULARES in category_list:
        key_value = get_main_urls.get(CELULARES).split('|')
        hierarchy = '|'.join(key_value[0:-1])
        url = key_value[-1]
        process_3 = Process(target=celulares_hierarchy.form_hierarchy, args=(hierarchy, url))
        jobs.append(process_3)

    if MODA in category_list:
        key_value = get_main_urls.get(MODA).split('|')
        hierarchy = '|'.join(key_value[0:-1])
        url = key_value[-1]
        process_4 = Process(target=moda_hierarchy.form_hierarchy, args=(hierarchy, url))
        jobs.append(process_4)

    if DEPORTES in category_list:
        key_value = get_main_urls.get(DEPORTES).split('|')
        hierarchy = '|'.join(key_value[0:-1])
        url = key_value[-1]
        process_5 = Process(target=deportes_hierarchy.form_hierarchy, args=(hierarchy, url))
        jobs.append(process_5)

    if ELECTRODOMESTICOS in category_list:
        key_value = get_main_urls.get(ELECTRODOMESTICOS).split('|')
        hierarchy = '|'.join(key_value[0:-1])
        url = key_value[-1]
        process_6 = Process(target=electrodomesticos_hierarchy.form_hierarchy, args=(hierarchy, url))
        jobs.append(process_6)

    if TV_AUDIO_Y_VIDEO in category_list:
        key_value = get_main_urls.get(TV_AUDIO_Y_VIDEO).split('|')
        hierarchy = '|'.join(key_value[0:-1])
        url = key_value[-1]
        process_7 = Process(target=tv_audio_y_video_hierarchy.form_hierarchy, args=(hierarchy, url))
        jobs.append(process_7)

    if CONSOLAS_Y_VIDEOJUEGOS in category_list:
        key_value = get_main_urls.get(CONSOLAS_Y_VIDEOJUEGOS).split('|')
        hierarchy = '|'.join(key_value[0:-1])
        url = key_value[-1]
        process_8 = Process(target=consolas_y_videojuegos_hierarchy.form_hierarchy, args=(hierarchy, url))
        jobs.append(process_8)

    if JUGUETES_NINOS_Y_BEBES in category_list:
        key_value = get_main_urls.get(JUGUETES_NINOS_Y_BEBES).split('|')
        hierarchy = '|'.join(key_value[0:-1])
        url = key_value[-1]
        process_9 = Process(target=juguetes_ninos_y_bebes_hierarchy.form_hierarchy,args=(hierarchy, url))
        jobs.append(process_9)

    if BELLEZA in category_list:
        key_value = get_main_urls.get(BELLEZA).split('|')
        hierarchy = '|'.join(key_value[0:-1])
        url = key_value[-1]
        process_10 = Process(target=belleza_hierarchy.form_hierarchy, args=(hierarchy, url))
        jobs.append(process_10)

    if COMPUTACION in category_list:
        key_value = get_main_urls.get(COMPUTACION).split('|')
        hierarchy = '|'.join(key_value[0:-1])
        url = key_value[-1]
        process_11 = Process(target=computacion_hierarchy.form_hierarchy, args=(hierarchy, url))
        jobs.append(process_11)

    for job in jobs:
        job.start()

    for job in jobs:
        job.join()


if __name__ == '__main__':
    start_program()