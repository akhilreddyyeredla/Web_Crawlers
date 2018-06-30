from Common.Etsy_common_imports import *


class Workers:
    PRODUCTS_PAGE_URLS_QUEUE_FILE = ''

    categories_queue = Queue()
    NUMBER_OF_THREADS = DataCollectors_Configuration.NO_OF_THEARDS
    starting_time = 0
    ending_time = 0
    products_page_url_queue_file = path_CONSTANTS.JEWELRY_QUEUE_PATH
    products_page_url_completed_file = path_CONSTANTS.JEWELRY_COMPLETED_PATH
    products_page_url_skipped_file = path_CONSTANTS.JEWELRY_SKIPPED_PATH

    # these sets are used to store links and avoid dulicapte links
    products_page_url_queue = set()
    products_page_url_completed = set()
    products_page_url_skipped = set()

    def __init__(self):
        print("starting JEWELRY product url collection")
        self.starting_time = time.time()
        self.PRODUCTS_PAGE_URLS_QUEUE_FILE = path_CONSTANTS.ACCESSORIES_QUEUE_PATH
        self.create_workers()
        self.crawl()
        self.products_page_url_queue = file_to_set(self.products_page_url_queue_file)
        self.products_page_url_completed = file_to_set(self.products_page_url_queue_file)
        self.products_page_url_skipped = file_to_set(self.products_page_url_skipped_file)

    # Create worker threads (will die when main exits)
    def create_workers(self):
        for _ in range(self.NUMBER_OF_THREADS):
            t = threading.Thread(target=self.work)
            t.daemon = True
            t.start()
            time.sleep(1)

    # Do the next job in the queue
    #@staticmethod
    def work(self):
        while True:
            url = self.categories_queue.get()
            # If we split it by ',' then we first item in list is hierarchy and second item in the list is
            # product_page_url
            url_split = url.split('|')
            hierarchy = '|'.join(url_split[0:-1])
            product_page_url = url_split[-1]
            # Create object for ProductURLScrapper so that each treadh access different object

            self.visit_page(threading.current_thread().name, hierarchy, product_page_url)
            self.categories_queue.task_done()

    # Each queued link is a new job
    #@staticmethod
    def create_jobs(self):
        # For files in the file iterate through each line and put each link into queue
        for link in file_to_set(self.PRODUCTS_PAGE_URLS_QUEUE_FILE):
            self.categories_queue.put(link)
        self.categories_queue.join()
        self.crawl()

    # Check if there are items in the queue, if so crawl them
    #@staticmethod
    def crawl(self):
        queued_links = file_to_set(self.PRODUCTS_PAGE_URLS_QUEUE_FILE)
        if len(queued_links) > 0:
            # print(str(len(queued_links)) + ' links in the queue')
            self.create_jobs()
        else:
            self.ending_time = time.time()
            total_time = self.ending_time - self.starting_time
            print('Total_time taken to collect JEWELRY category urls: ' + "|Start Time:"+str(self.starting_time)+"| End Time:"+str(self.ending_time)+"|Total Time:"+str(total_time) + 'sec')



    #@staticmethod
    def get_product_links(self,hierarchy, url):
        '''

        :param hierarchy: hierarchy of category
        :param url: product_page url is taken as input and parsed and product_urls are generated
        :return: if urls are present list of product urls or  returns zero
        '''
        response_obj = response_getter.Response()
        response = response_obj.get_content(url)
        if response:
            required_data_1 = response.findAll("div", {
                "class": "js-merch-stash-check-listing block-grid-item v2-listing-card position-relative flex-xs-none "})
            required_data_2 = response.findAll("div", {
                "class": "js-merch-stash-check-listing block-grid-item v2-listing-card position-relative pb-xs-0 "})
            required_data_3 = response.findAll("div", {
                "class": "js-merch-stash-check-listing block-grid-item v2-listing-card position-relative flex-xs-none pb-xs-0 "
            })

            gather_product_link = []

            if len(required_data_1) != 0:
                for links in required_data_1:
                    try:
                        if links is not None:
                            products_urls = links.find("a")['href']

                            hierarchy_products_urls = '{}|{}'.format(hierarchy, products_urls)
                            gather_product_link.append(hierarchy_products_urls)
                    except Exception as e:
                        print_exception('error', 'ETSY', hierarchy, url, e)
                        continue
                return gather_product_link

            elif len(required_data_2) != 0:
                for links in required_data_2:
                    try:
                        if links is not None:
                            products_urls = links.find("a")['href']

                            hierarchy_products_urls = '{}|{}'.format(hierarchy, products_urls)
                            gather_product_link.append(hierarchy_products_urls)
                    except Exception as e:
                        print_exception('error', 'ETSY', hierarchy, url, e)

                        continue
                return gather_product_link
            elif len(required_data_3) != 0:
                for links in required_data_3:
                    try:
                        if links is not None:
                            products_urls = links.find("a")['href']

                            hierarchy_products_urls = '{}|{}'.format(hierarchy, products_urls)
                            gather_product_link.append(hierarchy_products_urls)
                    except Exception as e:
                        print_exception('error', 'ETSY', hierarchy, url, e)
                        continue
                return gather_product_link
            else:
                try:
                    raise ValueError
                except ValueError:
                    print_exception('error', 'ETSY', hierarchy, url, 'ValueError')
                # prin "not found url {}".format(url)

        else:
            return 0


    def save_links(self,thread_name, hierarchy, product_page_url):
        # when hierarchy is splitted whith '|' the last item in list give last page number
        last_page = hierarchy.split('|')[-1]

        completed_urls = []  # to keep Track of urls which are completed
        skipped_urls = []  # to keep track of urls whicha are missed

        for current_page in range(1, int(last_page) + 1):
            if DataCollectors_Configuration.PRODUCT_URL_FLAG == DataCollectors_Configuration.URL_FLAG:  # collect sample urls
                # collect sample urls number equal to mentioned in config file
                if current_page <= DataCollectors_Configuration.NO_OF_PRODUCT_URL_TO_COLLECT:
                    url = '{}&page={}'.format(product_page_url, current_page)

                    # print('{} is visiting :{} '.format(thread_name, url))

                    product_urls = self.get_product_links(hierarchy, url)
                else:
                    break
            else:
                url = '{}&page={}'.format(product_page_url, current_page)

                # print('{} is visiting :{} '.format(thread_name, url))

                product_urls = self.get_product_links(hierarchy, url)
            # if product _urls value is zero then their wrong with url so add that url to skiiped_list so that we can
            # verify later else their is nothing wrong we can continue
            if product_urls == 0:
                skipped_url = '{}|{}'.format(hierarchy, url)
                skipped_urls.append(skipped_url)
                continue
            else:
                hierarchy_path = hierarchy.split('|')
                completed_url = '{}|{}'.format(hierarchy, url)
                completed_urls.append(completed_url)
                full_path_queue = '{}{}{}{}{}'.format(DataCollectors_Configuration.ETSY_URL_ROOT_FOLDER,
                                                      DataCollectors_Configuration.PATH_STYLE,
                                                      DataCollectors_Configuration.PATH_STYLE.join(hierarchy_path[2:-1]),
                                                      DataCollectors_Configuration.PATH_STYLE, DataCollectors_Configuration.PODUCTS_PAGE)
                full_path_completed = '{}{}{}{}{}'.format(
                    DataCollectors_Configuration.ETSY_URL_ROOT_FOLDER,
                    DataCollectors_Configuration.PATH_STYLE,
                    DataCollectors_Configuration.PATH_STYLE.join(hierarchy_path[2:-1]),
                    DataCollectors_Configuration.PATH_STYLE,
                    DataCollectors_Configuration.COMPLETED_PAGE
                )
                # write the urls into file and in hierarchy format
                if product_urls:
                    list_to_file(full_path_queue, product_urls)
                    write_file(full_path_completed, '')

        return completed_urls, skipped_urls






    # Updates  fills queue and updates files and collect urls
    #@staticmethod
    def visit_page(self,thread_name, hierarchy, product_page_url):
        if product_page_url not in self.products_page_url_completed:
            if product_page_url not in self.products_page_url_skipped:
                self.update_links(thread_name, hierarchy, product_page_url)

    # Get links and update the files
    #@staticmethod
    def update_links(self,thread_name, hierarchy, product_page_url):
        # print(thread_name + ' now visiting ' + product_page_url)

        completed_links, skipped_links = self.save_links(thread_name, hierarchy, product_page_url)

        if completed_links:
            # if we received completed links then remove current url for queue file and update completed file
            remove_url = '{}|{}'.format(hierarchy, product_page_url)
            self.products_page_url_queue.remove(remove_url)
            self.products_page_url_completed |= set(completed_links)
            self.products_page_url_skipped |= set(skipped_links)

            self.update_files(self.products_page_url_queue,
                                            self.products_page_url_queue_file,
                                            self.products_page_url_completed,
                                            self.products_page_url_completed_file)
            if skipped_links:
                # if there are any skipped links then update those also
                list_to_file(self.products_page_url_skipped_file, skipped_links)
        elif skipped_links:
            # If there are skipped links then write it them in a file
            remove_url = '{}|{}'.format(hierarchy, product_page_url)
            list_to_file(self.products_page_url_skipped_file, skipped_links)
            self.products_page_url_queue.remove(remove_url)
            set_to_file(self.products_page_url_queue_file, self.products_page_url_queue)

    #@staticmethod
    def update_files(self,queu, queue_file, completed, completed_file):

        """

        :param queu:list of urls to be updated
        :param queue_file: path of file to updated
        :param completed: list of urls to be updated
        :param completed_file: path of file to ba updated
        :return: NONE
        """

        set_to_file(queue_file, queu)
        set_to_file(completed_file, completed)


def start_collection():
    Workers()
