import os
import requests


def send_simple_message(cUser, eConName, eConEmail, eConRelation):

    return requests.post("https://api.mailgun.net/v3/sandboxa290eb457da745fdad8b11f801694050.mailgun.org/   messages", auth=("api", os.getenv("MAILGUN_API_KEY")),
                         data={"from": "Marbles App <mailgun@sandboxa290eb457da745fdad8b11f801694050.mailgun.org >",
                               "to": [{eConEmail}],
                               "subject": f"{cUser} has pressed the panic button!",
                               "text": f"{eConName}, {cUser}'s {eConRelation}. {cUser} has pressed the panic button. Pls go to {cUser} now to make sure he/she is okay. Sincerely, Marbles Team"}
                         )
