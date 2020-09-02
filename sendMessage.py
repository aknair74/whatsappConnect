from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there from Twilio!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+19256395097'
                          )

print(message.sid)
