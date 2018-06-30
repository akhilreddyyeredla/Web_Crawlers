from Common.Etsy_common_imports import *

PATH_STYLE = DataCollectors_Configuration.PATH_STYLE
ROOT_FOLDER = DataCollectors_Configuration.ROOT_FOLDER


class Workers:
    PROJECT_NAME = ''
    HOMEPAGE = ''
    CATEGORY_QUEUE_FILE = ''
    SUB_CATEGORY_QUEUE_FILE = ''
    SUB_SUB_CATEGORY_QUEUE_FILE = ''
    categories_queue = Queue.Queue()
    NUMBER_OF_THREADS = DataCollectors_Configuration.NO_OF_THEARDS
    starting_time = 0
    ending_time = 0

    def __init__(self, project_name, homepage, category_queue_file, sub_category_queue_file,
                 sub_sub_category_queue_file, category_name):
        Workers.starting_time = time.time()
        Workers.PROJECT_NAME = project_name
        Workers.HOMEPAGE = homepage
        Workers.CATEGORY_QUEUE_FILE = category_queue_file
        Workers.SUB_CATEGORY_QUEUE_FILE = sub_category_queue_file
        Workers.SUB_SUB_CATEGORY_QUEUE_FILE = sub_sub_category_queue_file
        print('starting paper_and_party_supplies hierarchy collection')
        Scrapper(Workers.PROJECT_NAME, Workers.HOMEPAGE, category_name)
        self.create_workers()
        Workers.crawl()

    # Create worker threads (will die when main exits)
    def create_workers(self):
        for _ in range(Workers.NUMBER_OF_THREADS):
            t = threading.Thread(target=Workers.work1)
            t.daemon = True
            t.start()

    # Do the next job in the queue
    @staticmethod
    def work1():
        while True:
            url = Workers.categories_queue.get()
            Scrapper.visit_page(threading.current_thread().name, url)
            Workers.categories_queue.task_done()

    # Each queued link is a new job
    @staticmethod
    def create_jobs():
        '''
            This meathod puts urls into queue and waits till the queue is completly filled
            and again search for files to put it in queue
        :return: None
        '''

        for link in file_to_set(Workers.SUB_CATEGORY_QUEUE_FILE):
            Workers.categories_queue.put(link)
        Workers.categories_queue.join()
        Workers.crawl()

    # Check if there are items in the queue, if so crawl them
    @staticmethod
    def crawl():
        # queued_links1 = file_to_set(Workers.CATEGORY_QUEUE_FILE)
        queued_links2 = file_to_set(Workers.SUB_CATEGORY_QUEUE_FILE)
        # queued_links3 = file_to_set(Workers.SUB_SUB_CATEGORY_QUEUE_FILE)

        if len(queued_links2) > 0:
            #print(str(len(queued_links2)) + ' links in the queue')
            Workers.create_jobs()
        else:
            Workers.ending_time = time.time()
            total_time = Workers.ending_time - Workers.starting_time
            print('Total_time to collect paper_and_party_supplies Hierarchy ' + str(total_time) + ' sec' )


