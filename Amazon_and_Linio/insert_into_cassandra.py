import json
import uuid

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from DataCollectors_Configuration import Cassandra_HOST, Cassandra_DB_name, Cassandra_PASSWORD,Cassandra_USER_NAME


def find_average_price(input_val):
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

    additional_info = json.dumps(product['additional_info'], sort_keys=True, indent=4)

    # data_tuple is tuple which contains a columns values which are present in cassandra DB
    data_tuple = (

        product['id'], product['asin'], product['category'], product['category_level_1'],
        product['category_level_2'], product['category_level_3'], product['currency'], product['date'],
        product['marketplace'], product['price'], product['product_id'], product['seller_name'],
        additional_info

    )
    return data_tuple


def connect_to_db():

    auth_provider = PlainTextAuthProvider(
        username=Cassandra_USER_NAME, password=Cassandra_PASSWORD)

    cluster = Cluster([Cassandra_HOST], auth_provider=auth_provider)
    session = cluster.connect(Cassandra_DB_name)
    return session


def insert(product_info):

    values = get_data_for_cassandra(product_info)
    session = connect_to_db()
    statement = "INSERT INTO market_place_data.website_data (" \
                "   id,               asin,             category , " \
                "   category_level_1, category_level_2, category_level_3, " \
                "   currency,         date,             marketplace,      " \
                "   price,            product_id,       additional_info," \
                "   seller) " \
                "   values(" \
                "           %s,   %s,     %s," \
                "           %s,   %s,     %s," \
                "           %s,   %s,     %s," \
                "           %s,   %s,     %s, " \
                "           %s" \
                ")"
    session.execute(statement, values)
