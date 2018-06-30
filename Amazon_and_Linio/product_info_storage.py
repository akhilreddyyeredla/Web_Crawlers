import DataCollectors_Configuration
import db_insert
import insert_into_cassandra
from Global_Constants import *
from Persist_BigQuery import persist_BigQuery


def write_single_file(hierarchy_path, data,PROJECT_NAME='All_MarketPlaces'):
    file_name = '{}.txt'.format('product_info.txt')
    path = '{}{}{}{}{}{}{}'.format(DataCollectors_Configuration.ROOT_FOLDER,
                                   DataCollectors_Configuration.PATH_STYLE,
                                   PROJECT_NAME,
                                   DataCollectors_Configuration.PATH_STYLE,
                                   hierarchy_path,
                                   DataCollectors_Configuration.
                                   PATH_STYLE,
                                   file_name
                                   )

    write_file = open(path, 'w')
    for line in data:
        write_file.write(line + '\n')


def store(market_place, date, hirarchy, time, info_dictionary):
    """

    :param market_place: Ex: AMAZON_US OR AMAZON_UK
    :param date: Current_date
    :param hirarchy: Hierarchy
    :param time: presnet time in UTC Format
    :param info_dictionary: product details dictionary
    :return: NONE
    """

    hierarchy_name = hirarchy.split('|')
    hierarchy_path = DataCollectors_Configuration.PATH_STYLE.join(hierarchy_name)

    if DataCollectors_Configuration.WRITE_TO == WRITE_TO_DB:

        # inserts (data) in to mysql_data_base
        db_insert.to_db(info_dictionary)

    elif DataCollectors_Configuration.WRITE_TO == WRITE_TO_FILE:
        write_single_file(hierarchy_path, info_dictionary)

        # print(data)
    elif DataCollectors_Configuration.WRITE_TO == WRITE_TO_CASSANDRA:

        # inserts (data) in to cassandra database
        insert_into_cassandra.insert(info_dictionary)

    elif DataCollectors_Configuration.WRITE_TO == WRITE_TO_BIGQUERY:

        # inserts (data) in to cassandra database
        persist_BigQuery(info_dictionary)



