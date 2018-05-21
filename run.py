from fb_module.profile_getter import FB_Profile_Driver

f = FB_Profile_Driver('cs232facebook@gmail.com', 'Facebook1!')

# sleeptime is a multiplier

def runner(sleeptime):
    while True:
        try:
            f.run('https://www.facebook.com/profile.php?id=100008426081012', '/tmp/', sleeptime)
            break
        except IndexError as err:
            if sleeptime < 25:
                print("IndexError iter " . sleeptime)
                runner(sleeptime + 1)
            else:
                print("IndexError: {0}".format(err))



runner(1)
