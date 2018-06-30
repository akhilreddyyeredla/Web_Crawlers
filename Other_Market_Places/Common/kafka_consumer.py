#from kafka import KafkaConsumer
def python_kafka_consumer_performance():
   topic = 'test'
   consumer = KafkaConsumer(bootstrap_servers='35.203.13.104:9092')
   consumer.subscribe(topic)
   for msg in consumer:
       print msg.value
python_kafka_consumer_performance()

