from Common.Ebay_common_imports import *


buss = {}
page_list = list()
ROOT_FOLDER = DataCollectors_Configuration.ROOT_FOLDER_EBAY_URL


# ROOT_FOLDER_INFO = DataCollectors_Configuration.ROOT_FOLDER_EBAY_INFO

class Workers:
    def __init__(self):
        self.urls = Queue()
        self.number_of_threads = DataCollectors_Configuration.NO_OF_THEARDS


    def Buss_url(self, file):
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
        print("Business" + "|" + "Start Time:" + str(start) + "|" + "End Time:" + str(
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
        page_url = line[1].replace("/n", "")
        dic_path = name.replace("|", "/")
        category_name = name.split("|")[0]

        # print(dic_path)
        file_name = '{}.txt'.format(category_name)
        file_path = '{}/{}/{}'.format(ROOT_FOLDER, category_name, file_name)
        if not os.path.exists("{}/{}".format(ROOT_FOLDER, category_name)):
            os.makedirs("{}/{}".format(ROOT_FOLDER, category_name))

        file_name1 = '{}_completed_pages.txt'.format(category_name)
        file_path1 = '{}/{}/{}'.format(ROOT_FOLDER, category_name, file_name1)
        # print file_path1
        file1= open(file_path1, 'a+')
        file1.close()
        page_list = open(DataCollectors_Configuration.home_pages.format(ROOT_FOLDER)).read().splitlines()
        if not os.path.exists("{}/{}".format(ROOT_FOLDER, dic_path)):
            os.makedirs("{}/{}".format(ROOT_FOLDER, dic_path))

        file_name = '{}_product_links.txt'.format(category_name)
        file_path = '{}/{}/{}'.format(ROOT_FOLDER, dic_path, file_name)


        # print(url)
        # Finding the number of pages
        number_soup = self.page(page_url)
        page_number = number_soup.findAll("h2", {"class": "srp-controls__count-heading"})
        if len(page_number) == 0:
            pass
        else:
            number = (page_number[0].text)
            count = number.split(" ")
            page_no = (count[2].replace(',', ''))
            total_pages = (int(int(page_no) / 45)) + 1
            # print page_url
            # print total_pages
            page_number = 1
            while (page_number != total_pages):

                my_url = page_url.replace("\n", "") + "?_pgn=" + str(page_number)
                if my_url not in page_list:
                    # print my_url
                    if my_url not in page_list:
                        # print(my_url)
                        page_soup = self.page(my_url)
                        page_info = page_soup.findAll("a", {"class": "s-item__link"})
                        if len(page_info) == 0:
                            break

                        for product in page_info:
                            product_url = (product['href'])
                            # print product_url
                            file = open(file_path, 'a+')
                            line_ = '{},{}\n'.format(name, product_url)
                            file.write(line_)
                            file.close()
                            # print product_url
                        line = '{}\n'.format(my_url)
                        file1 = open(file_path1, 'a+')
                        file1.write(line.encode('utf-8'))
                        file1.close()
                page_number = page_number + 1

