from flask import Flask, request, jsonify
from bot import broadcast
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home ():
  if request.method == 'POST':
    bot = broadcast(request.json)
    return bot.Processing_incoming_messages()

if (__name__) == '__main__':
  app.run()
