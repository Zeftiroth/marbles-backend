import os
import requests


# def send_simple_message(cUser, eConName, eConEmail, eConRelation):

#     return requests.post("https://api.mailgun.net/v3/sandboxa290eb457da745fdad8b11f801694050.mailgun.org/   messages", auth=("api", "key-a2e59f19d680870987eef72e0a6e2ec3"),
#                          data={"from": "Marbles App <mailgun@sandboxa290eb457da745fdad8b11f801694050.mailgun.org >",
#                                "to": ["zeft.huisen@gmail.com",
#                                       "me@sandboxa290eb457da745fdad8b11f801694050.mailgun.org"],
#                                "subject": f"{cUser} has pressed the panic button!",
#                                "text": f"{eConName}, {cUser}'s {eConRelation}. {cUser} has pressed the panic button. Pls go to {cUser} now to make sure he/she is okay. Sincerely, Marbles Team"}
#                          )
def send_simple_message(cUser, eConName, eConEmail, eConRelation

                        ):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxa290eb457da745fdad8b11f801694050.mailgun.org/messages",
        auth=("api", os.getenv("MAILGUN_API_KEY")),
        data={"from": "Marbles App <mailgun@sandboxa290eb457da745fdad8b11f801694050.mailgun.org >",
              "to": [f"{eConEmail}"],
              "subject": f"{cUser} has pressed the panic button",
              "text": f"{eConName}, {cUser}'s {eConRelation}. {cUser} has pressed the panic button. Pls go to {cUser} now to make sure he/she is okay. Sincerely, Marbles Team"})
