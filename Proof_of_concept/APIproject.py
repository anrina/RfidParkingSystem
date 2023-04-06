import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort, jsonify
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from pyngrok import ngrok
from pymongo import MongoClient
from datetime import datetime

# database code
#mongoClient = MongoClient(os.environ["MONGODB_URI"], 27017)
#mongoClient = MongoClient("localhost", 27017)
mongoClient = MongoClient("mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb")
#if os.environ["PHASE"] == "DEVELOPMENT":
#    app_db = mongoClient.blecollector_test # Database
#if os.environ["PHASE"] == "PRODUCTION":
#    app_db = mongoClient.blecollector # Database
app_db = mongoClient.blecollector_test # Database

app = Flask(__name__, static_url_path='/ui', static_folder='web/')

# get channel_secret and channel_access_token from your environment variable
channel_secret = "8ff61a03f307158696dd7ec0f2a8a62f"
channel_access_token = "Cwu58cODOPCdfIXGyIWkZ1ZH0GXaRpJwWPuhOdHrjbLoCUE78EhzbxCkCskYcXSwfXBV9wlSJZ5DZuu5zZyFk2/8jsY7JbMQ46GhK8m4bEdh8D0V8LRC2fEbbAEd+yV19+nEaz6BLEUQuujOn41eSgdB04t89/1O/w1cDnyilFU="
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)
count = 0

@app.route("/", methods=['GET'])
def hello_world():
    return "Hello, World!"

@app.route("/api/inject_logging", methods=['POST'])
def inject_logging():
    #if os.environ["PHASE"] == "DEVELOPMENT":
    data = request.get_json()
    data['timestamp'] = datetime.now()
    logging_col = app_db.logging # Collection
    logging_col.insert_one(data)
    print(data)
    return jsonify({"status": "OK"})
    #return jsonify({"status": "ERROR"})


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    #ngrok.set_auth_token("2LaKhw7TNXQJgaEBfUcPL3ah6OR_33DmnRvpEh9TodwLuNjHz")
    #public_url = ngrok.connect(options.port)
    #url = public_url.public_url.replace('http', 'https') + '/callback'
    #print(url)
    #line_bot_api.set_webhook_endpoint(url)
    app.run(debug=options.debug, port=options.port)
