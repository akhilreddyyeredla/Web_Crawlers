import sys
sys.path.insert(0, r'/usr/datacollector')

from info_collectors import informa_tica_y_oficina_info_collector, videojuegos_info_collector, \
    deportes_y_aire_libre_info_collector, electro_nica_info_collector, industria_empresas_y_ciencia_info_collector, \
    coche_y_moto_info_collector, hogar_jardi_n_bricolaje_y_mascotas_info_collector, \
    alimentacio_n_y_bebidas_info_collector, juguetes_y_bebe__info_collector, libros_info_collector, \
    belleza_y_salud_info_collector, cine_tv_y_mu_sica_info_collector, handmade_info_collector, moda_info_collector
from url_collectors import informa_tica_y_oficina_url_collector, videojuegos_url_collector, \
    deportes_y_aire_libre_url_collector, electro_nica_url_collector, industria_empresas_y_ciencia_url_collector, \
    coche_y_moto_url_collector, hogar_jardi_n_bricolaje_y_mascotas_url_collector, alimentacio_n_y_bebidas_url_collector, \
    juguetes_y_bebe__url_collector, libros_url_collector, belleza_y_salud_url_collector, \
    cine_tv_y_mu_sica_url_collector, handmade_url_collector, moda_url_collector
from hierarchy_collectors import informa_tica_y_oficina_hierarchy, videojuegos_hierarchy, \
    deportes_y_aire_libre_hierarchy, electro_nica_hierarchy, industria_empresas_y_ciencia_hierarchy, \
    coche_y_moto_hierarchy, hogar_jardi_n_bricolaje_y_mascotas_hierarchy, alimentacio_n_y_bebidas_hierarchy, \
    juguetes_y_bebe__hierarchy, libros_hierarchy, belleza_y_salud_hierarchy, cine_tv_y_mu_sica_hierarchy, \
    handmade_hierarchy, moda_hierarchy
from CONSTANTS import *
from multiprocessing import Process
from DataCollectors_Configuration import AMAZON_SPAIN_CATEGORY_LIST, START_HIERARCHY_COLLECTION, START_URL_COLLECTION, \
    START_INFO_COLLECTION

category_list = '|'.join(AMAZON_SPAIN_CATEGORY_LIST)


def start_info_collection():
    jobs = []
    if INFORMA_TICA_Y_OFICINA in category_list:
        process_1 = Process(target=informa_tica_y_oficina_info_collector.start_info_collection,
                            args=(INFORMA_TICA_Y_OFICINA,))
        process_1.daemon = True
        jobs.append(process_1)

    if VIDEOJUEGOS in category_list:
        process_2 = Process(target=videojuegos_info_collector.start_info_collection, args=(VIDEOJUEGOS,))
        process_2.daemon = True
        jobs.append(process_2)

    if DEPORTES_Y_AIRE_LIBRE in category_list:
        process_3 = Process(target=deportes_y_aire_libre_info_collector.start_info_collection,
                            args=(DEPORTES_Y_AIRE_LIBRE,))
        process_3.daemon = True
        jobs.append(process_3)

    if ELECTRO_NICA in category_list:
        process_4 = Process(target=electro_nica_info_collector.start_info_collection, args=(ELECTRO_NICA,))
        process_4.daemon = True
        jobs.append(process_4)

    if INDUSTRIA_EMPRESAS_Y_CIENCIA in category_list:
        process_5 = Process(target=industria_empresas_y_ciencia_info_collector.start_info_collection,
                            args=(INDUSTRIA_EMPRESAS_Y_CIENCIA,))
        process_5.daemon = True
        jobs.append(process_5)

    if COCHE_Y_MOTO in category_list:
        process_6 = Process(target=coche_y_moto_info_collector.start_info_collection, args=(COCHE_Y_MOTO,))
        process_6.daemon = True
        jobs.append(process_6)

    if HOGAR_JARDI_N_BRICOLAJE_Y_MASCOTAS in category_list:
        process_7 = Process(target=hogar_jardi_n_bricolaje_y_mascotas_info_collector.start_info_collection,
                            args=(HOGAR_JARDI_N_BRICOLAJE_Y_MASCOTAS,))
        process_7.daemon = True
        jobs.append(process_7)

    if ALIMENTACIO_N_Y_BEBIDAS in category_list:
        process_8 = Process(target=alimentacio_n_y_bebidas_info_collector.start_info_collection,
                            args=(ALIMENTACIO_N_Y_BEBIDAS,))
        process_8.daemon = True
        jobs.append(process_8)

    if JUGUETES_Y_BEBE_ in category_list:
        process_9 = Process(target=juguetes_y_bebe__info_collector.start_info_collection, args=(JUGUETES_Y_BEBE_,))
        process_9.daemon = True
        jobs.append(process_9)

    if LIBROS in category_list:
        process_10 = Process(target=libros_info_collector.start_info_collection, args=(LIBROS,))
        process_10.daemon = True
        jobs.append(process_10)

    if BELLEZA_Y_SALUD in category_list:
        process_11 = Process(target=belleza_y_salud_info_collector.start_info_collection, args=(BELLEZA_Y_SALUD,))
        process_11.daemon = True
        jobs.append(process_11)

    if CINE_TV_Y_MU_SICA in category_list:
        process_12 = Process(target=cine_tv_y_mu_sica_info_collector.start_info_collection, args=(CINE_TV_Y_MU_SICA,))
        process_12.daemon = True
        jobs.append(process_12)

    if HANDMADE in category_list:
        process_13 = Process(target=handmade_info_collector.start_info_collection, args=(HANDMADE,))
        process_13.daemon = True
        jobs.append(process_13)

    if MODA in category_list:
        process_14 = Process(target=moda_info_collector.start_info_collection, args=(MODA,))
        process_14.daemon = True
        jobs.append(process_14)

    for job in jobs:
        job.start()
    for job in jobs:
        if job.is_alive():
            job.join()


