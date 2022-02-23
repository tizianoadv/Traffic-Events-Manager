import paho.mqtt.client as mqtt
import json

def create_client(id):
    return mqtt.Client(str(id))

def connect_to_broker(client):
    mqtt_broker = "192.168.0.3"
    client.connect(mqtt_broker)

def list_to_serial(denm,i):
    data_out = {"stationId":"", "stationType":"", "cause":"", "lat":"", "lon":""}

    data_out["stationId"] = denm['list_id'][i]
    data_out["stationType"] = denm['list_type'][i]
    data_out["cause"] = denm['list_cause'][i]
    data_out["lat"] = denm['list_lat'][i]
    data_out["lon"] = denm['list_lon'][i]

    return data_out

def publish_denm_event(client, denm):
    i=0

    while i < len(denm['list_id']):
        data_out = list_to_serial(denm,i)
        client.publish("/home/eventhub/traffic_events",json.dumps(data_out))
        print("DENM: {}".format(json.dumps(data_out)))
        i +=1 

def publish_denm_no_event(client, denm_null):
    client.publish("/home/eventhub/traffic_events",json.dumps(denm_null))