from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC2a9e1c151fa57e1a35aa3e9e03794538"
# Your Auth Token from twilio.com/console
auth_token  = "a930e6e4310c84e71c086b0cabde852e"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14086936142", 
    from_="+18317038510",
    body="Hello from Python!")

print(message.sid)