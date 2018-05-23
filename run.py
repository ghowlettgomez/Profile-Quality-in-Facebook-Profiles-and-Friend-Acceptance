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
            if sleeptime < 5:
                print("IndexError iter " + str(sleeptime))
                runner(profile_url,path,sleeptime + 1,type)
            else:
                print("IndexError: {0}" + format(err))
        except ValueError as err:
            if sleeptime < 5:
                print("ValueError iter " + str(sleeptime))
                runner(profile_url,path,sleeptime + 1,type)
            else:
                print("ValueError: {0}" + format(err))


runner('https://www.facebook.com/profile.php?id=100008426081012', '/tmp/', 1, random.randint(0,4))
