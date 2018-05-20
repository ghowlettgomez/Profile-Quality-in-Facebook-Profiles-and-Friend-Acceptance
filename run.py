from fb_module.profile_getter import FB_Profile_Driver

f = FB_Profile_Driver('cs232facebook@gmail.com', 'Facebook1!')
f.run('https://www.facebook.com/yan.verdeja', '/tmp/screenshot.png')
