import sys
sys.path.insert(0, r'/usr/datacollector')

from url_collectors import automotriz_y_motocicletas_url_collector, bebe__url_collector, \
    co_mputo_y_tablets_url_collector, deportes_y_aire_libre_url_collector, electro_nicos_url_collector, \
    handmade_url_collector, herramientas_y_mejoras_del_hogar_url_collector, hogar_y_cocina_url_collector, \
    industria_empresas_y_ciencia_url_collector, juegos_y_juguetes_url_collector, libros_url_collector, \
    mascotas_y_accesorios_url_collector, peli_culas_series_de_tv_y_mu_sica_url_collector, \
    ropa_zapatos_y_accesorios_url_collector, salud_belleza_y_cuidado_personal_url_collector, software_url_collector, \
    videojuegos_url_collector
from info_collectors import automotriz_y_motocicletas_info_collector, bebe__info_collector, \
    co_mputo_y_tablets_info_collector, deportes_y_aire_libre_info_collector, electro_nicos_info_collector, \
    handmade_info_collector, herramientas_y_mejoras_del_hogar_info_collector, hogar_y_cocina_info_collector, \
    industria_empresas_y_ciencia_info_collector, juegos_y_juguetes_info_collector, libros_info_collector, \
    mascotas_y_accesorios_info_collector, peli_culas_series_de_tv_y_mu_sica_info_collector, \
    ropa_zapatos_y_accesorios_info_collector, salud_belleza_y_cuidado_personal_info_collector, software_info_collector, \
    videojuegos_info_collector
from hierarchy_collectors import automotriz_y_motocicletas_hierarchy, bebe__hierarchy, co_mputo_y_tablets_hierarchy, \
    deportes_y_aire_libre_hierarchy, electro_nicos_hierarchy, handmade_hierarchy, \
    herramientas_y_mejoras_del_hogar_hierarchy, hogar_y_cocina_hierarchy, industria_empresas_y_ciencia_hierarchy, \
    juegos_y_juguetes_hierarchy, libros_hierarchy, mascotas_y_accesorios_hierarchy, \
    peli_culas_series_de_tv_y_mu_sica_hierarchy, ropa_zapatos_y_accesorios_hierarchy, \
    salud_belleza_y_cuidado_personal_hierarchy, software_hierarchy, videojuegos_hierarchy
from CONSTANTS import *
from multiprocessing import Process
from DataCollectors_Configuration import AMAZON_MEXICO_CATEGORY_LIST, START_HIERARCHY_COLLECTION, START_URL_COLLECTION, \
    START_INFO_COLLECTION

category_list = '|'.join(AMAZON_MEXICO_CATEGORY_LIST)