def start_url_collection():
    jobs = []
    if INFORMA_TICA_Y_OFICINA in category_list:
        process_1 = Process(target=informa_tica_y_oficina_url_collector.start_program, args=(INFORMA_TICA_Y_OFICINA,))
        process_1.daemon = True
        jobs.append(process_1)

    if VIDEOJUEGOS in category_list:
        process_2 = Process(target=videojuegos_url_collector.start_program, args=(VIDEOJUEGOS,))
        process_2.daemon = True
        jobs.append(process_2)

    if DEPORTES_Y_AIRE_LIBRE in category_list:
        process_3 = Process(target=deportes_y_aire_libre_url_collector.start_program, args=(DEPORTES_Y_AIRE_LIBRE,))
        process_3.daemon = True
        jobs.append(process_3)

    if ELECTRO_NICA in category_list:
        process_4 = Process(target=electro_nica_url_collector.start_program, args=(ELECTRO_NICA,))
        process_4.daemon = True
        jobs.append(process_4)

    if INDUSTRIA_EMPRESAS_Y_CIENCIA in category_list:
        process_5 = Process(target=industria_empresas_y_ciencia_url_collector.start_program,
                            args=(INDUSTRIA_EMPRESAS_Y_CIENCIA,))
        process_5.daemon = True
        jobs.append(process_5)

    if COCHE_Y_MOTO in category_list:
        process_6 = Process(target=coche_y_moto_url_collector.start_program, args=(COCHE_Y_MOTO,))
        process_6.daemon = True
        jobs.append(process_6)

    if HOGAR_JARDI_N_BRICOLAJE_Y_MASCOTAS in category_list:
        process_7 = Process(target=hogar_jardi_n_bricolaje_y_mascotas_url_collector.start_program,
                            args=(HOGAR_JARDI_N_BRICOLAJE_Y_MASCOTAS,))
        process_7.daemon = True
        jobs.append(process_7)

    if ALIMENTACIO_N_Y_BEBIDAS in category_list:
        process_8 = Process(target=alimentacio_n_y_bebidas_url_collector.start_program, args=(ALIMENTACIO_N_Y_BEBIDAS,))
        process_8.daemon = True
        jobs.append(process_8)

    if JUGUETES_Y_BEBE_ in category_list:
        process_9 = Process(target=juguetes_y_bebe__url_collector.start_program, args=(JUGUETES_Y_BEBE_,))
        process_9.daemon = True
        jobs.append(process_9)

    if LIBROS in category_list:
        process_10 = Process(target=libros_url_collector.start_program, args=(LIBROS,))
        process_10.daemon = True
        jobs.append(process_10)

    if BELLEZA_Y_SALUD in category_list:
        process_11 = Process(target=belleza_y_salud_url_collector.start_program, args=(BELLEZA_Y_SALUD,))
        process_11.daemon = True
        jobs.append(process_11)

    if CINE_TV_Y_MU_SICA in category_list:
        process_12 = Process(target=cine_tv_y_mu_sica_url_collector.start_program, args=(CINE_TV_Y_MU_SICA,))
        process_12.daemon = True
        jobs.append(process_12)

    if HANDMADE in category_list:
        process_13 = Process(target=handmade_url_collector.start_program, args=(HANDMADE,))
        process_13.daemon = True
        jobs.append(process_13)

    if MODA in category_list:
        process_14 = Process(target=moda_url_collector.start_program, args=(MODA,))
        process_14.daemon = True
        jobs.append(process_14)

    for job in jobs:
        job.start()
    for job in jobs:
        if job.is_alive():
            job.join()


