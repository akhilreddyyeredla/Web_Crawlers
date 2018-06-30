from Common.Souq_common_imports import *


class Workers:
    NUMBER_OF_THREADS = DataCollectors_Configuration.NO_OF_THEARDS
    categories_queue = Queue.Queue()
    starting_time = 0
    ending_time = 0

    def __init__(self, ):
        #self.completed_queue = Queue.Queue()
        self.create_workers()
        self.completed_queue_obj = completed_queue.completed()
        #self.completed_thread = threading.Thread(target=self.completed_function)
        #self.completed_thread.daemon = True
        #self.flag = 0

    # Create worker threads (will die when main exits)
    def create_workers(self):
        for _ in range(Workers.NUMBER_OF_THREADS):
            t = threading.Thread(target=self.work)
            t.daemon = True
            t.start()

    # Do the next job in the queue
    #@staticmethod
    def work(self):
        while True:
            url = Workers.categories_queue.get()
            # If we split it by '|' then 0:-1 is hierarchy and -1 is a url
            # product_page_url
            url_split = url.split('|')
            hierarchy = '|'.join(url_split[0:-1])
            product_page_url = url_split[-1]
            info_completed_path = DataCollectors_Configuration.SOUQ_INFO_ROOT_FOLDER + DataCollectors_Configuration.PATH_STYLE + hierarchy.replace(
                '|', '/') + '/' + DataCollectors_Configuration.ELECTRONICS
            if not os.path.exists(info_completed_path):
                os.makedirs(info_completed_path.replace('\\', '/'))

            completed_path = '{}{}{}{}{}'.format(DataCollectors_Configuration.SOUQ_INFO_ROOT_FOLDER,

                                                 DataCollectors_Configuration.PATH_STYLE,
                                                 hierarchy.replace('|', '/'),
                                                 DataCollectors_Configuration.PATH_STYLE,
                                                 DataCollectors_Configuration.COMPLETED_PAGE
                                                 )

            f = open(completed_path, 'a+')
            f.close()

            # save_date is method which parsers the url and store it into db so that each thread access different object

            self.save_data(threading.current_thread().name, hierarchy, product_page_url)
            Workers.categories_queue.task_done()

    # Put all urls into queue and data is collected from all the urls
    #@staticmethod
    def collect_all_data(self,urls_list):
        for link in urls_list:
            Workers.categories_queue.put(link)
        Workers.categories_queue.join()

    # Check if there are items in the queue, if so crawl them
    #@staticmethod
    def crawl(self,urls_list):
        """
        :param urls_list: file loaction of product_urls.txt
        :return: none
        """
        queued_links = urls_list
        # If flag is equal to constant flag then collect sample data else collect all data
        if len(queued_links) > 0:
            self.collect_all_data(urls_list)


    # Save data in file or in dataBase



    def save_data(self, thread_name, hierarchy, url):
        """

        :param thread_name: name of current thread
        :param hierarchy: hierarchy of category
        :param url: product url which is parsed and save data in either file or database based on configuration
        :return: none
        """
        starting_time = time.time()

        # Raw_data is beautifulSoup object and it is passed through "get_data" to collect data
        response_obj = response_getter.Response()
        raw_data, status = response_obj.get_page_soup(url)
        if raw_data:
            # get product information as tuple
            data_obj = Electronics_ProductDetails()
            data = data_obj.get_data(raw_data, hierarchy, url)
            # print data

            hierarchy_name = hierarchy.split('|')
            hierarchy_path = DataCollectors_Configuration.PATH_STYLE.join(hierarchy_name)

            today_date = date.today()
            present_time = time.time()

            # Store the data externally
            store_obj = product_info_storage.store()
            store_obj.store_options(market_place=DataCollectors_Configuration.PROJECT_NAME, date=today_date, time=present_time,
                                    info_dictionary=data, hirarchy=hierarchy)

            # ending_time = time.time()
            # total_time = ending_time - starting_time

            completed_path = '{}{}{}{}{}'.format(DataCollectors_Configuration.SOUQ_INFO_ROOT_FOLDER,

                                                 DataCollectors_Configuration.PATH_STYLE,
                                                 hierarchy_path,
                                                 DataCollectors_Configuration.PATH_STYLE,
                                                 DataCollectors_Configuration.COMPLETED_PAGE
                                                 )
            #print hierarchy_path
            f = open(completed_path, 'a+')
            f.close()

            #line = (completed_path + "@" + hierarchy + "@" + url)
            text = {'path':completed_path,'hierarchy':hierarchy,'url':url}
            json_text = json.dumps(text)

            self.completed_queue_obj.add_to_queue(json_text)
            # if self.flag == 0:
            #     self.completed_thread.start()
            #     self.flag = 1

    # def completed_function(self):
    #
    #     while (self.completed_queue.qsize() != 0):
    #
    #         line = self.completed_queue.queue.pop()
    #         text = line.split('@')
    #         path = text[0]
    #         hierarchy = text[1]
    #         url = text[2]
    #         append_to_file(path, '{}|{}'.format(hierarchy, url))
    #         if self.completed_queue.qsize() > 10:
    #             pass
    #         else:
    #             time.sleep(10)
    #     if self.completed_queue.qsize() == 0:
    #         self.completed_function()

        # print('{} has completed {}|{}|thread_staring_time:{}|thread_ending_time:{}|total_time:{}sec'.format(
            #     thread_name,
            #     hierarchy,
            #     url,
            #     starting_time,
            #     ending_time,
            #     total_time))

    def get_all_files(self, root, pattern):
        """

        :param root: Root folder location
        :param pattern: pattern of file name which to be searched ex: '*_links.txt' is pattern
        :return: list of paths that matches with pattern
        """
        links_files = []

        # The below lines perform recurvise search of directories in the root folder and returns paths of file which
        # matches the pattern

        for root, dirs, files in os.walk(root):  # os.walk is python library to collect all directories
            for filename in fnmatch.filter(files, pattern):
                links_files.append(os.path.join(root, filename))
        return links_files

    def get_updated_links(self, queue_files, completed_files):
        queue_set = set()
        competed_set = set()

        for files in queue_files:

            count = 1
            for url in file_to_set(files):
                if DataCollectors_Configuration.PRODUCT_INFO_FLAG == DataCollectors_Configuration.PRODUCT_FlAG:
                    # load only sample urls mentioned in config file
                    if count <= DataCollectors_Configuration.NO_OF_PRODUCT_INFO_TO_COLLECT:
                        queue_set.add(url)
                        count = count + 1
                    else:

                        break
                else:
                    queue_set.add(url)

        for files in completed_files:

            count = 1
            for url in file_to_set(files):
                if DataCollectors_Configuration.PRODUCT_INFO_FLAG == DataCollectors_Configuration.PRODUCT_FlAG:
                    # load only sample urls mentioned in config file
                    if count <= DataCollectors_Configuration.NO_OF_PRODUCT_INFO_TO_COLLECT:
                        competed_set.add(url)
                        count = count + 1
                    else:

                        break
                else:
                    competed_set.add(url)
        final_set = queue_set - competed_set
        return final_set

    def get_page_data(self):
        """"
        :param: category is the present working category or folder
            This method is starting point of program It collects all the paths of products urls and iterate over each
            path and collect product info from each url
        """

        path = '{}{}{}'.format(DataCollectors_Configuration.SOUQ_URL_ROOT_FOLDER,
                               DataCollectors_Configuration.PATH_STYLE, DataCollectors_Configuration.ELECTRONICS)
        queue_files = self.get_all_files(root=path, pattern=DataCollectors_Configuration.SOUQ_PATTERN)
        completed_path = '{}{}{}'.format(DataCollectors_Configuration.SOUQ_INFO_ROOT_FOLDER,
                               DataCollectors_Configuration.PATH_STYLE, DataCollectors_Configuration.ELECTRONICS)
        competed_files = self.get_all_files(root=completed_path, pattern=DataCollectors_Configuration.PATTERN_2)
        urls_list = self.get_updated_links(queue_files, competed_files)
        self.crawl(urls_list)


def start_info_collection():
    print('starting Electronics information collection')
    starting_time = time.time()
    obj_info = Workers()
    obj_info.get_page_data()
    ending_time = time.time()
    total_time = ending_time - starting_time
    print('Electronics_info_collection:' + "|" + "Start Time:" + str(
        starting_time) + "|" + "End Time:" + str(ending_time) + "|" + "Total Duration:" + str(total_time) + ' sec')
