import sys
sys.path.insert(0, r'/usr/datacollector')

from info_collectors import musica_film_e_tv_info_collector, videogiochi_e_console_info_collector, \
    alimentari_e_cura_della_casa_info_collector, elettronica_e_informatica_info_collector, \
    commercio_industria_e_scienza_info_collector, sport_e_tempo_libero_info_collector, libri_e_audible_info_collector, \
    casa_giardino_fai_da_te_e_animali_info_collector, giochi_e_prima_infanzia_info_collector, \
    bellezza_e_salute_info_collector, abbigliamento_scarpe_e_gioielli_info_collector, auto_e_moto_info_collector, \
    handmade_info_collector
from url_collectors import musica_film_e_tv_url_collector, videogiochi_e_console_url_collector, \
    alimentari_e_cura_della_casa_url_collector, elettronica_e_informatica_url_collector, \
    commercio_industria_e_scienza_url_collector, sport_e_tempo_libero_url_collector, libri_e_audible_url_collector, \
    casa_giardino_fai_da_te_e_animali_url_collector, giochi_e_prima_infanzia_url_collector, \
    bellezza_e_salute_url_collector, abbigliamento_scarpe_e_gioielli_url_collector, auto_e_moto_url_collector, \
    handmade_url_collector
from hierarchy_collectors import musica_film_e_tv_hierarchy, videogiochi_e_console_hierarchy, \
    alimentari_e_cura_della_casa_hierarchy, elettronica_e_informatica_hierarchy, \
    commercio_industria_e_scienza_hierarchy, sport_e_tempo_libero_hierarchy, libri_e_audible_hierarchy, \
    casa_giardino_fai_da_te_e_animali_hierarchy, giochi_e_prima_infanzia_hierarchy, bellezza_e_salute_hierarchy, \
    abbigliamento_scarpe_e_gioielli_hierarchy, auto_e_moto_hierarchy, handmade_hierarchy

from CONSTANTS import *
from multiprocessing import Process
from DataCollectors_Configuration import AMAZON_ITALY_CATEGORY_LIST, START_HIERARCHY_COLLECTION, START_URL_COLLECTION, \
    START_INFO_COLLECTION

category_list = '|'.join(AMAZON_ITALY_CATEGORY_LIST)


def start_info_collection():
    jobs = []
    if MUSICA_FILM_E_TV in category_list:
        process_1 = Process(target=musica_film_e_tv_info_collector.start_info_collection, args=(MUSICA_FILM_E_TV,))
        process_1.daemon = True
        jobs.append(process_1)

    if VIDEOGIOCHI_E_CONSOLE in category_list:
        process_2 = Process(target=videogiochi_e_console_info_collector.start_info_collection,
                            args=(VIDEOGIOCHI_E_CONSOLE,))
        process_2.daemon = True
        jobs.append(process_2)

    if ALIMENTARI_E_CURA_DELLA_CASA in category_list:
        process_3 = Process(target=alimentari_e_cura_della_casa_info_collector.start_info_collection,
                            args=(ALIMENTARI_E_CURA_DELLA_CASA,))
        process_3.daemon = True
        jobs.append(process_3)

    if ELETTRONICA_E_INFORMATICA in category_list:
        process_4 = Process(target=elettronica_e_informatica_info_collector.start_info_collection,
                            args=(ELETTRONICA_E_INFORMATICA,))
        process_4.daemon = True
        jobs.append(process_4)

    if COMMERCIO_INDUSTRIA_E_SCIENZA in category_list:
        process_5 = Process(target=commercio_industria_e_scienza_info_collector.start_info_collection,
                            args=(COMMERCIO_INDUSTRIA_E_SCIENZA,))
        process_5.daemon = True
        jobs.append(process_5)

    if SPORT_E_TEMPO_LIBERO in category_list:
        process_6 = Process(target=sport_e_tempo_libero_info_collector.start_info_collection,
                            args=(SPORT_E_TEMPO_LIBERO,))
        process_6.daemon = True
        jobs.append(process_6)

    if LIBRI_E_AUDIBLE in category_list:
        process_7 = Process(target=libri_e_audible_info_collector.start_info_collection, args=(LIBRI_E_AUDIBLE,))
        process_7.daemon = True
        jobs.append(process_7)

    if CASA_GIARDINO_FAI_DA_TE_E_ANIMALI in category_list:
        process_8 = Process(target=casa_giardino_fai_da_te_e_animali_info_collector.start_info_collection,
                            args=(CASA_GIARDINO_FAI_DA_TE_E_ANIMALI,))
        process_8.daemon = True
        jobs.append(process_8)

    if GIOCHI_E_PRIMA_INFANZIA in category_list:
        process_9 = Process(target=giochi_e_prima_infanzia_info_collector.start_info_collection,
                            args=(GIOCHI_E_PRIMA_INFANZIA,))
        process_9.daemon = True
        jobs.append(process_9)

    if BELLEZZA_E_SALUTE in category_list:
        process_10 = Process(target=bellezza_e_salute_info_collector.start_info_collection, args=(BELLEZZA_E_SALUTE,))
        process_10.daemon = True
        jobs.append(process_10)

    if ABBIGLIAMENTO_SCARPE_E_GIOIELLI in category_list:
        process_11 = Process(target=abbigliamento_scarpe_e_gioielli_info_collector.start_info_collection,
                             args=(ABBIGLIAMENTO_SCARPE_E_GIOIELLI,))
        process_11.daemon = True
        jobs.append(process_11)

    if AUTO_E_MOTO in category_list:
        process_12 = Process(target=auto_e_moto_info_collector.start_info_collection, args=(AUTO_E_MOTO,))
        process_12.daemon = True
        jobs.append(process_12)

    if HANDMADE in category_list:
        process_13 = Process(target=handmade_info_collector.start_info_collection, args=(HANDMADE,))
        process_13.daemon = True
        jobs.append(process_13)
    for job in jobs:
        job.start()
    for job in jobs:
        if job.is_alive():
            job.join()


