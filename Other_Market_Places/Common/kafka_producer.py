#from kafka import KafkaProducer
def python_kafka_producer_performance(data):
   producer = KafkaProducer(bootstrap_servers='localhost:9092')
   topic = 'test'
   producer.send(topic, data)
   producer.flush()

