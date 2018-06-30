import datetime
import json
import re
import DataCollectors_Configuration
import CONSTANTS
import time



store_to_flag = DataCollectors_Configuration.WRITE_TO

product_parameters = {}

product_data = {}

path = DataCollectors_Configuration.ROOT_FOLDER


# Gathers all the product details of the given product URL

def get_data(product_parameters,product_link,hirearchy,dir):
    product = dict()

    # product is a dictionary and used superset field names as keys and get values by your own
    # parsing methods and assign them key values

    product['sku'] = product_parameters['SKU']
    product['asin'] = "not_available"  # new
    product['date'] = product_parameters['Date']
    product['time'] = product_parameters['Time']
    product['marketplace'] = CONSTANTS.MARKETPLACE
    product['domain'] = product_parameters["Domain"]
    product['category'] = CONSTANTS.BELLEZA
    product['category_level_1'] = product_parameters["SubCategory1"]
    product['category_level_2'] = product_parameters["SubCategory2"]
    product['category_level_3'] = product_parameters["SubCategory3"]
    product['category_level_4'] = product_parameters["SubCategory4"]
    product['category_level_5'] = product_parameters["SubCategory5"]
    product['category_level_6'] = product_parameters["SubCategory6"]
    product['category_level_7'] = product_parameters["SubCategory7"]
    product['category_level_8'] = product_parameters["SubCategory8"]
    product['category_level_9'] = product_parameters["SubCategory9"]

    if DataCollectors_Configuration.WRITE_TO == CONSTANTS.WRITE_TO_CASSANDRA:
        product['condition'] = (product_parameters["Condition"]["Condition"])
        product['additional_policies'] = 'NA'
        product['description'] = (product_parameters["Description"])
        product['highlights'] = 'NA'
        product['rating_details'] = "NA"  # new
        product['specifications'] = (product_parameters["Specifications"])
        product['seller_overall_rating'] = product_parameters["Seller_Overall_Rating"]
        product['seller_description'] = 'NA'
        product['return_policies'] = product_parameters['Return_Policies']
        product['warrenty'] = 'NA'
        product['shipping_policies'] = 'NA'
        product['from_manufracture'] = 'NA'  # new
        product['promotion'] = 'NA'  # new
        product['other_format_prices'] = 'NA'  # new
        product['seller_detailed_information'] = 'NA'  # new
    else:
        product['condition'] = json.dumps(product_parameters["Condition"]["Condition"])
        product['additional_policies'] = json.dumps({'Additional_policies': 'NA'})
        product['description'] = json.dumps(product_parameters["Description"])
        product['highlights'] = json.dumps({'Additional_policies': 'NA'})
        product['rating_details'] = json.dumps({'Additional_policies': 'NA'})  # new
        product['specifications'] = json.dumps(product_parameters["Specifications"])
        product['seller_overall_rating'] = json.dumps(product_parameters["Seller_Overall_Rating"])
        product['seller_description'] = json.dumps({'seller_desccription': 'NA'})
        product['return_policies'] = json.dumps(product_parameters["Return_Policies"])
        product['warrenty'] = json.dumps({'warrenty': 'NA'})
        product['shipping_policies'] = json.dumps({'shipping_policies': 'NA'})
        product['from_manufracture'] = json.dumps({'Additional_policies': 'NA'})  # new
        product['promotion'] = json.dumps({'Additional_policies': 'NA'})  # new
        product['other_format_prices'] = json.dumps({'Additional_policies': 'NA'})  # new
        product['seller_detailed_information'] = json.dumps({'Additional_policies': 'NA'})  # new

    product['saved_price'] = "NA"
    product['added_date'] = 'NA'
    product['availability'] = product_parameters['Availability']
    product['brand'] = product_parameters['Brand']
    product['discount_percentage'] = product_parameters["Discount"]
    product['product_selling_price'] = product_parameters["Price"]
    product['product_EAN'] = "NA"
    product['product_id'] = "NA"
    product['image_url'] = product_parameters["ImageUrl"]
    product['likes'] = "NA"
    product['isbn'] = "NA"
    product['isbn-10'] = "NA"
    product['isbn-13'] = "NA"
    product['MPN'] = "NA"
    product['name'] = product_parameters["Product_Name"]
    product['no_of_reviews'] = "NA"
    product['original_price'] = product_parameters["Original_Price"]
    product['rating'] = product_parameters['Rating']
    product['shipping_price'] = product_parameters["Shipping_Price"]
    product['size'] = "not_available"
    product['upc'] = "NA"
    product['url'] = product_link
    product['quantity_available'] = "NA"
    product['products_slod'] = "NA"
    product['seller_code'] = "NA"
    product['seller_location'] = "NA"
    product['seller_name'] = product_parameters["Seller_Name"]
    product['seller_negative_rating'] = "NA"
    product['seller_neutral_rating'] = "NA"
    product['seller_positive_rating'] = "NA"
    product['seller_rank'] = "NA"
    product['seller_store_link'] = "NA"
    product['seller_year_of_joining'] = "NA"
    product['shipping_available_countries'] = "NA"
    product['shipping_location'] = "NA"
    product['shipping_logistic_name'] = "NA"
    product['shipping_price'] = product_parameters["Shipping_Price"]
    product['shop_location'] = "NA"
    product['shop_name'] = "NA"
    product['no_of_sales'] = "NA"
    product['shop_rating'] = "NA"
    product['Tax_info'] = "NA"
    product['Visibility'] = "NA"
    product['currency'] = CONSTANTS.CURRENCY
    product['color_variants'] = "NA"  # new
    product['style_variants'] = "NA"  # new
    product['author_name'] = "NA"  # new

    # return storage(DataCollectors_Configuration.LINIO_PROJECT_not_availableME, datetime.datetime.now().strftime("%d-%m-%y")
    #                , hirearchy, time.time(), product,product['sku'],dir)

    return product

