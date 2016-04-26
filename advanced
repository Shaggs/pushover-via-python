#!/usr/bin/python
dict = {'user token': username}
import time
import requests
import datetime

app = "" # App token
title = raw_input("Insert Title: ").
message = raw_input("Insert Message: ")
print "Please set Prioity to (0) basic message (1) Important (2) Emergancy"
pri = raw_input("Set Priority (0) (1) or (2): ")
if pri is not 0 or 1 or 2:
 print "Please enter 0, 1 or 2"
else
 for k in dict:
    user = k
    params = {
    'token': app,
    'user': user,
    'title': title,
    'message': message,
    'retry': 300, 
    'expire': 40,
    'priority': pri ,
    'sound': 'siren',
    'ack': False
    }
    msg = requests.post('https://api.pushover.net/1/messages.json', data=params)
    print "POSTed message to " + dict[k]
    json_data = msg.json()
    print json_data['receipt']
    time.sleep(5)
    d = json_data['receipt']
    v = requests.get("https://api.pushover.net/1/receipts/"+ d + ".json?token=" + app)
    out = v.json()
while out['acknowledged'] is 0:
    print "not yet" #placed for debugging
    time.sleep(5)
    v = requests.get("https://api.pushover.net/1/receipts/"+ d + ".json?token=" + app)
    out = v.json()

def all_acknowledged(dict):
    for user in params:
        if not params['ack']:
            return False
    return True

while not all_acknowledged(dict):
    ack = out['acknowledged_by']
    for k in dict:
        if ack in k:
            acked = dict[k]
            params['ack'] = True
            t = datetime.datetime.strftime(datetime.datetime.now(), '%H:%M')
            print (acked + " acknowledged at " + t)
    v = requests.get("https://api.pushover.net/1/receipts/"+ d + ".json?token=" + app)
    out = v.json()
