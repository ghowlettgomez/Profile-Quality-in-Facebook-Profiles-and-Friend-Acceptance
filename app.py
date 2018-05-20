#!/usr/bin/python3.6

from fb_module.profile_getter import FB_Profile_Driver
import urllib.parse

def home_handler(env, start_fn):
    start_fn('200 OK', [('Content-Type', 'text/html')])
    return[bytes('<form action="make_profile" method="post">Facebook URL: <input type="text" name="url"><br><input type="submit" value="Submit"></form>', 'utf-8')]

def make_profile(env, start_fn):
    try:
        request_body_size = int(env.get('CONTENT_LENGTH', 0))
    except(ValueError):
        request_body_size = 0

    raw_body = env['wsgi.input'].read(request_body_size).decode()
    body = urllib.parse.parse_qs(raw_body)

    f = FB_Profile_Driver('cs232facebook@gmail.com', 'Facebook1!')
    f.run(body['url'][0], '/tmp/screenshot2.png')

    start_fn('200 OK', [('Content-Type', 'text/html')])
    return[bytes("Getting profile.", 'utf-8')]

routes = {
    '/': home_handler,
    '/make_profile': make_profile,
}

class Application(object):
    def __init__(self, routes):
        self.routes = routes

    def not_found(self, env, start_fn):
        start_fn('404 Not Found', [('Content-Type', 'text/html')])
        return [bytes("404 Not Found", 'utf-8')]

    def __call__(self, env, start_fn):
        handler = self.routes.get(env.get('PATH_INFO')) or self.not_found
        return handler(env, start_fn)

app = Application(routes)