def start_info_collection():
    jobs = []
    if AUTOMOTRIZ_Y_MOTOCICLETAS in category_list:
        thread_1 = Process(target=automotriz_y_motocicletas_info_collector.start_info_collection,
                           args=(AUTOMOTRIZ_Y_MOTOCICLETAS,))
        thread_1.daemon = True
        jobs.append(thread_1)

    if BEBE_ in category_list:
        thread_2 = Process(target=bebe__info_collector.start_info_collection, args=(BEBE_,))
        thread_2.daemon = True
        jobs.append(thread_2)

    if CO_MPUTO_Y_TABLETS in category_list:
        thread_3 = Process(target=co_mputo_y_tablets_info_collector.start_info_collection, args=(CO_MPUTO_Y_TABLETS,))
        thread_3.daemon = True
        jobs.append(thread_3)

    if DEPORTES_Y_AIRE_LIBRE in category_list:
        thread_4 = Process(target=deportes_y_aire_libre_info_collector.start_info_collection,
                           args=(DEPORTES_Y_AIRE_LIBRE,))
        thread_4.daemon = True
        jobs.append(thread_4)

    if ELECTRO_NICOS in category_list:
        thread_5 = Process(target=electro_nicos_info_collector.start_info_collection, args=(ELECTRO_NICOS,))
        thread_5.daemon = True
        jobs.append(thread_5)

    if HANDMADE in category_list:
        thread_6 = Process(target=handmade_info_collector.start_info_collection, args=(HANDMADE,))
        thread_6.daemon = True
        jobs.append(thread_6)

    if HERRAMIENTAS_Y_MEJORAS_DEL_HOGAR in category_list:
        thread_7 = Process(target=herramientas_y_mejoras_del_hogar_info_collector.start_info_collection,
                           args=(HERRAMIENTAS_Y_MEJORAS_DEL_HOGAR,))
        thread_7.daemon = True
        jobs.append(thread_7)

    if HOGAR_Y_COCINA in category_list:
        thread_8 = Process(target=hogar_y_cocina_info_collector.start_info_collection, args=(HOGAR_Y_COCINA,))
        thread_8.daemon = True
        jobs.append(thread_8)

    if INDUSTRIA_EMPRESAS_Y_CIENCIA in category_list:
        thread_9 = Process(target=industria_empresas_y_ciencia_info_collector.start_info_collection,
                           args=(INDUSTRIA_EMPRESAS_Y_CIENCIA,))
        thread_9.daemon = True
        jobs.append(thread_9)

    if JUEGOS_Y_JUGUETES in category_list:
        thread_10 = Process(target=juegos_y_juguetes_info_collector.start_info_collection, args=(JUEGOS_Y_JUGUETES,))
        thread_10.daemon = True
        jobs.append(thread_10)

    if LIBROS in category_list:
        thread_11 = Process(target=libros_info_collector.start_info_collection, args=(LIBROS,))
        thread_11.daemon = True
        jobs.append(thread_11)

    if MASCOTAS_Y_ACCESORIOS in category_list:
        thread_12 = Process(target=mascotas_y_accesorios_info_collector.start_info_collection,
                            args=(MASCOTAS_Y_ACCESORIOS,))
        thread_12.daemon = True
        jobs.append(thread_12)

    if PELI_CULAS_SERIES_DE_TV_Y_MU_SICA in category_list:
        thread_13 = Process(target=peli_culas_series_de_tv_y_mu_sica_info_collector.start_info_collection,
                            args=(PELI_CULAS_SERIES_DE_TV_Y_MU_SICA,))
        thread_13.daemon = True
        jobs.append(thread_13)

    if ROPA_ZAPATOS_Y_ACCESORIOS in category_list:
        thread_14 = Process(target=ropa_zapatos_y_accesorios_info_collector.start_info_collection,
                            args=(ROPA_ZAPATOS_Y_ACCESORIOS,))
        thread_14.daemon = True
        jobs.append(thread_14)

    if SALUD_BELLEZA_Y_CUIDADO_PERSONAL in category_list:
        thread_15 = Process(target=salud_belleza_y_cuidado_personal_info_collector.start_info_collection,
                            args=(SALUD_BELLEZA_Y_CUIDADO_PERSONAL,))
        thread_15.daemon = True
        jobs.append(thread_15)

    if SOFTWARE in category_list:
        thread_16 = Process(target=software_info_collector.start_info_collection, args=(SOFTWARE,))
        thread_16.daemon = True
        jobs.append(thread_16)

    if VIDEOJUEGOS in category_list:
        thread_17 = Process(target=videojuegos_info_collector.start_info_collection, args=(VIDEOJUEGOS,))
        thread_17.daemon = True
        jobs.append(thread_17)
    for job in jobs:
        job.start()
        job.join()