def start_hierarchy_collection():
    jobs = []
    if INFORMA_TICA_Y_OFICINA in category_list:
        process_1 = Process(target=informa_tica_y_oficina_hierarchy.start_program)
        process_1.daemon = True

        jobs.append(process_1)

    if VIDEOJUEGOS in category_list:
        process_2 = Process(target=videojuegos_hierarchy.start_program)
        process_2.daemon = True

        jobs.append(process_2)

    if DEPORTES_Y_AIRE_LIBRE in category_list:
        process_3 = Process(target=deportes_y_aire_libre_hierarchy.start_program)
        process_3.daemon = True

        jobs.append(process_3)

    if ELECTRO_NICA in category_list:
        process_4 = Process(target=electro_nica_hierarchy.start_program)
        process_4.daemon = True

        jobs.append(process_4)

    if INDUSTRIA_EMPRESAS_Y_CIENCIA in category_list:
        process_5 = Process(target=industria_empresas_y_ciencia_hierarchy.start_program)
        process_5.daemon = True

        jobs.append(process_5)

    if COCHE_Y_MOTO in category_list:
        process_6 = Process(target=coche_y_moto_hierarchy.start_program)
        process_6.daemon = True

        jobs.append(process_6)

    if HOGAR_JARDI_N_BRICOLAJE_Y_MASCOTAS in category_list:
        process_7 = Process(target=hogar_jardi_n_bricolaje_y_mascotas_hierarchy.start_program)
        process_7.daemon = True

        jobs.append(process_7)

    if ALIMENTACIO_N_Y_BEBIDAS in category_list:
        process_8 = Process(target=alimentacio_n_y_bebidas_hierarchy.start_program)
        process_8.daemon = True

        jobs.append(process_8)

    if JUGUETES_Y_BEBE_ in category_list:
        process_9 = Process(target=juguetes_y_bebe__hierarchy.start_program)
        process_9.daemon = True

        jobs.append(process_9)

    if LIBROS in category_list:
        process_10 = Process(target=libros_hierarchy.start_program)
        process_10.daemon = True

        jobs.append(process_10)

    if BELLEZA_Y_SALUD in category_list:
        process_11 = Process(target=belleza_y_salud_hierarchy.start_program)
        process_11.daemon = True

        jobs.append(process_11)

    if CINE_TV_Y_MU_SICA in category_list:
        process_12 = Process(target=cine_tv_y_mu_sica_hierarchy.start_program)
        process_12.daemon = True

        jobs.append(process_12)

    if HANDMADE in category_list:
        process_13 = Process(target=handmade_hierarchy.start_program)
        process_13.daemon = True

        jobs.append(process_13)

    if MODA in category_list:
        process_14 = Process(target=moda_hierarchy.start_program)
        process_14.daemon = True

        jobs.append(process_14)

    for job in jobs:
        job.start()
        job.join()


if __name__ == '__main__':

    if START_HIERARCHY_COLLECTION:
        start_hierarchy_collection()

    if START_URL_COLLECTION:
        start_url_collection()

    if START_INFO_COLLECTION:
        start_info_collection()
