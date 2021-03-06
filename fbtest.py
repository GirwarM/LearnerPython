from flask import Flask, request
from pymessenger.bot import Bot
import random

import requests
from botocore.vendored.requests.api import request
app = Flask(__name__)

ACCESS_TOKEN="<add token for your FB page from developers.facebook.com>"
VERIFY_TOKEN = "VERIFY_TOKEN"

bot=Bot(ACCESS_TOKEN)

@app.route("/", methods=['GET','POST'])
def response():
    if request.method=='GET':
        if request.arg.get("hub.verify_token")==VERIFY_TOKEN:
            print('Verified')
            return requests.args.get("hub.challenge")
        else:
            return "invalid verification token"
    if requests.method=="POST":
        output=request.get_json()
        for event in output['entry']:
            messaging=event['messaging']
            for x in messaging:
                if x.get('message'):
                    recipient_id=x['sender']['id']
                    if x['message'].get('text'):
                        message=get_message()
                        bot.send_text_message(recipient_id,message)
                    if x['message'].get('attachments'):
                        for att in x['message'].get('attachments'):
                            bot.send_attachment_url(recipient_id, att['type'],att['payload']['url'])
                    else:
                        pass
        return 'Success'
    
def get_message():
    sample_responses=['Welcome to Sahayog Page,we will get back to you, happy to connect to you']
    return random.choice(sample_response)

if __name__=="__main__":
    app.run(port=5000,debug=True)
          
