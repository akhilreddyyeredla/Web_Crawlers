import sys
sys.path.insert(0, r'/usr/datacollector')

from info_collectors import kleidung_schuhe_and_uhren_info_collector, haushalt_garten_baumarkt_info_collector, \
    auto_motorrad_and_gewerbe_info_collector, handmade_and_amazon_launchpad_info_collector, \
    spielzeug_and_baby_info_collector, sport_and_freizeit_info_collector, filme_serien_musik_and_games_info_collector, \
    elektronik_and_computer_info_collector, beauty_drogerie_and_lebensmittel_info_collector
from url_collectors import kleidung_schuhe_and_uhren_url_collector, haushalt_garten_baumarkt_url_collector, \
    auto_motorrad_and_gewerbe_url_collector, handmade_and_amazon_launchpad_url_collector, \
    spielzeug_and_baby_url_collector, sport_and_freizeit_url_collector, filme_serien_musik_and_games_url_collector, \
    elektronik_and_computer_url_collector, beauty_drogerie_and_lebensmittel_url_collector
from hierarchy_collectors import kleidung_schuhe_and_uhren_hierarchy, haushalt_garten_baumarkt_hierarchy, \
    auto_motorrad_and_gewerbe_hierarchy, handmade_and_amazon_launchpad_hierarchy, spielzeug_and_baby_hierarchy, \
    sport_and_freizeit_hierarchy, filme_serien_musik_and_games_hierarchy, elektronik_and_computer_hierarchy, \
    beauty_drogerie_and_lebensmittel_hierarchy

from CONSTANTS import *
from multiprocessing import Process
from DataCollectors_Configuration import AMAZON_GERMANY_CATEGORY_LIST, START_HIERARCHY_COLLECTION, START_URL_COLLECTION, \
    START_INFO_COLLECTION

category_list = '|'.join(AMAZON_GERMANY_CATEGORY_LIST)


def start_info_collection():
    jobs = []
    if KLEIDUNG_SCHUHE_AND_UHREN in category_list:
        process_1 = Process(target=kleidung_schuhe_and_uhren_info_collector.start_info_collection,
                            args=(KLEIDUNG_SCHUHE_AND_UHREN,))
        process_1.daemon = True
        jobs.append(process_1)

    if HAUSHALT_GARTEN_BAUMARKT in category_list:
        process_2 = Process(target=haushalt_garten_baumarkt_info_collector.start_info_collection,
                            args=(HAUSHALT_GARTEN_BAUMARKT,))
        process_2.daemon = True
        jobs.append(process_2)

    if AUTO_MOTORRAD_AND_GEWERBE in category_list:
        process_3 = Process(target=auto_motorrad_and_gewerbe_info_collector.start_info_collection,
                            args=(AUTO_MOTORRAD_AND_GEWERBE,))
        process_3.daemon = True
        jobs.append(process_3)

    if HANDMADE_AND_AMAZON_LAUNCHPAD in category_list:
        process_4 = Process(target=handmade_and_amazon_launchpad_info_collector.start_info_collection,
                            args=(HANDMADE_AND_AMAZON_LAUNCHPAD,))
        process_4.daemon = True
        jobs.append(process_4)

    if SPIELZEUG_AND_BABY in category_list:
        process_5 = Process(target=spielzeug_and_baby_info_collector.start_info_collection, args=(SPIELZEUG_AND_BABY,))
        process_5.daemon = True
        jobs.append(process_5)

    if SPORT_AND_FREIZEIT in category_list:
        process_6 = Process(target=sport_and_freizeit_info_collector.start_info_collection, args=(SPORT_AND_FREIZEIT,))
        process_6.daemon = True
        jobs.append(process_6)

    if FILME_SERIEN_MUSIK_AND_GAMES in category_list:
        process_7 = Process(target=filme_serien_musik_and_games_info_collector.start_info_collection,
                            args=(FILME_SERIEN_MUSIK_AND_GAMES,))
        process_7.daemon = True
        jobs.append(process_7)

    if ELEKTRONIK_AND_COMPUTER in category_list:
        process_8 = Process(target=elektronik_and_computer_info_collector.start_info_collection,
                            args=(ELEKTRONIK_AND_COMPUTER,))
        process_8.daemon = True
        jobs.append(process_8)

    if BEAUTY_DROGERIE_AND_LEBENSMITTEL in category_list:
        process_9 = Process(target=beauty_drogerie_and_lebensmittel_info_collector.start_info_collection,
                            args=(BEAUTY_DROGERIE_AND_LEBENSMITTEL,))
        process_9.daemon = True
        jobs.append(process_9)
    for job in jobs:
        job.start()
    for job in jobs:
        if job.is_alive():
            job.join()


