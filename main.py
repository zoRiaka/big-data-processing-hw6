from time import sleep
from kafka import KafkaProducer, KafkaConsumer
import csv
from json import dumps
from datetime import datetime

producer = KafkaProducer(bootstrap_servers='kafka-server:9092', api_version=(2, 0, 2),
                         value_serializer=lambda x: dumps(x).encode('ascii'))

with open('/opt/app/sample.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        row['created_at'] = str(datetime.now())
        new_row = row['created_at'] + ' : ' + row['text'] + ' (' + row['author_id'] + ')'
        data = f'{new_row}'
        result = producer.send('tweets', data)
        sleep(0.07)
    producer.flush()
