#!/usr/bin/env python3
import threading
import json
import paho.mqtt.client as mqtt
from time import sleep
from functions import *
from mqtt_functions import *

event = 0
event_info = {"list_id":[], "list_type":[], "cause":[], "lat":[], "lon":[]}
path_clear = False
messages_sent = 0

def on_message_cam(client, userdata, message):
    global event_info
    global path_clear 

    received = json.loads(str(message.payload.decode("utf-8")))
    if received['cause'] != 0:
        update_event(received, event_info)
        path_clear = False
    else:
        path_clear = True

    #print("event_info: ", event_info)

def receive_event():
    mqttBroker = "192.168.0.3"
    client = mqtt.Client("eventhub")
    client.connect(mqttBroker)
    client.subscribe("/home/eventhub/traffic_events")
    client.on_message = on_message_cam
    client.loop_forever()

def send_to_webserver():
    path_clear
    event_info
    global messages_sent

    client1 = create_client(0)
    connect_to_broker(client1,"192.168.0.4")
    
    while True:
        sleep(1)
        if path_clear and len(event_info["list_id"]) != 0 and messages_sent < 2:
            print("send_to_webserver - Path clear : {}".format(event_info))
            publish_event_webserver(client1, event_info)
            messages_sent += 1

def send_to_buffer():
    path_clear
    event_info
    global messages_sent

    client2 = create_client(0)
    connect_to_broker(client2,"192.168.0.6")

    while True:
        sleep(1)
        if path_clear and len(event_info["list_id"]) != 0 and messages_sent < 2:
            print("send_to_buffer - Path clear : {}".format(event_info))
            publish_event_buffer(client2, event_info)
            messages_sent += 1

def check_messages_sent():
    global messages_sent
    global event_info

    while True:
        sleep(0.5)
        if(messages_sent == 2):
            messages_sent = 0
            erase_event(event_info)

th1 = threading.Thread(target=receive_event)
th2 = threading.Thread(target=send_to_webserver)
th3 = threading.Thread(target=send_to_buffer)
th4 = threading.Thread(target=check_messages_sent)

th1.start()
th2.start()
th3.start()
th4.start()

th1.join()
th2.join()
th3.join()
th4.join()





