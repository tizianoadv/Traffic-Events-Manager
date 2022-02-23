import json

def decode_to_dict(received):
    return json.loads(received)

def check_speed(received, jam_info):
    if(not(received['stationId'] in jam_info["list_id"])) and (received['speed'] < 90):
        jam_info["list_id"].append(received['stationId'])
        jam_info["list_type"].append(received['stationType'])
        jam_info["list_speed"].append(received['speed'])
        jam_info["list_heading"].append(received['heading'])
        jam_info["list_lat"].append(received['gpsLat'])
        jam_info["list_lon"].append(received['gpsLon'])

def traffic_jam(jam_info):
    jam_arised = False

    if len(jam_info["list_id"]) == 3:
        jam_arised = True
    
    return jam_arised

def erase_traffic_jam(jam_info):
    jam_info["list_id"].clear()
    jam_info["list_type"].clear()
    jam_info["list_speed"].clear()
    jam_info["list_heading"].clear()
    jam_info["list_lat"].clear()
    jam_info["list_lon"].clear()

def check_accident(denm_data, denm_Id_List, accident_event):

    if(accident_event == 0) and (denm_Id_List):
        denm_Id_List.clear()

    if (not(denm_data['stationId'] in denm_Id_List)) and (denm_data['cause'] == 4):
        denm_Id_List.append(denm_data['stationId'])
        accident_event += 1
        
    return accident_event

def check_denm(denm_info, received):
    denm_info["list_id"].append(received['stationId'])
    denm_info["list_type"].append(received['stationType'])
    denm_info["list_cause"].append(received['cause'])
    denm_info["list_lat"].append(received['gpsLat'])
    denm_info["list_lon"].append(received['gpsLon'])

def erase_denm(denm_info):
    denm_info["list_id"].clear()
    denm_info["list_type"].clear()
    denm_info["list_cause"].clear()
    denm_info["list_lat"].clear()
    denm_info["list_lon"].clear()