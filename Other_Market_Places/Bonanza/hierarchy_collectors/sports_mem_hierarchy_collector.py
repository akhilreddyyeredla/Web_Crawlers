from Common.Bonanza_common_imports import *



class Workers:
    def __init__(self):
        self.urls_queue = Queue.Queue()

    def create_workers(self):
        """
        Creates threadpool and with max number of threads mentioned in cinfig file and targets work fucntion
        :return: none
        """
        for _ in range(NO_OF_THEARDS):
            thread = Thread(target=self.work)
            # make the thread daemon to stop the thread when main program exits
            thread.daemon = True
            thread.start()

    def work(self):
        """
        Work is function which gets url from queue and slipt it into hierarchy name and page url
        then pass that url to get_level_1_hierarchy(hierarchy_name, page_url) this function will
        travel recurcivesly and find hierarchy
        :return: None
        """
        while True:
            value = self.urls_queue.get().split('|')
            name = '|'.join(value[0:-1])
            url = value[-1]

            self.find_hierarchy(name, url)  # to call scrapper method which collects all products urls
            self.urls_queue.task_done()



    def find_hierarchy(self, hierarchy, url):
        response_obj = response_getter.Response()
        site = response_obj.get_content(url.replace('search', 'facets'))
        if site:
            sub_category_container = site.find('ul', {'class': 'cat_kids shown'})
            if sub_category_container:
                sub_category_list = sub_category_container.findAll('li')
                if len(sub_category_list) != 0:
                    for sub_category in sub_category_list:
                        category_name = re.sub('[^a-zA-Z0-9&]', '_', sub_category.a.text.strip()).replace('&', 'and')
                        category_url = sub_category.a['href']

                        hierarchy_name = '{}|{}'.format(hierarchy, category_name)
                        self.find_hierarchy(hierarchy_name, category_url)
            else:
                create_project_dir(
                    Bonanza_DataCollectors_Configuration.ROOT_FOLDER_BONANZA_HIERARCHY + "/" + hierarchy.replace("|",
                                                                                                                 "/"))

                # Requesting the URL by replacing facets with the search and replace with the suffix url that is in config

                total_page = response_obj.get_content(url.replace('facets', 'search').replace(URL_SUFFIX, ''))
                try:
                    tot_pages = int(
                        total_page.find_all('div', {'class': 'scroll_progress_bar_container'})[0].get('title').split(
                            ' ')[-1])
                except IndexError:
                    print(url)
                    tot_pages = 1

                main_hierarchy = hierarchy + "|" + str(
                    tot_pages)  # Store the hirerachy_level concat with the page numbers

                urls_list = []

                for page_no in range(1, tot_pages):
                    # page_no == 1 we are collecting the sample_URL
                    if DataCollectors_Configuration.PRODUCT_URL_FLAG == DataCollectors_Configuration.URL_FLAG:
                        # page_no is less than DataCollectors_Configuration.Product_URL_To_Collect
                        if page_no < DataCollectors_Configuration.NO_OF_PRODUCT_URL_TO_COLLECT:
                            page_url = '{}|{}&q[page]={}'.format(main_hierarchy, url, page_no + 1)
                            urls_list.append(page_url)  # appending to the list
                        else:
                            break

                    # append all i.e not sample URL's
                    else:
                        page_url = '{}|{}&q[page]={}'.format(main_hierarchy, url, page_no + 1)
                        urls_list.append(page_url)  # appending

                # Writing into the Queue files
                list_to_file(urls_list,
                             DataCollectors_Configuration.ROOT_FOLDER_BONANZA_HIERARCHY + '/' + hierarchy.split("|")[
                                 0] + '/{}_link_queue.txt'.format(hierarchy.split("|")[0]))
                self.write_hirerachy_file(hierarchy, url)

    def level_1(self, hierarchy, url):
        response_obj = response_getter.Response()
        site = response_obj.get_content(url.replace('search', 'facets'))

        if site:
            sub_category_container = site.find('ul', {'class': 'cat_kids shown'})
            if sub_category_container:
                sub_category_list = sub_category_container.findAll('li')
                if len(sub_category_list) != 0:
                    for sub_category in sub_category_list:
                        category_name = re.sub('[^a-zA-Z0-9&]', '_', sub_category.a.text.strip()).replace('&', 'and')
                        category_url = sub_category.a['href']

                        hierarchy_name = '{}|{}'.format(hierarchy, category_name)

                        line = '{}|{}'.format(hierarchy_name, category_url)

                        self.urls_queue.put(line)
                    self.urls_queue.join()

    def write_hirerachy_file(self, hirerachy, url):
        path = DataCollectors_Configuration.ROOT_FOLDER_BONANZA_HIERARCHY + '/' + hirerachy.split("|")[0]
        # print path
        file_2 = open(path + '/{}_link_completed.txt'.format(hirerachy.split("|")[0]), 'a')
        # print file_2
        file_2.close()

    def name(self, url):
        response_obj = response_getter.Response()
        site = response_obj.get_content(url)
        if site:
            category = site.find_all('div', {'class': 'category_group_container'})[DataCollectors_Configuration.SPORTS_MEM_INDEX]
            main_category_name = site.find_all('div', {'class': 'category_group_container_mid'})[
                DataCollectors_Configuration.SPORTS_MEM_INDEX].find(
                'a').text
            main_category = re.sub('[^a-zA-Z0-9&]', '_', main_category_name).replace('&', 'and')
            if main_category:
                for sub_category in category.find_all('div', {'class': 'sub_category_list'})[0].find_all('a', {'class',
                                                                                                               'link_to_search'}):
                    sub_name = main_category + "|" + re.sub('[^a-zA-Z0-9&]', '_', sub_category.text.strip()).replace(
                        '&', 'and')
                    sub_link = sub_category['href']
                    # print sub_name + "|" + sub_link
                    create_project_dir(
                        DataCollectors_Configuration.ROOT_FOLDER_BONANZA_HIERARCHY + "/" + sub_name.replace("|", "/"))

                    # Requesting the URL by replacing facets with the search and replace with the suffix url that is in
                    # DataCollectors_Configuration
                    total_page = response_obj.get_content(
                        sub_link.replace('facets', 'search').replace(Bonanza_DataCollectors_Configuration.URL_SUFFIX, ''))

                    # tot_pages we will get total pages
                    try:
                        tot_pages = int(total_page.find_all('div', {'class': 'scroll_progress_bar_container'})[0].get(
                            'title').split(' ')[-1])
                    except IndexError:
                        print(url)
                        tot_pages = 1

                    main_hierarchy = sub_name + "|" + str(
                        tot_pages)  # Store the hirerachy_level concat with the page numbers

                    urls_list = []
                    for page_no in range(0, tot_pages):
                        # page_no == 1 we are collecting the sample_URL
                        if DataCollectors_Configuration.PRODUCT_URL_FLAG == DataCollectors_Configuration.URL_FLAG:
                            # page_no is less than DataCollectors_Configuration.Product_URL_To_Collect
                            if page_no < DataCollectors_Configuration.NO_OF_PRODUCT_URL_TO_COLLECT:
                                page_url = '{}|{}&q[page]={}'.format(main_hierarchy, sub_link, page_no + 1)
                                urls_list.append(page_url)  # appending to the list
                            else:
                                break

                        # append all i.e not sample URL's
                        else:
                            page_url = '{}|{}&q[page]={}'.format(main_hierarchy, sub_link, page_no + 1)
                            urls_list.append(page_url)  # appending to the list
                    # Writing into the Queue files
                    list_to_file(urls_list,
                                 DataCollectors_Configuration.ROOT_FOLDER_BONANZA_HIERARCHY + '/' + sub_name.split("|")[
                                     0] + '/{}_link_queue.txt'.format(sub_name.split("|")[0]))
                    self.write_hirerachy_file(sub_name, sub_link)
                    self.level_1(sub_name, sub_link)


def start_hierarchy():
    url = BONANZA_MAIN_URL
    print("SPORTS_MEM Hierarchy Started")
    start = time.time()
    workers_obj = Workers()
    workers_obj.create_workers()

    workers_obj.name(url)
    stop = time.time()
    # print("antiques Hierarchy completed" + str(stop-start))
    print("SPORTS_MEM Hierarchy " + "|" + "Start Time:" + str(start) + "|" + "End Time:" + str(
        stop) + "|" + "Total Duration:" + str(stop - start))
