import sys
sys.path.insert(0, r'/usr/datacollector')
from hierarchy_collectors import beaute__sante__e_picerie_hierarchy, jouets_enfants_et_be_be_s_hierarchy, \
    ve_tements_chaussures_bijoux_hierarchy, maison_bricolage_animalerie_hierarchy, high_tech_et_informatique_hierarchy, \
    auto_et_moto_hierarchy, musique_dvd_et_blu_ray_hierarchy, livres_and_audible_hierarchy, \
    jeux_vide_o_et_consoles_hierarchy, commerce_industrie_et_science_hierarchy, sports_et_loisirs_hierarchy, \
    handmade_hierarchy
from url_collectors import beaute__sante__e_picerie_url_collector, jouets_enfants_et_be_be_s_url_collector, \
    ve_tements_chaussures_bijoux_url_collector, maison_bricolage_animalerie_url_collector, \
    high_tech_et_informatique_url_collector, auto_et_moto_url_collector, musique_dvd_et_blu_ray_url_collector, \
    livres_and_audible_url_collector, jeux_vide_o_et_consoles_url_collector, \
    commerce_industrie_et_science_url_collector, sports_et_loisirs_url_collector, handmade_url_collector
from info_collectors import beaute__sante__e_picerie_info_collector, jouets_enfants_et_be_be_s_info_collector, \
    ve_tements_chaussures_bijoux_info_collector, maison_bricolage_animalerie_info_collector, \
    high_tech_et_informatique_info_collector, auto_et_moto_info_collector, musique_dvd_et_blu_ray_info_collector, \
    livres_and_audible_info_collector, jeux_vide_o_et_consoles_info_collector, \
    commerce_industrie_et_science_info_collector, sports_et_loisirs_info_collector, handmade_info_collector
from CONSTANTS import *
from multiprocessing import Process
from DataCollectors_Configuration import AMAZON_FRANCE_CATEGORY_LIST, START_HIERARCHY_COLLECTION, START_URL_COLLECTION, \
    START_INFO_COLLECTION

category_list = '|'.join(AMAZON_FRANCE_CATEGORY_LIST)


def start_info_collection():
    jobs = []
    if BEAUTE__SANTE__E_PICERIE in category_list:
        process_1 = Process(target=beaute__sante__e_picerie_info_collector.start_info_collection,
                            args=(BEAUTE__SANTE__E_PICERIE,))
        process_1.daemon = True
        jobs.append(process_1)

    if JOUETS_ENFANTS_ET_BE_BE_S in category_list:
        process_2 = Process(target=jouets_enfants_et_be_be_s_info_collector.start_info_collection,
                            args=(JOUETS_ENFANTS_ET_BE_BE_S,))
        process_2.daemon = True
        jobs.append(process_2)

    if VE_TEMENTS_CHAUSSURES_BIJOUX in category_list:
        process_3 = Process(target=ve_tements_chaussures_bijoux_info_collector.start_info_collection,
                            args=(VE_TEMENTS_CHAUSSURES_BIJOUX,))
        process_3.daemon = True
        jobs.append(process_3)

    if MAISON_BRICOLAGE_ANIMALERIE in category_list:
        process_4 = Process(target=maison_bricolage_animalerie_info_collector.start_info_collection,
                            args=(MAISON_BRICOLAGE_ANIMALERIE,))
        process_4.daemon = True
        jobs.append(process_4)

    if HIGH_TECH_ET_INFORMATIQUE in category_list:
        process_5 = Process(target=high_tech_et_informatique_info_collector.start_info_collection,
                            args=(HIGH_TECH_ET_INFORMATIQUE,))
        process_5.daemon = True
        jobs.append(process_5)

    if AUTO_ET_MOTO in category_list:
        process_6 = Process(target=auto_et_moto_info_collector.start_info_collection, args=(AUTO_ET_MOTO,))
        process_6.daemon = True
        jobs.append(process_6)

    if MUSIQUE_DVD_ET_BLU_RAY in category_list:
        process_7 = Process(target=musique_dvd_et_blu_ray_info_collector.start_info_collection,
                            args=(MUSIQUE_DVD_ET_BLU_RAY,))
        process_7.daemon = True
        jobs.append(process_7)

    if LIVRES_AND_AUDIBLE in category_list:
        process_8 = Process(target=livres_and_audible_info_collector.start_info_collection, args=(LIVRES_AND_AUDIBLE,))
        process_8.daemon = True
        jobs.append(process_8)

    if JEUX_VIDE_O_ET_CONSOLES in category_list:
        process_9 = Process(target=jeux_vide_o_et_consoles_info_collector.start_info_collection,
                            args=(JEUX_VIDE_O_ET_CONSOLES,))
        process_9.daemon = True
        jobs.append(process_9)

    if COMMERCE_INDUSTRIE_ET_SCIENCE in category_list:
        process_10 = Process(target=commerce_industrie_et_science_info_collector.start_info_collection,
                             args=(COMMERCE_INDUSTRIE_ET_SCIENCE,))
        process_10.daemon = True
        jobs.append(process_10)

    if SPORTS_ET_LOISIRS in category_list:
        process_11 = Process(target=sports_et_loisirs_info_collector.start_info_collection, args=(SPORTS_ET_LOISIRS,))
        process_11.daemon = True
        jobs.append(process_11)

    if HANDMADE in category_list:
        process_12 = Process(target=handmade_info_collector.start_info_collection, args=(HANDMADE,))
        process_12.daemon = True
        jobs.append(process_12)

    for job in jobs:
        job.start()
    for job in jobs:
        if job.is_alive():
            job.join()


