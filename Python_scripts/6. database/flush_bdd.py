import redis

def flush(rediSocket):
    i=0
    key_string = "event"
    
    while(i<50):
        cle = key_string + str(i)
        rediSocket.delete(cle)
        i+=1

rediSocket = redis.Redis(host='localhost', port=6379, db=0)
flush(rediSocket)