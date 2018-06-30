import json
import time
import Queue
import threading
class completed:
    def __init__(self):
        self.completed_queue = Queue.Queue()
        self.completed_thread = threading.Thread(target=self.completed_function)
        self.completed_thread.daemon = True
        self.completed_thread.start()
        self.past_path = ""
        self.flag = 1
        self.file = ""
        self.count = 0
        print self.count
        self.queue_list = []
    def add_to_queue(self,line):
        self.completed_queue.queue.append(line)
    def completed_function(self):
        while(True):
            if self.completed_queue.qsize() != 0:

                if self.count < 10:
                    print self.count
                    line = self.completed_queue.queue.pop()
                    self.queue_list.append(line)
                    self.count = self.count + 1
                else:
                    #print "else"
                    self.count = 0
                    self.hash_function(self.queue_list)
                    self.queue_list = []
            # elif self.completed_queue.qsize() == 0:
            #     time.sleep(10)
            #     self.hash_function(self.queue_list)
            #     self.count = 0
            #     self.queue_list = []

    def hash_function(self,list):

        list_dic = {}
        for line in list:
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
    def dic_to_file(self,dic):
        for key in dic:
            file = open(key,'a+')
            for line in dic[key]:
                file.write(line +'\n')
            file.close()
            # print list_dic
