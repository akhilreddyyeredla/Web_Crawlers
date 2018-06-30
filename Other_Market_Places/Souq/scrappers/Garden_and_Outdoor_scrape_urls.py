from Common.Souq_common_imports import *





# class Paths(object):
#     def __int__(self):
#         self.project_name_url = DataCollectors_Configuration.SOUQ_URL_ROOT_FOLDER
#         self.project_name_info = DataCollectors_Configuration.SOUQ_INFO_ROOT_FOLDER
#         self.project_name = CONSTANTS.PROJECT_NAME
#         # Queue to impliment threadpool
#         self.urls_queue = Queue.Queue()
#
#         # To store File paths
#         self.queue_file = Souq.path_CONSTANTS.Garden_and_Outdoor_QUEUE_FILE
#         self.completed_file = Souq.path_CONSTANTS.Garden_and_Outdoor_COMPLETED_FILE
#         self.skipped_file = Souq.path_CONSTANTS.Garden_and_Outdoor_SKIPPED_FILE
#
#         # To store files data in to memory
#         self.queue_list = Souq.file_operations.file_to_list(self.queue_file)
#         self.completed_list = Souq.file_operations.file_to_list(self.completed_file)
#         self.skipped_list = Souq.file_operations.file_to_list(self.skipped_file)
#         self.starting_time = 0
#         self.ending_time = 0



# name_url = file_to_dictionary(URLS_FILE)

