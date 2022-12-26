from flask import Flask, request
import ast

app = Flask(__name__)
messages = []
user1 = ""
user2 = ""
user_1_status = "offline"
user_2_status = "offline"
sos_mode = "False"


@app.route('/')
def home():
    return "Home"

def messager(sender, time, message, seen):
    m = {
        'sender':sender,
        'time':time,
        'message':message,
        'seen':seen
    }
    return str(m)

@app.route('/user',methods=["POST"])
def register():
    global user1
    global user2
    d = request.get_data().decode()
    data = ast.literal_eval(d)
    if data["user_num"] == "1":
        user1 = data["user_num"]
        return "200"
    elif data["user_num"] == "2":
        user2 = data["user_num"]
        return "200"
    else:
        return "400"

@app.route('/get_status', methods=["GET"])
def get_status():
    global user_1_status
    global user_2_status
    d = request.get_data().decode()
    if d == "1":
        return user_1_status
    elif d == "2":
        return user_2_status
    else:
        return "400"

@app.route("/change_status", methods=["POST"])
def change_status():
    global user_1_status
    global user_2_status
    d = request.get_data().decode()
    data = ast.literal_eval(d)
    if data["user_num"] == "1":
        user_1_status = data["change_to"]
        return "200"
    elif data["user_num"] == "2":
        user_2_status = data["change_to"]
        return "200"
    else:
        return "400"

@app.route('/sos_mode', methods=["POST"])
def sosmode():
    global sos_mode
    d = request.get_data().decode()
    if d == "True":
        sos_mode = "True"
        return "200"
    elif d == "False":
        sos_mode = "False"
        return "200"
    else:
        return "400"

@app.route('/get_sos', methods=["GET"])
def get_sos():
    global sos_mode
    return sos_mode

@app.route('/send', methods=["POST"])
def send():
    global messages
    d = request.get_data().decode()
    data = ast.literal_eval(d)
    m = messager(data["sender"], data["time"], data["message"], "False")
    messages.append(str(m))
    return "200"

@app.route('/get_messages', methods=["GET"])
def get_messages():
    global messages
    return str(messages)

app.run(port=5000,debug=True)