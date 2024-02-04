import pika
import json
import sys
import os
import django

project_path="C:\\Users\\Lenovo\\MICROSERVICE_PROJECT _DJANGO\\ProductManagement"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProductManagement.settings")
django.setup()

# Import the model
from product_app.models import FavProducts

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare the queue before consuming
queue_name = 'favourite_products'
channel.queue_declare(queue=queue_name)
print('this is the callback')

def callback(ch, method, properties, body):
    print('Recived a message')
    data = json.loads(body)
    print(data)
    if properties.content_type == 'products-created':
        FavProducts.objects.create (
            user_id=data.get('user_id')
            product_id=data.get('product-id')
        )
        print(products-created)
# Start consuming messages
channel.basic_consume(queue=queue_name,on_message_callback=callback, auto_ack=True)
print('Waiting for messages...')
channel.start_consuming()
# print(sys.executable)