def start_url_collection():
    jobs = []
    if MUSICA_FILM_E_TV in category_list:
        process_1 = Process(target=musica_film_e_tv_url_collector.start_program, args=(MUSICA_FILM_E_TV,))
        process_1.daemon = True
        jobs.append(process_1)

    if VIDEOGIOCHI_E_CONSOLE in category_list:
        process_2 = Process(target=videogiochi_e_console_url_collector.start_program, args=(VIDEOGIOCHI_E_CONSOLE,))
        process_2.daemon = True
        jobs.append(process_2)

    if ALIMENTARI_E_CURA_DELLA_CASA in category_list:
        process_3 = Process(target=alimentari_e_cura_della_casa_url_collector.start_program,
                            args=(ALIMENTARI_E_CURA_DELLA_CASA,))
        process_3.daemon = True
        jobs.append(process_3)

    if ELETTRONICA_E_INFORMATICA in category_list:
        process_4 = Process(target=elettronica_e_informatica_url_collector.start_program,
                            args=(ELETTRONICA_E_INFORMATICA,))
        process_4.daemon = True
        jobs.append(process_4)

    if COMMERCIO_INDUSTRIA_E_SCIENZA in category_list:
        process_5 = Process(target=commercio_industria_e_scienza_url_collector.start_program,
                            args=(COMMERCIO_INDUSTRIA_E_SCIENZA,))
        process_5.daemon = True
        jobs.append(process_5)

    if SPORT_E_TEMPO_LIBERO in category_list:
        process_6 = Process(target=sport_e_tempo_libero_url_collector.start_program, args=(SPORT_E_TEMPO_LIBERO,))
        process_6.daemon = True
        jobs.append(process_6)

    if LIBRI_E_AUDIBLE in category_list:
        process_7 = Process(target=libri_e_audible_url_collector.start_program, args=(LIBRI_E_AUDIBLE,))
        process_7.daemon = True
        jobs.append(process_7)

    if CASA_GIARDINO_FAI_DA_TE_E_ANIMALI in category_list:
        process_8 = Process(target=casa_giardino_fai_da_te_e_animali_url_collector.start_program,
                            args=(CASA_GIARDINO_FAI_DA_TE_E_ANIMALI,))
        process_8.daemon = True
        jobs.append(process_8)

    if GIOCHI_E_PRIMA_INFANZIA in category_list:
        process_9 = Process(target=giochi_e_prima_infanzia_url_collector.start_program, args=(GIOCHI_E_PRIMA_INFANZIA,))
        process_9.daemon = True
        jobs.append(process_9)

    if BELLEZZA_E_SALUTE in category_list:
        process_10 = Process(target=bellezza_e_salute_url_collector.start_program, args=(BELLEZZA_E_SALUTE,))
        process_10.daemon = True
        jobs.append(process_10)

    if ABBIGLIAMENTO_SCARPE_E_GIOIELLI in category_list:
        process_11 = Process(target=abbigliamento_scarpe_e_gioielli_url_collector.start_program,
                             args=(ABBIGLIAMENTO_SCARPE_E_GIOIELLI,))
        process_11.daemon = True
        jobs.append(process_11)

    if AUTO_E_MOTO in category_list:
        process_12 = Process(target=auto_e_moto_url_collector.start_program, args=(AUTO_E_MOTO,))
        process_12.daemon = True
        jobs.append(process_12)

    if HANDMADE in category_list:
        process_13 = Process(target=handmade_url_collector.start_program, args=(HANDMADE,))
        process_13.daemon = True
        jobs.append(process_13)

    for job in jobs:
        job.start()
    for job in jobs:
        if job.is_alive():
            job.join()


