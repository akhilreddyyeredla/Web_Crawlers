from Common.Ebay_common_imports import *

tup1 = ()
product_info_start = time.time()
ROOT_FOLDER = DataCollectors_Configuration.ROOT_FOLDER_EBAY_INFO
ROOT_FOLDER_URL = DataCollectors_Configuration.ROOT_FOLDER_EBAY_URL

class workers:
    def __init__(self):
        self.urls_queue = Queue()
        self.number_of_threads = DataCollectors_Configuration.NO_OF_THEARDS
        self.message = ""
        self.completed_queue_obj = completed_queue.completed()
    def start(self, urls_list):


        self.create_works()
        for line in urls_list:

            self.urls_queue.put(line)
        self.urls_queue.join()

    def create_works(self):


        for _ in range(self.number_of_threads):
            t = threading.Thread(target=self.work)
            t.daemon = True
            t.start()

    def work(self):


        while True:
            url = self.urls_queue.get()


            self.process(url)

            self.urls_queue.task_done()




    def DATE(self):
        today = date.today()
        return str(today)

    def TIME(self):
        time_ = datetime.time(datetime.now())
        return str(time_)

    def find_page(self, url):
        my_url = url
        uClient = requests.get(my_url)
        page_html = uClient.content
        uClient.close()
        page_soup = soup(page_html, "lxml")
        return page_soup

    def img(self, raw_data, hierarchy, url):
        try:
            img_data = raw_data.findAll("img", {"id": "icImg"})
            img_url = img_data[0]['src']
            return (img_url)
        except Exception as e:
            # print_exception('image_url not found','eBAy',hierarchy,url,e)
            self.message = self.message + "IMG URL, "
            return 'Not Avaliable'

    def name(self, raw_data, hierarchy, url):
        try:
            product = raw_data.findAll("span", {"id": "vi-lkhdr-itmTitl"})
            product_name = product[0].text
            return (product_name)
        except Exception as e:
            # print_exception('Name not found','eBAy',hierarchy,url,e)
            self.message = self.message + "Product_name, "
            return 'NA'

    def price(self, raw_data, hierarchy, url):
        try:
            rate = raw_data.findAll("span", {"class": "notranslate"})
            product_price1 = rate[0].text.split(" ")[1]
            product_price = product_price1[1:]
            money_type = product_price1[0]
            CURRENCY = self.currency(money_type)
            return (product_price + "," + CURRENCY)
        except Exception as e:
            # print_exception('Price not found','eBAy',hierarchy,url,e)
            self.message = self.message + "Price, "

            return 'NA'

    def currency(self, data):
        try:
            if (data == "$"):
                country_currency = "USD"
                return (country_currency)
            else:
                country_currency = 'ESD'
                return (country_currency)
        except Exception as e:
            # print_exception('Currency not found','eBAy',e)
            self.message = self.message + "Currency, "

            return 'NA'

    def shipping(self, raw_data, hierarchy, url):
        try:
            shipping_rate = raw_data.findAll("span", {"id": "fshippingCost"})
            shipping_cost = shipping_rate[0].text.strip()
            return (shipping_cost)
        except Exception as e:
            # print_exception('Shipping charges not found','eBAy',hierarchy,url,e)
            self.message = self.message + "Shipping, "
            return 'NA'

    def country(self, raw_data, hierarchy, url):
        try:
            deviliry_content = raw_data.findAll("span", {"itemprop": "areaServed"})
            dev_country = str(deviliry_content[0].text.strip()).replace("\n", "")
            dev_country = dev_country.split('|')[0]
            return (dev_country)
        except Exception as e:
            # print_exception('Shipping Delivary country not avaliable','eBAy',hierarchy,url,e)
            self.message = self.message + "Country, "
            return 'NA'

    def rating(self, raw_data, hierarchy, url):
        try:
            p_rating = raw_data.findAll("span", {"itemprop": "aggregateRating"})
            if (len(p_rating) == 0):
                product_rating = "NA"
                return product_rating
            else:
                product_rating = p_rating[0].a['aria-label'].split(",")[0][:10]
                return product_rating
        except Exception as e:
            # print_exception('Rating Not found','eBAy',hierarchy,url,e)
            self.message = self.message + "Rating, "
            return 'NA'

    def condition(self, raw_data, hierarchy, url):
        try:
            item = raw_data.findAll("div", {"itemprop": "itemCondition"})
            item_condition = item[0].text.replace("\n", " ")
            return item_condition
        except Exception as e:
            # print_exception('iteam condition not found','eBAy',hierarchy,url,e)
            self.message = self.message + "Condition, "
            return 'NA'

    def item_sold(self, raw_data, hierarchy, url):
        try:
            item1 = raw_data.findAll("span",
                                     {"class": "vi-qtyS-hot-red vi-bboxrev-dsplblk vi-qty-vert-algn vi-qty-pur-lnk"})
            no_of_item_sold = item1[0].text
            return (no_of_item_sold)
        except Exception as e:
            # print_exception('No of items sold not avaliable','eBAy',hierarchy,url,e)
            self.message = self.message + "Items_Sold"
            return 'NA'

    def item_avlb(self, raw_data, hierarchy, url):
        try:
            item = raw_data.findAll("span", {"id": "qtySubTxt"})
            items_available1 = str(item[0].text).strip()
            items_available = items_available1[:12]
            return items_available
        except Exception as e:
            # print_exception('No of iteams sold not found','eBAy',hierarchy,url,e)
            self.message = self.message + "No of Items Avaliable, "
            return "NA"

    def item_from(self, raw_data, hierarchy, url):
        try:
            item_location = raw_data.findAll("span", {"itemprop": "availableAtOrFrom"})
            item_country = item_location[0].text.replace(",", "|")
            return (item_country)
        except Exception as e:
            # print_exception('item location not found','eBAy',hierarchy,url,e)
            self.message = self.message + "Item_locaition, "
            return 'NA'

    def shipping_by(self, raw_data, hierarchy, url):
        try:
            shipping = raw_data.findAll("span", {"id": "fShippingSvc"})
            logistics_name = shipping[0].text.strip()
            return (logistics_name)
        except Exception as e:
            # print_exception('Shipping logistics not found','eBAy',hierarchy,url,e)
            self.message = self.message + "Shipping_logistics, "
            return 'NA'

    def ean(self, raw_data, hierarchy, url):
        try:
            count = 0
            found = 0
            table = raw_data.findAll("div", {"class": "itemAttr"})
            field_name = table[0].findAll("td", {"class": "attrLabels"})
            value = table[0].findAll("td", {"width": "50.0%"})
            for field in field_name:
                name = field.text.strip()
                if (name == 'EAN:'):
                    found = 1
                    break
                count = count + 1
            if (found == 0):
                ean_value = "NA"
            else:
                ean_value = value[count].text.strip()
            return ean_value
        except Exception as e:
            # print_exception('Ean not found','eBAy',hierarchy,url,e)
            self.message = self.message + "EAN, "
            return "NA"

    def seller_url(self, raw_data, hierarchy, url):
        try:
            seller_data = raw_data.findAll("span", {"class": "mbg-nw"})
            seller_name = seller_data[0].text.replace(",", "-")
            seller = raw_data.findAll("div", {"class": "mbg vi-VR-margBtm3"})
            url = seller[0].a['href']
            seller_soup = self.find_page(url)
            seller_Positive = self.seller_positive(seller_soup, hierarchy, url)
            seller_Negtive = self.seller_negtive(seller_soup, hierarchy, url)
            seller_Neutral = self.seller_neutral(seller_soup, hierarchy, url)
            seller_Review = self.seller_allreview(seller_soup, hierarchy, url)
            seller_Location = self.seller_location(seller_soup, hierarchy, url)
            seller_Membership = self.seller_membership(seller_soup)
            return str(
                "NA," + seller_Location + "," + seller_name + "," + seller_Negtive + "," + seller_Neutral + "," + seller_Positive + "," + seller_Review + "," + "NA," + seller_Membership)
        except Exception as e:
            # print_exception('Seller Not found','eBAy',hierarchy,url,e)
            self.message = self.message + "Seller_info, "
            return "NA"

    def seller_positive(self, raw_data, hierarchy, url):
        try:
            positive = raw_data.findAll("span", {"class": "num"})
            positive_review = positive[0].text.replace(",", "-")
            return (positive_review)
        except Exception as e:
            # print_exception('seller_positive review not found','eBAy',hierarchy,url,e)
            self.message = self.message + "seller_positive_Review, "
            return 'NA'

    def seller_negtive(self, raw_data, hierarchy, url):
        try:
            negtive = raw_data.findAll("span", {"class": "num"})
            negtive_review = negtive[2].text.replace(",", "-")
            return (negtive_review)
        except Exception as e:
            # print_exception('seller_negative not found','eBAy',hierarchy,url,e)
            self.message = self.message + "Seller_Negative_Review, "
            return 'NA'

    def seller_neutral(self, raw_data, hierarchy, url):
        try:
            neutral = raw_data.findAll("span", {"class": "num"})
            neutral_review = neutral[1].text.replace(",", "-")
            return (neutral_review)
        except Exception as e:
            # print_exception('seller_neutral not found','eBAy',hierarchy,url,e)
            self.message = self.message + "Seller_neutral_review, "
            return 'NA'

    def seller_allreview(self, raw_data, hierarchy, url):
        try:
            review = raw_data.findAll("div", {"class": "perctg"})
            seller_review = review[0].text.strip().replace(",", "-")[:6]
            return (seller_review)
        except Exception as e:
            # print_exception('seller_overal review not found','eBAy',hierarchy,url,e)
            self.message = self.message + "seller_overall_review, "
            return 'NA'

    def seller_location(self, raw_data, hierarchy, url):
        try:
            location = raw_data.findAll("span", {"class": "mem_loc"})
            seller_place = location[0].text.replace(",", "-")
            return (seller_place)
        except Exception as e:
            # print_exception('seller_location not found','eBAy',hierarchy,url,e)
            self.message = self.message + "Seller_location, "
            return 'NA'

    def seller_membership(self, raw_data):
        try:
            mem = raw_data.findAll("span", {"class": "info"})
            seller_mem = mem[0].text.replace(",", "|")
            return (seller_mem)
        except Exception as e:
            # print_exception('seller membership Details not found','eBAy',hierarchy,url,e)
            self.message = self.message + "seller_membership, "
            return 'NA'

    def store(self, raw_data, hierarchy, url):
        try:
            info = raw_data.findAll("div", {"class": "si-ss-eu"})
            store_number = info[0].a['title']
            store_no = store_number.split(" ")
            storename = store_no[1][5:]
            return (storename)
        except Exception as e:
            # print_exception('Store name not found','eBAy',hierarchy,url,e)
            self.message = self.message + "Store, "
            return 'NA'

    def item_num(self, raw_data, hierarchy, url):
        try:
            item = raw_data.findAll("div", {"id": "descItemNumber"})
            item_number = str(item[0].text)
            return item_number
        except Exception as e:
            # print_exception('Item number not found','eBAy',hierarchy,url,e)
            self.message = self.message + "Item_number, "
            return 'NA'

    def upc(self, raw_data, hierarchy, url):
        try:
            count = 0
            found = 0
            table = raw_data.findAll("div", {"class": "itemAttr"})
            field_name = table[0].findAll("td", {"class": "attrLabels"})
            value = table[0].findAll("td", {"width": "50.0%"})
            for field in field_name:
                name = field.text.strip()
                if (name == 'UPC:'):
                    found = 1
                    break
                count = count + 1
            if (found == 0):
                upc_value = "NA"
            else:
                upc_value = value[count].text.strip()
            return upc_value
        except Exception as e:
            # print_exception('UPC number not found','eBAy',hierarchy,url,e)
            self.message = self.message + "UPC, "
            return "NA"

    def warenty(self, raw_data, hierarchy, url):
        try:
            count = 0
            found = 0
            table = raw_data.findAll("div", {"class": "itemAttr"})
            field_name = table[0].findAll("td", {"class": "attrLabels"})
            value = table[0].findAll("td", {"width": "50.0%"})
            for field in field_name:
                name = field.text.strip()
                if (name == 'Warrenty:'):
                    found = 1
                    break
                count = count + 1
            if (found == 0):
                warrenty_value = "NA"
            else:
                warrenty_value = value[count].text.strip()
            return warrenty_value
        except Exception as e:
            # print_exception('Warrenty not found','eBAy',hierarchy,url,e)
            self.message = self.message + "Warrenty, "
            return "NA"

    def isbn(self, raw_data, hierarchy, url):
        try:
            count = 0
            found = 0
            table = raw_data.findAll("div", {"class": "itemAttr"})
            field_name = table[0].findAll("td", {"class": "attrLabels"})
            value = table[0].findAll("td", {"width": "50.0%"})
            for field in field_name:
                name = field.text.strip()
                if (name == 'ISBN:'):
                    found = 1
                    break
                count = count + 1
            if (found == 0):
                isbn_value = "NA"
            else:
                isbn_value = value[count].text.strip()
            return isbn_value
        except Exception as e:
            self.message = self.message + "ISBN, "
            # print_exception('ISBN not found','eBAy',hierarchy,url,e)

            return "NA"

    def mpn(self, raw_data, hierarchy, url):
        try:
            num = raw_data.findAll("h2", {"itemprop": "mpn"})
            MPN = num[0].text.replace(",", "-")
            return MPN
        except Exception as e:
            # print_exception('MPN numbe rnot found','eBAy',hierarchy,url,e)
            self.message = self.message + "MPN, "
            return 'NA'

    def brand(self, raw_data, hierarchy, url):
        try:
            brnd = raw_data.findAll("h2", {"itemprop": "brand"})
            BRAND = brnd[0].text.replace(",", "-")
            return BRAND
        except Exception as e:
            # print_exception('Brand not found','eBAy',hierarchy,url,e)
            self.message = self.message + "Brand, "
            return 'NA'

    def policy(self, raw_data, hierarchy, url):
        Return_policy = {}
        try:
            ret = raw_data.findAll("span", {"id": "vi-ret-accrd-txt"})
            return_policy = ret[0].text.strip().replace(",", "-")
            return return_policy
        except Exception as e:
            # print_exception('Return Policy not found','eBAy',hierarchy,url,e)
            self.message = self.message + "Return_policy, "
            return "NA"

    def size(self, raw_data, hierarchy, url):
        try:
            count = 0
            found = 0
            table = raw_data.findAll("div", {"class": "itemAttr"})
            field_name = table[0].findAll("td", {"class": "attrLabels"})
            value = table[0].findAll("td", {"width": "50.0%"})
            for field in field_name:
                name = field.text.strip()
                if (name == 'Size:' or name == 'Size::' or name == 'Size ::'):
                    found = 1
                    break
                count = count + 1
            if (found == 0):
                size_value = "NA"
            else:
                size_value = value[count].text.strip()
            return size_value
        except Exception as e:
            # print_exception('item size not found','eBAy',hierarchy,url,e)
            self.message = self.message + "Size, "
            return "NA"

    def specification(self, raw_data, hierarchy, url):
        spe = {}
        try:

            table = raw_data.findAll("div", {"class": "itemAttr"})
            field = table[0].findAll("td", {"class": "attrLabels"})
            value = table[0].findAll("td", {"width": "50.0%"})
            count = 0
            for data in field:
                property = data.text.strip().replace("\n", "").replace("\t", "")
                property_name = value[count].text.replace("\n", "").replace("\t", "").replace(",", "|")
                spe[property] = property_name
                count = count + 1
            JSON = json.dumps(spe)
            return JSON
        except Exception as e:
            # print_exception('Specifications not found','eBAy',hierarchy,url,e)
            self.message = self.message + "specifications"
            JSON = json.dumps(spe)
            return JSON

    def get_data(self, raw_data, full_name, url):
        categorys = full_name.split("|")
        completed_file_name = 'collectibles_completed_links.txt'
        directory_path = full_name.replace("|", "/")

        item_number = self.item_num(raw_data, full_name, url)

        file_name = '{}.txt'.format(item_number)
        file_path = '{}/{}/{}'.format(ROOT_FOLDER, directory_path, file_name)
        completed_file_path = '{}/{}/{}'.format(ROOT_FOLDER, directory_path, completed_file_name)
        completed_file = open(completed_file_path,'a+')
        completed_file.close()
        p_url = str(url)
        product = {}
        seller = self.seller_url(raw_data, full_name, url)
        seller_details = seller.split(",")
        cost_info = self.price(raw_data, full_name, url).split(",")
        # print item_number
        product['sku'] = 'NA'
        product['asin'] = 'NA'  # newprocess
        product['date'] = self.DATE()
        product['time'] = self.TIME()
        product['marketplace'] = 'EBAY_US'
        product['domain'] = 'www.ebay.com'
        product['category'] = categorys[0]
        product['category_level_1'] = categorys[1]
        product['category_level_2'] = categorys[2]
        product['category_level_3'] = categorys[3]
        product['category_level_4'] = 'NA'
        product['category_level_5'] = 'NA'
        product['category_level_6'] = 'NA'
        product['category_level_7'] = 'NA'
        product['category_level_8'] = 'NA'
        product['category_level_9'] = 'NA'

        product['condition'] = self.condition(raw_data, full_name, url)
        product['additional_policies'] = 'NA'
        product['description'] = 'NA'
        product['highlights'] = 'NA'
        product['rating_details'] = 'NA'  # ne
        product['specifications'] = self.specification(raw_data, full_name, url)
        product['seller_overall_rating'] = seller_details[6]
        product['seller_description'] = 'NA'
        product['return_policies'] = self.policy(raw_data, full_name, url)
        product['warrenty'] = self.warenty(raw_data, full_name, url)
        product['shipping_policies'] = 'NA'
        product['from_manufracture'] = 'NA'  # new
        product['promotion'] = 'NA'  # new
        product['other_format_prices'] = 'NA'  # new
        product['seller_detailed_information'] = 'NA'  # new

        product['saved_price'] = 'NA'
        product['added_date'] = 'NA'
        product['availability'] = 'NA'
        product['brand'] = self.brand(raw_data, full_name, url)
        product['discount_percentage'] = 'NA'
        product['product_selling_price'] = cost_info[0]
        product['product_EAN'] = self.ean(raw_data, full_name, url)
        product['product_id'] = self.item_num(raw_data, full_name, url)
        product['image_url'] = self.img(raw_data, full_name, url)
        product['likes'] = 'NA'
        product['isbn'] = self.isbn(raw_data, full_name, url)
        product['isbn-10'] = 'NA'  # new
        product['isbn-13'] = 'NA'  # new
        product['MPN'] = self.mpn(raw_data, full_name, url)
        product['name'] = self.name(raw_data, full_name, url)
        product['no_of_reviews'] = 'NA'
        product['original_price'] = 'NA'
        product['rating'] = self.rating(raw_data, full_name, url)
        product['shipping_price'] = self.shipping(raw_data, full_name, url)
        product['size'] = self.size(raw_data, full_name, url)
        product['upc'] = self.upc(raw_data, full_name, url)
        product['url'] = url
        product['quantity_available'] = self.item_avlb(raw_data, full_name, url)
        product['products_slod'] = self.item_sold(raw_data, full_name, url)
        product['seller_code'] = seller_details[0]
        product['seller_location'] = seller_details[1]
        product['seller_name'] = seller_details[2]
        product['seller_negative_rating'] = seller_details[3]
        product['seller_neutral_rating'] = seller_details[4]
        product['seller_positive_rating'] = seller_details[5]
        product['seller_rank'] = seller_details[7]
        product['seller_store_link'] = "NA"
        product['seller_year_of_joining'] = seller_details[8]
        product['shipping_available_countries'] = self.country(raw_data, full_name, url)
        product['shipping_location'] = self.item_from(raw_data, full_name, url)
        product['shipping_logistic_name'] = self.shipping_by(raw_data, full_name, url)
        product['shipping_price'] = self.shipping(raw_data, full_name, url)
        product['shop_location'] = 'NA'
        product['shop_name'] = self.store(raw_data, full_name, url)
        product['no_of_sales'] = 'NA'
        product['shop_rating'] = 'NA'
        product['Tax_info'] = 'NA'
        product['Visibility'] = 'NA'
        product['currency'] = cost_info[1]
        product['color_variants'] = 'NA'  # new
        product['style_variants'] = 'NA'  # new
        product['author_name'] = 'NA'  # new

        # store the data into a tuple because it will be easy to identify which feilds are missing
        print_exception(self.message, 'Ebay', full_name, url, 'NA')
        store_obj = product_info_storage.store()
        store_obj.store_options("Ebay",self.DATE(),full_name,self.TIME(),product)
        text = {'path': completed_file_path, 'hierarchy': full_name, 'url': url}
        json_text = json.dumps(text)

        self.completed_queue_obj.add_to_queue(json_text)
        #completed_file = open(completed_file_path, 'a+')
        #wrriting_line = '{},{}'.format(full_name, url)
        #completed_file.write(wrriting_line + '\n')
        #completed_file.close()
    def process(self, line):


        full_line = line.split(",")
        full_name = full_line[0]
        product_url = full_line[1]
        my_url = product_url
        uClient = requests.get(my_url)
        page_html = uClient.content
        uClient.close()
        page_soup = soup(page_html, "lxml")
        self.get_data(page_soup, full_name, product_url)

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

    def collection_start(self, root):
        print root

        pattern_1 = "*_product_links.txt"
        pattern_2 = "*_completed_links.txt"
        get_queue__file = self.get_all_files(root, pattern_1)
        get_completed_files = self.get_all_files(ROOT_FOLDER, pattern_2)
        completed_list = set()
        queue_list = set()
        for file in get_completed_files:
            with open(file, 'rt') as read_file:
                for line in read_file:
                    line1 = line.split(",")
                    name = line1[0]
                    dic_path = name.replace("|", "/")
                    if not os.path.exists("{}/{}".format(ROOT_FOLDER, dic_path)):
                        os.makedirs("{}/{}".format(ROOT_FOLDER, dic_path))
                    completed_list.add(line.replace('\n', ''))

        for file in get_queue__file:
            count = 0
            with open(file, 'rt') as read_file:
                for line in read_file:
                    line1 = line.split(",")
                    name = line1[0]
                    dic_path = name.replace("|", "/")
                    if not os.path.exists("{}/{}".format(ROOT_FOLDER, dic_path)):
                        os.makedirs("{}/{}".format(ROOT_FOLDER, dic_path))
                    line = line.replace('\n', '')
                    if line in completed_list:
                        continue
                    else:
                        if count <= DataCollectors_Configuration.NO_OF_PRODUCT_INFO_TO_COLLECT:
                            queue_list.add(line.replace('\n', ''))
                            count = count + 1
                        else:
                            break

        self.start(queue_list)
        self.create_works()
        product_info_stop = time.time()


