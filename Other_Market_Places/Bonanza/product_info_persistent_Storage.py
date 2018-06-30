
from Common.Bonanza_common_imports import *
from Common.Persist_BigQuery import persist_BigQuery


def write_single_file(hierarchy_path, data):
    dumped = data
    file_name = '{}.txt'.format('product_info')
    path = '{}{}{}{}{}{}{}'.format(DataCollectors_Configuration.ROOT_FOLDER,
                                   DataCollectors_Configuration.PATH_STYLE,
                                   DataCollectors_Configuration.BONANZA_PROJECT_NAME,
                                   DataCollectors_Configuration.PATH_STYLE,
                                   hierarchy_path,
                                   DataCollectors_Configuration.PATH_STYLE,
                                   file_name)

    write_file = open(path, 'a')
    with write_file as fp:
        fp.write(json.dumps(dumped)+"\n")


def write_to_multiple_files(hierarchy_path, data):
    dumped = data
    file_name = '{}.json'.format(str(time.time()))
    path = '{}{}{}{}{}{}{}'.format(DataCollectors_Configuration.ROOT_FOLDER,
                                   DataCollectors_Configuration.PATH_STYLE,
                                   DataCollectors_Configuration.BONANZA_PROJECT_NAME,
                                   DataCollectors_Configuration.PATH_STYLE,
                                   hierarchy_path,
                                   DataCollectors_Configuration.PATH_STYLE,
                                   file_name)

    write_file = open(path, 'a')
    with write_file as fp:
        fp.write(json.dumps(dumped) + "\n")


def storage(market_place, date, hirarchy, time, info_dictionary):
    """
    :param market_place: Ex: Bonanza
    :param date: Current_date
    :param hirarchy: Hierarchy
    :param time: presnet time in UTC Format
    :param info_dictionary: product details dictionary
    :return: NONE
    """

    hierarchy_name = hirarchy.split('|')
    hierarchy_path = DataCollectors_Configuration.PATH_STYLE.join(hierarchy_name)

    if DataCollectors_Configuration.WRITE_TO == CONSTANTS.WRITE_TO_DB:

        # inserts (data) in to mysql_data_base
        db_insert.to_db(info_dictionary)

    elif DataCollectors_Configuration.WRITE_TO == CONSTANTS.WRITE_TO_FILE:
        write_single_file(hierarchy_path, info_dictionary)
        #print info_dictionary

    elif DataCollectors_Configuration.WRITE_TO == CONSTANTS.WRITE_TO_MULTIPLE_FILE:
        write_to_multiple_files(hierarchy_path, info_dictionary)


    elif DataCollectors_Configuration.WRITE_TO == CONSTANTS.WRITE_TO_CASSANDRA:

        # inserts (data) in to cassandra database
        insert_into_cassandra.insert(info_dictionary)
    elif DataCollectors_Configuration.WRITE_TO == CONSTANTS.WRITE_TO_BIG_QUERY:
        persist_BigQuery(info_dictionary)
        
