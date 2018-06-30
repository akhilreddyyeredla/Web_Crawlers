from Common.Souq_common_imports import *


class ProductDetails:
    def __init__(self):
        self.message = ""

    def ProductSKU(self,page_soup,url):
        return "NA"


    def ProductDate(self):
        today = date.today()
        return str(today)

    def ProductTime(self):
        t = datetime.time(datetime.now())
        return str(t)

    def Name(self,name):
        name = name.split("|")
        concat = ""
        for i in range(0, 11):
            if i < len(name):
                concat = concat + ',{}'.format(name[i])
            else:
                concat = concat + ",Not_Applicable"

        return str(concat).split(',')

    def ProductCondition(self,page_soup, hierarchy,url):
        try:
            # my_dic={}
            condition = page_soup.find('dd', {'class': 'unit-condition'}).text.strip()
            if condition:
                # my_dic['Condition']=condition
                # Condition = json.dumps(my_dic)

                return re.sub('[^a-zA-Z0-9 .]', '', condition)
            else:
                return "not_available"
        except Exception as e:
             #print e
             #print(url)
             #print_exception("Product Condition not found","SOUQ",hierarchy,url,e)
             self.message = self.message + "product_Condition, "
             return "not_available"

    def ProductSavedPrice(self,page_soup, hierarchy,url):
        try:
            saved_price = page_soup.find('span', {'class': 'noWrap'}).text.strip()
            if saved_price:

                return str(saved_price.replace("AED", ""))
            else:
                return "not_available"
        except Exception as e:
            #print e
            #print(url)
            #print_exception("Product_saved price not found","SOUQ",hierarchy,url,ei)
            self.message = self.message + "Product_saved_price, "
        return "not_available"

    def ProductAddedDate(self,page_soup,url):
        return "NA"


    def ProductAdditionalPolicies(self,page_soup,url):
        return "NA"


    def ProductAvailability(self,page_soup, hierarchy,url):
        try:

            availability = page_soup.find('b', {'class': 'txtcolor-alert xleft'}).text.strip().replace(",", "-")
            if availability:
                    Product_Availability = availability
                    return str(Product_Availability)
            else:
                    return "not_available"
        except Exception as e:
            #print e
            #print(url)
            #print_exception("Product_availability not found","SOUQ",hierarchy,url,e)
            self.message = self.message + "Product_Avaliablity, "
            return "not_avaliable"

    def ProductBrand(self,page_soup,url):
        brand = page_soup.find('div', {'class': 'small-12 columns product-title'})
        if brand:
            brand_name = brand.find('a').text

            return re.sub(('[^a-zA-Z0-9 .]'), '', brand_name)
        else:
            return "not_available"


    def ProductDescription(self,page_soup,url):
        my_dic = {}
        desc = page_soup.find_all('div', {'class': 'item-details-mini clearfix'})
        for desct in desc:
            description = desct.find_all('li')
            description_paras = desct.findAll('p')
            if description and len(description_paras) !=0:
                li = []
                for iterate in description:
                    description_list = iterate.text.strip().replace(',', '').replace("$", "")

                    li.append(description_list)
                for description_para in description_paras:
                    display = description_para.text.strip().replace(',', '').replace("$", "")

                    li.append(display)
                my_dic["Description"] = li
            elif description:
                for iterate in description:
                    description_list = iterate.text.strip().replace(',', '').replace("$", "")

                    my_dic["Description"] = description_list
            elif len(description_paras) !=0:
                li = []
                for description_para in description_paras:
                    display = description_para.text.strip().replace(',', '').replace("$", "")

                    li.append(display)
                my_dic["Description"] = li

        final_description = json.dumps(my_dic).replace(",", "_")
        return final_description


    def ProductDiscountPercentage(self,page_soup, hierarchy,url):
        try:
            discount_percent = page_soup.find('span', {'class': 'discount'}).text.strip().replace(",", "-")
            if discount_percent:

                return str(discount_percent)
            else:
                return "not_available"
        except Exception as e:
            #print e
            #print(url)
            #print_exception("Discount percentage not found","SOUQ",hierarchy,url,e)
            self.message = self.message + "Discount percentage, "
            return "not_available"


    def ProductSellingPrice(self,page_soup,url):
        selling_price = page_soup.find('h3', {'class': 'price is sk-clr1'})
        if selling_price:
            price = selling_price.text.strip()

            return price.replace("AED", "").replace(',', '')
        else:
            return "not_available"


    def ProductEAN(self,page_soup, hierarchy,url):
        container1 = page_soup.find_all('div', {'id': 'specs-full'})
        if container1:
            for num in container1:
                spe = num.find_all('dl', {'class': 'stats'})
                for specfi in spe:
                    names = specfi.find_all('dt')
                    Specication = specfi.find_all('dd')
                    for i in range(20):
                        try:
                            fun = names[i].text
                            fun1 = Specication[i].text
                            if fun == "Item EAN":

                                return str(fun1)
                        except Exception as e:
                            #print e
                            #print(url)
                            #print_exception("Product_Ean not found","SOUQ",hierarchy,url,e)
                            self.message = self.message + "Ean, "
                            return "not_available"
        else:
            return "not_available"


    def ProductHighlights(self,page_soup,url):
        return "NA"


    def ProductId(self,page_soup,url):
        return "NA"


    def ProductImageUrl(self,page_soup,url):
        image = page_soup.find('div', {'class': 'img-bucket zoom-enabled'})
        zoom_image = page_soup.find('div', {'class': 'img-bucket'})
        if image:

            return str(image.img['src'])

        elif zoom_image:
            # image_url=zoom_image.img['src']

            return str(zoom_image.img['src'])
        else:
            return "not_available"


    def ProductISBN(self,page_soup, hierarchy,url):
        container1 = page_soup.find_all('div', {'id': 'specs-full'})
        if container1:
            for x in container1:
                spe = x.find_all('dl', {'class': 'stats'})
                for specfi in spe:
                    names = specfi.find_all('dt')
                    Specication = specfi.find_all('dd')
                    for i in range(20):
                        try:
                            fun = names[i].text
                            fun1 = Specication[i].text
                            if fun == "ISBN":

                                return str(fun1)
                        except Exception as e:
                             #print e
                             #print(url)
                             #print_exception("ISBN not found","SOUQ",hierarchy,url,e)
                             self.message = self.message + "ISBN, "
                             return "not_available"
        else:
            return "not_available"


    def ProductLikes(self,page_soup,url):
        return "NA"


    def ProductMPN(self,page_soup,url):
        return "NA"


    def ProductName(self,page_soup, hierarchy,url):
        try:
            product_title = page_soup.find('h1').text.strip().replace(',', '-')

            return re.sub(('[^a-zA-Z0-9 .]'), '', product_title)
        except Exception as e:
             #print e
             #print(url)
             #print_exception("Product_name not found","SOUQ",hierarchy,url,e)
             self.message = self.message + "Product_name, "
             return "not_available"


    def ProductNoOfReviews(self,page_soup,url):
        return "NA"


    def ProductOriginalPrice(self,page_soup, hierarchy,url):
        try:
            original_price = page_soup.find('span', {'class': 'was'}).text.strip()
            if original_price:

                return str(original_price.replace("AED", ""))
            else:
                return "not_available"
        except Exception as e:
            #print e
            #print(url)
            # print_exception("product_orginal_price not found","SOUQ",hierarchy,url,e)
            self.message = self.message + "product_orginal_price, "
            return "not_available"


    def Productrating(self,page_soup, hierarchy,url):
        try:
            rating = page_soup.find('div', {'class': 'rate-of-avg'}).text.strip()
            if rating:

                return str(rating)
            else:
                return "not_available"
        except Exception as e:
             #print e
             #print(url)
             #print_exception("product_rating not found","SOUQ",hierarchy,url,e)
             self.message = self.message + "Product_rating, "
             return "not_available"


    def ProductShippingPrices(self,page_soup,url):
        return "NA"


    def ProductSize(self,page_soup, hierarchy,url):
        container1 = page_soup.find_all('div', {'id': 'specs-full'})
        if container1:
            for num in container1:
                spe = num.find_all('dl', {'class': 'stats'})
                for specfi in spe:
                    names = specfi.find_all('dt')
                    Specication = specfi.find_all('dd')
                    for i in range(24):
                        try:
                            fun = names[i].text
                            fun1 = Specication[i].text
                            if fun == "Size":

                                return str(fun1)
                        except Exception as e:
                            #print e
                            #print(url)
                            #print_exception("Product_size not found","SOUQ",hierarchy,url,e)
                            self.message = self.message + "product_Size, "
                            return "not_available"""
        else:
            return "not_available"


    def ProductSpecifications(self,page_soup, hierarchy,url):
        my_dic = {}
        i = 0
        container1 = page_soup.find_all('div', {'id': 'specs-short'})
        if container1:
            for x in container1:
                spe = x.find_all('dl', {'class': 'stats'})
                for specfi in spe:
                    names = specfi.find_all('dt')
                    Specication = specfi.find_all('dd')
                    for i in range(len(names)):
                        try:
                            fun = names[i].text
                            fun1 = Specication[i].text
                            my_dic[fun] = fun1
                        except Exception as e:
                            #print e
                            #print url
                            #print_exception("Product_Specification not found","SOUQ",hierarchy,url,e)
                            self.message = self.message + "Specifications, "
                            pass

            some = json.dumps(my_dic).replace(",", " ")

            return re.sub('[^a-zA-Z0-9 .]', '', some)
        else:
            return "not_available"


    def ProductUPC(self,page_soup,url):
        return "NA"


    def ProductsAvailable(self,page_soup,url):
        return "NA"


    def ProductsSold(self,page_soup,url):
        return "NA"


    def ProductReturnPolicies(self,page_soup,url):
        return "NA"


    def SellerCode(self,page_soup,url):
        return "NA"


    def SellerLocation(self,page_soup,url):
        return "NA"


    def SellerName(self,page_soup, hierarchy,url):
            try:
                    sold = page_soup.find('span', {'class': 'unit-seller-link'})
                    if len(sold)==0:
                            return "not_avaliable"

                    else:
                            seller = sold.text.strip().encode('utf-8')
                            try:
                                    name = seller.split('(')
                                    return name[0]
                            except Exception as e:
                                    #print e
                                    #print url
                                    #print_exception("seller name not found","SOUQ",hierarchy,url,e)
                                    self.message = self.message + "seller_name, "
                                    return seller
            except Exception as e:
                    #print e
                    #print(url)
                    #print_exception("seller not found","SOUQ",hierarchy,url,e)
                    self.message = self.message + "seller_field, "
                    return "not_avaliable"


    def SellerNegativeRating(self,page_soup,url):
        return "NA"


    def SellerNeutralRating(self,page_soup,url):
        return "NA"


    def SellerPositiveRating(self,page_soup,url):
        return "NA"


    def SellerOverallRating(self,page_soup,url):
        return "NA"


    def SellerRank(self,page_soup,url):
        return "NA"


    def SellerYearOfJoining(self,page_soup,url):
        return "NA"


    def ShippingAvailableCountries(self,page_soup,url):
        return "NA"


    def ShippingLocation(self,page_soup,url):
        return "NA"


    def ShippingLogisticName(self,page_soup,url):
        return "NA"


    def ShippingPrice(self,page_soup,url):
        return "NA"


    def ShopLocation(self,page_soup,url):
        return "NA"


    def ShopName(self,page_soup,url):
        return "NA"


    def ShopNoOfSales(self,page_soup,url):
        return "NA"


    def ShopRating(self,page_soup,url):
        return "NA"


    def TaxInformation(self,page_soup,url):
        return "NA"


    def ProductVisibility(self,page_soup,url):
        return "NA"


    def ProductWarranty(self,page_soup,url):
        return "NA"


    def ProductShippingPolicies(self,page_soup,url):
        return "NA"


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


    def get_data(self,raw_data, hierarchy, product_url):
        product_url = product_url
        main_name = self.Name(hierarchy)
        product = dict()

        # product is a dictionary and used superset field names as keys and get values by your own
        # parsing methods and assign them key values

        product['sku']                            = self.ProductSKU(raw_data,product_url)
        product['asin']                           = 'NA'
        product['date']                           = self.ProductDate()
        product['time']                           = self.ProductTime()
        product['marketplace']                    = DataCollectors_Configuration.PROJECT_NAME
        product['domain']                         = DataCollectors_Configuration.PROJECT_DOMAIN
        product['category']                       = main_name[1]
        product['category_level_1']               = main_name[2]
        product['category_level_2']               = main_name[3]
        product['category_level_3']               = main_name[4]
        product['category_level_4']               = 'NA'
        product['category_level_5']               = 'NA'
        product['category_level_6']               = 'NA'
        product['category_level_7']               = 'NA'
        product['category_level_8']               = 'NA'
        product['category_level_9']               = 'NA'


        product['condition']                    = self.ProductCondition(raw_data,hierarchy,product_url)
        product['additional_policies']          = self.ProductAdditionalPolicies(raw_data,product_url)
        product['description']                  = self.ProductDescription(raw_data,product_url)
        product['highlights']                   = self.ProductHighlights(raw_data,product_url)
        product['rating_details']               = 'NA'
        product['specifications']               = self.ProductSpecifications(raw_data,hierarchy,product_url)
        product['seller_overall_rating']        = self.SellerOverallRating(raw_data,product_url)
        product['seller_description']           = 'NA'
        product['return_policies']              = self.ProductReturnPolicies(raw_data,product_url)
        product['warrenty']                     = self.ProductWarranty(raw_data,product_url)
        product['shipping_policies']            = self.ProductShippingPolicies(raw_data,product_url)
        product['from_manufracture']            = 'NA'
        product['promotion']                    = 'NA'
        product['other_format_prices']          = 'NA'
        product['seller_detailed_information']  = 'NA'

        product['saved_price']                  = self.ProductSavedPrice(raw_data,hierarchy,product_url)
        product['added_date']                   = self.ProductAddedDate(raw_data,product_url)
        product['availability']                 = self.ProductAvailability(raw_data,hierarchy,product_url)
        product['brand']                        = self.ProductBrand(raw_data,product_url)
        product['discount_percentage']          = self.ProductDiscountPercentage(raw_data,hierarchy,product_url)
        product['product_selling_price']        = self.validate_selling_price(self.ProductSellingPrice(raw_data,product_url))
        product['product_EAN']                  = self.ProductEAN(raw_data,hierarchy,product_url)
        product['product_id']                   = self.ProductId(raw_data,product_url)
        product['image_url']                    = self.ProductImageUrl(raw_data,product_url)
        product['likes']                        = self.ProductLikes(raw_data,product_url)
        product['isbn']                         = self.ProductISBN(raw_data,hierarchy,product_url)
        product['isbn-10']                      = 'NA'
        product['isbn-13']                      = 'NA'
        product['MPN']                          = self.ProductMPN(raw_data,product_url)
        product['name']                         = self.ProductName(raw_data,hierarchy,product_url)
        product['no_of_reviews']                = self.ProductNoOfReviews(raw_data,product_url)
        product['original_price']               = self.ProductOriginalPrice(raw_data,hierarchy,product_url)
        product['rating']                       = self.Productrating(raw_data,hierarchy,product_url)
        product['shipping_price']               = self.ShippingPrice(raw_data,product_url)
        product['size']                         = self.ProductSize(raw_data,hierarchy,product_url)
        product['upc']                          = self.ProductUPC(raw_data,product_url)
        product['url']                          = product_url
        product['quantity_available']           = self.ProductsAvailable(raw_data,product_url)
        product['products_slod']                = self.ProductsSold(raw_data,product_url)
        product['seller_code']                  = self.SellerCode(raw_data,product_url)
        product['seller_location']              = self.SellerLocation(raw_data,product_url)
        product['seller_name']                  = self.SellerName(raw_data,hierarchy,product_url)
        product['seller_negative_rating']       = self.SellerNegativeRating(raw_data,product_url)
        product['seller_neutral_rating']        = self.SellerNeutralRating(raw_data,product_url)
        product['seller_positive_rating']       = self.SellerPositiveRating(raw_data,product_url)
        product['seller_rank']                  = self.SellerRank(raw_data,product_url)
        product['seller_store_link']            = 'NA'
        product['seller_year_of_joining']       = self.SellerYearOfJoining(raw_data,product_url)
        product['shipping_available_countries'] = self.ShippingAvailableCountries(raw_data,product_url)
        product['shipping_location']            = self.ShippingLocation(raw_data,product_url)
        product['shipping_logistic_name']       = self.ShippingLogisticName(raw_data,product_url)
        product['shipping_price']               = self.ShippingPrice(raw_data,product_url)
        product['shop_location']                = self.ShopLocation(raw_data,product_url)
        product['shop_name']                    = self.ShopName(raw_data,product_url)
        product['no_of_sales']                  = self.ShopNoOfSales(raw_data,product_url)
        product['shop_rating']                  = self.ShopRating(raw_data,product_url)
        product['Tax_info']                     = 'NA'
        product['Visibility']                   = 'NA'
        product['currency']                     = 'AED'
        product['color_variants']               = 'NA'
        product['style_variants']               = 'NA'
        product['author_name']                  = 'NA'
        #data_json = {'sku':self.ProductSKU(raw_data, product_url),'asin':'NA','date' : self.ProductDate(),'time':self.ProductTime(),'marketplace' : CONSTANTS.PROJECT_NAME,'domain' : CONSTANTS.PROJECT_DOMAIN,'category' : main_name[1],'category_level_1' : main_name[2],'category_level_2' : main_name[3],'category_level_3' : main_name[4],'category_level_4' : 'NA','category_level_5' : 'NA','category_level_6' : 'NA','category_level_7' : 'NA','category_level_8' : 'NA','category_level_9' : 'NA','condition' : self.ProductCondition(raw_data, hierarchy, product_url),'additional_policies' : self.ProductAdditionalPolicies(raw_data, product_url),'description' : self.ProductDescription(raw_data, product_url),'highlights' : self.ProductHighlights(raw_data, product_url),'rating_details' : 'NA','specifications' : self.ProductSpecifications(raw_data, hierarchy, product_url),'seller_overall_rating' : self.SellerOverallRating(raw_data, product_url),'seller_description' : 'NA','return_policies' : self.ProductReturnPolicies(raw_data, product_url),'warrenty' : self.ProductWarranty(raw_data, product_url),'shipping_policies' : self.ProductShippingPolicies(raw_data, product_url),'from_manufracture' : 'NA','promotion' : 'NA','other_format_prices' : 'NA','seller_detailed_information' : 'NA','saved_price' : self.ProductSavedPrice(raw_data, hierarchy, product_url),'added_date' : self.ProductAddedDate(raw_data, product_url),'availability' : self.ProductAvailability(raw_data, hierarchy, product_url),'brand' : self.ProductBrand(raw_data, product_url),'discount_percentage' : self.ProductDiscountPercentage(raw_data, hierarchy, product_url),'product_selling_price' : self.validate_selling_price(self.ProductSellingPrice(raw_data, product_url)),'product_EAN' : self.ProductEAN(raw_data, hierarchy, product_url),'product_id' : self.ProductId(raw_data, product_url),'image_url' : self.ProductImageUrl(raw_data, product_url),'likes' : self.ProductLikes(raw_data, product_url),'isbn' : self.ProductISBN(raw_data, hierarchy, product_url),'isbn-10' : 'NA','isbn-13' : 'NA','MPN' : self.ProductMPN(raw_data, product_url),'name' : self.ProductName(raw_data, hierarchy, product_url),'no_of_reviews' : self.ProductNoOfReviews(raw_data, product_url),'original_price' : self.ProductOriginalPrice(raw_data, hierarchy, product_url),'rating' : self.Productrating(raw_data, hierarchy, product_url),'shipping_price' : self.ShippingPrice(raw_data, product_url),'size' : self.ProductSize(raw_data, hierarchy, product_url),'upc' : self.ProductUPC(raw_data, product_url),'url' : product_url,'quantity_available': self.ProductsAvailable(raw_data, product_url),'products_slod' : self.ProductsSold(raw_data, product_url),'seller_code' : self.SellerCode(raw_data, product_url),'seller_location' : self.SellerLocation(raw_data, product_url),'seller_name' : self.SellerName(raw_data, hierarchy, product_url),'seller_negative_rating' : self.SellerNegativeRating(raw_data, product_url),'seller_neutral_rating' : self.SellerNeutralRating(raw_data, product_url),'seller_positive_rating' : self.SellerPositiveRating(raw_data, product_url),'seller_rank' : self.SellerRank(raw_data, product_url),'seller_store_link' : 'NA','seller_year_of_joining' : self.SellerYearOfJoining(raw_data, product_url),'shipping_available_countries' : self.ShippingAvailableCountries(raw_data, product_url),'shipping_location' : self.ShippingLocation(raw_data, product_url),'shipping_logistic_name' : self.ShippingLogisticName(raw_data, product_url),'shipping_price' : self.ShippingPrice(raw_data, product_url),'shop_location' : self.ShopLocation(raw_data, product_url),'shop_name' : self.ShopName(raw_data, product_url),'no_of_sales' : self.ShopNoOfSales(raw_data, product_url),'shop_rating' : self.ShopRating(raw_data, product_url),'Tax_info' : 'NA','Visibility' : 'NA','currency' : 'AED','color_variants' : 'NA','style_variants' : 'NA','author_name' : 'NA'}

        # store the data into a tuple because it will be easy to identify which feilds are missing
        #print data_json
        #if not os.path.exists('test_data'):
            #os.makedirs('test_data')

        #completed_path = '{}{}{}{}'.format(DataCollectors_Configuration.SOUQ_URL_ROOT_FOLDER,'test_data', DataCollectors_Configuration.PATH_STYLE, 'data')

        #f = open(completed_path, 'a+')
        #f.write(str(data_json)+'\n')
        print_exception(self.message,'Souq',hierarchy,product_url,"NA")
        return product
