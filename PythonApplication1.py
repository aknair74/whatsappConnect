from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC78087c23ae1dc687ff7ca9bed5f0f74e'
auth_token = '2f840caa5f8b9ec9fde0caed6f2d0d8a'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there from Twilio!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+19256395097'
                          )

print(message.sid)
