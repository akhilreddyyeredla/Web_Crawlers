from Common.Bonanza_common_imports import *


class ProductDetails():
    def __init__(self):
        self.message = ""

    def find_if_exits(self, input_val):
        if input_val:
            if 'not_available' in input_val:
                return 'not_available'
            return input_val.replace('_', '')
        else:
            return 'not_available'

    def validate_selling_price(self, input_val):
        if input_val == '.':
            return 'not_available'
        else:
            return input_val

    def get_data(self, product_parameters):
        product = dict()

        # product is a dictionary and used superset field names as keys and get values by your own
        # parsing methods and assign them key values

        product['sku'] = product_parameters['SKU']
        product['asin'] = "NA"  # new
        product['date'] = product_parameters['Date']
        product['time'] = product_parameters['Time']
        product['marketplace'] = product_parameters["Marketplace"]
        product['domain'] = product_parameters["Domain"]
        product['category'] = product_parameters["Category"]
        product['category_level_1'] = product_parameters["SubCategory1"]
        product['category_level_2'] = product_parameters["SubCategory2"]
        product['category_level_3'] = product_parameters["SubCategory3"]
        product['category_level_4'] = product_parameters["SubCategory4"]
        product['category_level_5'] = product_parameters["SubCategory5"]
        product['category_level_6'] = product_parameters["SubCategory6"]
        product['category_level_7'] = product_parameters["SubCategory7"]
        product['category_level_8'] = product_parameters["SubCategory8"]
        product['category_level_9'] = product_parameters["SubCategory9"]

        product['condition'] = (product_parameters["Condition"]["Condition"])
        product['additional_policies'] = 'NA'
        product['description'] = (product_parameters["Description"]["Description"])
        product['highlights'] = 'Not_Applicable'
        product['rating_details'] = "Not_Applicable"  # new
        product['specifications'] = (product_parameters["Specifications"])
        product['seller_overall_rating'] = 'Not_Applicable'
        product['seller_description'] = 'Not_Applicable'
        product['return_policies'] = (product_parameters["Return_Policies"]["Policies"])
        product['warrenty'] = (product_parameters["Warranty"]["Warranty"])
        product['shipping_policies'] = 'Not_Applicable'
        product['from_manufracture'] = 'Not_Applicable'  # new
        product['promotion'] = 'Not_Applicable'  # new
        product['other_format_prices'] = 'Not_Applicable'  # new
        product['seller_detailed_information'] = 'Not_Applicable'  # new

        product['saved_price'] = "Not_Applicable"
        product['added_date'] = 'NA'
        product['availability'] = "NA"
        product['brand'] = "NA"
        product['discount_percentage'] = product_parameters["Discount"]
        product['product_selling_price'] = product_parameters["Price"]
        product['product_EAN'] = product_parameters["EAN"]
        product['product_id'] = product_parameters["Id"]
        product['image_url'] = product_parameters["ImageUrl"]
        product['likes'] = "Not Applicable"
        product['isbn'] = "Not Applicable"
        product['isbn-10'] = "Not Applicable"
        product['isbn-13'] = "Not Applicable"
        product['MPN'] = product_parameters["MPN"]
        product['name'] = product_parameters["Product_Name"]
        product['no_of_reviews'] = "NA"
        product['original_price'] = product_parameters["Original_Price"]
        product['rating'] = product_parameters['Rating']
        product['shipping_price'] = product_parameters["Shipping_Price"]
        product['size'] = product_parameters["Size"]
        product['upc'] = "Not_Applicable"
        product['url'] = product_parameters["URL"]
        product['quantity_available'] = product_parameters["Quantity"]
        product['products_slod'] = "Not_Applicable"
        product['seller_code'] = "Not_Applicable"
        product['seller_location'] = "Not_Applicable"
        product['seller_name'] = product_parameters["Seller_Name"]
        product['seller_negative_rating'] = "Not_Applicable"
        product['seller_neutral_rating'] = "Not_Applicable"
        product['seller_positive_rating'] = "Not_Applicable"
        product['seller_rank'] = "Not_Applicable"
        product['seller_store_link'] = "Not_Applicable"
        product['seller_year_of_joining'] = "Not_Applicable"
        product['shipping_available_countries'] = "Not_Applicable"
        product['shipping_location'] = "Not_Applicable"
        product['shipping_logistic_name'] = "Not_Applicable"
        product['shipping_price'] = product_parameters["Shipping_Price"]
        product['shop_location'] = "Not_Applicable"
        product['shop_name'] = "Not_Applicable"
        product['no_of_sales'] = "Not_Applicable"
        product['shop_rating'] = "Not_Applicable"
        product['Tax_info'] = "Not_Applicable"
        product['Visibility'] = "Not_Applicable"
        product['currency'] = product_parameters["Currency"]
        product['color_variants'] = "Not_Applicable"  # new
        product['style_variants'] = "Not_Applicable"  # new
        product['author_name'] = "Not_Applicable"  # new

        return product

    def get_details(self, raw_data, hierarchy, url):
        # Notes thread start time

        line = hierarchy.split("|")
        # print line

        page_soup = raw_data

        # Stores all the default values of the product's details
        product_parameters = {
            "SKU": "NA",  # ss
            "UPC": "Not Applicable",  # ss
            "Rating": "NA",  # ss
            "Shipping_Policies": {'Policies': "Not Applicable"},  # ss
            "Marketplace": "NA",  # ss
            "Description": {'Description': "NA", },  # ss
            "Seller_Name": "NA",  # ss
            "Domain": "NA",  # ss
            "Date": "NA",  # ss
            "Time": "NA",  # ss
            "SubCategory1": "NA",  # ss
            "SubCategory2": "NA",  # ss
            "SubCategory3": "NA",  # ss
            "SubCategory4": "NA",  # ss
            "SubCategory5": "NA",  # ss
            "SubCategory6": "NA",  # ss
            "SubCategory7": "NA",  # ss
            "SubCategory8": "NA",  # ss
            "SubCategory9": "NA",  # ss
            "URL": "NA",  # ss
            "Category": "NA",  # ss
            "Sold": "Not Applicable",  # ss
            "Return_Policies": {'Policies': "Not Applicable"},  # ss
            "Seller_Code": "Not Applicable",  # ss
            "Seller_Location": "Not Applicable",  # ss
            "Seller_Negative_Rating": "Not Applicable",  # ss
            "Seller_Neutral_Rating": "Not Applicable",  # ss
            "Seller_Overall_Rating": "Not Applicable",  # ss
            "Seller_Positive_Rating": "Not Applicable",  # ss
            "Seller_Rank": "Not Applicable",  # ss
            "Seller_Year_Joining": "Not Applicable",  # ss
            "Available_Countries": "Not Applicable",  # ss
            "Shipping_Location": "Not Applicable",  # ss
            "Logistic_Name": "Not Applicable",  # ss
            "Shop_Location": "Not Applicable",  # ss
            "Shop_Name": "Not Applicable",  # ss
            "Shop_Sales": "Not Applicable",  # ss
            "Shop_Rating": "Not Applicable",  # ss
            "Tax_Info": "Not Applicable",  # ss
            "Visibility": "Not Applicable",  # ss
            "ImageUrl": "NA",  # ss
            "ISBN": "Not Applicable",  # ss
            "Brand": "NA",  # ss
            "Price": "NA",  # ss
            "Availability": "NA",  # ss
            "Currency": "MXN",  # ss
            "Seller_Rating": "NA",  # ss
            "EAN": "NA",  # ss
            "Highlights": {'Highlights': "Not Applicable"},  # ss
            "Id": "Not Applicable",  # ss
            "Product_Name": "NA",  # ss
            "Likes": "Not Applicable",  # ss
            "MPN": "Not Applicable",  # ss
            "Reviews": "NA",  # ss
            "Shipping_Price": "NA",  # ss
            "Saved_Price": "Not Applicable",  # ss
            "Added_Date": "NA",  # ss
            "Additional_Policies": {'Policies': "NA"},  # ss
            "Quantity": "NA",  # ss
            "Condition": {"Condition": "NA"},  # ss
            "Discount": "NA",  # SS
            "Warranty": {'Warranty': "NA"},  # ss
            "Original_Price": "NA",  # ss
            "Size": "NA",  # ss
            "Specifications": {"Variants": "NA", "Weight": "NA", "Color": "NA", "Othery_Sellers": "NA", }  # ss
        }

        # Finds product name
        try:
            prod_name = page_soup.find_all('div', {'class': 'item_listing_title_and_price'})[0].find('h2').text.replace(
                ' ', '_').strip().encode('utf8', 'ignore')
            # print prod_name
        except Exception as e:
            # print_exception('product name not found','Bonanza',hierarchy,url,e)
            # print(url)
            # print 'Error: with product name.'
            self.message = self.message + "product name"
            prod_name = "NA"

        # Finds original product price
        try:
            product_original_price = page_soup.find('span', {'class': 'nondiscount_price'}).text.replace('$',
                                                                                                         '').replace(
                ',', '')
            product_parameters["Original_Price"] = product_original_price
            # print product_original_price
        except Exception as e:
            # print_exception('product original_price not found','Bonanza',hierarchy,url,e)
            # print(url)
            self.message = self.message + "product original_price"
            product_parameters["Original_Price"] = "NA"

        # Finds product selling price
        try:
            prod_price = page_soup.find_all('div', {'class': 'item_price'})[0].text.strip().replace('$', '').replace(
                ',', '').encode('utf8', 'ignore')
            # print prod_price
        except Exception as e:
            # print_exception('product selling_price not found','Bonanza',hierarchy,url,e)
            # print(url)
            self.message = self.message + "product selling_price"
            prod_price = "NA"

        # Finds product's shop name
        try:
            shop_name = page_soup.find_all('div', {'class': 'booth_link'})[0].find('a').text.replace("'s booth",
                                                                                                     '').replace(' ',
                                                                                                                 '_').strip().encode(
                'utf8', 'ignore')  # print shop_name
        except Exception as e:
            # print_exception('product shop_name not found','Bonanza',hierarchy,url,e)
            # print(url)
            self.message = self.message + "shop_name"
            shop_name = "NA"

        try:
            shop_rating = page_soup.find_all('div', {'class': 'feedback_rating'})[0].find('a').text.replace('%  rating',
                                                                                                            '').encode(
                'utf8', 'ignore')
            # print shop_rating
        except Exception as e:
            # print_exception('product shop_rating not found','Bonanza',hierarchy,url,e)
            # print(url)
            self.message = self.message + "shop_rating"
            shop_rating = "NA"

        # Finds product's description
        try:
            description_url = page_soup.find_all('div', {'class': 'plain_text_description'})[0].get('data-url')
            response_obj = response_getter.Response()
            descr_page = response_obj.get_page_soup(DataCollectors_Configuration.DOMAIN_NAME + description_url)

            description = descr_page.find('body').text.encode('utf8', 'ignore')
            # print description
        except Exception as e:
            # print_exception('product description not found','Bonanza',hierarchy,url,e)
            # print(url)
            self.message = self.message + "product description"
            description = "NA"

        # Finds Return Policies
        try:
            return_policy = page_soup.find_all('div', {'class': 'item_listing_additional_details_section'})[
                1].text.strip()
            return_policy = return_policy.replace('Return policy', '', ).strip().encode('utf8', 'ignore')
            # print return_policy
        except Exception as e:
            # print_exception('product return_policy not found','Bonanza',hierarchy,url,e)
            # print(url)
            self.message = self.message + " product return_policy"
            return_policy = "NA"

        # Finds shipping policies
        try:
            shipping_policy = page_soup.find_all('div', {'class': 'item_listing_additional_details_section'})[
                0].text.strip()
            shipping_policy = shipping_policy.replace('Shipping options', '').strip().encode('utf8', 'ignore')
            shipping_policy = re.sub('[^a-zA-Z0-9 .]', '', shipping_policy)
            # print shipping_policy
        except Exception as e:
            # print_exception('product shipping_polices not found','Bonanza',hierarchy,url,e)
            # print(url)
            self.message = self.message + " product shipping_policies"
            shipping_policy = "NA"

        # Collects image URL
        try:
            image_url = page_soup.find_all('img', {'itemprop': 'image'})[0].get('src')
            # print image_url
        except Exception as e:
            # print_exception('product image_url not found','Bonanza',hierarchy,url,e)
            # print(url)
            self.message = self.message + "product image_url"
            image_url = "NA"

        product_parameters["ImageUrl"] = image_url
        product_parameters["URL"] = url
        product_parameters["Currency"] = DataCollectors_Configuration.CURRENCY
        product_parameters["Product_Name"] = prod_name
        product_parameters["Price"] = prod_price
        product_parameters["Shop_Name"] = shop_name
        product_parameters["Shop_Rating"] = shop_rating
        product_parameters["Description"]["Description"] = description
        product_parameters['Date'] = datetime.datetime.now().strftime("%d-%m-%y")
        product_parameters['Time'] = datetime.datetime.now().strftime("%H:%M:%S")
        product_parameters["Marketplace"] = DataCollectors_Configuration.PROJECT_NAME
        product_parameters["Domain"] = DataCollectors_Configuration.DOMAIN_NAME

        product_parameters["Return_Policies"]["Policies"] = return_policy
        product_parameters["Shipping_Policies"]["Policies"] = shipping_policy

        sub_category_number = 1

        # Assigns sub-category values to product details
        try:
            product_parameters["Category"] = line[0]
            for sub_category in line[1:]:
                product_parameters['SubCategory{}'.format(sub_category_number)] = sub_category
                sub_category_number += 1
                # print sub_category
        except Exception as e:
            # print_exception('product sub_category values not found','Bonanza',hierarchy,url,e)
            self.message = self.message + "sub_category values"
            pass

        # Reads all the traits from the table
        try:
            traits_table = page_soup.find_all('table', {'class': 'extended_info_table'})[0].find_all('td')
            no_of_rows = len(traits_table)
            for row in range(0, no_of_rows, 2):
                key = traits_table[row].text.strip().replace(':', '').encode('utf8', 'ignore')
                value = traits_table[row + 1].text.replace('View details', '').replace('\n', '').strip().encode('utf8',
                                                                                                                'ignore')
                if 'Quantity' in key:
                    product_parameters["Quantity"] = value
                elif 'Condition' in key:
                    product_parameters["Condition"]["Condition"] = value
                elif 'Rating'.lower() in key.lower():
                    product_parameters["Specifications"]["Rating"] = value
                elif 'Size' in key:
                    product_parameters["Size"] = value
                elif 'UPC' in key:
                    product_parameters["UPC"] = value
                elif 'SKU' in key:
                    product_parameters["SKU"] = value
                elif 'warranty' in key.lower():
                    product_parameters["Warranty"]["Warranty"] = value
                elif 'EAN' in key:
                    product_parameters["EAN"] = value
                elif 'Brand' in key:
                    product_parameters["Brand"] = value
                elif 'MPN' in key:
                    product_parameters["MPN"] = value
                elif 'Reviews' in key:
                    continue
                elif 'Category' in key:
                    continue
                else:
                    product_parameters["Specifications"][key] = value
                    if DataCollectors_Configuration.DEBUG == DataCollectors_Configuration.ON:
                        print 'Traits-table- ', key + ' ' + value
        except Exception as e:
            # print_exception('traits_table not found','Bonanza',hierarchy,url,e)
            # print(url)
            self.message = self.message + "traits_table"
            pass
            # Reads all the listing details from the table
        try:
            listing_table = page_soup.find_all('table', {'class': 'extended_info_table'})[1].find_all('td')
            no_of_rows = len(listing_table)
            for row in range(0, no_of_rows, 2):
                key = listing_table[row].text.strip().encode('utf8', 'ignore')
                value = listing_table[row + 1].text.strip().encode('utf8', 'ignore')
                if 'Posted for sale' in key:
                    product_parameters["Added_Date"] = value
                elif 'Item number' in key:
                    product_parameters["Id"] = value
                elif 'Shipping discount' in key:
                    product_parameters["Shipping_Price"] = value
                elif 'Price discount' in key:
                    product_parameters["Discount"] = value
                elif 'Seller policies' in key:
                    product_parameters["Seller_Name"] = listing_table[row + 1].find('a').get('href').split('/')[-1]
                else:
                    print 'Listing-table- ', key, value
        except Exception as e:
            # print_exception('listing_table not found','Bonanza',hierarchy,url,e)
            # print(urclass Scrapper:l)
            self.message = self.message + "listing_table"
            pass

        product_parameters['Date'] = datetime.datetime.now().strftime("%d-%m-%y")
        product_parameters['Time'] = datetime.datetime.now().strftime("%H:%M:%S")
        productdetails_obj = ProductDetails()
        print_exception(self.message,"Bonanza",hierarchy,url,"NA")
        return productdetails_obj.get_data(product_parameters)
