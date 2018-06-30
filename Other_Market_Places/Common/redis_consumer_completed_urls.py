from insert_into_cassandra import persist_Cassandra
import redis_producer_completed_urls
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
                    queue_obj = redis_producer_completed_urls.RedisQueue('completed_links')
                    json_data = queue_obj.get_from_redis()
                except:
                    json_data = None
                if json_data:
                    # print 'in json data'
                    # print json_data
                    data_list.append(json_data + '\n')

            #         out_put_file.write(json_data)

            else:
                list_dic = {}
                for line in data_list:
                    text = json.loads(line)
                    # print line
                    path = text['path']
                    hierarchy = text['hierarchy'].encode('utf-8')
                    url = text['url'].encode('utf-8')
                    data = '{}|{}'.format(hierarchy, url)
                    if path in list_dic:
                        list_dic[path].append(data)

                    else:
                        list_dic[path] = [data]
                self.dic_to_file(list_dic)
                starting_time = time.time()
                data_list = []



    def dic_to_file(self, dic):
        for key in dic:
            file = open(key, 'a+')
            for line in dic[key]:
                file.write(line + '\n')
            file.close()
    # def write_to():
    # time.sleep(REDIS_DELAY)
    # write_to_file()
    # write_to()

if __name__ == '__main__':
    redis_obj = redis_insert()
    redis_obj.write_to_file()

