import pymongo
import hashlib
import time

def protect(string):
    for _ in range(1000):
        string = hashlib.sha512(string+"asdkkl21j312j3lkjasdi9930132009)(Sd9asd--as0d-012-3-023-0_)_)-0asd-0asdasdasd]]{AS{D[asd[[123]12]3asd[[ASD]]]123;12312l3laskdlASDKKAJSDKjasd").hexdigest()
        
    return string


db = pymongo.MongoClient("localhost", 27017).onx
site="Onx"



def expired():
    reference = {"1m":60*60*24*31, "10min":60*10, "1h":60*60, "1d":60*60*24, "1w":60*60*24*7}
    while True:
        for x in db.pastes.find({"$not":{"expiration":False}}):
            if time.time() - x['time'] >= reference[x['expiration']]:
                db.pastes.remove({"id":x['id']})
        
        time.sleep(60)
