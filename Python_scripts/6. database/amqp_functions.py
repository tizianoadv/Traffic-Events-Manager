import pika
import json
from pika.exchange_type import ExchangeType

def amqp_configuration():
    credentials = pika.PlainCredentials('database.client', 'database.client')
    parameters = pika.ConnectionParameters('192.168.0.6',5672,'/',credentials)
    connection = pika.BlockingConnection(parameters)

    return connection

def amqp_connection(connection):
    channel = connection.channel()
    channel.queue_declare(queue='traffic_events')

    return channel
    
def end_connection(connection):
    connection.close()










