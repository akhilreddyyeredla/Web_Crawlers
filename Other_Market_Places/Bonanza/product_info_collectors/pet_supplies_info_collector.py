from Common.Bonanza_common_imports import *


class Workers:


    def __init__(self, ):
        self.NUMBER_OF_THREADS = DataCollectors_Configuration.NO_OF_THEARDS
        self.categories_queue = Queue.Queue()
        self.starting_time = 0
        self.ending_time = 0
        print('starting PET_SUPPLIES information collection')
        self.completed_obj = completed_queue.completed()
        Workers.starting_time = time.time()
        self.create_workers()

    # Create worker threads (will die when main exits)
    def create_workers(self):
        for _ in range(self.NUMBER_OF_THREADS):
            t = threading.Thread(target=Workers.work)
            t.daemon = True
            t.start()

    # Do the next job in the queue
    # @staticmethod
    def work(self):
        while True:
            url = self.categories_queue.get()
            # If we split it by '|' then 2:-2 is hierarchy and -1 is a url
            # product_page_url
            url_split = url.split('|')
            hierarchy = '|'.join(url_split[2:-2])
            product_page_url = url_split[-1]
            # save_date is method which parsers the url and store it into db so that each thread access different object

            self.save_data(threading.current_thread().name, hierarchy, product_page_url)
            self.categories_queue.task_done()

    # Put all urls into queue and data is collected from all the urls
    # @staticmethod
    def collect_all_data(self, urls_list):
        for link in urls_list:
            self.categories_queue.put(link)
        self.categories_queue.join()
        # Workers.crawl(urls_list)

    def crawl(self, urls_list):
        """

        :param urls_list: file location of product_urls.txt
        :return: none
        """
        queued_links = urls_list
        # If flag is equal to constant flag then collect sample data else collect all data
        if len(queued_links) > 0:
            # print(str(len(queued_links)) + ' links in the queue')
            self.collect_all_data(urls_list)
        else:
            self.ending_time = time.time()
            total_time = self.ending_time - self.starting_time
            # print('Total_time taken to collect antiques category products:' + str(total_time) + ' sec')
            print("PET_SUPPLIES_info_completed" + "|" + "Start Time:" + str(self.starting_time) + "|" + "End Time:" + str(
                self.ending_time) + "|" + "Total Duration:" + str(total_time))


    def save_data(self, thread_name, hierarchy, url):
        """
        :param thread_name: name of current thread
        :param hierarchy: hierarchy of category
        :param url: product url which is parsed and save data in either file or database based on DataCollectors_Configu
        ration
        :return: none
        """
        starting_time = time.time()

        # Raw_data is beautifulSoup object and it is passed through "get_data" to collect data
        response_obj = response_getter.Response()
        raw_data = response_obj.get_content(url)
        if raw_data:
            # get product information as tuple

            obj = pet_supplies_parser_collector.ProductDetails()
            data = obj.get_details(raw_data, hierarchy, url)
            hierarchy_name = hierarchy.split('|')
            hierarchy_path = DataCollectors_Configuration.PATH_STYLE.join(hierarchy_name)

            today_date = date.today()
            present_time = time.time()

            # Store the data externally
            storage(market_place=DataCollectors_Configuration.BONANZA_PROJECT_NAME, date=today_date, time=present_time,
                    info_dictionary=data, hirarchy=hierarchy)

            ending_time = time.time()
            total_time = ending_time - starting_time

            market_place = DataCollectors_Configuration.PROJECT_NAME
            Domain_name = DataCollectors_Configuration.DOMAIN_NAME
            hierarchy_length = len(hierarchy_name)
            hierarchy_path = DataCollectors_Configuration.PATH_STYLE.join(hierarchy_name)

            completed_path = '{}{}{}{}{}'.format(DataCollectors_Configuration.ROOT_FOLDER_BONANZA_INFO,
                                                 DataCollectors_Configuration.PATH_STYLE,
                                                 hierarchy_path,
                                                 DataCollectors_Configuration.PATH_STYLE,
                                                 DataCollectors_Configuration.COMPLETED_INFO_FILE)
            line = '{}|{}|{}|{}'.format(market_place, Domain_name, hierarchy, hierarchy_length)
            json_data = {'path': completed_path, 'hierarchy': line, 'url': url}
            json_line = json.dumps(json_data)
            self.completed_obj.add_to_queue(json_line)
            # print('{} has completed {}|{}|thread_staring_time:{}|thread_ending_time:{}|total_time:{}sec'.format(
            #     thread_name,
            #     hierarchy,
            #     url,
            #     starting_time,
            #     ending_time,
            #     total_time))
            #

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
                    # load only sample urls mentioned in DataCollectors_Configuration file
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
                    # load only sample urls mentioned in DataCollectors_Configuration file
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
        queue_path = '{}{}{}'.format(DataCollectors_Configuration.ROOT_FOLDER_BONANZA_URL,
                                     DataCollectors_Configuration.PATH_STYLE, DataCollectors_Configuration.ANTIQUES_INFO)
        competed_path = '{}{}{}'.format(DataCollectors_Configuration.ROOT_FOLDER_BONANZA_INFO,
                                        DataCollectors_Configuration.PATH_STYLE, DataCollectors_Configuration.ANTIQUES_INFO)

        queue_files = self.get_all_files(root=queue_path, pattern=DataCollectors_Configuration.BONANZA_PATTERN_3)
        competed_files = self.get_all_files(root=competed_path, pattern=DataCollectors_Configuration.BONANZA_PATTERN_4)

        urls_list = self.get_updated_links(queue_files, competed_files)

        workers_obj = Workers()
        workers_obj.crawl(urls_list)


def start_info_collection():
    product_info = Workers()
    product_info.get_page_data()
