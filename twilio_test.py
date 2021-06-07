from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACab8cdf5516d4926859b6bc0779e1ac4c"
auth_token = "383b20d729df7459f9197516c48f5a6e"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+91-9739817305",
    from_="+1 15182899852" ,  #+1 210-762-4855"
    body=" Detected" )
