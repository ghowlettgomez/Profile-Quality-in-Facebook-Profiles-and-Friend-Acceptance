from flask import Flask, request, send_from_directory
from fb_module.profile_getter import FB_Profile_Driver

"""This is an apache based app. The tutorial we used is at
	https://www.datasciencebytes.com/bytes/2015/02/24/running-a-flask-app-on-aws-ec2/
"""
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp'
f = FB_Profile_Driver('cs232facebook@gmail.com', 'Facebook1!')

@app.route("/")
def hello():
    return "Usable Security API!"

@app.route("/get_profile", methods=['GET'])
def get_profile():
	profile_url = request.args.get('profile_url', None)
	try:
		profile_name = profile_url.split('/')[-1]
	except:
		return 'That is not a profile_url'
	f.run(profile_url, '/tmp/' + profile_name)
	return send_from_directory(app.config['UPLOAD_FOLDER'], profile_name + 'screenshot.png', as_attachment=True)


if __name__ == '__main__':
    app.run()
