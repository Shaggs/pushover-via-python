#!/usr/bin/env-python3
import requests

app = "" # add token from pushover here
user = "" # add your user token here

title = input("Insert Title: ")

msg = input("Insert Message: ")
params = {
    'token': app,
    'user': user,
    'title': title,
    'message': msg,
    'priority': 1
    }
output = requests.post('https://api.pushover.net/1/messages.json', data=params)
print "sending"
out = output.json()
if out['status'] is 1:
 print("message sent")
else:
	print ("message not sent")
	print output.json()