def start_url_collection():
    jobs = []
    if BEAUTE__SANTE__E_PICERIE in category_list:
        process_1 = Process(target=beaute__sante__e_picerie_url_collector.start_program,
                            args=(BEAUTE__SANTE__E_PICERIE,))
        process_1.daemon = True
        jobs.append(process_1)

    if JOUETS_ENFANTS_ET_BE_BE_S in category_list:
        process_2 = Process(target=jouets_enfants_et_be_be_s_url_collector.start_program,
                            args=(JOUETS_ENFANTS_ET_BE_BE_S,))
        process_2.daemon = True
        jobs.append(process_2)

    if VE_TEMENTS_CHAUSSURES_BIJOUX in category_list:
        process_3 = Process(target=ve_tements_chaussures_bijoux_url_collector.start_program,
                            args=(VE_TEMENTS_CHAUSSURES_BIJOUX,))
        process_3.daemon = True
        jobs.append(process_3)

    if MAISON_BRICOLAGE_ANIMALERIE in category_list:
        process_4 = Process(target=maison_bricolage_animalerie_url_collector.start_program,
                            args=(MAISON_BRICOLAGE_ANIMALERIE,))
        process_4.daemon = True
        jobs.append(process_4)

    if HIGH_TECH_ET_INFORMATIQUE in category_list:
        process_5 = Process(target=high_tech_et_informatique_url_collector.start_program,
                            args=(HIGH_TECH_ET_INFORMATIQUE,))
        process_5.daemon = True
        jobs.append(process_5)

    if AUTO_ET_MOTO in category_list:
        process_6 = Process(target=auto_et_moto_url_collector.start_program, args=(AUTO_ET_MOTO,))
        process_6.daemon = True
        jobs.append(process_6)

    if MUSIQUE_DVD_ET_BLU_RAY in category_list:
        process_7 = Process(target=musique_dvd_et_blu_ray_url_collector.start_program, args=(MUSIQUE_DVD_ET_BLU_RAY,))
        process_7.daemon = True
        jobs.append(process_7)

    if LIVRES_AND_AUDIBLE in category_list:
        process_8 = Process(target=livres_and_audible_url_collector.start_program, args=(LIVRES_AND_AUDIBLE,))
        process_8.daemon = True
        jobs.append(process_8)

    if JEUX_VIDE_O_ET_CONSOLES in category_list:
        process_9 = Process(target=jeux_vide_o_et_consoles_url_collector.start_program, args=(JEUX_VIDE_O_ET_CONSOLES,))
        process_9.daemon = True
        jobs.append(process_9)

    if COMMERCE_INDUSTRIE_ET_SCIENCE in category_list:
        process_10 = Process(target=commerce_industrie_et_science_url_collector.start_program,
                             args=(COMMERCE_INDUSTRIE_ET_SCIENCE,))
        process_10.daemon = True
        jobs.append(process_10)

    if SPORTS_ET_LOISIRS in category_list:
        process_11 = Process(target=sports_et_loisirs_url_collector.start_program, args=(SPORTS_ET_LOISIRS,))
        process_11.daemon = True
        jobs.append(process_11)

    if HANDMADE in category_list:
        process_12 = Process(target=handmade_url_collector.start_program, args=(HANDMADE,))
        process_12.daemon = True
        jobs.append(process_12)

    for job in jobs:
        job.start()
    for job in jobs:
        if job.is_alive():
            job.join()


