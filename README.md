# Web_Crawlers
Amazon_and_Linio:
  - Amazon_AUS
  - Amazon_FRANCE	
  - Amazon_Germany	
  - Amazon_Italy	
  - Amazon_Mexico	
  - Amazon_Spain	
  - Amazon_UK	
  - Amazon_US
  - Amazon_cad	
  - Linio_08042018
 
Other_Market_Places:
  - Bonanza
  - EBAY
  - Etsy
  - Linio
  - Souq
  - Common -> 1. which contains of All the import statments and config statments
              2. All storage .py files like Kafka, Mysql, Cassandra, BigQuery


Amazon_XXXX:
  - hierarchy_collectors -> which collects the all the category names,urls and stored into a file accorinding to the category.
  - url_collectors -> Reads the Hirerchy file of a category and collects all the product urls and stores into a file according to the category.
  - info_collectors -> Reads the Url collector file and passes it to product parser and the info which is retured will be stored according to the configuration.
  - product_parsers -> Collects the data like name, price, rating etc(https://github.com/akhilreddyyeredla/Web_Crawlers/blob/master/datacollectors_fields%20(2).csv)
  
terapeak:
  - main.py -> need to mention the cookies data and the category url which should be scrapped and passes the ebay id to eBayTera.py.
  - eBayTera.py -> Scraps the fileds like name, price, rating etc along with terapeak data and stores into a file. 
