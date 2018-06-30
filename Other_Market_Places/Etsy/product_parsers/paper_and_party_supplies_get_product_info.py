from Common.Etsy_common_imports import *
'''
This takes beautifulSoup object and parse it and returns required details 
the details which will be returned if present or else it will return not_available

'''
class Product_Details:
    def __int__(self):
        self.message = ""


    def get_date_and_time(self):
        current_date = datetime.datetime.now()
        current_date.strftime("%y-%m-%d %H:%M:%S")
        current_date = str(current_date)
        return current_date.split(" ")


    def get_hirerachy(self,hirerachy):
        items = hirerachy.split('|')
        length = len(items)
        category_names = ''
        for level in range(0, 12):
            if level < length:
                category_names = category_names + '{},'.format(items[level])
            else:
                category_names = category_names + 'not_available,'
        return category_names.split(',')


    def get_shop_name(self,raw_data):
        shop_name = raw_data.find('span', {'itemprop': 'title'})
        if shop_name:
            return shop_name.text
        else:
            return 'not_available'


    def get_seller_name(self,raw_data):
        seller_name_tag = raw_data.find('div', {'class': 'show-lg show-xl show-tv shop-owner col-xs-3 text-center'})
        if seller_name_tag:
            seller_name = seller_name_tag.find('p').text
            if seller_name:
                return seller_name
            else:
                return 'not_available'
        else:
            return 'not_available'


    def get_shop_rating(self,raw_data):
        rating_tag = raw_data.find('input', {'name': 'rating'})
        if rating_tag:
            rating = str(rating_tag['value'])
            return rating
        else:
            return 'not_available'


    def get_year_of_joining(self,raw_data):
        year_tag = raw_data.find('span', {'class': 'etsy-since no-wrap'})
        if year_tag:
            year = year_tag.text
            year = year.split(' ')
            return str(year[-1])
        else:
            return 'not_available'


    def get_shop_loaction(self,raw_data):
        location_tag = raw_data.find('span', {'data-key': 'user_location'})
        if location_tag:
            location = location_tag.text.strip()
            location = location.replace(', ', '-')
            return location
        else:
            return 'not_available'


    def get_no_of_sales(self,raw_data):
        sales_tag = raw_data.findAll('span', {'class': 'mr-xs-2 pr-xs-2 br-xs-1'})
        if sales_tag[0]:
            no_of_sales = sales_tag[0].text.split(' ')
            return no_of_sales[0]
        else:
            return 'not_available'


    def get_no_of_likes_for_shop(self,raw_data):
        # < a class ="" href="/in-en/shop/myAgenda365/favoriters" rel="nofollow" > 764 Admirers < / a > < / div >
        shop_likes_tags = raw_data.find('div', {'class': 'mt-lg-5 pt-lg-2 bt-xs-1'})
        if shop_likes_tags:
            shop_likes_anchor_tags = shop_likes_tags.findAll('a')
            if shop_likes_anchor_tags:
                try:
                    shop_likes_text = shop_likes_anchor_tags[1].text
                    shop_likes = shop_likes_text.split(' ')
                    return shop_likes[0]
                except:
                    self.message = self.message + "shop_likes, "
                    return 'not_available'
            else:
                return 'not_available'
        else:
            return 'not_available'


    def get_item_name(self,raw_data):
        my_name = raw_data.find('span', {'itemprop': 'name'})
        if my_name:
            my_name = my_name.text.strip()
            name = re.sub('[^a-zA-Z0-9.]', '_', my_name)
            return name
        else:
            return 'not_available'


    def get_overview(self,raw_data):
        overview_raw = raw_data.find('div', {'id': 'item-overview'})
        if overview_raw:
            overview_tag = overview_raw.find('ul', {'class': 'properties'})
            if overview_tag:
                overview_tag = str(overview_tag).replace('</li>', "|")
                overview_text = BeautifulSoup(overview_tag, 'html.parser').text.strip()
                overview = re.sub('[^a-zA-Z0-9 |:]', '_', overview_text)
                return overview
            else:
                return 'not_available'
        else:
            return 'not_available'


    def get_acutalprice(self,raw_data):
        price = raw_data.find('meta', {'itemprop': 'price'})
        currency = raw_data.find('meta', {'itemprop': 'currency'})
        if price and currency:
            acutal_price = price['content'].replace(',', '')
            return acutal_price
        return 'not_available'


    def get_image(self,raw_data):
        image_url = raw_data.find('li', {'id': 'image-1'})
        if image_url:
            image_url = image_url['data-full-image-href']
            return image_url
        else:
            return 'not_available'


    def get_description(self,raw_data):
        p_description = raw_data.find('div', {'class': 'preview-text'})
        if p_description:
            p_description = p_description.text.strip()
            description = re.sub('[^a-zA-Z0-9 .]', '', p_description)
            return description
        else:
            return 'not_available'


    def get_shiiping_details(self,raw_data):
        shipping = raw_data.find('div', {'class': 'col-xs-12 pl-lg-0 pr-lg-0 pb-xs-1 pb-lg-0 pt-xs-1'})
        if shipping:

            shipping_from = raw_data.find('div', {'class': 'text-gray mb-xs-1 mt-xs-1'})

            if shipping_from:
                shipping_from = shipping_from.text.strip()
                return shipping_from
            else:
                return 'not_available'
        else:
            return 'not_available'


    def get_shiiping_locations(self,raw_data):
        locations_can_be_shipped = raw_data.find('select', {'name': 'estimate-country'})
        if locations_can_be_shipped:
            locations = re.sub('[^a-zA-Z0-9 .]', '_', locations_can_be_shipped.text.strip())
            return locations.replace(',', '|')
        else:
            return 'not_available'


    def get_rating(self,raw_data):
        rating_data = raw_data.find('div', {'class': 'stars-svg '})
        if rating_data:
            rating_tag = rating_data.find('input', {'name': 'rating'})
            if rating_data:
                rating_value = rating_tag['value'].strip()
                return rating_value
            else:
                return 'not_available'
        else:
            return 'not_available'


    def get_no_of_review(self,raw_data):
        reviews_data = raw_data.find('span', {'class': 'pl-xs-1 text-gray-lighter'})
        if reviews_data:
            ref = re.sub('[(*,*)]', '', reviews_data.text.strip())
            return str(ref)
        else:
            return 'not_available'


    def get_refunds_details(self,raw_data):
        refunds_tags = raw_data.find('div', {'data-id': 'refunds'})
        if refunds_tags:
            refunds = refunds_tags.find('div', {'class': 'content-toggle-body text-gray prose'})
            if refunds:
                refund_data = re.sub('[^a-zA-Z0-9 .]', '', refunds.text)
                return refund_data
            else:
                return 'not_available'
        else:
            return 'not_available'


    def get_product_id(self,raw_data):
        listing_id = raw_data.find('input', {'name': 'listing_inventory_id'})
        if listing_id:
            id_ = listing_id['value']
            return id_
        else:
            return 'not_available'


    def get_seller_details(self,raw_data):
        url_tag = raw_data.find('a', {'itemprop': 'url'})

        if url_tag:
            url = url_tag['href']
            response_obj = response_getter.Response()
            shop_raw_data = response_obj.get_content(url)

            if shop_raw_data:
                seller_name = self.get_seller_name(shop_raw_data)

                shop_rating = self.get_shop_rating(shop_raw_data)

                year_of_joining = self.get_year_of_joining(shop_raw_data)

                shop_location = self.get_shop_loaction(shop_raw_data)

                no_of_sales = self.get_no_of_sales(shop_raw_data)

                no_of_likes_for_shop = self.get_no_of_likes_for_shop(shop_raw_data)

                seller_data = list()
                seller_data.append('NA')  # seller code
                seller_data.append(shop_location)  # seller loaction
                seller_data.append(seller_name)  # seller name
                seller_data.append('NA')  # seller negative_ rating
                seller_data.append('NA')  # seller nuetral_rating
                seller_data.append(no_of_likes_for_shop)  # seller postive rating
                seller_data.append(shop_rating)  # seller overall rating
                seller_data.append('NA')  # seller rank
                seller_data.append(year_of_joining)  # seller year if joining
                seller_data.append(self.get_shiiping_locations(raw_data))  # shipping avaible country
                seller_data.append(self.get_shiiping_details(raw_data))  # shipping location
                seller_data.append(self.get_shiiping_details(raw_data))  # shop name
                seller_data.append('NA')  # no_of_sales
                seller_data.append(shop_location)  # shop_rating
                seller_data.append(self.get_shop_name(raw_data))  # shop name
                seller_data.append(no_of_sales)  # no of sales
                seller_data.append(shop_rating)  # shop rating

                return seller_data
        return 'NA,not_available,NA,NA,NA,not_available,NA,not_available,not_available,NA,not_available,NA,NA,' \
               'not_available,not_available,not_available,not_available '.split(',')


    def get_listing_id(self,url):
        items = url.split('/')
        return items[5]


    def get_quantity_availble(self,raw_data):
        quantity_tags = raw_data.find('select', {'id': 'inventory-select-quantity'})
        if quantity_tags:
            quantity = quantity_tags.findAll('option')
            if quantity:
                return quantity[-1].text
            else:
                return 'not_available'
        else:
            return 'not_available'


    def get_shipping_policies(self,raw_data):
        shipping_polices_tag = raw_data.find('div', {'data-appears-component-name': 'listing_page_policy_shipping_details'})

        if shipping_polices_tag:
            shipping = shipping_polices_tag.find('div', {'class': 'preview-text text-gray prose'})
            if shipping:
                shipping_polices = re.sub('[^a-zA-Z0-9 .]', '', shipping.text.strip())
                return shipping_polices
            else:
                return 'not_available'
        else:
            return 'not_available'


    def get_listing_date(self,raw_data):
        date_tag = raw_data.find('div', {'id': 'fineprint'})
        if date_tag:
            listed_date = date_tag.findAll('li')
            if listed_date:
                listed = re.sub('[^a-zA-Z0-9]', '-', listed_date[0].text).replace('--', '-').split('-')
                if listed:
                    listing_date = '-'.join(listed[2:])
                    return listing_date
                else:
                    return 'not_available'
            else:
                return 'not_available'
        else:
            return 'not_available'


    def get_additonal_policies(self,raw_data):
        additional_polices_tag = raw_data.find('div', {'data-appears-component-name': 'listing_page_policy_additional'})
        if additional_polices_tag:
            additonal_polices = re.sub('[^a-zA-Z0-9 .]', '', additional_polices_tag.text.strip())
            return additonal_polices
        else:
            return 'not_available'


    def get_likes(self,raw_data):
        likes_tag = raw_data.find('div', {'id': 'fineprint'})
        if likes_tag:
            likes = likes_tag.findAll('li')
            if likes[1]:
                return likes[1].text.strip().split(' ')[0]
        else:
            return 'not_available'


    def get_product_condition(self):
        return 'NA'


    def get_product_saved_price(self,raw_data):
        saved_price = raw_data.find('p', {'class', 'text-smallest promo-saving-text'})
        if saved_price:
            return saved_price.text.strip().split(' ')[-2]
        else:
            return 'not_available'


    def get_discount_price(self,raw_data):
        discount_price = raw_data.find('strike', {'class', 'text-gray-lighter text-smallest normal'})
        if discount_price:
            price = re.sub('[^a-zA-Z0-9.]', '', discount_price.text.strip()).split(' ')[-1]
            return price.replace('US', '')
        else:
            return 'not_available'


    def get_discount_percentage(self,raw_data):
        saved_price = raw_data.find('p', {'class', 'text-smallest promo-saving-text'})
        if saved_price:
            return re.sub('[^a-zA-Z0-9 .]', '', saved_price.text.strip().split(' ')[-1])
        else:
            return 'not_available'


    def find_if_handmade(self,raw_data):
        hand_made_container = raw_data.find('div', {'id': 'handmadeLogo_feature_div'})
        if hand_made_container:
            return True
        else:
            return False


    def find_if_exits(self,input_val):
        if input_val:
            if 'not_available' in input_val:
                return 'not_available'
            return input_val.replace('_', '')
        else:
            return 'not_available'


    def validate_selling_price(self,input_val):
        if input_val == '.':
            return 'not_available'
        else:
            return input_val


    def find_average_price(self,input_val):
        if '-' in input_val:
            values = input_val.split('-')
            if len(values) != 0:
                avg = 0
                for value in values:
                    avg = avg+float(value)
                avg = avg/2
                return avg
        if 'not_available' == input_val:
            return float(0)

        else:
            return float(input_val)


    def get_data_for_cassandra(self,product_dic):
        product = dict()
        product['id']               = uuid.uuid1()
        product['asin']             = product_dic['asin']
        product['category']         = product_dic['category']
        product['category_level_1'] = product_dic['category_level_1']
        product['category_level_2'] = product_dic['category_level_2']
        product['category_level_3'] = product_dic['category_level_3']
        product['currency']         = product_dic['currency']
        product['date']             = product_dic['date']
        product['marketplace']      = product_dic['marketplace']
        product['price']            = self.find_average_price(product_dic['product_selling_price'])
        product['product_id']       = product_dic['product_id']
        product['seller_name']      = product_dic['seller_name']
        product['additional_info']  = {}

        product_keys = product.keys()
        product_dic_keys = product_dic.keys()

        for key in product_dic_keys:
            if key not in product_keys:
                product['additional_info'].update(((key, product_dic[key]),))

        return product


    def get_data(self,raw_data, hierarchy, product_url):
        hirerachy_list = self.get_hirerachy(hierarchy)
        date = self.get_date_and_time()
        seller_data = self.get_seller_details(raw_data)
        product = dict()

        # print(hirerachy_list)
        # product is a dictionary and used superset field names as keys and get values by your own
        # parsing methods and assign them key values

        product['sku']                            = 'NA'
        product['asin']                           = 'NA'
        product['date']                           = date[0]
        product['time']                           = date[1]
        product['marketplace']                    = hirerachy_list[0]
        product['domain']                         = hirerachy_list[1]
        product['category']                       = hirerachy_list[2]
        product['category_level_1']               = hirerachy_list[3]
        product['category_level_2']               = hirerachy_list[4]
        product['category_level_3']               = hirerachy_list[5]
        product['category_level_4']               = hirerachy_list[6]
        product['category_level_5']               = hirerachy_list[7]
        product['category_level_6']               = hirerachy_list[8]
        product['category_level_7']               = hirerachy_list[9]
        product['category_level_8']               = hirerachy_list[10]
        product['category_level_9']               = hirerachy_list[11]


        product['condition']                    = 'NA'
        product['additional_policies']          = self.get_additonal_policies(raw_data)
        product['description']                  = self.get_description(raw_data)
        product['highlights']                   = self.get_overview(raw_data)
        product['rating_details']               = 'NA'
        product['specifications']               = 'NA'
        product['seller_overall_rating']        = seller_data[6]
        product['seller_description']           = 'NA'
        product['return_policies']              = self.get_refunds_details(raw_data)
        product['warrenty']                     = 'NA'
        product['shipping_policies']            = self.get_shipping_policies(raw_data)
        product['from_manufracture']            = 'NA'
        product['promotion']                    = 'NA'
        product['other_format_prices']          = 'NA'
        product['seller_detailed_information']  = 'NA'


        product['saved_price']                  = self.get_product_saved_price(raw_data)
        product['added_date']                   = self.get_listing_date(raw_data)
        product['availability']                 = 'NA'
        product['brand']                        = 'NA'
        product['discount_percentage']          = self.get_discount_percentage(raw_data)
        product['product_selling_price']        = self.validate_selling_price(self.get_acutalprice(raw_data))
        product['product_EAN']                  = 'NA'
        product['product_id']                   = self.get_listing_id(product_url)
        product['image_url']                    = self.get_image(raw_data)
        product['likes']                        = self.get_likes(raw_data)
        product['isbn']                         = 'NA'
        product['isbn-10']                      = 'NA'
        product['isbn-13']                      = 'NA'
        product['MPN']                          = 'NA'
        product['name']                         = self.get_item_name(raw_data)
        product['no_of_reviews']                = self.get_no_of_review(raw_data)
        product['original_price']               = self.get_discount_price(raw_data)
        product['rating']                       = self.get_rating(raw_data)
        product['shipping_price']               = 'NA'
        product['size']                         = 'NA'
        product['upc']                          = 'NA'
        product['url']                          = product_url
        product['quantity_available']           = self.get_quantity_availble(raw_data)
        product['products_slod']                = 'NA'
        product['seller_code']                  = seller_data[0]
        product['seller_location']              = seller_data[1]
        product['seller_name']                  = seller_data[2]
        product['seller_negative_rating']       = seller_data[3]
        product['seller_neutral_rating']        = seller_data[4]
        product['seller_positive_rating']       = seller_data[5]
        product['seller_rank']                  = seller_data[7]
        product['seller_store_link']            = 'NA'
        product['seller_year_of_joining']       = seller_data[8]
        product['shipping_available_countries'] = seller_data[9]
        product['shipping_location']            = seller_data[10]
        product['shipping_logistic_name']       = seller_data[11]
        product['shipping_price']               = seller_data[12]
        product['shop_location']                = seller_data[13]
        product['shop_name']                    = seller_data[14]
        product['no_of_sales']                  = seller_data[15]
        product['shop_rating']                  = seller_data[16]
        product['Tax_info']                     = 'NA'
        product['Visibility']                   = 'NA'
        product['currency']                     = 'USD'
        product['color_variants']               = 'NA'
        product['style_variants']               = 'NA'
        product['author_name']                  = 'NA'
        print_exception(self.message,product['marketplace'],hierarchy,product_url,"NA")
        return product