def get_details(prod_url_info, raw_data):
    # Notes thread start time
    thread_start_time = datetime.datetime.now().strftime("%d-%m-%y  %H:%M:%S")
    start_time = time.time()
    hirerachy = prod_url_info.split("|")[-2]
    line = prod_url_info.split('|')

    dirs = ''
    try:
        if DataCollectors_Configuration.DEBUG == CONSTANTS.ON:
            print 'directories: ', line[2:-1]
        for category in line[2:-1]:
            dirs += category + '+'

    except:
        dirs = CONSTANTS.BELLEZA

    product_link = line[-1]

    # Stores all the default values of the product's details
    product_parameters = {
        "SKU": "not_available",  # ss
        "UPC": "NA",  # ss
        "Rating": "not_available",  # ss
        "Shipping_Policies": {'Policies': "NA"},  # ss
        "Marketplace": CONSTANTS.MARKETPLACE,  # ss
        "Description": {'Description': "not_available", },  # ss
        "Seller_Name": "not_available",  # ss
        "Domain": CONSTANTS.MAIN_URL,  # ss
        "Date": "not_available",  # ss
        "Time": "not_available",  # ss
        "SubCategory1": "not_available",  # ss
        "SubCategory2": "not_available",  # ss
        "SubCategory3": "not_available",  # ss
        "SubCategory4": "not_available",  # ss
        "SubCategory5": "not_available",  # ss
        "SubCategory6": "not_available",  # ss
        "SubCategory7": "not_available",  # ss
        "SubCategory8": "not_available",  # ss
        "SubCategory9": "not_available",  # ss
        "URL": product_link,  # ss
        "Category": line[2],  # ss
        "Sold": "NA",  # ss
        "Return_Policies": {'Policies': "NA"},  # ss
        "Seller_Code": "NA",  # ss
        "Seller_Location": "NA",  # ss
        "Seller_Negative_Rating": "NA",  # ss
        "Seller_Neutral_Rating": "NA",  # ss
        "Seller_Overall_Rating": "NA",  # ss
        "Seller_Positive_Rating": "NA",  # ss
        "Seller_Rank": "NA",  # ss
        "Seller_Year_Joining": "NA",  # ss
        "Available_Countries": "NA",  # ss
        "Shipping_Location": "NA",  # ss
        "Logistic_Name": "NA",  # ss
        "Shop_Location": "NA",  # ss
        "Shop_Name": "NA",  # ss
        "Shop_Sales": "NA",  # ss
        "Shop_Rating": "NA",  # ss
        "Tax_Info": "NA",  # ss
        "Visibility": "NA",  # ss
        "ImageUrl": "not_available",  # ss
        "ISBN": "NA",  # ss
        "Brand": "not_available",  # ss
        "Price": "not_available",  # ss
        "Availability": "not_available",  # ss
        "Currency": CONSTANTS.CURRENCY,  # ss
        "Seller_Rating": "not_available",  # ss
        "EAN": "NA",  # ss
        "Highlights": {'Highlights': "NA"},  # ss
        "Id": "NA",  # ss
        "Product_Name": "not_available",  # ss
        "Likes": "NA",  # ss
        "MPN": "NA",  # ss
        "Reviews": "not_available",  # ss
        "Shipping_Price": "not_available",  # ss
        "Saved_Price": "NA",  # ss
        "Added_Date": "NA",  # ss
        "Additional_Policies": {'Policies': "NA"},  # ss
        "Quantity": "not_available",  # ss
        "Condition": {"Condition": "not_available"},  # ss
        "Discount": "not_available",  # SS
        "Warranty": {'Warranty': "not_available"},  # ss
        "Original_Price": "not_available",  # ss
        "Size": "not_available",  # ss
        "Specifications": {
            "Variants": "not_available",
            "Aroma": "not_available",
            "Model": "not_available",
            "Age": "not_available",
            "Guarantee": "not_available",
            "Battery_Type": "not_available",
            "Physical_Detail": "not_available",
            "Mattress_Firmness": "not_available",
            "Weight": "not_available",
            "Power": "not_available",
            "Screen_Size": "not_available",
            "Format": "not_available",
            "Megapixels": "not_available",
            "OS": "not_available",
            "Screen": "not_available",
            "RAM": "not_available",
            "Secondary_Camera": "not_available",
            "Processor": "not_available",
            "Processor_Speed": "not_available",
            "Capacity": "not_available",
            "Pieces_In_Set": "not_available",
            "Color": "not_available",
            "Type": "not_available",
            "Shape": "not_available",
            "Material": "not_available",
            "HDMI_Ports": "not_available",
            "Optical_Zoom": "not_available",
            "Dimensions": "not_available",
            "Other_Sellers": "not_available",
        }  # ss
    }

    # Getting the link of each result product
    product_source = raw_data

    # Getting name of the product
    try:
        temp_str = product_source.find_all("h1")[0].text
    except:
        temp_str = "not_available"

    temp_str = temp_str.strip()

    # Final product name after processing for the required format
    product_name = temp_str.replace('\n', '').encode('utf8', 'ignore')

    # Retrieving price of the product
    try:
        price_text = product_source.find_all("div", {'class': 'price price-main'})[0].text.strip()
        price = re.sub('[^0-9\-.]', '', price_text).replace(',', '')
    except:
        price = "not_available"

    # Retrieving brand of the product
    try:
        brand = product_source.find_all('a', {'itemprop': 'brand'})[0].text.strip().replace('\n', '').encode('utf8',
                                                                                                             'ignore')
    except:
        brand = "not_available"

    # Retrieving image_URL of the product
    try:
        image_url = 'https:' + product_source.find_all('div', {'class': 'swiper-wrapper'})[0].find_all('img')[0].get(
            'data-lazy')
    except:
        image_url = 'not_available'

    availability = ''

    # Finds availability of the product
    try:
        if product_source.find_all('button', {'class': 'btn btn-lg btn-disabled'})[0].text.replace('\n',
                                                                                                   '').strip() == 'Agotado':
            availability = 'Not Available'
        else:
            availability = 'Available'
    except:
        availability = 'Available'

    # Finds rating of the product
    try:
        rating = product_source.find_all('div', {'class': 'review-subtitle col-md-6 col-lg-12'})[0].find_all('h2')[
            0].text
        rating = re.findall(r'[\d+]', rating)
        if DataCollectors_Configuration.DEBUG == CONSTANTS.ON:
            print 'Rating: ', rating[0]
        rating = rating[0].encode('utf8', 'ignore')
    except:
        rating = "not_available"

    # Finds the seller name
    try:
        seller_name = \
            product_source.find_all('div', {'class': 'seller-information'})[0].find_all('a', {'class': 'link-lower'})[
                0].text.encode('utf8', 'ignore')
    except:
        seller_name = "not_available"

    # Finds the seller rating
    try:
        seller_rating = product_source.find_all('span', {'class': 'score'})[0].text.encode('utf8', 'ignore')
    except:
        seller_rating = "not_available"

    # Finds other sellers of the same product
    try:
        sellers = ''
        other_sellers = product_source.find_all('a', {'class': 'btn btn-primary-outline btn-sm col-xl-8 col-xs-12'})
        if other_sellers:
            for seller in other_sellers:
                sellers = sellers + seller.find_all('a')[0].text.encode('utf8') + '|' + seller.find(
                    'span').text + '|' + seller.find(
                    'div', {'class': 'price-secondary'}).text + '|'.encode('utf8', 'ignore')
    except:
        sellers = 'not_available'
    description = ''

    # Retrieves the description of the product
    try:
        desc = product_source.find_all("div", {'class': 'product-bg-container col-xs-12'})[0]
        bullets = desc.find_all('li')
        if bullets:
            for bullet_point in bullets:
                description = description + re.sub(r'[\s+]', ' ', format(bullet_point.text)) + '|'.encode('utf8',
                                                                                                          'ignore')
        else:
            description = description + desc.text.replace('\n', '').strip().encode('utf8', 'ignore')
    except:
        description = 'not_available'

    variants = ''

    # Finds the variants of the product
    try:
        options = product_source.find_all('label', {'class': 'btn btn-sm btn-default-outline'})
        if options:
            for option in options:
                variants = variants + format(option.text.replace('\n', '').strip()) + '|'.encode('utf8', 'ignore')
        else:
            variants = 'not_available'
    except:
        variants = 'not_available'

    # Finds the discount and original price of the product if any available
    try:
        discount = product_source.find_all('span', {'class': 'discount'})[0].text.replace('-', '').encode('utf8',
                                                                                                          'ignore')
        original_price = product_source.find_all('span', {'class': 'original-price'})[0].text.replace('$', '').replace(
            ',', '').encode('utf8', 'ignore')
        if not price:
            price = "not_available"
    except:
        discount = 'not_available'
        original_price = 'not_available'

    product_parameters['Discount'] = discount
    product_parameters['Original_Price'] = original_price
    product_parameters['Availability'] = availability
    product_parameters['Product_Name'] = product_name.strip().replace(' ', '_')
    product_parameters['Specifications']['Variants'] = variants
    product_parameters['Price'] = price
    product_parameters['Brand'] = brand
    product_parameters['Description'] = description
    product_parameters['Rating'] = rating
    product_parameters['ImageUrl'] = image_url
    product_parameters['Shipping_Price'] = "not_available"
    product_parameters['Seller_Name'] = seller_name
    product_parameters["Seller_Overall_Rating"] = seller_rating

    if not sellers:
        product_parameters['Other_Sellers'] = "not_available"
    else:
        product_parameters['Other_Sellers'] = sellers

    # Retrieving other specifications of the product
    try:
        table = product_source.find_all("table", {"class": "table"})

        num = len(table[0].find_all('td'))
        for i in range(0, num, 2):
            key = table[0].find_all('td')[i].text.encode('utf-8', 'ignore')
            value = table[0].find_all('td')[i + 1].text.replace(' ', '_').encode('utf-8', 'ignore')
            if key == 'SKU':
                product_parameters['SKU'] = value
            elif key == 'Modelo':
                product_parameters['Specifications']['Model'] = value
            elif 'a del producto' in key:
                product_parameters['Specifications']['Guarantee'] = value
            elif 'Detalle' in key:
                product_parameters['Specifications']['Physical_Detail'] = value
            elif 'n del producto' in key:
                product_parameters['Condition']['Condition'] = value
            elif key == 'Aroma':
                product_parameters['Specifications']['Aroma'] = value
            elif key == 'Contenido':
                product_parameters['Specifications']['Content'] = value
            elif 'Peso' in key:
                product_parameters['Specifications']['Weight'] = value
            elif 'de producto en meses' in key:
                product_parameters['Warranty']['Warranty'] = value
            elif 'Formato' == key:
                product_parameters['Format'] = value
            elif '(L x P x A cm)' in key:
                product_parameters['Specifications']['Dimensions'] = value
            elif 'Color' == key:
                product_parameters['Specifications']['Color'] = value
            elif 'Caracter' in key:
                product_parameters['Specifications']['Characteristics'] = value
            elif 'Barril' in key:
                product_parameters['Specifications']['Barrel'] = value
            elif 'Tipo de cutis' in key:
                product_parameters['Specifications']['Skin_Type'] = value
            elif 'Placas' in key:
                product_parameters['Specifications']['Plates'] = value
            elif 'Tipo de cabello' in key:
                product_parameters['Specifications']['Hair_Type'] = value
            elif 'Cabezales' == key:
                product_parameters['Specifications']['Cabezales'] = value
            elif 'tica de devoluci' in key:
                product_parameters['Return_Policies'] = value
            elif 'Resistente al agua' in key:
                product_parameters['Specifications']['Waterproof'] = value
            elif 'Potencia' == key:
                product_parameters['Specifications']['Power'] = value
            elif 'Tecnolog' in key:
                product_parameters['Specifications']['Technology'] = value
            else:
                product_parameters["Specifications"][key] = value

    except:
        table = "not_available"

    sub_category_number = 1

    # Assigns sub-category values to product details
    try:
        if DataCollectors_Configuration.DEBUG == CONSTANTS.ON:
            print "Sub Categories: ", line[3:-1]
        for sub_category in line[3:-1]:
            product_parameters['SubCategory{}'.format(sub_category_number)] = sub_category
            sub_category_number += 1
    except:
        pass

    # Date and time at the instance of collecting product details
    product_parameters['Date'] = datetime.datetime.now().strftime("%d-%m-%y")
    product_parameters['Time'] = datetime.datetime.now().strftime("%H:%M:%S")



    # thread_end_time = datetime.datetime.now().strftime("%d-%m-%y  %H:%M:%S")
    # end_time = time.time()
    # Prints product URL information, thread start time, end time and toal time taken for completion
    # the first number is serial
    # print prod_url_info + ' | ' + thread_start_time + ' | ' + thread_end_time + '|', int(end_time - start_time), '\bs'

    return get_data(product_parameters,product_link,hirerachy,dirs) , product_parameters['Date'], product_parameters['Time']