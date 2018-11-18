# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import send_sms

app = Flask(__name__)

class Person:
    def __init__(self, name):
        self.name = name
        self.countJoined = 0

person1 = Person("Name1")
person2 = Person("Name2")

group = { '+14379998888': person1, '+16474445555': person2 }

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():

    body = request.values.get('Body', None)
    senderNumber = request.values.get('From', None) 
    senderName = group[senderNumber].name
    
    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'Yes':
        group[senderNumber] += 1
        for phoneNumber in group.keys():
            if phoneNumber != senderNumber:
                send_sms.sendSms(senderName + ' has joined', phoneNumber)
    elif body == 'No':
        resp.message("Hope to see you next time")
    else:
        resp.message("Sorry, I didn't get that")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
