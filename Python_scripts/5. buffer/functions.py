
def copy_event_info(received, event_info):
    i = 0
    while i < len(received['list_id']):
        event_info['list_id'].append(received['list_id'][i])
        event_info['list_type'].append(received['list_type'][i])
        i+=1
    event_info['cause'] = received['cause']
    event_info['lat'] = received['lat']
    event_info['lon'] = received['lon']

def erase_event_info(event_info):
    event_info["list_id"].clear()
    event_info["list_type"].clear()
    event_info['cause'] = 0
    event_info['lat'] = 0
    event_info['lon'] = 0