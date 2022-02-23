import paho.mqtt.client as mqtt

def create_client(id):
    return mqtt.Client(str(id))

def connect_to_broker(client):
    mqtt_broker = "172.16.3.254"
    client.connect(mqtt_broker)

def publish_mqtt_msg(client, json):
    client.publish("/home/gateway/traffic_events",json)