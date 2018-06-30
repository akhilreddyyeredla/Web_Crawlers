from Common.Ebay_common_imports import *

main_list = set()
urls_list = set()
leaf_list = set()
ROOT_FOLDER = DataCollectors_Configuration.ROOT_FOLDER_EBAY_HIERARCHY


class workers:
    def __init__(self):
        self.urls = Queue()
        self.number_of_threads = DataCollectors_Configuration.NO_OF_THEARDS

    def mus(self, file):
        self.create_works()
        start = time.time()
        with open(file, 'rt') as f:
            for line in f:
                line1 = line.split(",")
                name = line1[0]
                dic_path = name.replace("|", "/")
                if not os.path.exists("{}/{}".format(ROOT_FOLDER, dic_path)):
                    os.makedirs("{}/{}".format(ROOT_FOLDER, dic_path))
                self.urls.put(line)
            self.urls.join()
        stop = time.time()
        print("Music" + "|" + "Start Time:" + str(start) + "|" + "End Time:" + str(
            stop) + "|" + "Total Duration:" + str(stop - start))

    def create_works(self):
        for _ in range(self.number_of_threads):
            t = threading.Thread(target=self.work)
            t.daemon = True
            t.start()

    def work(self):
        while True:
            url = self.urls.get()

            self.page_find(url)
            self.urls.task_done()




    def page(self, url):
        my_url = url
        uClient = requests.get(my_url)
        page_html = uClient.content
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        return page_soup

    def page_find(self, url):
        line = url.split(",")
        name = line[0]
        url = line[1].replace("\n", "")
        main_list.add(url)
        # print main_list
        soup = self.page(url)
        container = soup.findAll("a", {"class": "b-textlink b-textlink--sibling"})
        directory_path = name.split("|")[0]
        # print directory_path
        file_name = '{}_product_leaf.txt'.format(directory_path)
        file_path = '{}/{}/{}'.format(ROOT_FOLDER, directory_path, file_name)

        # print file_path
        file = open(file_path, 'a+')
        file.close()
        for data in container:
            sub_url = data['href'].encode('utf-8')
            if sub_url not in main_list:
                if sub_url not in urls_list:
                    urls_list.add(sub_url)
                    leaf_soup = self.page(sub_url)
                    leaf_container = leaf_soup.findAll("a", {"class": "b-textlink b-textlink--sibling"})
                    for leaf_data in leaf_container:
                        page_list = open(DataCollectors_Configuration.home_leaf.format(ROOT_FOLDER)).read().splitlines()
                        leaf_url = leaf_data['href'].encode('utf-8')
                        if leaf_url not in page_list:
                            if leaf_url not in leaf_list:
                                leaf_list.add(leaf_url)
                                leaf_name = leaf_data.text.replace(" ", "_").replace("&", "AND").replace(",",
                                                                                                         "_").encode(
                                    'utf-8')
                                highercy = name + "|" + re.sub('[^a-zA-Z0-9]', '_', leaf_name)
                                # print highercy
                                dic_path = name.split("|")
                                directory_path = dic_path[0]
                                if not os.path.exists(directory_path):
                                    os.makedirs(directory_path)

                                f = open(file_path, 'a+')

                                line_ = '{},{}\n'.format(highercy, leaf_url)
                                file.write(line_)
                                file.close()

