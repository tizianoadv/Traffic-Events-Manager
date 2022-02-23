def update_event(received,event_info):
    if len(event_info["list_id"]) < 2 : #Number max of a list of event
        event_info["list_id"].append(received['stationId'])
        event_info["list_type"].append(received['stationType'])
        event_info["cause"] = received['cause']
        event_info["lat"] = received['lat']
        event_info["lon"] = received['lon']

def erase_event(event_info):
    event_info["list_id"].clear()
    event_info["list_type"].clear()