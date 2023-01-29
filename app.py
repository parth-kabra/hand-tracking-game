from flask import Flask, render_template, url_for, request, session, redirect
from flask_socketio import SocketIO, emit
from engineio.payload import Payload
import threading
from objects import getJson

app = Flask(__name__)
Payload.max_decode_packets = 500
io = SocketIO(app, cors_allowed_origins="*")

obj = ""

@app.route("/")
def home():
    return render_template("index.html")

@io.on("send_data")
def SHARE(a = 1):
    emit("hand", obj, broadcast = True)

def shareHand():
    global obj
    obj = getJson()

    threading.Timer(1, shareHand).start()

if __name__ == "__main__":
    shareHand()
    io.run(app, host = "0.0.0.0", port = 8080, debug = True)