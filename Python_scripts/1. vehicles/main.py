#!/usr/bin/env python3
import threading
from functions import *
from mqtt_functions import *

event = 0

def driving_on_highway():
    global event

    #Creation of Cam message object
    cam_obj = Cam()   

    #Initialisation of Cam message
    cam = get_cam(cam_obj)

    #Creation of Denm message object
    denm_obj = Denm()

    #Initialisation of the connection with the broker
    client = create_client(cam_obj.getId())
    connect_to_broker(client)

    while True:
        sleep(0.5)
        #Set the time of sleeping regarding to the speed
        freezing_time(cam_obj.getSpeed())
        
        #update location and speed data
        #update_cam(cam_obj)
        cam = get_cam(cam_obj)

        #Check for events
        if event != 0:
            #If event arises -> send Denm message + slowing down cars
            denm = get_denm(cam_obj, denm_obj, event)
            new_cam = slowing_down(cam_obj) #Slowing down vehicles
            print(denm)
            print(new_cam)
            publish_mqtt_msg(client, new_cam)
            publish_mqtt_msg(client, denm)
        else:#if no events
            print(cam)
            publish_mqtt_msg(client, cam)
        
        

def arising_events():
    global event
    event_list = [3, 4, 5, 6, 7]

    while True:
        sleep(5) #Duration of between verifications
        if (random.randint(1,10)) > 5:
            event = random.choice(event_list)
            sleep(10) #Duration of an event
            if(event == 4): #If accident
                event = 5 # -> traffic jam for +10s
                sleep(10)
            event = 0


cars = threading.Thread(target=driving_on_highway)
trucks = threading.Thread(target=driving_on_highway)
motorcycles = threading.Thread(target=driving_on_highway)
highway_operator = threading.Thread(target=arising_events)

cars.start()
trucks.start()
motorcycles.start()
highway_operator.start()

cars.join()
trucks.join()
motorcycles.join()
highway_operator.join()
