# 1 using redis
# 2 using queue
completed_links_store = 1

using_redis = 1
using_queue = 2
## Big Query Configuration file

key_path = "/usr/datacollector/CBEC-Insights-91fbc0a4af35.json"
dataset_id = 'eu_cbec_bi_data'
table_id = 'marketplaces'

## MySQL database configuration file
MYSQL_USER_NAME = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_HOST = 'localhost'
MYSQL_DB_name = 'amazon_uk'

## Cassandra database configuration file
Cassandra_USER_NAME = 'root'
Cassandra_PASSWORD = 'Root@123456'
Cassandra_HOST = '35.200.145.21'
Cassandra_DB_name = 'marketplaces'




# 1 to write into  sql_db
# 2 to write into file
# 3 to write into cassandra
# 4 to write into multiple file
# 5 to write into BigQuery
WRITE_TO = 4