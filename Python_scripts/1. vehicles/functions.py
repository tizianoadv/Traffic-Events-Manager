import random
import json
from cam import *
from denm import *
from time import sleep

def update_cam(cam_obj):
    speed = speed_calculator() 
    heading = round(random.uniform(16.00,18.00), 2)
    lat = round(random.uniform(49.242111,49.256912), 6)
    lon = round(random.uniform(4.065633,4.082189), 6)
    Cam.setId(cam_obj, id)
    Cam.setType(cam_obj, type)
    Cam.setSpeed(cam_obj, speed)
    Cam.setHeading(cam_obj, heading)
    Cam.setGps(cam_obj, lat, lon)


def speed_calculator():
    speed = 0
    if (random.randint(1,100) > 90):
        speed = random.randint(70, 89)
    else:
        speed = random.randint(90, 130)
    return speed

def slowing_down(cam_obj):
    Cam.setSpeed(cam_obj,random.randint(15, 20))
    return json.dumps(cam_obj.__dict__)

def get_cam(cam_obj):
    id = random.randint(1,1000)
    type_list = [5, 10, 15]
    type = random.choice(type_list)
    speed = random.randint(90, 130)#speed_calculator() 
    heading = round(random.uniform(16.00,18.00), 2)
    lat = round(random.uniform(49.242111,49.256912), 6)
    lon = round(random.uniform(4.065633,4.082189), 6)
    Cam.setId(cam_obj, id)
    Cam.setType(cam_obj, type)
    Cam.setSpeed(cam_obj, speed)
    Cam.setHeading(cam_obj, heading)
    Cam.setGps(cam_obj, lat, lon)
    #49.242111 #4.065633
    
    return json.dumps(cam_obj.__dict__)


def get_denm(cam_obj, denm_obj, event):
    id = Cam.getId(cam_obj)
    type = Cam.getType(cam_obj)
    cause = event
    Denm.setId(denm_obj, id)
    Denm.setType(denm_obj, type)
    Denm.setCause(denm_obj, cause)
    Denm.setGps(denm_obj,Cam.getGpsLat(cam_obj),Cam.getGpsLon(cam_obj))

    return json.dumps(denm_obj.__dict__)

def freezing_time(speed):
    if speed < 90 :
        sleep(1)
    else:
        sleep(0.1)