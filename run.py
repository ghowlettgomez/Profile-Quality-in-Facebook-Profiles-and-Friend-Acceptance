from fb_module.profile_getter import FB_Profile_Driver

f = FB_Profile_Driver('cs232facebook@gmail.com', 'Facebook1!')

x = 0

def runner():
    while True:
        try:
            f.run('https://www.facebook.com/profile.php?id=100008426081012', '/tmp/screenshot.png')
            break
        except IndexError:
            runner()

runner()
