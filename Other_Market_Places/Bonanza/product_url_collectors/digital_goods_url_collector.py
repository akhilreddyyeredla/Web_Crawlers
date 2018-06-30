from Common.Bonanza_common_imports import *

project_name = DataCollectors_Configuration.BONANZA_PROJECT_NAME



queue_file = '{}/{}/Digital_Goods/Digital_Goods_link_queue.txt'.format(DataCollectors_Configuration.ROOT_FOLDER_BONANZA_HIERARCHY,
                                                             project_name)
completed_file = '{}/{}/Digital_Goods/Digital_Goods_link_completed.txt'.format(
    DataCollectors_Configuration.ROOT_FOLDER_BONANZA_URL, project_name)


# The program  Starts from here
class Workers:

    def __init__(self, to_be_visited):
        self.urls_queue = Queue.Queue()
        self.create_workers()
        self.crawl(to_be_visited)

    #@staticmethod
    # This meathod creates threadpool and target work meathod
    def create_workers(self):
        for _ in range(DataCollectors_Configuration.NO_OF_THEARDS):
            t = Thread(target=Workers.work)
            t.daemon = True
            t.start()

    ## name_url = file_to_dictionary(urls_file)
    @staticmethod
    def work(self):
        while True:
            value = self.urls_queue.get().split('|')
            name = '|'.join(value[0:-2])
            url = value[-1]
            total_page = value[-2]
            # print('visiting_url_|{}'.format(url))

            self.get_product_urls(name, total_page,url)  # to call scrapper method which collects all products urls
            self.urls_queue.task_done()

    # create jobs for workers and wait till all work is finished
    #@staticmethod
    def create_jobs(self,to_be_visited_urls):
        for link in to_be_visited_urls:
            self.urls_queue.put(link)
        self.urls_queue.join()

    # check if links are present in file then create jobs
    #@staticmethod
    def crawl(self,to_be_visited_urls):
        queued_links = to_be_visited_urls
        if len(queued_links) > 0:
            self.create_jobs(to_be_visited_urls)





    def write_hirerachy_file(self,category_name, total_concat):
        path = DataCollectors_Configuration.ROOT_FOLDER_BONANZA_URL + '/' + category_name.replace("|", "/")
        # file = open(path + '/{}_url_completed.txt'.format(path.split("/")[-1]), 'a')
        with open(path + '/{}_url_link.txt'.format(path.split("/")[-1]), 'a') as file_1:
            file_1.write(total_concat + "\n")

    def write_complete_file(self,category_name, url):
        path2 = DataCollectors_Configuration.ROOT_FOLDER_BONANZA_URL + '/' + category_name.split("|")[0]
        with open(path2 + '/{}_link_completed.txt'.format(path2.split("/")[-1]), 'a') as file_2:
            file_2.write(category_name + "|" + url + "\n")

    # This method gets the product url of all dynamical_pages
    #@staticmethod
    def get_product_urls(self,category_name, total_page, url):
        hierarchy_length = str(len(category_name.split("|")))
        dynamic = url
        complete_write = category_name + "|" + total_page
        responce_obj = response_getter.Response()
        dynamic_page = responce_obj.get_content(dynamic)
        if dynamic_page:
            products = dynamic_page.find_all('div', {'class': 'list_style_row'})
            products_1 = dynamic_page.find_all('li', {'class': 'item_title '})
            if len(products) != 0:
                for product in products:
                    product_url = DataCollectors_Configuration.DOMAIN_NAME + product.find('a').get('href')
                    total_concat = DataCollectors_Configuration.PROJECT_NAME + "|" + DataCollectors_Configuration.DOMAIN_NAME + "|" + category_name + "|" + hierarchy_length + "|" + product_url
                    # print total_concat
                    self.write_hirerachy_file(category_name, total_concat)
                self.write_complete_file(complete_write, url)
                # print "Collected and written into the completed files" + '|'+ category_name + "|" + url
            elif len(products_1) != 0:
                for product in products_1:
                    product_url = DataCollectors_Configuration.DOMAIN_NAME + product.find('a').get('href')
                    total_concat = DataCollectors_Configuration.PROJECT_NAME + "|" + DataCollectors_Configuration.DOMAIN_NAME + "|" + category_name + "|" + hierarchy_length + "|" + product_url
                    # print total_concat
                    self.write_hirerachy_file(category_name, total_concat)
                self.write_complete_file(complete_write, url)
                # print "Collected and written into the completed files" +'|'+ category_name + "|" + url


def start_url_collection():
    # To store files data in to memory
    global starting_time
    starting_time = time.time()
    print("started DIGITAL_GOODS urls collection")
    queue_list = Bonanza.file_operations.file_to_list(queue_file)
    completed_list = Bonanza.file_operations.file_to_list(completed_file)
    to_be_visited_urls = queue_list - completed_list

    Workers(to_be_visited_urls)
    ending_time = time.time()
    total_time = ending_time - starting_time
    # print("ANTIQUES urls collected in :" + str(total_time) + " secs")
    print("Digital_Goods urls" + "|" + "Start Time:" + str(starting_time) + "|" + "End Time:" + str(
        ending_time) + "|" + "Total Duration:" + str(total_time))

    # here the product urls collection is finished now start product details collection


