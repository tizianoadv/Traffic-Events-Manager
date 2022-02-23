import paho.mqtt.client as mqtt
import json

def create_client(id):
    return mqtt.Client(str(id))

def connect_to_broker(client, addr_broker):
    client.connect(addr_broker)

def publish_event_webserver(client, denm):
    client.publish("/home/webserver/traffic_events",json.dumps(denm))

def publish_event_buffer(client, denm):
    client.publish("/home/buffer/traffic_events",json.dumps(denm))