# api/consumers.py
from channels.generic.websocket import WebsocketConsumer
import json
import requests
from time import sleep

jobState = 'Waiting'

class JobStateConsumer(WebsocketConsumer):
#    def __init__(self, jid='', jst=''):
#        self.jobid = jid
#        self.jobstate = jst
    
    def connect(self):
        print('===JobStateConsumer::connect() ... connected!!!')
        self.accept()
    
    def disconnect(self, close_code):
        pass
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        url = 'http://localhost:8443/jobs/' + text_data_json['jobid']
        headers = {
            'Content-Type': 'application/json',
            'api-key': 'in1uP28Y1Et9YGp95VLYzhm5Jgd5M1r0CKI7326RHwbVcHGa'
        }
        data = {}
        res = requests.get(url, headers=headers, data=json.dumps(data))
        res_data = json.loads(res.content.decode("utf8"))
        global jobState
        jobState = res_data["state"]
        print('===JobStateConsumer::receive() job state: ', jobState)
#        print(res)
#        text_data_json = json.loads(text_data)
#        self.jobid = text_data_json['jobid']
#        self.jobstate = text_data_json['jobstate']
#        print('===JobStateConsumer::receive() text_data_json: ', text_data_json)
#        jobState = text_data_json['message']
#        jobState = 'Running'
        sleep(1)
        self.send(text_data=json.dumps({
                                       'jobid': res_data["id"],
                                       'jobstate': jobState
                                       }))