def start_hierarchy_collection():
    jobs = []
    if MUSICA_FILM_E_TV in category_list:
        process_1 = Process(target=musica_film_e_tv_hierarchy.start_program)
        process_1.daemon = True

        jobs.append(process_1)

    if VIDEOGIOCHI_E_CONSOLE in category_list:
        process_2 = Process(target=videogiochi_e_console_hierarchy.start_program)
        process_2.daemon = True

        jobs.append(process_2)

    if ALIMENTARI_E_CURA_DELLA_CASA in category_list:
        process_3 = Process(target=alimentari_e_cura_della_casa_hierarchy.start_program)
        process_3.daemon = True

        jobs.append(process_3)

    if ELETTRONICA_E_INFORMATICA in category_list:
        process_4 = Process(target=elettronica_e_informatica_hierarchy.start_program)
        process_4.daemon = True

        jobs.append(process_4)

    if COMMERCIO_INDUSTRIA_E_SCIENZA in category_list:
        process_5 = Process(target=commercio_industria_e_scienza_hierarchy.start_program)
        process_5.daemon = True

        jobs.append(process_5)

    if SPORT_E_TEMPO_LIBERO in category_list:
        process_6 = Process(target=sport_e_tempo_libero_hierarchy.start_program)
        process_6.daemon = True

        jobs.append(process_6)

    if LIBRI_E_AUDIBLE in category_list:
        process_7 = Process(target=libri_e_audible_hierarchy.start_program)
        process_7.daemon = True

        jobs.append(process_7)

    if CASA_GIARDINO_FAI_DA_TE_E_ANIMALI in category_list:
        process_8 = Process(target=casa_giardino_fai_da_te_e_animali_hierarchy.start_program)
        process_8.daemon = True

        jobs.append(process_8)

    if GIOCHI_E_PRIMA_INFANZIA in category_list:
        process_9 = Process(target=giochi_e_prima_infanzia_hierarchy.start_program)
        process_9.daemon = True

        jobs.append(process_9)

    if BELLEZZA_E_SALUTE in category_list:
        process_10 = Process(target=bellezza_e_salute_hierarchy.start_program)
        process_10.daemon = True

        jobs.append(process_10)

    if ABBIGLIAMENTO_SCARPE_E_GIOIELLI in category_list:
        process_11 = Process(target=abbigliamento_scarpe_e_gioielli_hierarchy.start_program)
        process_11.daemon = True

        jobs.append(process_11)

    if AUTO_E_MOTO in category_list:
        process_12 = Process(target=auto_e_moto_hierarchy.start_program)
        process_12.daemon = True

        jobs.append(process_12)

    if HANDMADE in category_list:
        process_13 = Process(target=handmade_hierarchy.start_program)
        process_13.daemon = True

        jobs.append(process_13)

    for job in jobs:
        job.start()
    for job in jobs:
        if job.is_alive():
            job.join()

    start_url_collection()


if __name__ == '__main__':

    if START_HIERARCHY_COLLECTION:
        start_hierarchy_collection()

    if START_URL_COLLECTION:
        start_url_collection()

    if START_INFO_COLLECTION:
        start_info_collection()

