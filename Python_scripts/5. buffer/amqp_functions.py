import pika
from pika.exchange_type import ExchangeType


def amqp_configuration():
    credentials = pika.PlainCredentials('database.client', 'database.client')
    parameters = pika.ConnectionParameters('192.168.0.6',5672,'/',credentials)
    connection = pika.BlockingConnection(parameters)

    return connection

def amqp_connection(connection):
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    return channel

def amqp_pub(channel,message): 
    channel.basic_publish(exchange='', routing_key='traffic_events', body=message)

def end_connection(connection):
    connection.close()
    
