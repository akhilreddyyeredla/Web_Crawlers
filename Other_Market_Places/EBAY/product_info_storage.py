from Common.Ebay_common_imports import *
ROOT_FOLDER = DataCollectors_Configuration.ROOT_FOLDER

def find_average_price(input_val):
    if '-' in input_val:
        values = input_val.split('-')
        if len(values) !=0:
            avg = 0
            for value in values:
                avg = avg+float(value)
            avg = avg/2
            return avg
    if 'not_available' == input_val:
        return float(0)

    else:
        return float(input_val)

def get_data_for_cassandra(product_dic):
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
    product['price']            = find_average_price(product_dic['product_selling_price'])
    product['product_id']       = product_dic['product_id']
    product['seller_name']      = product_dic['seller_name']
    product['additional_info']  = {}

    product_keys = product.keys()
    product_dic_keys = product_dic.keys()

    for key in product_dic_keys:
        if key not in product_keys:
            product['additional_info'].update(((key, product_dic[key]),))

    return product

def storage(full_name,market_channel,date,time,category,item_number,product):
    data = (
        product['date'], product['time'], product['marketplace'], product['domain'],
        product['category'], product['category_level_1'], product['category_level_2'], product['category_level_3'],
        product['category_level_4'], product['category_level_5'], product['category_level_6'],
        product['category_level_7'],
        product['category_level_8'], product['category_level_9'], product['condition'], product['saved_price'],
        product['added_date'], product['additional_policies'], product['availability'], product['brand'],
        product['description'], product['discount_percentage'], product['product_selling_price'],
        product['product_EAN'], product['highlights'], product['product_id'], product['image_url'],
        product['likes'], product['isbn'], product['isbn-10'], product['isbn-13'],
        product['MPN'], product['name'], product['no_of_reviews'], product['original_price'],
        product['rating'], product['rating_details'], product['shipping_policies'], product['size'],
        product['sku'], product['upc'], product['url'], product['quantity_available'],
        product['products_slod'], product['return_policies'], product['seller_code'], product['seller_location'],
        product['seller_name'], product['seller_negative_rating'], product['seller_neutral_rating'],
        product['seller_positive_rating'],
        product['seller_overall_rating'], product['seller_rank'], product['seller_store_link'],
        product['seller_year_of_joining'],
        product['shipping_available_countries'], product['shipping_location'], product['shipping_logistic_name'],
        product['shipping_price'],
        product['shop_location'], product['shop_name'], product['no_of_sales'], product['shop_rating'],
        product['Tax_info'], product['Visibility'], product['warrenty'], product['currency'],
        product['specifications'], product['shipping_price'], product['from_manufracture'],
        product['color_variants'],
        product['style_variants'], product['promotion'], product['author_name'], product['other_format_prices'],
        product['seller_description'], product['asin'], product['seller_detailed_information']
    )

    if DataCollectors_Configuration.WRITE_TO == constant.WRITE_TO_CASSANDRA:
        data_dic = get_data_for_cassandra(product)
        additional_info = json.dumps(data_dic['additional_info'], sort_keys=True, indent=4)

        # data_tuple is tuple which contains a columns values which are present in cassandra DB
        data_tuple = (

            data_dic['id'], data_dic['asin'], data_dic['category'], data_dic['category_level_1'],
            data_dic['category_level_2'], data_dic['category_level_3'], data_dic['currency'], product['date'],
            data_dic['marketplace'], data_dic['price'], data_dic['product_id'], additional_info,
            product['seller_name']

        )
        print("IN")
        insert_into_cassandra.insert(data_tuple)
    elif DataCollectors_Configuration.WRITE_TO == constant.WRITE_TO_MYSQL:
         database.to_db(data)
    elif DataCollectors_Configuration.WRITE_TO == constant.WRITE_TO_FILE:
        highercy = full_name.replace("|", "/")
        directory_path = "{}/{}/{}".format(ROOT_FOLDER, 'EBAY', highercy)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            file_name = '{}.txt'.format(item_number)
            file_path = '{}/{}/{}/{}'.format(ROOT_FOLDER, 'EBAY', highercy, file_name)
            with open(file_path, 'a') as file1:
                file1.write(str(data))
    elif DataCollectors_Configuration.WRITE_TO == constant.WRITE_TO_BIG_QUERY:
        data_dic = get_data_for_cassandra(product)
        data_dic [ 'country' ] = 'US';

        # data_tuple is tuple which contains a columns values which are present in cassandra DB
        data_tuple = (

            str(data_dic['id']), product['date'], data_dic['country'], data_dic [ 'marketplace' ], 
            data_dic [ 'category' ], data_dic['category_level_1'], data_dic['category_level_2'], 
            data_dic['category_level_3'], product [ 'seller_name' ], data_dic['asin'], data_dic [ 'product_id' ], 
            data_dic['currency'], data_dic['price'], str(data_dic['additional_info']), product['name'],'NA','NA'
        )
        print("IN")
        bigquery_insert.test_table_insert_rows(data_tuple)
