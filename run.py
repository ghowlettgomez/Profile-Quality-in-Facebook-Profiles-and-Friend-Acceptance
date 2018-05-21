from fb_module.profile_getter import FB_Profile_Driver

f = FB_Profile_Driver('cs232facebook@gmail.com', 'Facebook1!')
while True:
    try:
        f.run('https://www.facebook.com/profile.php?id=100008426081012', '/tmp/')
        break
    except IndexError:
        f.run('https://www.facebook.com/profile.php?id=100008426081012', '/tmp/')
