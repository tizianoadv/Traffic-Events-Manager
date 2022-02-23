import redis
def store_data(rediSocket, event_to_store, numEvent):
    key_string = "event"
    key = key_string + str(numEvent)
    rediSocket.set(str(key),str(event_to_store))

