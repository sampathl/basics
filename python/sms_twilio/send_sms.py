from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC2a9e1c151fa57e1aXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "XXXXXXXXXXXXXXX"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+1XXXXXXXXXX", 
    from_="+18317038510",
    body="Hello from Python!")

print(message.sid)