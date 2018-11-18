from twilio.rest import Client 
 
def sendSms(message, number):
    account_sid = '<Account SID>' 
    auth_token = '<Auth Token>' 
    client = Client(account_sid, auth_token) 
 
    message = client.messages.create( 
                              from_='+12183334545',  
                              body=message,      
                              to=number 
                          ) 
 
    print(message.sid)



#if __name__ == "__main__":
 #   sendSms('Test message', '+14379971245')
