#!/usr/bin/env python3
import threading
import redis
from amqp_functions import *
from functions import *
from redis_functions import *

global rediSocket
numEvent = 0
last_cause = 0 
first_event = True
event_info = {"list_id":[], "list_type":[], "cause":[], "lat":[], "lon":[]}

def callback(ch, method, properties, body):
    global event_info
    global first_event
    global last_cause
    global rediSocket
    global numEvent

    received = json.loads(body)
    #print("IN CALLBACK : {}".format(received))

    if first_event:
        #on stocke
        first_event = False
        copy_event_info(received, event_info) # Copie des informations
        last_cause = received['cause']
    else:
        if received['cause'] == last_cause:
            # on stocke
            copy_event_info(received, event_info)
        else:
            # on envoie
            print("SEND TO BDD : {}".format(event_info))
            store_data(rediSocket,event_info,numEvent)
            numEvent += 1
            # on efface event_info 
            erase_event_info(event_info)
            # on copie le nouveau
            copy_event_info(received, event_info)
            last_cause = received['cause']

  
def amqp_sub(channel):
    channel.basic_consume(queue='traffic_events',auto_ack=True,on_message_callback=callback)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

def receive_event():
    global rediSocket
    rediSocket = redis.Redis(host='localhost', port=6379, db=0)
    try:
        connection = amqp_configuration()
        channel = amqp_connection(connection)
        amqp_sub(channel)
    except KeyboardInterrupt:
        end_connection()


th1 = threading.Thread(target=receive_event)

th1.start()

th1.join()