def start_url_collection():
    jobs = []
    if AUTOMOTRIZ_Y_MOTOCICLETAS in category_list:
        thread_1 = Process(target=automotriz_y_motocicletas_url_collector.start_program,
                           args=(AUTOMOTRIZ_Y_MOTOCICLETAS,))
        thread_1.daemon = True
        jobs.append(thread_1)

    if BEBE_ in category_list:
        thread_2 = Process(target=bebe__url_collector.start_program, args=(BEBE_,))
        thread_2.daemon = True
        jobs.append(thread_2)

    if CO_MPUTO_Y_TABLETS in category_list:
        thread_3 = Process(target=co_mputo_y_tablets_url_collector.start_program, args=(CO_MPUTO_Y_TABLETS,))
        thread_3.daemon = True
        jobs.append(thread_3)

    if DEPORTES_Y_AIRE_LIBRE in category_list:
        thread_4 = Process(target=deportes_y_aire_libre_url_collector.start_program, args=(DEPORTES_Y_AIRE_LIBRE,))
        thread_4.daemon = True
        jobs.append(thread_4)

    if ELECTRO_NICOS in category_list:
        thread_5 = Process(target=electro_nicos_url_collector.start_program, args=(ELECTRO_NICOS,))
        thread_5.daemon = True
        jobs.append(thread_5)

    if HANDMADE in category_list:
        thread_6 = Process(target=handmade_url_collector.start_program, args=(HANDMADE,))
        thread_6.daemon = True
        jobs.append(thread_6)

    if HERRAMIENTAS_Y_MEJORAS_DEL_HOGAR in category_list:
        thread_7 = Process(target=herramientas_y_mejoras_del_hogar_url_collector.start_program,
                           args=(HERRAMIENTAS_Y_MEJORAS_DEL_HOGAR,))
        thread_7.daemon = True
        jobs.append(thread_7)

    if HOGAR_Y_COCINA in category_list:
        thread_8 = Process(target=hogar_y_cocina_url_collector.start_program, args=(HOGAR_Y_COCINA,))
        thread_8.daemon = True
        jobs.append(thread_8)

    if INDUSTRIA_EMPRESAS_Y_CIENCIA in category_list:
        thread_9 = Process(target=industria_empresas_y_ciencia_url_collector.start_program,
                           args=(INDUSTRIA_EMPRESAS_Y_CIENCIA,))
        thread_9.daemon = True
        jobs.append(thread_9)

    if JUEGOS_Y_JUGUETES in category_list:
        thread_10 = Process(target=juegos_y_juguetes_url_collector.start_program, args=(JUEGOS_Y_JUGUETES,))
        thread_10.daemon = True
        jobs.append(thread_10)

    if LIBROS in category_list:
        thread_11 = Process(target=libros_url_collector.start_program, args=(LIBROS,))
        thread_11.daemon = True
        jobs.append(thread_11)

    if MASCOTAS_Y_ACCESORIOS in category_list:
        thread_12 = Process(target=mascotas_y_accesorios_url_collector.start_program, args=(MASCOTAS_Y_ACCESORIOS,))
        thread_12.daemon = True
        jobs.append(thread_12)

    if PELI_CULAS_SERIES_DE_TV_Y_MU_SICA in category_list:
        thread_13 = Process(target=peli_culas_series_de_tv_y_mu_sica_url_collector.start_program,
                            args=(PELI_CULAS_SERIES_DE_TV_Y_MU_SICA,))
        thread_13.daemon = True
        jobs.append(thread_13)

    if ROPA_ZAPATOS_Y_ACCESORIOS in category_list:
        thread_14 = Process(target=ropa_zapatos_y_accesorios_url_collector.start_program,
                            args=(ROPA_ZAPATOS_Y_ACCESORIOS,))
        thread_14.daemon = True
        jobs.append(thread_14)

    if SALUD_BELLEZA_Y_CUIDADO_PERSONAL in category_list:
        thread_15 = Process(target=salud_belleza_y_cuidado_personal_url_collector.start_program,
                            args=(SALUD_BELLEZA_Y_CUIDADO_PERSONAL,))
        thread_15.daemon = True
        jobs.append(thread_15)

    if SOFTWARE in category_list:
        thread_16 = Process(target=software_url_collector.start_program, args=(SOFTWARE,))
        thread_16.daemon = True
        jobs.append(thread_16)

    if VIDEOJUEGOS in category_list:
        thread_17 = Process(target=videojuegos_url_collector.start_program, args=(VIDEOJUEGOS,))
        thread_17.daemon = True
        jobs.append(thread_17)
    for job in jobs:
        job.start()
        job.join()


