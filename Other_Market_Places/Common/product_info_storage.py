import Souq_DataCollectors_configuration as DataCollectors_Configuration
import db_insert
from insert_into_cassandra import persist_Cassandra
from Global_Constants import *
from Persist_BigQuery import persist_BigQuery
from insert_into_kafka import persist_kafka
import redis_insert
import json
import os
class single_file():
    def __init__(self):
        pass

    def write_single_file(slef,hierarchy_path, data, PROJECT_NAME='All_MarketPlaces'):
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


class store():
    def __init__(self):
        pass
    def store_options(self,market_place, date, hirarchy, time, info_dictionary):
        """

        :param market_place: Ex: AMAZON_US OR AMAZON_UK
        :param date: Current_date
        :param hirarchy: Hierarchy
        :param time: presnet time in UTC Format
        :param info_dictionary: product details dictionary
        :return: NONE
        """
        # print info_dictionary
        hierarchy_name = hirarchy.split('|')
        hierarchy_path = DataCollectors_Configuration.PATH_STYLE.join(hierarchy_name)

        if DataCollectors_Configuration.WRITE_TO == WRITE_TO_DB:

            # inserts (data) in to mysql_data_base
            db_insert.to_db(info_dictionary)

        elif DataCollectors_Configuration.WRITE_TO == WRITE_TO_FILE:
            single_file_obj = single_file()
            single_file_obj.write_single_file(hierarchy_path, info_dictionary)

            # print(data)
        elif DataCollectors_Configuration.WRITE_TO == WRITE_TO_CASSANDRA:

            # inserts (data) in to cassandra database
            persist_Cassandra(info_dictionary)

        elif DataCollectors_Configuration.WRITE_TO == WRITE_TO_BIGQUERY:

            persist_BigQuery(info_dictionary)
        elif DataCollectors_Configuration.WRITE_TO == WRITE_TO_KAFKA:
            persist_kafka(info_dictionary)


        elif DataCollectors_Configuration.WRITE_TO == WRITE_TO_REDIS:
            data = json.dumps(info_dictionary)


            queue_obj = redis_insert.RedisQueue('cassandra')
            queue_obj.put_into_redis(data)
