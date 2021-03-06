from flask import Flask, request, send_from_directory, jsonify
from fb_module.profile_getter import FB_Profile_Driver
import uuid
import threading
import random
import os
import os.path

"""This is an apache based app. The tutorial we used is at
    https://www.datasciencebytes.com/bytes/2015/02/24/running-a-flask-app-on-aws-ec2/
"""
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp'

@app.route("/")
def hello():
    return "Usable Security API!"

@app.route("/get_profile", methods=['GET'])
def get_profile():
    profile_url = request.args.get('profile_url', None)
    f = FB_Profile_Driver('cs232facebook@gmail.com', 'Facebook1!')
    unique_id = str(uuid.uuid4())
    image_type = random.randint(0, 4)
    run_args = [profile_url, '/tmp/' + unique_id, 1,image_type]
    run_thread = threading.Thread(target=f.runner, args=run_args)
    run_thread.start()
    return jsonify(unique_id=unique_id,
                   type=image_type)

@app.route("/get_little", methods=['GET'])
def get_little():
    unique_id = request.args.get('unique_id', None)
    file_location = app.config['UPLOAD_FOLDER'] + '/' + unique_id + 'screenshot_small.png'
    if os.path.isfile(file_location):
        return send_from_directory(app.config['UPLOAD_FOLDER'], unique_id + 'screenshot_small.png')
    else:
        return "The screenshot is not loaded yet. Please wait a minute then reload the page."

@app.route("/get_big", methods=['GET'])
def get_big():
    unique_id = request.args.get('unique_id', None)
    file_location = app.config['UPLOAD_FOLDER'] + '/' + unique_id + 'screenshot_full.png'
    if os.path.isfile(file_location):
        return send_from_directory(app.config['UPLOAD_FOLDER'], unique_id + 'screenshot_full.png')
    else:
        return "The screenshot is not loaded yet. Please wait a minute then reload the page."

@app.route("/delete_screenshots", methods=['get'])
def delete_screenshots():
    unique_id = request.args.get('unique_id', None)
    little_path = app.config['UPLOAD_FOLDER'] + '/' + unique_id + 'screenshot_small.png'
    big_path = app.config['UPLOAD_FOLDER'] + '/' + unique_id + 'screenshot_full.png'
    os.remove(little_path)
    os.remove(big_path)
    return jsonify(success=True)

if __name__ == '__main__':
    app.run()