class LinksGenerator:
    no_of_items = 0
    no_of_pages = 0

    # Intialize the varaibles with default values
    def __init__(self, project_name):
        self.category_links = set()
        self.sub_category_links = set()
        self.sub_sub_category_links = set()
        self.product_links = set()
        self.category_name = ""
        self.time = ''
        self.no_of_items = 0
        self.no_of_pages = 0
        self.project_name = project_name

    # To find the div tag of All categories
    @staticmethod
    def get_div_class(url):
        response = response_getter.get_content(url)
        if response:
            required_data = response.findAll("div", {"class": "mb-xs-3 pb-xs-3 bb-xs-1 filter-chrome"})
            nav_tag = response.find('nav')
            anchor_tag = nav_tag.findAll('a')
            LinksGenerator.no_of_items = len(response.findAll("div", {
                "class": "js-merch-stash-check-listing block-grid-item v2-listing-card position-relative flex-xs-none "}))
            try:
                # Find last page
                LinksGenerator.no_of_pages = int(anchor_tag[-2]['data-page'])
            except KeyError as e:
                # If there is no last page then it contains only one page
                LinksGenerator.no_of_pages = 1
            return required_data
        else:
            return None

    # To store the links of subcategories
    @staticmethod
    def gen_list(response_list):
        category = []
        for link in response_list:
            category.append(link.find("a")['href'])
        return category

    # To get links of main categories and sub-categories
    def get_category_links(self, url):
        required_data = LinksGenerator.get_div_class(url)
        if required_data is None:
            return None
        else:
            # Find parent categories
            response_list1 = required_data[0].findAll("li", {"class": "pl-xs-2"})
            # Find child categorie
            response_list2 = required_data[0].findAll("li", {"class": "pl-xs-4"})
            # Find hierarchy of category
            self.category_name = response_list1[0].find('a')['data-path']

            name = self.category_name.split(".")

            # if there are only a parent category and no child categories then it is last level of category
            if len(response_list1) == 1 and len(response_list2) == 0:

                response_list = LinksGenerator.gen_list(response_list1)
                total_pages = LinksGenerator.no_of_pages
                path = DataCollectors_Configuration.PATH_STYLE.join(name[1:])
                product_page_url = response_list[0]
                create_directory_and_hierarchy_files(self.project_name, path, total_pages, product_page_url)

                self.sub_sub_category_links |= set(response_list)  # " |= " is a union operator to convert list into set
                return self.sub_sub_category_links

            # if there are  more parent categores and no child categories then it is sub_level of category
            elif len(response_list1) >= 1 and len(response_list2) == 0:
                response_list = LinksGenerator.gen_list(response_list1)
                self.category_links |= set(response_list)
                return self.category_links

            # If there are only one parent category and more child categories and hierarchy length
            #  is greater than 1 then it is sub_sub_level
            elif len(response_list1) == 1 and len(response_list2) != 0 and len(name) >= 1:
                response_list = LinksGenerator.gen_list(response_list2)
                self.sub_category_links |= set(response_list)
                return self.sub_category_links

    @staticmethod
    def get_category_name(url):
        required_data = LinksGenerator.get_div_class(url)
        response = required_data[0].findAll("li", {"class": "pl-xs-2"})
        return response[0].find("a")['data-path']