# The program  Starts from here
class Workers():


    def __init__(self):
        #print "in init"
        self.project_name_url = DataCollectors_Configuration.SOUQ_URL_ROOT_FOLDER
        self.project_name_info = DataCollectors_Configuration.SOUQ_INFO_ROOT_FOLDER
        self.project_name = DataCollectors_Configuration.PROJECT_NAME
        # Queue to impliment threadpool
        self.urls_queue = Queue.Queue()

        # To store File paths
        self.queue_file = Souq.path_CONSTANTS.Garden_and_Outdoor_QUEUE_FILE
        self.completed_file = Souq.path_CONSTANTS.Garden_and_Outdoor_COMPLETED_FILE
        self.skipped_file = Souq.path_CONSTANTS.Garden_and_Outdoor_SKIPPED_FILE

        # To store files data in to memory
        self.queue_list = Souq.file_operations.file_to_list(self.queue_file)
        self.completed_list = Souq.file_operations.file_to_list(self.completed_file)
        self.skipped_list = Souq.file_operations.file_to_list(self.skipped_file)


        self.starting_time = time.time()
        print("started Garden_and_Outdoor urls collection")
        self.create_workers()
        self.crawl()

    # @staticmethod
    # This meathod creates threadpool and target work meathod
    def create_workers(self):
        #print "Create"
        for _ in range(DataCollectors_Configuration.NO_OF_THEARDS):

            t = Thread(target=self.work)
            t.daemon = True
            t.start()

    # name_url = file_to_dictionary(urls_file)
    # @staticmethod
    def work(self):

        #print("Work")
        while True:
            #print "in while"
            #print path_obj.urls_queue.get()
            value = self.urls_queue.get().split('|')
            name = '|'.join(value[0:-1])
            #print name
            create_project_dir(self.project_name_url + '/' + name.replace('|', '/'))
            #create_project_dir(self.project_name_info + '/' + name.replace('|', '/'))
            url = value[-1]
            self.scrapper(name, url)  # to call scrapper method which collects all products urls
            self.urls_queue.task_done()
    # create jobs for workers and wait till all work is finished
    # @staticmethod
    def create_jobs(self):
        for link in file_to_list(self.queue_file):
            #print link
            self.urls_queue.put(link)
            self.urls_queue.join()
        self.crawl()
    # check if links are present in file then create jobs
    # @staticmethod
    def crawl(self):
        queued_links = file_to_list(self.queue_file)
        if len(queued_links) > 0:
            self.create_jobs()
        else:
            ending_time = time.time()
            total_time = str(ending_time - self.starting_time)
            print('Garden_and_Outdoor urls collected in :' + "|" + "Start Time:" + str(
                self.starting_time) + "|" + "End Time:" + str(ending_time) + "|" + "Total Duration:" + str(
                total_time) + ' secs')
            # here the product urls collection is finished now start product details collection
    # @staticmethod
    def get_product_urls(self, category_name, url):

        # Getting links from the url.
        out_filename = [category_name.replace('|', '/'), '{}_links.txt'.format(category_name.split('|')[-1])]
        urls_list = []
        iterator = 2  # should increment page numbers from 2 page
        base_url = url
        sent_url = url
        file_line = '{}|{}'.format(category_name, url)
        while True:
            #print sent_url
            # Get soup object and receivied url.
            response_obj = response_getter.Response()
            page_soup, received_url = response_obj.get_page_soup(sent_url)
            if not page_soup:
                # is retturn value is none then the their is error in link so skip that link and continue
                sent_url = '{}{}{}'.format(base_url, "&section=2&page=", iterator)

                iterator = iterator + 1
                try:
                    self.queue_list.remove(file_line)
                    self.skipped_list.add(file_line)
                    self.update_files(self.queue_list, self.queue_file, self.skipped_list,
                                      self.skipped_file)
                    continue
                except KeyError as e:
                    print_exception('error', 'Souq', category_name, url, e)
                    # print e
                    # print sent_url
                    self.skipped_list.add(file_line)
                    self.update_files(self.queue_list, self.queue_file, self.skipped_list,
                                      self.skipped_file)
                    continue
            elif page_soup == DataCollectors_Configuration.BAD_STATUS:
                # If page soup is bad status then ther are no pages to iterate
                try:
                    self.queue_list.remove(file_line)
                    self.completed_list.add(file_line)
                    self.update_files(self.queue_list, self.queue_file, self.completed_list,
                                      self.completed_file)
                    break
                except KeyError as e:
                    print_exception('error', 'Souq', category_name, url, e)
                    # print e
                    # print sent_url
                    self.completed_list.add(file_line)  # add url to completed
                    self.update_files(self.queue_list, self.queue_file, self.completed_list,
                                      self.completed_file)
                    break
            elif sent_url == received_url:
                # collect sample urls
                if DataCollectors_Configuration.PRODUCT_URL_FLAG == DataCollectors_Configuration.PRODUCT_FlAG:
                    # collect no_of sample urls as mentioned in DataCollectors_Configuration file
                    if iterator <= DataCollectors_Configuration.NO_OF_PRODUCT_URL_TO_COLLECT:
                        # create next page url
                        sent_url = '{}{}{}'.format(base_url, "&section=2&page=", iterator)
                        iterator = iterator + 1
                        container = page_soup.find_all('div',
                                                       {'class': 'column column-block block-grid-large single-item'})
                        # Scan the page and collect product urls
                        for product_container in container:
                            links = product_container.find('a')  # search for anchor tags in the html response
                            product_url = links['href']
                            urls_list.append(category_name + '|' + product_url + '\n')
                        Souq.file_operations.dictionary_to_file(out_filename, urls_list)
                    else:
                        try:
                            self.queue_list.remove(file_line)  # remove url present in queue
                            self.completed_list.add(file_line)  # add url to completed
                            self.update_files(self.queue_list, self.queue_file,
                                              self.completed_list, self.completed_file)
                            break
                        except Exception as e:
                            print_exception('error', 'Souq', category_name, url, e)
                            # print e
                            # print sent_url
                            self.completed_list.add(file_line)  # add url to completed
                            self.update_files(self.queue_list, self.queue_file,
                                              self.completed_list,self.completed_file)
                            break
                else:
                    # create next page url
                    sent_url = '{}{}{}'.format(base_url, "?section=2&page=", iterator)
                    iterator = iterator + 1
                    container = page_soup.find_all('div',
                                                   {'class': 'column column-block block-grid-large single-item'})
                    # Scan the page and collect product urls
                    for product_container in container:
                        links = product_container.find('a')  # search for anchor tags in the html response
                        product_url = links['href']
                        urls_list.append(category_name + '|' + product_url + '\n')
                    Souq.file_operations.dictionary_to_file(out_filename, urls_list)
            else:
                try:
                    # Write product urls to file and update files.
                    self.queue_list.remove(file_line)  # remove url present in queue
                    self.completed_list.add(file_line)  # add url to completed
                    self.update_files(self.queue_list, self.queue_file, self.completed_list,
                                      self.completed_file)
                    break
                except Exception as e:
                    print_exception('error', 'Souq', category_name, url, e)
                    # print e
                    # print sent_url
                    self.completed_list.add(file_line)
                    self.update_files(self.queue_list, self.queue_file, self.skipped_list,
                                      self.skipped_file)
                    break

    # This meathod checks wheter the given link new or old if its is present in completed file then it skips
    # @staticmethod
    def scrapper(self, name, url):
        if url not in self.completed_list:
            self.get_product_urls(name, url)
    # @staticmethod
    def update_files(self, old_list, old_file, new_list, new_file):
        Souq.file_operations.list_to_file(old_list, old_file)
        Souq.file_operations.list_to_file(new_list, new_file)


def start_url_collection():

    #print path_obj.queue_file
    Workers()
