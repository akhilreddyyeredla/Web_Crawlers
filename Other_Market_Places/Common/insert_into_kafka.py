import json
import uuid
from kafka_producer import python_kafka_producer_performance
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# from DataCollectors_Configuration import Cassandra_HOST, Cassandra_DB_name, Cassandra_PASSWORD,Cassandra_USER_NAME


country = {
    'AMAZON_AUS': 'Australia',
    'AMAZON_CANADA': 'Cannada',
    'AMAZON_FR': 'France',
    'AMAZON_GR': 'Germany',
    'AMAZON_IT': 'Italy',
    'AMAZON_ES': 'Spain',
    'AMAZON_UK': 'United Kingdom',
    'AMAZON_US': 'USA',
    'AMAZON_MEX': 'Mexico',
    'Bonanza_US': 'USA',
    'EBAY_US': 'USA',
    'Etsy': 'USA',
    'Linio_Mexico': 'Mexico',
    'Souq_UAE': 'UAE'
}


def find_average_price(input_val):
    if '-' in input_val:
        values = input_val.split('-')
        if len(values) != 0:
            avg = 0.0
            for value in values:
                avg = avg + float(value)
            avg = avg / (2 * 1.0)
            return float(avg)
    if 'not_available' == input_val:
        return float(0)

    else:
        return float(input_val)


def get_data_dicitonary(product_dic):
    product = dict()
    product['id'] = (uuid.uuid1())
    product['asin'] = product_dic['asin']
    product['category'] = product_dic['category']
    product['category_level_1'] = product_dic['category_level_1']
    product['category_level_2'] = product_dic['category_level_2']
    product['category_level_3'] = product_dic['category_level_3']
    product['currency'] = product_dic['currency']
    product['date'] = product_dic['date']
    product['marketplace'] = product_dic['marketplace']
    product['price'] = (find_average_price(product_dic['product_selling_price']))
    product['product_id'] = product_dic['product_id']
    product['seller'] = str(product_dic['seller_name'])
    product['additional_info'] = {}
    product['country'] = str(country.get(product['marketplace'])).encode('utf-8')
    product_keys = product.keys()
    product_dic_keys = product_dic.keys()

    for key in product_dic_keys:
        if key not in product_keys:
            product['additional_info'].update(((key, product_dic[key]),))

    # print '***************************************************************'
    # print json.dumps(product, sort_keys=True, indent=4)
    # print '***************************************************************'
    '''
    # data_tuple is tuple which contains a columns values which are present in cassandra DB
    data_tuple = {

                   'id':          product['id'],
                   'date':        product['date'],
                   'country':     country.get(product['marketplace']),
                   'marketplace':  product['marketplace'],
                    product['category'],
                    product['category_level_1'],
                    product['category_level_2'],
                    product['category_level_3'],
                    product['seller_name'],
                    product['asin'],
                    product['product_id'],
                    product['currency'],
                    product['price'],
                    additional_info

    }
    print '********************************Tuple***********************************'
    print json.dumps(data_tuple, sort_keys=True, indent=4)
    print '************************************************************************'
    return data_tuple
    '''
    return product


class persist_kafka:
    def __init__(self, data):
        kafka_dic = {}
        # print(data['product_EAN'])
        # print(data['seller_name'])
        # print(data['url'])
        data_dic = get_data_dicitonary(data)
        # data_tuple is tuple which contains a columns values which are present in cassandra DB
        additional_info = json.dumps(data_dic['additional_info'], sort_keys=True, indent=4)
        data_tuple = (data_dic['id'], data_dic['asin'], data_dic['category'], data_dic['category_level_1'],
                      data_dic['category_level_2'], data_dic['category_level_3'], data_dic['currency'], data['date'],
                      data_dic['marketplace'], data_dic['price'], data_dic['product_id'], additional_info,
                      data['seller_name'], "NA", "NA", data['url'], data['product_EAN'], "UAE", data['name'])
        """Insert / fetch table data."""
        kafka_dic['id'] = data_dic['id']
        kafka_dic['asin'] = data_dic['asin']
        kafka_dic['category'] = data_dic['category']
        kafka_dic['category_level_1'] = data_dic['category_level_1']
        kafka_dic['category_level_2'] = data_dic['category_level_2']
        kafka_dic['category_level_3'] = data_dic['category_level_3']
        kafka_dic['currency'] = data_dic['currency']
        kafka_dic['date'] = data['date']
        kafka_dic['marketplace'] = data_dic['marketplace']
        kafka_dic['price'] = data_dic['price']
        kafka_dic['product_id'] = data_dic['product_id']
        kafka_dic['additional_info'] = additional_info
        kafka_dic['seller_name'] = data['seller_name']
        kafka_dic['bsr'] = "NA"
        kafka_dic['seller_score'] = "NA"
        kafka_dic['url'] = data['url']
        kafka_dic['product_EAN'] = data['product_EAN']
        kafka_dic['country'] = "UAE"
        kafka_dic['name'] = data['name']
        tuple_data = (
        kafka_dic['id'], kafka_dic['additional_info'].replace(',', ''), kafka_dic['asin'], kafka_dic['bsr'],
        kafka_dic['category'], kafka_dic['category_level_1'], kafka_dic['category_level_2'],
        kafka_dic['category_level_3'], kafka_dic['country'], kafka_dic['currency'], kafka_dic['date'],
        kafka_dic['product_EAN'], kafka_dic['marketplace'], kafka_dic['price'], kafka_dic['product_id'],
        kafka_dic['name'], kafka_dic['url'], kafka_dic['seller_name'], kafka_dic['seller_score'])
        python_kafka_producer_performance(str(data_tuple))
    # insert(data_tuple)
    # print data_tuple


def connect_to_db():
    auth_provider = PlainTextAuthProvider(
        username=Cassandra_USER_NAME, password=Cassandra_PASSWORD)

    cluster = Cluster([Cassandra_HOST], auth_provider=auth_provider)
    session = cluster.connect('eu_cbec_bi_data')
    return session


def insert(values):
    # values = get_data_for_cassandra(product_info)
    session = connect_to_db()
    statement = "INSERT INTO eu_cbec_bi_data.marketplaces (" \
                "   id,               asin,             category , " \
                "   category_level_1, category_level_2, category_level_3, " \
                "   currency,         date,             marketplace,      " \
                "   price,            product_id,       additional_info," \
                "   seller,bsr,seller_score,product_url,ean,country,product_name) " \
                "   values(" \
                "           %s,   %s,     %s," \
                "           %s,   %s,     %s," \
                "           %s,   %s,     %s," \
                "           %s,   %s,     %s, " \
                "           %s,%s,%s,%s,%s,%s,%s" \
                ")"
    session.execute(statement, values)
