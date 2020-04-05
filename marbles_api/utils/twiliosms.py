from twilio.rest import Client
import os
import requests
from config import Config


def send_sms(cUser, eConName, eConNum):

    account_sid = Config.ACCOUNT_SID
    auth_token = Config.AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=[
                f"This is the Marbles App. User {cUser} is in need of your help! Please check on them quickly"],
            from_="+19132465603",
            to={eConNum}
        )