def start_hierarchy_collection():
    jobs = []
    if BEAUTE__SANTE__E_PICERIE in category_list:
        process_1 = Process(target=beaute__sante__e_picerie_hierarchy.start_program)
        process_1.daemon = True

        jobs.append(process_1)

    if JOUETS_ENFANTS_ET_BE_BE_S in category_list:
        process_2 = Process(target=jouets_enfants_et_be_be_s_hierarchy.start_program)
        process_2.daemon = True

        jobs.append(process_2)

    if VE_TEMENTS_CHAUSSURES_BIJOUX in category_list:
        process_3 = Process(target=ve_tements_chaussures_bijoux_hierarchy.start_program)
        process_3.daemon = True

        jobs.append(process_3)

    if MAISON_BRICOLAGE_ANIMALERIE in category_list:
        process_4 = Process(target=maison_bricolage_animalerie_hierarchy.start_program)
        process_4.daemon = True

        jobs.append(process_4)

    if HIGH_TECH_ET_INFORMATIQUE in category_list:
        process_5 = Process(target=high_tech_et_informatique_hierarchy.start_program)
        process_5.daemon = True

        jobs.append(process_5)

    if AUTO_ET_MOTO in category_list:
        process_6 = Process(target=auto_et_moto_hierarchy.start_program)
        process_6.daemon = True

        jobs.append(process_6)

    if MUSIQUE_DVD_ET_BLU_RAY in category_list:
        process_7 = Process(target=musique_dvd_et_blu_ray_hierarchy.start_program)
        process_7.daemon = True

        jobs.append(process_7)

    if LIVRES_AND_AUDIBLE in category_list:
        process_8 = Process(target=livres_and_audible_hierarchy.start_program)
        process_8.daemon = True

        jobs.append(process_8)

    if JEUX_VIDE_O_ET_CONSOLES in category_list:
        process_9 = Process(target=jeux_vide_o_et_consoles_hierarchy.start_program)
        process_9.daemon = True

        jobs.append(process_9)

    if COMMERCE_INDUSTRIE_ET_SCIENCE in category_list:
        process_10 = Process(target=commerce_industrie_et_science_hierarchy.start_program)
        process_10.daemon = True

        jobs.append(process_10)

    if SPORTS_ET_LOISIRS in category_list:
        process_11 = Process(target=sports_et_loisirs_hierarchy.start_program)
        process_11.daemon = True

        jobs.append(process_11)

    if HANDMADE in category_list:
        process_12 = Process(target=handmade_hierarchy.start_program)
        process_12.daemon = True

        jobs.append(process_12)

    for job in jobs:
        job.start()
    for job in jobs:
        if job.is_alive():
            job.join()


if __name__ == '__main__':

    if START_HIERARCHY_COLLECTION:
        start_hierarchy_collection()

    if START_URL_COLLECTION:
        start_url_collection()

    if START_INFO_COLLECTION:
        start_info_collection()
