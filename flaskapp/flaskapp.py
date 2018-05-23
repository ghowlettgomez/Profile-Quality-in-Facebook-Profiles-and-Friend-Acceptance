from flask import Flask, request, send_from_directory, jsonify
from fb_module.profile_getter import FB_Profile_Driver
import uuid
import threading
import random

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
    unique_id = uuid.uuid4().int
    image_type = random.randint(0, 4)
    run_args = [profile_url, '/tmp/' + str(unique_id), 1,image_type]
    run_thread = threading.Thread(target=f.runner, args=run_args)
    run_thread.start()
    return jsonify(unique_id=unique_id,
                   type=image_type)

@app.route("/get_little", methods=['GET'])
def get_little():
    unique_id = request.args.get('unique_id', None)
    return send_from_directory(app.config['UPLOAD_FOLDER'], str(unique_id) + 'screenshot_small.png')

@app.route("/get_big", methods=['GET'])
def get_big():
    unique_id = request.args.get('unique_id', None)
    return send_from_directory(app.config['UPLOAD_FOLDER'], str(unique_id) + 'screenshot_full.png')

if __name__ == '__main__':
    app.run()
