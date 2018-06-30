import json
import uuid
from google.cloud import bigquery
import Storage_config
import Souq_DataCollectors_configuration

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


class persist_BigQuery:
    def __init__(self, data):
        # print(data['product_EAN'])
        # print(data['seller_name'])
        # print(data['url'])
        product = self.get_data_dicitonary(data)
        # data_tuple is tuple which contains a columns values which are present in cassandra DB
        data_tuple = (str(product['id']), product['date'], 'UAE', product['marketplace'], product['category'],
                      product['category_level_1'], product['category_level_2'], product['category_level_3'],
                      data['seller_name'], product['asin'], product['product_id'], product['currency'],
                      product['price'], str(product['additional_info']), data['name'], 'NA', 'NA', data['product_EAN'])

        bigquery_client = bigquery.Client.from_service_account_json(Storage_config.key_path)
        self.schema = [bigquery.SchemaField('id', 'STRING'), bigquery.SchemaField('date', 'DATE'),
                       bigquery.SchemaField('country', 'STRING'), bigquery.SchemaField('marketplace', 'STRING'),
                       bigquery.SchemaField('category', 'STRING'), bigquery.SchemaField('category_level_1', 'STRING'),
                       bigquery.SchemaField('category_level_2', 'STRING'),
                       bigquery.SchemaField('category_level_3', 'STRING'), bigquery.SchemaField('seller', 'STRING'),
                       bigquery.SchemaField('asin', 'STRING'), bigquery.SchemaField('product_id', 'STRING'),
                       bigquery.SchemaField('currency', 'STRING'), bigquery.SchemaField('price', 'FLOAT'),
                       bigquery.SchemaField('additional_info', 'STRING'),
                       bigquery.SchemaField('product_name', 'STRING'), bigquery.SchemaField('seller_score', 'STRING'),
                       bigquery.SchemaField('bsr', 'STRING'), bigquery.SchemaField('ean', 'STRING')]

        """Insert / fetch table data."""
        # print(data_tuple)
        dataset_id = Storage_config.dataset_id
        table_id = Storage_config.table_id
        dataset_ref = bigquery_client.dataset(dataset_id)
        table_ref = dataset_ref.table(table_id)
        table = bigquery_client.get_table(table_ref)
        # [START table_insert_rows]
        rows_to_insert = [data_tuple]
        errors = bigquery_client.insert_rows(table, rows_to_insert)
        if errors:
            print errors
        else:
            # print '***********************'
            print errors
            # print '***********************'


    def find_average_price(self,input_val):
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


    def get_data_dicitonary(self,product_dic):
        product = dict()
        product['id'] = str(uuid.uuid1()).encode('utf-8')
        product['asin'] = product_dic['asin']
        product['category'] = product_dic['category']
        product['category_level_1'] = product_dic['category_level_1']
        product['category_level_2'] = product_dic['category_level_2']
        product['category_level_3'] = product_dic['category_level_3']
        product['currency'] = product_dic['currency']
        product['date'] = product_dic['date']
        product['marketplace'] = product_dic['marketplace']
        product['price'] = str(self.find_average_price(product_dic['product_selling_price'])).encode('utf-8')
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