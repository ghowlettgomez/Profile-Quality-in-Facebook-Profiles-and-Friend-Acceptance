from fb_module.profile_getter import FB_Profile_Driver
import sys
import random



f = FB_Profile_Driver('cs232facebook@gmail.com', 'Facebook1!')

# sleeptime is a multiplier

def runner(profile_url, path, sleeptime, type):
    while True:
        try:
            f.run(profile_url, path, sleeptime, type)
            break
        except IndexError as err:
            if sleeptime < 25:
                print("IndexError iter " . sleeptime)
                runner(sleeptime + 1,openreqs)
            else:
                print("IndexError: {0}".format(err))
        except ValueError as err:
            if sleeptime < 25:
                print("ValueError iter " . sleeptime)
                runner(sleeptime + 1,openreqs)
            else:
                print("ValueError: {0}".format(err))


runner('https://www.facebook.com/profile.php?id=100008426081012', '/tmp/', 1, random.randint(0,4))
