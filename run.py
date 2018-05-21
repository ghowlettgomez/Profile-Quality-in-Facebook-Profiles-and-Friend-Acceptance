from fb_module.profile_getter import FB_Profile_Driver
import sys

openreqs = False

openreqstring = sys.argv[1]
if openreqstring == "y" or openreqstring == "Y" or openreqstring == "t" or openreqstring == "T":
    openreqs = True


f = FB_Profile_Driver('cs232facebook@gmail.com', 'Facebook1!')

# sleeptime is a multiplier

def runner(sleeptime,openrequests):
    while True:
        try:
            f.run('https://www.facebook.com/profile.php?id=100008426081012', '/tmp/', sleeptime, openrequests)
            break
        except IndexError as err:
            if sleeptime < 25:
                print("IndexError iter " . sleeptime)
                runner(sleeptime + 1)
            else:
                print("IndexError: {0}".format(err))
        except ValueError as err:
            if sleeptime < 25:
                print("ValueError iter " . sleeptime)
                runner(sleeptime + 1)
            else:
                print("ValueError: {0}".format(err))


runner(1, openreqs)
