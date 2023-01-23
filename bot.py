import json
import requests
import datetime

class broadcast():
  def __init__(self, json):
    self.json = json
    self.dict_messages = json['data']
    self.APIUrl = 'https://api.ultramsg.com/{{instance_id}}/'
    self.token = '{{token}}'

  def send_requests(self, type, data):
    data = {"to" : chatID,
	    "body" : text}
    answer = self.send_requests('messages/chat', data)
    return answer

  def time(self, chatID):
    t = datetime.datetime.now()
    time = t.strftime('%Y-%m-%d %H:%M:%S')
    return self.send_message(chatID, time)
