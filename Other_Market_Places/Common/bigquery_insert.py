import time
from google.cloud import bigquery


#bigquery_client = bigquery.Client.from_service_account_json("/usr/datacollector/CBEC-Insights-91fbc0a4af35.json")

def _millis():
    return int(time.time() * 1000)

SCHEMA = [
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
    bigquery.SchemaField('additional_info', 'STRING'),
    bigquery.SchemaField('product_name', 'STRING'),
    bigquery.SchemaField('seller_score', 'STRING'),
    bigquery.SchemaField('bsr', 'STRING')
]


def test_table_insert_rows(data):
    """Insert / fetch table data."""
    dataset_id = 'eu_cbec_bi_data'
    table_id = 'marketplaces'
    dataset = bigquery.Dataset(bigquery_client.dataset(dataset_id))
 
    table = bigquery.Table(dataset.table(table_id), schema=SCHEMA)

    # [START table_insert_rows]
    rows_to_insert = [data]

    errors = bigquery_client.insert_rows(table, rows_to_insert)  # API request

    assert errors == []

    # [END table_insert_rows]
    

#test_table_insert_rows(data)
