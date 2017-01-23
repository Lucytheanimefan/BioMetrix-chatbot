import os
from flask import Flask
from flask import render_template,jsonify, request
import csv
import sys
import server
from server import *
from parser import *
import sys
import json
from JSONEncoder import JSONEncoder
import witCommands.witCommands
from witCommands.witCommands import get_response

app = Flask(__name__)

#db = server.get_db()

reload(sys)
sys.setdefaultencoding('utf-8')


@app.route("/")
@app.route("/home")
@app.route("/chat")
def home():
	return render_template('chat.html')


@app.route("/sendMessage", methods = ["POST", "GET"])
def send():
	print "in send message in py"
	print("In send message")
	message = request.json['message']
	print("Message: "+message)
	resp = get_response(message)
	print("Resp: ")
	print(resp)
	return jsonify(result=resp)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)