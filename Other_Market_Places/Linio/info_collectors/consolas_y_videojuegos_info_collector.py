from Common.Linio_Mex_common_imports import *


class Workers:
    def __init__(self):
        self.urls_queue = Queue()
        self.completed_obj = completed_queue.completed()

    def create_workers(self):
        """
        Creates threadpool and with max number of threads mentioned in DataCollectors_Configuration file and targets work function
        :return: none
        """
        for _ in range(DataCollectors_Configuration.NO_OF_THEARDS):
            thread = Thread(target=self.work)
            # make the thread daemon to stop the thread when main program exits
            thread.daemon = True
            thread.start()


    def work(self):
        """
        Work is function which get urls from queue and calls get_products_urls(hierarchy|url)
        :return: None
        """
        while True:
            value = self.urls_queue.get()

            self.get_product_info(value)  # to call get_products method which collects all products urls
            self.urls_queue.task_done()

    def get_product_info(self,hierarchy_url):
        """

        :param hierarchy_url: string in this format 'hierarchy|page_url"
        :return: None
        :working : requsts the url and then find last page and call's traverse_page function
        """
        name_list = hierarchy_url.split('|')
        hierarchy_name = '|'.join(name_list[0:-1])

        page_url = name_list[-1]

        # urls_list = []

        hierarchy_path = '/'.join(name_list[2:-1])
        completed_path = '{}{}{}'.format(DataCollectors_Configuration.LINIO_MEX_INFO_ROOT,
                                         DataCollectors_Configuration.PATH_STYLE, hierarchy_path)

        response_obj = Response()
        response = response_obj.get_content(page_url)
        store_obj = product_info_storage.store()
        if response:
            product_data_obj = consolas_y_videojuegos_get_details()
            data, date, time = product_data_obj.get_details(hierarchy_url, response)

            if data:
                store_obj.store_options(Linio_Mex_config.MARKETPLACE, date, hierarchy_name, time, data)
                file_path = '{}/{}'.format(completed_path, COMPLETED_INFO_FILE)
                # print file_path
                json_data = {'path':file_path,'hierarchy':hierarchy_name,'url':page_url}
                json_line = json.dumps(json_data)
                self.completed_obj.add_to_queue(json_line)
                #linio_mex_append_to_file(file_path, hierarchy_url)

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


    def start_info_collection(self, folder_name, worker_obj):
        """

        :param folder_name: category_folder name
        :return: None
        """
        queue_path = '{}{}{}'.format(DataCollectors_Configuration.LINIO_MEX_URL_ROOT,
                                     DataCollectors_Configuration.PATH_STYLE, folder_name)
        queue_files = self.get_all_files(queue_path, DataCollectors_Configuration.PATTERN_3)

        completed_path = '{}{}{}'.format(DataCollectors_Configuration.LINIO_MEX_INFO_ROOT,
                                         DataCollectors_Configuration.PATH_STYLE, folder_name)
        completed_files = self.get_all_files(completed_path, DataCollectors_Configuration.PATTERN_4)

        completed_set = set()
        for files in completed_files:
            if os.path.exists(files):
                links = linio_mex_file_to_set(files)
                for link in links:
                    completed_set.add(link)
                    # print link

        for files in queue_files:
            if os.path.exists(files):
                for url in linio_mex_file_to_set(files):
                    # print(url)
                    url_split = url.split('|')
                    hierarchy_path = '/'.join(url_split[2:-1])
                    if url in completed_set:
                        # print url
                        pass
                    else:

                        completed_path = '{}{}{}'.format(DataCollectors_Configuration.LINIO_MEX_INFO_ROOT,
                                                         DataCollectors_Configuration.PATH_STYLE, hierarchy_path)

                        if os.path.exists(completed_path):

                            pass

                        else:
                            linio_mex_create_project_dir(completed_path)
                        worker_obj.urls_queue.put(url)

                            # get_product_urls(line)
        worker_obj.urls_queue.join()


def start_program(folder_name):
    """
    :param folder_name: category_folder name
    :return
    """

    print('started {} info collection').format(folder_name)
    start_time = time.time()

    # creates threadpool
    worker_obj = Workers()
    worker_obj.create_workers()

    # call this function to start url collection

    worker_obj.start_info_collection(folder_name,worker_obj)

    end_time = time.time()
    total_time = end_time - start_time
    print '{}_info_collection|started-{}|ended-{}|total_time_taken-{} '.format(folder_name, start_time, end_time, total_time)


