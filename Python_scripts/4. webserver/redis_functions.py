
def redis_get(rediSocket,numEvent):
    key_string = "event"
    key = key_string + str(numEvent)
    return rediSocket.get(str(key))