#!/usr/bin/python
import requests

app = "" # add token from pushover here
user = "" # add your user token here

title = raw_input("Insert Title: ")

msg = raw_input("Insert Message: ")
params = {
    'token': app,
    'user': user,
    'title': title,
    'message': msg,
    'priority': 1
    }
output = requests.post('https://api.pushover.net/1/messages.json', data=params)
print "sending"
jout = output.json()
if jout['status'] is 1:
 print "message sent"
else:
	print "message not sent"
	print output.json()