def start_url_collection():
    jobs = []
    if KLEIDUNG_SCHUHE_AND_UHREN in category_list:
        process_1 = Process(target=kleidung_schuhe_and_uhren_url_collector.start_program,
                            args=(KLEIDUNG_SCHUHE_AND_UHREN,))
        process_1.daemon = True
        jobs.append(process_1)

    if HAUSHALT_GARTEN_BAUMARKT in category_list:
        process_2 = Process(target=haushalt_garten_baumarkt_url_collector.start_program,
                            args=(HAUSHALT_GARTEN_BAUMARKT,))
        process_2.daemon = True
        jobs.append(process_2)

    if AUTO_MOTORRAD_AND_GEWERBE in category_list:
        process_3 = Process(target=auto_motorrad_and_gewerbe_url_collector.start_program,
                            args=(AUTO_MOTORRAD_AND_GEWERBE,))
        process_3.daemon = True
        jobs.append(process_3)

    if HANDMADE_AND_AMAZON_LAUNCHPAD in category_list:
        process_4 = Process(target=handmade_and_amazon_launchpad_url_collector.start_program,
                            args=(HANDMADE_AND_AMAZON_LAUNCHPAD,))
        process_4.daemon = True
        jobs.append(process_4)

    if SPIELZEUG_AND_BABY in category_list:
        process_5 = Process(target=spielzeug_and_baby_url_collector.start_program, args=(SPIELZEUG_AND_BABY,))
        process_5.daemon = True
        jobs.append(process_5)

    if SPORT_AND_FREIZEIT in category_list:
        process_6 = Process(target=sport_and_freizeit_url_collector.start_program, args=(SPORT_AND_FREIZEIT,))
        process_6.daemon = True
        jobs.append(process_6)

    if FILME_SERIEN_MUSIK_AND_GAMES in category_list:
        process_7 = Process(target=filme_serien_musik_and_games_url_collector.start_program,
                            args=(FILME_SERIEN_MUSIK_AND_GAMES,))
        process_7.daemon = True
        jobs.append(process_7)

    if ELEKTRONIK_AND_COMPUTER in category_list:
        process_8 = Process(target=elektronik_and_computer_url_collector.start_program, args=(ELEKTRONIK_AND_COMPUTER,))
        process_8.daemon = True
        jobs.append(process_8)

    if BEAUTY_DROGERIE_AND_LEBENSMITTEL in category_list:
        process_9 = Process(target=beauty_drogerie_and_lebensmittel_url_collector.start_program,
                            args=(BEAUTY_DROGERIE_AND_LEBENSMITTEL,))
        process_9.daemon = True
        jobs.append(process_9)

    for job in jobs:
        job.start()
    for job in jobs:
        if job.is_alive():
            job.join()



def start_hierarchy_collection():
    jobs = []
    if KLEIDUNG_SCHUHE_AND_UHREN in category_list:
        process_1 = Process(target=kleidung_schuhe_and_uhren_hierarchy.start_program)
        process_1.daemon = True

        jobs.append(process_1)

    if HAUSHALT_GARTEN_BAUMARKT in category_list:
        process_2 = Process(target=haushalt_garten_baumarkt_hierarchy.start_program)
        process_2.daemon = True

        jobs.append(process_2)

    if AUTO_MOTORRAD_AND_GEWERBE in category_list:
        process_3 = Process(target=auto_motorrad_and_gewerbe_hierarchy.start_program)
        process_3.daemon = True

        jobs.append(process_3)

    if HANDMADE_AND_AMAZON_LAUNCHPAD in category_list:
        process_4 = Process(target=handmade_and_amazon_launchpad_hierarchy.start_program)
        process_4.daemon = True

        jobs.append(process_4)

    if SPIELZEUG_AND_BABY in category_list:
        process_5 = Process(target=spielzeug_and_baby_hierarchy.start_program)
        process_5.daemon = True

        jobs.append(process_5)

    if SPORT_AND_FREIZEIT in category_list:
        process_6 = Process(target=sport_and_freizeit_hierarchy.start_program)
        process_6.daemon = True

        jobs.append(process_6)

    if FILME_SERIEN_MUSIK_AND_GAMES in category_list:
        process_7 = Process(target=filme_serien_musik_and_games_hierarchy.start_program)
        process_7.daemon = True

        jobs.append(process_7)

    if ELEKTRONIK_AND_COMPUTER in category_list:
        process_8 = Process(target=elektronik_and_computer_hierarchy.start_program)
        process_8.daemon = True

        jobs.append(process_8)

    if BEAUTY_DROGERIE_AND_LEBENSMITTEL in category_list:
        process_9 = Process(target=beauty_drogerie_and_lebensmittel_hierarchy.start_program)
        process_9.daemon = True

        jobs.append(process_9)

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
