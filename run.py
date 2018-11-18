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
person3 = Person("Name3")

group = { '+14373334444': person1, '+16475556767': person2, '+15196667878': person3 }

def demo_trigger(phoneNumber):
    send_sms.sendSms('Your scheduled meditation session will start is about to begin. Will you join? (Yes/No)', phoneNumber)
    

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():

    body = request.values.get('Body', None)
    senderNumber = request.values.get('From', None) 
    senderName = group[senderNumber].name
    
    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'Yes':
        group[senderNumber].countJoined += 1
        for phoneNumber in group.keys():
            if phoneNumber != senderNumber:
                send_sms.sendSms(senderName + ' has joined', phoneNumber)
        send_sms.sendSms('Thanks for joining!', senderNumber)
    elif body == 'No':
        resp.message("Hope to see you next time")
    elif body == 'Trigger':
        for phoneNumber in group.keys():
            demo_trigger(phoneNumber)
    else:
        resp.message("Sorry, I didn't get that")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
