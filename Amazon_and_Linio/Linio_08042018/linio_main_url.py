# -*- encoding: utf-8 -*-

import sys
sys.path.insert(0, r'/home/eunimart/Work/eunimart_dev_pavan/Data_collector')

import response_getter
import DataCollectors_Configuration
from CONSTANTS import *
from url_collectors import belleza_url_collector,celulares_url_collector\
    ,computacion_url_collector,consolas_y_videojuegos_url_collector\
    ,deportes_url_collector,electrodomesticos_url_collector,hogar_url_collector\
    ,juguetes_ninos_y_bebes_url_collector,moda_url_collector\
    ,salud_y_bienestar_url_collector,tv_audio_y_video_url_collector
from multiprocessing import Process


def start_url_program():
    category_list = DataCollectors_Configuration.LINIO_MEX_CATEGORIES

    jobs = []
    if SALUD_Y_BIENESTAR in category_list:
        process_1 = Process(target=salud_y_bienestar_url_collector.start_program, args=(SALUD_Y_BIENESTAR,))
        jobs.append(process_1)

    if HOGAR in category_list:
        process_2 = Process(target=hogar_url_collector.start_program, args=(HOGAR, ))
        jobs.append(process_2)

    if CELULARES in category_list:
        process_3 = Process(target=celulares_url_collector.start_program, args=(CELULARES, ))
        jobs.append(process_3)

    if MODA in category_list:
        process_4 = Process(target=moda_url_collector.start_program, args=(MODA,))
        jobs.append(process_4)

    if DEPORTES in category_list:
        process_5 = Process(target=deportes_url_collector.start_program, args=(DEPORTES,))
        jobs.append(process_5)

    if ELECTRODOMESTICOS in category_list:
        process_6 = Process(target=electrodomesticos_url_collector.start_program, args=(ELECTRODOMESTICOS,))
        jobs.append(process_6)

    if TV_AUDIO_Y_VIDEO in category_list:
        process_7 = Process(target=tv_audio_y_video_url_collector.start_program, args=(TV_AUDIO_Y_VIDEO, ))
        jobs.append(process_7)

    if CONSOLAS_Y_VIDEOJUEGOS in category_list:
        process_8 = Process(target=consolas_y_videojuegos_url_collector.start_program, args=(CONSOLAS_Y_VIDEOJUEGOS,))
        jobs.append(process_8)

    if JUGUETES_NINOS_Y_BEBES in category_list:
        process_9 = Process(target=juguetes_ninos_y_bebes_url_collector.start_program, args=(JUGUETES_NINOS_Y_BEBES, ))
        jobs.append(process_9)

    if BELLEZA in category_list:
        process_10 = Process(target=belleza_url_collector.start_program, args=(BELLEZA, ))
        jobs.append(process_10)

    if COMPUTACION in category_list:

        process_11 = Process(target=computacion_url_collector.start_program, args=(COMPUTACION, ))
        jobs.append(process_11)

    for job in jobs:
        job.start()

    for job in jobs:
        job.join()

if __name__ == '__main__':
    start_url_program()