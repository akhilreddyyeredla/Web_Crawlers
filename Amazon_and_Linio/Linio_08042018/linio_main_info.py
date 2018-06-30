# -*- encoding: utf-8 -*-

import sys
sys.path.insert(0, r'/home/eunimart/Work/eunimart_dev_pavan/Data_collector')

import response_getter
import DataCollectors_Configuration
from CONSTANTS import *
from info_collectors import belleza_info_collector,celulares_info_collector\
    ,computacion_info_collector,consolas_y_videojuegos_info_collector,deportes_info_collector\
    ,electrodomesticos_info_collector,hogar_info_collector\
    ,juguetes_ninos_y_bebes_info_collector,moda_info_collector,salud_y_bienestar_info_collector\
    ,tv_audio_y_video_info_collector
from multiprocessing import Process


def start_info_program():
    category_list = DataCollectors_Configuration.LINIO_MEX_CATEGORIES

    jobs = []
    if SALUD_Y_BIENESTAR in category_list:
        process_1 = Process(target=salud_y_bienestar_info_collector.start_program, args=(SALUD_Y_BIENESTAR,))
        jobs.append(process_1)

    if HOGAR in category_list:
        process_2 = Process(target=hogar_info_collector.start_program, args=(HOGAR, ))
        jobs.append(process_2)

    if CELULARES in category_list:
        process_3 = Process(target=celulares_info_collector.start_program, args=(CELULARES, ))
        jobs.append(process_3)

    if MODA in category_list:
        process_4 = Process(target=moda_info_collector.start_program, args=(MODA,))
        jobs.append(process_4)

    if DEPORTES in category_list:
        process_5 = Process(target=deportes_info_collector.start_program, args=(DEPORTES,))
        jobs.append(process_5)

    if ELECTRODOMESTICOS in category_list:
        process_6 = Process(target=electrodomesticos_info_collector.start_program, args=(ELECTRODOMESTICOS,))
        jobs.append(process_6)

    if TV_AUDIO_Y_VIDEO in category_list:
        process_7 = Process(target=tv_audio_y_video_info_collector.start_program, args=(TV_AUDIO_Y_VIDEO, ))
        jobs.append(process_7)

    if CONSOLAS_Y_VIDEOJUEGOS in category_list:
        process_8 = Process(target=consolas_y_videojuegos_info_collector.start_program, args=(CONSOLAS_Y_VIDEOJUEGOS,))
        jobs.append(process_8)

    if JUGUETES_NINOS_Y_BEBES in category_list:
        process_9 = Process(target=juguetes_ninos_y_bebes_info_collector.start_program, args=(JUGUETES_NINOS_Y_BEBES, ))
        jobs.append(process_9)

    if BELLEZA in category_list:
        process_10 = Process(target=belleza_info_collector.start_program, args=(BELLEZA, ))
        jobs.append(process_10)

    if COMPUTACION in category_list:

        process_11 = Process(target=computacion_info_collector.start_program, args=(COMPUTACION, ))
        jobs.append(process_11)

    for job in jobs:
        job.start()

    for job in jobs:
        job.join()


if __name__ == '__main__':
    start_info_program()