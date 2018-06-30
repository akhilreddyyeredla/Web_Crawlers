import json
import time
from google.cloud import bigquery
bigquery_client = bigquery.Client.from_service_account_json("/usr/datacollector/CBEC-Insights-91fbc0a4af35.json")
def test_table_insert_rows():
    """Insert / fetch table data."""
    dataset_id = 'eu_cbec_bi_data'
    table_id = 'marketplaces'
    dataset = bigquery.Dataset(bigquery_client.dataset(dataset_id))
    errors = bigquery_client.query("select count(*) from eu_cbec_bi_data.marketplaces where country='UAE'")    
    results = errors.result()
    #print len(results)
    for rows in results:
        print rows

def test_table_query_data():
    results = {}
    """Insert / fetch table data."""
    print "IN"
    dataset_id = 'eu_cbec_bi_data'
    table_id = 'marketplaces'
    dataset = bigquery.Dataset(bigquery_client.dataset(dataset_id))
    errors = bigquery_client.query("SELECT category_level_1 FROM eu_cbec_bi_data.marketplaces where ean='2724458442837'")    
    results = errors.result()
    #print len(results)
    #results = str(results)
    #dict = json.loads(results.read())
    #print results
    for rows in results:
        print rows

         

    
test_table_insert_rows()
test_table_query_data()