class Scrapper:
    project_name = ''
    base_url = ''
    # These are the files to store links and feed them to thread queue
    category_queue_file = ''
    sub_category_queue_file = ''
    sub_sub_category_queue_file = ''
    skipped_queue_file = ''

    category_completed_file = ''
    sub_category_completed_file = ''
    sub_sub_category_completed_file = ''
    skipped_completed_file = ''

    # these sets are used to store links and avoid dulicapte links
    category_queue = set()
    sub_category_queue = set()
    sub_sub_category_queue = set()
    skipped_queue = set()

    category_completed = set()
    sub_category_completed = set()
    sub_sub_category_completed = set()
    skipped_completed = set()

    def __init__(self, project_name, base_url, name):
        Scrapper.project_name = project_name
        Scrapper.base_url = base_url
        Scrapper.category_queue_file = Scrapper.project_name + CONSTANTS.CATEGORY_QUEUE.format(name)
        Scrapper.category_completed_file = Scrapper.project_name + CONSTANTS.CATEGORY_COMPLETED.format(name)
        Scrapper.sub_category_queue_file = Scrapper.project_name + CONSTANTS.SUB_CATEGORY_QUEUE.format(name)
        Scrapper.sub_category_completed_file = Scrapper.project_name + CONSTANTS.SUB_CATEGORY_COMPLETED.format(name)
        Scrapper.sub_sub_category_queue_file = Scrapper.project_name + CONSTANTS.SUB_SUB_CATEGORY_QUEUE.format(name)
        Scrapper.sub_sub_category_completed_file = Scrapper.project_name + CONSTANTS.SUB_CATEGORY_COMPLETED.format(
            name)
        Scrapper.skipped_queue_file = Scrapper.project_name + CONSTANTS.SKIPPED_QUEUE.format(name)
        Scrapper.skipped_completed_file = Scrapper.project_name + CONSTANTS.SKIPPED_COMPLETD.format(name)
        self.boot(name)
        self.visit_page('First Scrapper', Scrapper.base_url)

    # Creates directory and files for project on first run and starts the Scrapper
    @staticmethod
    def boot(name):
        create_project_dir(Scrapper.project_name)
        # create_data_store_file(Scrapper.project_name, 'Analysis',"Category,Access_time\n")
        create_data_files(Scrapper.project_name, Scrapper.base_url, name)

        Scrapper.category_queue = file_to_set(Scrapper.category_queue_file)
        Scrapper.category_completed = file_to_set(Scrapper.category_completed_file)
        Scrapper.sub_category_queue = file_to_set(Scrapper.sub_category_queue_file)
        Scrapper.sub_category_completed = file_to_set(Scrapper.sub_category_completed_file)
        Scrapper.sub_sub_category_queue = file_to_set(Scrapper.sub_sub_category_queue_file)
        Scrapper.sub_sub_category_completed = file_to_set(Scrapper.sub_sub_category_completed_file)
        Scrapper.skipped_queue = file_to_set(Scrapper.skipped_queue_file)
        Scrapper.skipped_completed = file_to_set(Scrapper.skipped_completed_file)

    # Updates user display, fills queue and updates files
    @staticmethod
    def visit_page(thread_name, page_url):
        if page_url not in Scrapper.category_completed:
            if page_url not in Scrapper.sub_category_completed:
                if page_url not in Scrapper.sub_sub_category_completed:
                    if page_url not in Scrapper.skipped_queue:
                        Scrapper.update_links(thread_name, page_url)

    # Get links and update the files
    @staticmethod
    def update_links(thread_name, page_url):
        #print(thread_name + ' now visiting ' + page_url)

        finder = LinksGenerator(Scrapper.project_name)
        links = finder.get_category_links(page_url)
        if links is None:
            try:
                Scrapper.category_queue.remove(page_url)
                Scrapper.skipped_queue.add(page_url)
                Scrapper.update_files(Scrapper.category_queue, Scrapper.category_queue_file,
                                      Scrapper.skipped_queue, Scrapper.skipped_queue_file)
            except:
                Scrapper.sub_category_queue.remove(page_url)
                Scrapper.skipped_queue.add(page_url)
                Scrapper.update_files(Scrapper.sub_category_queue, Scrapper.sub_category_queue_file,
                                      Scrapper.skipped_queue, Scrapper.skipped_queue_file)

        elif len(finder.category_links) != 0:
            Scrapper.add_links_to_queue(links, Scrapper.sub_category_queue, Scrapper.sub_category_completed)
            Scrapper.category_queue.remove(page_url)
            Scrapper.category_completed.add(page_url)
            Scrapper.update_files(Scrapper.category_queue, Scrapper.category_queue_file,
                                  Scrapper.category_completed, Scrapper.category_completed_file)
            Scrapper.update_files(Scrapper.sub_category_queue, Scrapper.sub_category_queue_file,
                                  Scrapper.sub_category_completed, Scrapper.sub_category_completed_file)

        elif len(finder.sub_category_links) != 0:
            Scrapper.add_links_to_queue(links, Scrapper.sub_category_queue, Scrapper.sub_category_completed)
            try:
                Scrapper.sub_category_queue.remove(page_url)
                Scrapper.sub_category_completed.add(page_url)
                Scrapper.update_files(Scrapper.sub_category_queue, Scrapper.sub_category_queue_file,
                                      Scrapper.sub_category_completed, Scrapper.sub_category_completed_file)
            except:
                Scrapper.category_queue.remove(page_url)
                Scrapper.category_completed.add(page_url)
                Scrapper.update_files(Scrapper.category_queue, Scrapper.category_queue_file,
                                      Scrapper.category_completed, Scrapper.category_completed_file)
                Scrapper.update_files(Scrapper.sub_category_queue, Scrapper.sub_category_queue_file,
                                      Scrapper.sub_category_completed, Scrapper.sub_category_completed_file)

        elif len(finder.sub_sub_category_links) != 0:
            Scrapper.add_links_to_queue(links, Scrapper.sub_sub_category_queue, Scrapper.sub_sub_category_completed)
            try:
                Scrapper.sub_category_queue.remove(page_url)
                Scrapper.sub_category_completed.add(page_url)
                Scrapper.update_files(Scrapper.sub_category_queue, Scrapper.sub_category_queue_file,
                                      Scrapper.sub_category_completed, Scrapper.sub_category_completed_file)
                Scrapper.update_files(Scrapper.sub_sub_category_queue, Scrapper.sub_sub_category_queue_file,
                                      Scrapper.sub_sub_category_completed, Scrapper.sub_sub_category_completed_file)
            except:
                Scrapper.sub_sub_category_queue.remove(page_url)
                Scrapper.sub_sub_category_completed.add(page_url)
                Scrapper.update_files(Scrapper.sub_sub_category_queue, Scrapper.sub_sub_category_queue_file,
                                      Scrapper.sub_sub_category_completed, Scrapper.sub_sub_category_completed_file)

    # Saves queue data to project files
    @staticmethod
    def add_links_to_queue(links, queu, completed):

        for url in links:
            if (url in queu) or (url in completed):
                continue
            queu.add(url)

    @staticmethod
    def update_files(queu, queue_file, completed, completed_file):
        set_to_file(queue_file, queu)
        set_to_file(completed_file, completed)
