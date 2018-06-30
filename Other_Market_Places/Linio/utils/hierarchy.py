from Common.Linio_Mex_common_imports import *


class Worker:
    def __init__(self):
        self.urls_queue = Queue()
        self.create_workers()

    def create_workers(self):
        """
        Creates threadpool and with max number of threads mentioned in config file and targets work fucntion
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
        then pass that url to second_level_hierarchy(hierarchy_name, page_url) this function will
        travel recurcivesly and find hierarchy
        :return: None
        """
        while True:
            value = self.urls_queue.get().split('|')
            name = '|'.join(value[0:-1])
            url = value[-1]

            self.second_level_hierarchy(name, url)  # to call scrapper method which collects all products urls
            self.urls_queue.task_done()



    def create_project_dir(self, directory):
        if not os.path.exists(directory):
            # print('Creating directory ' + directory)
            os.makedirs(directory)


    def find_last_level(self, page_container):
        nav_container = page_container.find('li', {'class': 'active has-children'})
        if nav_container:
            return self.find_last_level(nav_container)
        else:
            return page_container

    def find_last_page(self,page_container):
        page_tags = page_container.find_all('li', {'class': 'page-item'})

        try:
            return int(page_tags[-1].a['href'].split('page=')[-1])
        except Exception:
            return 1


    def create_path(self, hierarchy):
        hierarchy_list = hierarchy.split('|')

        path = '{}/{}'.format(LINIO_MEX_HIERARCHY_ROOT, '/'.join(hierarchy_list[2:]))

        return path


    def second_level_hierarchy(self, hierarchy, url):
        response_obj = Response()
        page_container = response_obj.get_content(url)
        if page_container:
            nav_container = page_container.find('li', {'class': 'active has-children'})

            if nav_container:
                # print nav_container.prettify()
                last_nav_container = self.find_last_level(nav_container)
                if last_nav_container:
                    link_containers_1 = last_nav_container.find_all('li', {'class': 'has-children'})
                    link_containers_2 = last_nav_container.find_all('li', {'class': ' '})
                    if len(link_containers_1) > 0:

                        for link_container in link_containers_1:
                            url_tag = link_container.find('a')
                            page_url = '{}{}'.format(linio_mex_main_url, url_tag['href'])
                            category_name = url_tag.span.text.encode('utf-8').strip().replace(',', '').replace(' ', '_')
                            # hierarchy_list = hierarchy.split('|')
                            hierarchy_name = '{}|{}'.format(hierarchy, category_name)
                            # print hierarchy_name
                            self.second_level_hierarchy(hierarchy_name, page_url)

                    elif len(link_containers_2) > 0:
                        for link_container in link_containers_2:
                            url_tag = link_container.find('a')
                            page_url = '{}{}'.format(linio_mex_main_url, url_tag['href'])
                            category_name = url_tag.span.text.encode('utf-8').strip().replace(',', '').replace(' ', '_')

                            hierarchy_name = '{}|{}'.format(hierarchy, category_name)

                            path = self.create_path(hierarchy_name)
                            if os.path.exists(path):
                                # print 'exits'
                                pass
                            else:
                                last_page = self.find_last_page(page_container)

                                last_level_line = '{}|{}|{}'.format(hierarchy_name, last_page, page_url)
                                # print last_level_line
                                linio_mex_create_directory_and_hierarchy_files(path, last_level_line)
                    else:
                        hierarchy_name = '{}'.format(hierarchy)

                        path = self.create_path(hierarchy_name)
                        if os.path.exists(path):
                            # print 'exits'
                            pass
                        else:
                            last_page = self.find_last_page(page_container)

                            last_level_line = '{}|{}|{}'.format(hierarchy_name, last_page, url)
                            # print last_level_line
                            linio_mex_create_directory_and_hierarchy_files(path, last_level_line)

    def moda_level(self, hierarchy, content_containers, worker_obj):
        for content_container in content_containers:

            dev_containers = content_container.find_all('div', recursive=False)

            for dev_container in dev_containers:
                anchor_tag = dev_container.find('a', {'class': 'canvas'})
                if anchor_tag:
                    page_url = '{}{}'.format(linio_mex_main_url, anchor_tag['href'])
                    response_obj = Response()
                    res_container = response_obj.get_content(page_url)

                    category_container = dev_container.find('div', {'class': 'banner-menu'})
                    img_container = dev_container.find('img')

                    if category_container:
                        category_name = category_container.h2.text.encode('utf-8').strip().replace(',', '').replace(' ',
                                                                                                                    '_')

                        hierarchy_name = '{}|{}'.encode('utf-8').format(hierarchy, category_name)

                    elif img_container:
                        category_name = img_container['title'].encode('utf-8').strip().replace(',', '').replace(' ', '_')

                        hierarchy_name = '{}|{}'.encode('utf-8').format(hierarchy, category_name)

                    if res_container:
                        content_containers_1 = res_container.find_all('div', {'class': 'banner-fashion-layout-1'})
                        content_containers_2 = res_container.find_all('div', {'class': 'banner-fashion-layout-6'})
                        content_containers_3 = res_container.find_all('div', {'class': 'banner-fashion-layout-7'})
                        content_containers_4 = res_container.find_all('div', {'class': 'banner-fashion-layout-4'})
                        if content_containers_1:
                            self.first_level_hierarchy(hierarchy_name, content_containers_1, worker_obj)
                        if content_containers_2:
                            self.first_level_hierarchy(hierarchy_name, content_containers_2, worker_obj)
                        if content_containers_3:
                            self.first_level_hierarchy(hierarchy_name, content_containers_3, worker_obj)
                        if content_containers_4:
                            self.first_level_hierarchy(hierarchy_name, content_containers_4, worker_obj)

    def first_level_hierarchy(self, hierarchy, content_containers, worker_obj):

        for content_container in content_containers:

            dev_containers = content_container.find_all('div', recursive=False)

            for dev_container in dev_containers:
                anchor_tags = dev_container.find_all('a', {'class': 'canvas'})
                page_url = ""
                for anchor_tag in anchor_tags:
                    if anchor_tag:
                        if linio_mex_main_url in anchor_tag['href']:
                            page_url = anchor_tag['href']
                        else:
                            page_url = '{}{}'.format(linio_mex_main_url, anchor_tag['href'])

                    category_container = dev_container.find('div', {'class': 'banner-menu'})
                    img_container = dev_container.find('img')
                    sub_category_line = ""
                    if category_container:
                        category_name = category_container.h2.text.encode('utf-8').strip().replace(',', '').replace(' ',
                                                                                                                    '_')

                        sub_category_line = '{}|{}'.encode('utf-8').format(hierarchy, category_name)

                    elif img_container:
                        category_name = img_container['title'].encode('utf-8').strip().replace(',', '').replace(' ', '_')

                        sub_category_line = '{}|{}'.encode('utf-8').format(hierarchy, category_name)

                    line = '{}|{}'.format(sub_category_line, page_url)
                    # print line
                    worker_obj.urls_queue.put(line)
        worker_obj.urls_queue.join()