def start_hierarchy_collection():
    jobs = []
    if AUTOMOTRIZ_Y_MOTOCICLETAS in category_list:
        thread_1 = Process(target=automotriz_y_motocicletas_hierarchy.start_program)
        thread_1.daemon = True

        jobs.append(thread_1)

    if BEBE_ in category_list:
        thread_2 = Process(target=bebe__hierarchy.start_program)
        thread_2.daemon = True

        jobs.append(thread_2)

    if CO_MPUTO_Y_TABLETS in category_list:
        thread_3 = Process(target=co_mputo_y_tablets_hierarchy.start_program)
        thread_3.daemon = True

        jobs.append(thread_3)

    if DEPORTES_Y_AIRE_LIBRE in category_list:
        thread_4 = Process(target=deportes_y_aire_libre_hierarchy.start_program)
        thread_4.daemon = True

        jobs.append(thread_4)

    if ELECTRO_NICOS in category_list:
        thread_5 = Process(target=electro_nicos_hierarchy.start_program)
        thread_5.daemon = True

        jobs.append(thread_5)

    if HANDMADE in category_list:
        thread_6 = Process(target=handmade_hierarchy.start_program)
        thread_6.daemon = True

        jobs.append(thread_6)

    if HERRAMIENTAS_Y_MEJORAS_DEL_HOGAR in category_list:
        thread_7 = Process(target=herramientas_y_mejoras_del_hogar_hierarchy.start_program)
        thread_7.daemon = True

        jobs.append(thread_7)

    if HOGAR_Y_COCINA in category_list:
        thread_8 = Process(target=hogar_y_cocina_hierarchy.start_program)
        thread_8.daemon = True

        jobs.append(thread_8)

    if INDUSTRIA_EMPRESAS_Y_CIENCIA in category_list:
        thread_9 = Process(target=industria_empresas_y_ciencia_hierarchy.start_program)
        thread_9.daemon = True

        jobs.append(thread_9)

    if JUEGOS_Y_JUGUETES in category_list:
        thread_10 = Process(target=juegos_y_juguetes_hierarchy.start_program)
        thread_10.daemon = True

        jobs.append(thread_10)

    if LIBROS in category_list:
        thread_11 = Process(target=libros_hierarchy.start_program)
        thread_11.daemon = True

        jobs.append(thread_11)

    if MASCOTAS_Y_ACCESORIOS in category_list:
        thread_12 = Process(target=mascotas_y_accesorios_hierarchy.start_program)
        thread_12.daemon = True

        jobs.append(thread_12)

    if PELI_CULAS_SERIES_DE_TV_Y_MU_SICA in category_list:
        thread_13 = Process(target=peli_culas_series_de_tv_y_mu_sica_hierarchy.start_program)
        thread_13.daemon = True

        jobs.append(thread_13)

    if ROPA_ZAPATOS_Y_ACCESORIOS in category_list:
        thread_14 = Process(target=ropa_zapatos_y_accesorios_hierarchy.start_program)
        thread_14.daemon = True

        jobs.append(thread_14)

    if SALUD_BELLEZA_Y_CUIDADO_PERSONAL in category_list:
        thread_15 = Process(target=salud_belleza_y_cuidado_personal_hierarchy.start_program)
        thread_15.daemon = True

        jobs.append(thread_15)

    if SOFTWARE in category_list:
        thread_16 = Process(target=software_hierarchy.start_program)
        thread_16.daemon = True

        jobs.append(thread_16)

    if VIDEOJUEGOS in category_list:
        thread_17 = Process(target=videojuegos_hierarchy.start_program)
        thread_17.daemon = True

        jobs.append(thread_17)
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

