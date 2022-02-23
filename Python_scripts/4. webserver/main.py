#!/usr/bin/env python3
import threading
import redis
import json
import subprocess
import paho.mqtt.client as mqtt
from time import sleep
from redis_functions import *
from functions import *

global file
global rediSocket
numEvent = 0

def on_message_cam(client, userdata, message):
    global numEvent
    global rediSocket
    global file

    sleep(2)
    received = redis_get(rediSocket, numEvent)
    if received != None:
        numEvent += 1
        event_info = str(received.decode("utf-8"))
        print(event_info)
        create_html_template(event_info)
    

def receive_event():
    global rediSocket
    global file

    erase_html_template()
    
    rediSocket = redis.Redis(host='192.168.0.5', port=6379)

    mqttBroker = "192.168.0.4"
    client = mqtt.Client("webserver")
    client.connect(mqttBroker)
    client.subscribe("/home/webserver/traffic_events")
    client.on_message = on_message_cam
    client.loop_forever()

receive_event()

"""th1 = threading.Thread(target=receive_event)

th1.start()

th1.join()"""









