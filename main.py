from flask import Flask,send_file,render_template
import os

# from flask_socketio import SocketIO
# async_mode = None
app = Flask(__name__)
# socket_ = SocketIO(app, async_mode=async_mode)
PATH=r"."
@app.get('/')
def home():
    files=os.listdir(PATH)
    return render_template("index.html",files=files)

@app.get("/download/<file_name>")#new comment 
def download_file(file_name):
    path=rf"{PATH}\{file_name}"
    return send_file(path,as_attachment=False,mimetype='video/mp4')

app.run(host='0.0.0.0',port=3000,debug=True)

