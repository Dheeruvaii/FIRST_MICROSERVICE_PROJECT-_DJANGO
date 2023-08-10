import pika
import json

def publish(user_id, product_id):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    exchange_name = 'user_favorite_products'
    message = {
        'user_id': user_id,
        'product_id': product_id
    }

    # channel.exchange_declare(exchange=exchange_name, exchange_type='fanout')
    channel.basic_publish(exchange='', routing_key='favourite_products', body=json.dumps(message))

    print(f" [x] Sent favorite product request for User {user_id}, Product {product_id}")

    connection.close()
