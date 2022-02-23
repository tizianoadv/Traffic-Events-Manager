#!/usr/bin/env python3
import threading
import paho.mqtt.client as mqtt
from time import sleep
from functions import *
from mqtt_functions import *

jam_arised = False
denm_arised = False

jam_info = {"list_id":[], "list_type":[], "list_speed":[], "list_heading":[], "list_lat":[], "list_lon":[]}
denm_info = {"list_id":[], "list_type":[], "list_cause":[], "list_lat":[], "list_lon":[]}

def on_message_cam(client, userdata, message):
    global jam_arised
    global denm_arised
    global jam_info
    global denm_info

    received = decode_to_dict(str(message.payload.decode("utf-8")))

    if 'speed' in received.keys(): #Cam message
        #print("Cam message: ", received)

        check_speed(received, jam_info)

        if traffic_jam(jam_info):
            jam_arised = True

    else: # Denm message
        check_denm(denm_info, received)

def report_info():
    global jam_arised
    global jam_info
    denm_info_null = {"stationId":[], "stationType":[], "cause":0, "lat":[], "lon":[]}

    client = create_client(0)
    connect_to_broker(client)

    while True:
        sleep(1)

        if(jam_arised):
            #print("traffic")
            #print(jam_info)
            #print(denm_info)
            publish_denm_event(client, denm_info)
            erase_traffic_jam(jam_info)
            erase_denm(denm_info)
            jam_arised = False
        else:
            #print("No jam")
            publish_denm_no_event(client, denm_info_null)
        

def affiche_acc():
    global accident_event

    while True:
        sleep(1)
        if(accident_event >= 2):
            #print("Accident")
            accident_event = 0
        else:
            pass#print("No accident")

def receive_cam():
    mqttBroker = "172.16.3.254"
    client = mqtt.Client("gateway")
    client.connect(mqttBroker)
    client.subscribe("/home/gateway/traffic_events")
    client.on_message = on_message_cam
    client.loop_forever()

th1 = threading.Thread(target=receive_cam)
th2 = threading.Thread(target=report_info)

th1.start()
th2.start()


th1.join()
th2.join()




