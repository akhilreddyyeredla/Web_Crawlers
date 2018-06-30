import json
import uuid
from google.cloud import bigquery
import DataCollectors_Configuration


country = {
    'AMAZON_AUS': 'Australia',
    'AMAZON_CANADA':'Cannada',
    'AMAZON_FR': 'France',
    'AMAZON_GR': 'Germany',
    'AMAZON_IT': 'Italy',
    'AMAZON_ES':'Spain',
    'AMAZON_UK': 'United Kingdom',
    'AMAZON_US': 'USA',
    'AMAZON_MEX':'Mexico',
    'Bonanza_US': 'USA',
    'EBAY_US': 'USA',
    'Etsy': 'USA',
    'Linio_Mexico':'Mexico',
    'Souq_UAE': 'UAE'
}


def find_average_price(input_val):
    if '-' in input_val:
        values = input_val.split('-')
        if len(values) != 0:
            avg = 0
            for value in values:
                avg = avg + float(value)
            avg = avg / 2
            return avg
    if 'not_available' == input_val:
        return float(0)

    else:
        return float(input_val)


def get_tuple(product_dic):
    product = dict()
    product['id'] = uuid.uuid1()
    product['asin'] = product_dic['asin']
    product['category'] = product_dic['category']
    product['category_level_1'] = product_dic['category_level_1']
    product['category_level_2'] = product_dic['category_level_2']
    product['category_level_3'] = product_dic['category_level_3']
    product['currency'] = product_dic['currency']
    product['date'] = product_dic['date']
    product['marketplace'] = product_dic['marketplace']
    product['price'] = find_average_price(product_dic['product_selling_price'])
    product['product_id'] = product_dic['product_id']
    product['seller_name'] = product_dic['seller_name']
    product['additional_info'] = {}

    product_keys = product.keys()
    product_dic_keys = product_dic.keys()

    for key in product_dic_keys:
        if key not in product_keys:
            product['additional_info'].update(((key, product_dic[key]),))

    additional_info = json.dumps(product['additional_info'], sort_keys=True, indent=4,encoding='utf-8')

    # data_tuple is tuple which contains a columns values which are present in cassandra DB
    data_tuple = (

                    product['id'],
                    product['date'],
                    country.get(product['marketplace']),
                    product['marketplace'],
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

    )
    return data_tuple


class persist_BigQuery:
        def __init__(self, data):
                self.data = get_tuple(data)
                # self.bigquery_client = bigquery.Client.from_service_account_json(DataCollectors_Configuration.key_path)
                self.bigquery_client = bigquery.Client()
                self.schema = [
                                        bigquery.SchemaField('id', 'STRING'),
                                        bigquery.SchemaField('date', 'DATE' ),
                                        bigquery.SchemaField('country', 'STRING'),
                                        bigquery.SchemaField('marketplace', 'STRING'),
                                        bigquery.SchemaField('category', 'STRING'),
                                        bigquery.SchemaField('category_level_1', 'STRING'),
                                        bigquery.SchemaField('category_level_2', 'STRING'),
                                        bigquery.SchemaField('category_level_3', 'STRING'),
                                        bigquery.SchemaField('seller', 'STRING'),
                                        bigquery.SchemaField('asin', 'STRING'),
                                        bigquery.SchemaField('product_id', 'STRING'),
                                        bigquery.SchemaField('currency', 'STRING'),
                                        bigquery.SchemaField('price', 'FLOAT'),
                                        bigquery.SchemaField('additional_info', 'STRING')
                ]

                """Insert / fetch table data."""

                dataset_id = DataCollectors_Configuration.dataset_id
                table_id = DataCollectors_Configuration.table_id
                dataset = bigquery.Dataset(self.bigquery_client.dataset(dataset_id))
                table = bigquery.Table(dataset.table(table_id))
                # [START table_insert_rows]
                rows_to_insert = [data]
                errors = self.bigquery_client.insert_rows(table, rows_to_insert)
                assert errors == []