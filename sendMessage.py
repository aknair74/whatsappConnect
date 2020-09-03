from twilio.rest import Client
#from credentials import account_sid, auth_token, my_cell, my_twilio
account_sid = 'AC78087c23ae1dc687ff7ca9bed5f0f74e'
auth_token = 'your_token'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there from Twilio!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+19256395097'
                          )

print(message.sid)