def form_hierarchy(hierarchy, url):
    path = hierarchy.split('|')
    print 'Started {} Hierarchy Collection'.format(path[-1])
    start_time = time.time()

    worker_obj = Worker()
    worker_obj.create_workers()

    response_obj = Response()
    page_container = response_obj.get_content(url)
    if page_container:
        hierarchy_obj = Worker()
        content_containers_1 = page_container.find_all('div', {'class': 'banner-layout-5'})
        content_containers_2 = page_container.find_all('div', {'class': 'banner-layout-4'})
        content_containers_3 = page_container.find_all('div', {'class': 'banner-layout-8'})
        content_containers_4 = page_container.find_all('div', {'class': 'banner-layout-10'})

        if content_containers_1:
            hierarchy_obj.first_level_hierarchy(hierarchy, content_containers_1, worker_obj)
        if content_containers_2:
            hierarchy_obj.first_level_hierarchy(hierarchy, content_containers_2, worker_obj)
        if content_containers_3:
            hierarchy_obj.moda_level(hierarchy, content_containers_3, worker_obj)
        if content_containers_4:
            hierarchy_obj.first_level_hierarchy(hierarchy, content_containers_4, worker_obj)

    end_time = time.time()

    total = end_time - start_time
    print '{} hierarchy collected |Started -> {} secs | Ended -> {} secs| Total -> {} secs '.format(path[-1],
                                                                                                    start_time,
                                                                                                    end_time, total)
