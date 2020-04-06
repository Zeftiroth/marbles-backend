from twilio.rest import Client
import os
import requests
from config import Config


def send_sms(cUser, eConName, eConNum,  eConRelation):

    account_sid = Config.ACCOUNT_SID
    auth_token = Config.AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=[
                f"{eConName}, {cUser}'s {eConRelation}. {cUser} has pressed the panic button. Pls go to {cUser} now to make sure he/she is okay. Sincerely, Marbles Team"],
            from_="+19132465603",
            to={eConNum}
        )
