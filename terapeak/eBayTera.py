
from datetime import datetime
import json
import time
import datetime
import threading
import requests
from datetime import date
import Queue
tup1 = ()
product_info_start = time.time()
import requests
import os

import time
from bs4 import BeautifulSoup as soup
import Queue


urls = Queue.Queue()
number_of_threads = 4
buss = {}
page_list = list()
f = open('terapeak_home_decor.txt','a+')

def page(url):
    my_url = url
    uClient = requests.get(my_url)
    page_html = uClient.content
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    return page_soup

class workers:
    def __init__(self):
        self.urls_queue = Queue.Queue()
        self.number_of_threads = 4
        self.message = ""

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
        time_ = datetime.time()
        return str(time_)

    def find_page(self, url):
        my_url = url
        uClient = requests.get(my_url)
        page_html = uClient.content
        uClient.close()
        page_soup = soup(page_html, "lxml")
        return page_soup

    def img(self, raw_data,  url):
        try:
            img_data = raw_data.findAll("img", {"id": "icImg"})
            img_url = img_data[0]['src']
            return (img_url)
        except Exception as e:
            # print_exception('image_url not found','eBAy',url,e)
            self.message = self.message + "IMG URL, "
            return 'Not Avaliable'

    def name(self, raw_data,  url):
        try:
            product = raw_data.findAll("span", {"id": "vi-lkhdr-itmTitl"})
            product_name = product[0].text
            return (product_name)
        except Exception as e:
            # print_exception('Name not found','eBAy',url,e)
            self.message = self.message + "Product_name, "
            return 'NA'

    def price(self, raw_data,  url):
        try:
            rate = raw_data.findAll("span", {"class": "notranslate"})
            product_price1 = rate[0].text.split(" ")[1]
            product_price = product_price1[1:]
            money_type = product_price1[0]
            CURRENCY = self.currency(money_type)
            return (product_price + "," + CURRENCY)
        except Exception as e:
            # print_exception('Price not found','eBAy',url,e)
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

    def shipping(self, raw_data,  url):
        try:
            shipping_rate = raw_data.findAll("span", {"id": "fshippingCost"})
            shipping_cost = shipping_rate[0].text.strip()
            return (shipping_cost)
        except Exception as e:
            # print_exception('Shipping charges not found','eBAy',url,e)
            self.message = self.message + "Shipping, "
            return 'NA'

    def country(self, raw_data,  url):
        try:
            deviliry_content = raw_data.findAll("span", {"itemprop": "areaServed"})
            dev_country = str(deviliry_content[0].text.strip()).replace("\n", "")
            dev_country = dev_country.split('|')[0]
            return (dev_country)
        except Exception as e:
            # print_exception('Shipping Delivary country not avaliable','eBAy',url,e)
            self.message = self.message + "Country, "
            return 'NA'

    def rating(self, raw_data,  url):
        try:
            p_rating = raw_data.findAll("span", {"itemprop": "aggregateRating"})
            if (len(p_rating) == 0):
                product_rating = "NA"
                return product_rating
            else:
                product_rating = p_rating[0].a['aria-label'].split(",")[0][:10]
                return product_rating
        except Exception as e:
            # print_exception('Rating Not found','eBAy',url,e)
            self.message = self.message + "Rating, "
            return 'NA'

    def condition(self, raw_data,  url):
        try:
            item = raw_data.findAll("div", {"itemprop": "itemCondition"})
            item_condition = item[0].text.replace("\n", " ")
            return item_condition
        except Exception as e:
            # print_exception('iteam condition not found','eBAy',url,e)
            self.message = self.message + "Condition, "
            return 'NA'

    def item_sold(self, raw_data,  url):
        try:
            item1 = raw_data.findAll("span",
                                     {"class": "vi-qtyS-hot-red vi-bboxrev-dsplblk vi-qty-vert-algn vi-qty-pur-lnk"})
            no_of_item_sold = item1[0].text
            return (no_of_item_sold)
        except Exception as e:
            # print_exception('No of items sold not avaliable','eBAy',url,e)
            self.message = self.message + "Items_Sold"
            return 'NA'

    def item_avlb(self, raw_data,  url):
        try:
            item = raw_data.findAll("span", {"id": "qtySubTxt"})
            items_available1 = str(item[0].text).strip()
            items_available = items_available1[:12]
            return items_available
        except Exception as e:
            # print_exception('No of iteams sold not found','eBAy',url,e)
            self.message = self.message + "No of Items Avaliable, "
            return "NA"

    def item_from(self, raw_data,  url):
        try:
            item_location = raw_data.findAll("span", {"itemprop": "availableAtOrFrom"})
            item_country = item_location[0].text.replace(",", "|")
            return (item_country)
        except Exception as e:
            # print_exception('item location not found','eBAy',url,e)
            self.message = self.message + "Item_locaition, "
            return 'NA'

    def shipping_by(self, raw_data,  url):
        try:
            shipping = raw_data.findAll("span", {"id": "fShippingSvc"})
            logistics_name = shipping[0].text.strip()
            return (logistics_name)
        except Exception as e:
            # print_exception('Shipping logistics not found','eBAy',url,e)
            self.message = self.message + "Shipping_logistics, "
            return 'NA'

    def ean(self, raw_data,  url):
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
            # print_exception('Ean not found','eBAy',url,e)
            self.message = self.message + "EAN, "
            return "NA"

    def seller_url(self, raw_data,  url):
        try:
            seller_data = raw_data.findAll("span", {"class": "mbg-nw"})
            seller_name = seller_data[0].text.replace(",", "-")
            seller = raw_data.findAll("div", {"class": "mbg vi-VR-margBtm3"})
            url = seller[0].a['href']
            seller_soup = self.find_page(url)
            seller_Positive = self.seller_positive(seller_soup,  url)
            seller_Negtive = self.seller_negtive(seller_soup,  url)
            seller_Neutral = self.seller_neutral(seller_soup,  url)
            seller_Review = self.seller_allreview(seller_soup,  url)
            seller_Location = self.seller_location(seller_soup,  url)
            seller_Membership = self.seller_membership(seller_soup)
            return str(
                "NA," + seller_Location + "," + seller_name + "," + seller_Negtive + "," + seller_Neutral + "," + seller_Positive + "," + seller_Review + "," + "NA," + seller_Membership)
        except Exception as e:
            # print_exception('Seller Not found','eBAy',url,e)
            self.message = self.message + "Seller_info, "
            return "NA"

    def seller_positive(self, raw_data,  url):
        try:
            positive = raw_data.findAll("span", {"class": "num"})
            positive_review = positive[0].text.replace(",", "-")
            return (positive_review)
        except Exception as e:
            # print_exception('seller_positive review not found','eBAy',url,e)
            self.message = self.message + "seller_positive_Review, "
            return 'NA'

    def seller_negtive(self, raw_data,  url):
        try:
            negtive = raw_data.findAll("span", {"class": "num"})
            negtive_review = negtive[2].text.replace(",", "-")
            return (negtive_review)
        except Exception as e:
            # print_exception('seller_negative not found','eBAy',url,e)
            self.message = self.message + "Seller_Negative_Review, "
            return 'NA'

    def seller_neutral(self, raw_data,  url):
        try:
            neutral = raw_data.findAll("span", {"class": "num"})
            neutral_review = neutral[1].text.replace(",", "-")
            return (neutral_review)
        except Exception as e:
            # print_exception('seller_neutral not found','eBAy',url,e)
            self.message = self.message + "Seller_neutral_review, "
            return 'NA'

    def seller_allreview(self, raw_data,  url):
        try:
            review = raw_data.findAll("div", {"class": "perctg"})
            seller_review = review[0].text.strip().replace(",", "-")[:6]
            return (seller_review)
        except Exception as e:
            # print_exception('seller_overal review not found','eBAy',url,e)
            self.message = self.message + "seller_overall_review, "
            return 'NA'

    def seller_location(self, raw_data,  url):
        try:
            location = raw_data.findAll("span", {"class": "mem_loc"})
            seller_place = location[0].text.replace(",", "-")
            return (seller_place)
        except Exception as e:
            # print_exception('seller_location not found','eBAy',url,e)
            self.message = self.message + "Seller_location, "
            return 'NA'

    def seller_membership(self, raw_data):
        try:
            mem = raw_data.findAll("span", {"class": "info"})
            seller_mem = mem[0].text.replace(",", "|")
            return (seller_mem)
        except Exception as e:
            # print_exception('seller membership Details not found','eBAy',url,e)
            self.message = self.message + "seller_membership, "
            return 'NA'

    def store(self, raw_data,  url):
        try:
            info = raw_data.findAll("div", {"class": "si-ss-eu"})
            store_number = info[0].a['title']
            store_no = store_number.split(" ")
            storename = store_no[1][5:]
            return (storename)
        except Exception as e:
            # print_exception('Store name not found','eBAy',url,e)
            self.message = self.message + "Store, "
            return 'NA'

    def item_num(self, raw_data,  url):
        try:
            item = raw_data.findAll("div", {"id": "descItemNumber"})
            item_number = str(item[0].text)
            return item_number
        except Exception as e:
            # print_exception('Item number not found','eBAy',url,e)
            self.message = self.message + "Item_number, "
            return 'NA'

    def upc(self, raw_data,  url):
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
            # print_exception('UPC number not found','eBAy',url,e)
            self.message = self.message + "UPC, "
            return "NA"

    def warenty(self, raw_data,  url):
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
            # print_exception('Warrenty not found','eBAy',url,e)
            self.message = self.message + "Warrenty, "
            return "NA"

    def isbn(self, raw_data,  url):
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
            # print_exception('ISBN not found','eBAy',url,e)

            return "NA"

    def mpn(self, raw_data,  url):
        try:
            num = raw_data.findAll("h2", {"itemprop": "mpn"})
            MPN = num[0].text.replace(",", "-")
            return MPN
        except Exception as e:
            # print_exception('MPN numbe rnot found','eBAy',url,e)
            self.message = self.message + "MPN, "
            return 'NA'

    def brand(self, raw_data,  url):
        try:
            brnd = raw_data.findAll("h2", {"itemprop": "brand"})
            BRAND = brnd[0].text.replace(",", "-")
            return BRAND
        except Exception as e:
            # print_exception('Brand not found','eBAy',url,e)
            self.message = self.message + "Brand, "
            return 'NA'

    def policy(self, raw_data,  url):
        Return_policy = {}
        try:
            ret = raw_data.findAll("span", {"id": "vi-ret-accrd-txt"})
            return_policy = ret[0].text.strip().replace(",", "-")
            return return_policy
        except Exception as e:
            # print_exception('Return Policy not found','eBAy',url,e)
            self.message = self.message + "Return_policy, "
            return "NA"

    def size(self, raw_data,  url):
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
            # print_exception('item size not found','eBAy',url,e)
            self.message = self.message + "Size, "
            return "NA"

    def specification(self, raw_data,  url):
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
            # print_exception('Specifications not found','eBAy',url,e)
            self.message = self.message + "specifications"
            JSON = json.dumps(spe)
            return JSON

    def get_data(self, raw_data, url,tera_data):


        item_number = self.item_num(raw_data, url)

 
        
        p_url = str(url)
        product = {}
        seller = self.seller_url(raw_data, url)
        seller_details = seller.split(",")
        cost_info = self.price(raw_data, url).split(",")
        # print item_number
        product['sku'] = 'NA'
        product['asin'] = 'NA'  # newprocess
        product['date'] = self.DATE()
        product['time'] = self.TIME()
        product['marketplace'] = 'EBAY_US'
        product['domain'] = 'www.ebay.com'

        product['averageShippingCostUsd'] = tera_data['averageShippingCostUsd']
        product['listingType'] = tera_data['listingType']
        product['title'] = tera_data['title']
        product['maxTransactionDate'] = tera_data['maxTransactionDate']
        product['totalItemsSold'] = tera_data['totalItemsSold']
        product['totalSalesUsd'] = tera_data['totalSalesUsd']
        product['averageItemPriceUsd'] = tera_data['averageItemPriceUsd']
        product['listingCondition'] =tera_data['listingCondition']
        product['totalBids'] = tera_data['totalBids']
        product['linked'] = tera_data['linked']
        product['condition'] = self.condition(raw_data, url)
        product['additional_policies'] = 'NA'
        product['description'] = 'NA'
        product['highlights'] = 'NA'
        product['rating_details'] = 'NA'  # ne
        product['specifications'] = self.specification(raw_data, url)
        try:
            product['seller_overall_rating'] = seller_details[6]
        except:
            product['seller_overall_rating'] = 'NA'
        product['seller_description'] = 'NA'
        product['return_policies'] = self.policy(raw_data, url)
        product['warrenty'] = self.warenty(raw_data, url)
        product['shipping_policies'] = 'NA'
        product['from_manufracture'] = 'NA'  # new
        product['promotion'] = 'NA'  # new
        product['other_format_prices'] = 'NA'  # new
        product['seller_detailed_information'] = 'NA'  # new

        product['saved_price'] = 'NA'
        product['added_date'] = 'NA'
        product['availability'] = 'NA'
        product['brand'] = self.brand(raw_data,  url)
        product['discount_percentage'] = 'NA'
        product['product_selling_price'] = cost_info[0]
        product['product_EAN'] = self.ean(raw_data,  url)
        product['product_id'] = self.item_num(raw_data,  url)
        product['image_url'] = self.img(raw_data,  url)
        product['likes'] = 'NA'
        product['isbn'] = self.isbn(raw_data,  url)
        product['isbn-10'] = 'NA'  # new
        product['isbn-13'] = 'NA'  # new
        product['MPN'] = self.mpn(raw_data,  url)
        product['name'] = self.name(raw_data,  url)
        product['no_of_reviews'] = 'NA'
        product['original_price'] = 'NA'
        product['rating'] = self.rating(raw_data,  url)
        product['shipping_price'] = self.shipping(raw_data,  url)
        product['size'] = self.size(raw_data,  url)
        product['upc'] = self.upc(raw_data,  url)
        product['url'] = url
        product['quantity_available'] = self.item_avlb(raw_data,  url)
        product['products_slod'] = self.item_sold(raw_data,  url)
        try:
            product['seller_code'] = seller_details[0]
        except:
            product['seller_code'] = 'NA'
        try:
            product['seller_location'] = seller_details[1]
        except:
            product['seller_location'] = 'NA'
        try:
            product['seller_name'] = seller_details[2]
        except:
            product['seller_name'] = 'NA'
        try:
            product['seller_negative_rating'] = seller_details[3]
        except:
            product['seller_negative_rating'] = 'NA'
        try:

            product['seller_neutral_rating'] = seller_details[4]
        except:
            product['seller_neutral_rating'] = 'NA'
        try:
            product['seller_positive_rating'] = seller_details[5]
        except:
            product['seller_positive_rating'] = 'NA'
        try:
            product['seller_rank'] = seller_details[7]
        except:
            product['seller_rank'] = 'NA'
        product['seller_store_link'] = "NA"
        try:
            product['seller_year_of_joining'] = seller_details[8]
        except:
            product['seller_year_of_joining'] = 'NA'
        product['shipping_available_countries'] = self.country(raw_data,  url)
        product['shipping_location'] = self.item_from(raw_data, url)
        product['shipping_logistic_name'] = self.shipping_by(raw_data,  url)
        product['shipping_price'] = self.shipping(raw_data,  url)
        product['shop_location'] = 'NA'
        product['shop_name'] = self.store(raw_data, url)
        product['no_of_sales'] = 'NA'
        product['shop_rating'] = 'NA'
        product['Tax_info'] = 'NA'
        product['Visibility'] = 'NA'
        try:
            product['currency'] = cost_info[1]
        except:
            product['currency'] =  'USD'
        product['color_variants'] = 'NA'  # new
        product['style_variants'] = 'NA'  # new
        product['author_name'] = 'NA'  # new
        data_js = json.dumps(product)
        print data_js
        f.write(data_js+'\n')
        # store the data into a tuple because it will be easy to identify which feilds are missing
        


    def process(self,tera_data1):
        tera_data = json.loads(tera_data1)
        line = tera_data['itemId']

        urls = 'https://www.ebay.com/itm/' + str(line).replace('\n', '') + '?rmvSB=true'
        my_url = urls
        uClient = requests.get(my_url)
        page_html = uClient.content
        uClient.close()
        page_soup = soup(page_html, "lxml")
        self.get_data(page_soup, my_url,tera_data)
