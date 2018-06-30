from insert_into_cassandra import persist_Cassandra
import redis_insert
import threading
import json
from Queue import Queue
from Souq_DataCollectors_configuration import REDIS_OUTPUT_PATH, REDIS_DELAY
import time
import datetime


# out_put_file  = open(REDIS_OUTPUT_PATH.format(time.time()),'w')
class redis_insert:
    def __init__(self):
        pass

    def write_to_file(self):
        starting_time = time.time()
        # title = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
        # out_put_file  = open(REDIS_OUTPUT_PATH.format(title),'w')
        data_list = []
        while True:

            time_lapsed = time.time() - starting_time
            if int(time_lapsed) < REDIS_DELAY:
                # print int(time_lapsed) , REDIS_DELAY
                # out_put_file  = open(REDIS_OUTPUT_PATH.format(time.time()),'w')
                try:
                    queue_obj = redis_insert.RedisQueue('cassandra')
                    json_data = queue_obj.get_from_redis()
                except:
                    json_data = None
                if json_data:
                    # print 'in json data'
                    # print json_data
                    data_list.append(json_data + '\n')

            #         out_put_file.write(json_data)

            else:
                title = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
                out_put_file = open(REDIS_OUTPUT_PATH.format(title), 'w')
                # print len(data_list)
                for data in data_list:
                    # print data
                    # print title
                    out_put_file.write(data)
                time.sleep(10)
                data_list = []
                out_put_file.close()
                print ' ****** wrote to file *******'
                starting_time = time.time()

    # def write_to():
    # time.sleep(REDIS_DELAY)
    # write_to_file()
    # write_to()

if __name__ == '__main__':
    redis_obj = redis_insert()
    redis_obj.write_to_file()

