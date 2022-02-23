#!/usr/bin/env python3
import threading
import json
import paho.mqtt.client as mqtt
from time import sleep
from amqp_functions import *
from functions import *


event_arised = False
event_info = {"list_id":[], "list_type":[], "cause":[], "lat":[], "lon":[]}

def on_message_cam(client, userdata, message):
    global event_info
    global event_arised 

    received = json.loads(str(message.payload.decode("utf-8")))
    print("Received : {}".format(received))

    copy_event_info(received, event_info)

    event_arised = True
    

def receive_event():
    mqttBroker = "192.168.0.6"
    client = mqtt.Client("buffer")
    client.connect(mqttBroker)
    client.subscribe("/home/buffer/traffic_events")
    client.on_message = on_message_cam
    client.loop_forever()

def send_to_queue():
    event_info
    global event_arised

    connection = amqp_configuration()
    channel = amqp_connection(connection)

    while True:
        try:
            if(event_arised):
                amqp_pub(channel,json.dumps(event_info))
                event_arised = False
                erase_event_info(event_info)
        except KeyboardInterrupt:
            end_connection(connection)


th1 = threading.Thread(target=receive_event)
th2 = threading.Thread(target=send_to_queue)

th1.start()
th2.start()

th1.join()
th2.join()







