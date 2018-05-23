# Profile-Quality-in-Facebook-Profiles-and-Friend-Acceptance
Flask app used for the Evaluating Contact Requests study for UChicago's Usable Security Spring 2018 class. This app is made to be run on an apache server based upon the instructions given in [this link](https://www.datasciencebytes.com/bytes/2015/02/24/running-a-flask-app-on-aws-ec2/). It has four end points: 

1. /get_profile takes in a link to a facebook profile, gets the selenium webdriver running in the background to make the little and big screen, and returns the type of big screenshot to be returned plus the unique id for this participant.

2. /get_little gets the little screenshot of the friend request which is just a photo of the request itself. It takes in the unique id from /get_profile

3. /get_big gets the big screenshot of the friend request which is a photo the altered friend profile itself. It takes in the unique id from /get_profile

4. /delete_screenshots deletes the screenshots produced by /get_profile

There are five types of big screenshots that we take: 
  1. a completely full profile
  2. a profile without a timeline
  3. a profile with the intro section deleted
  4. a profile with only a cover photo, profile picture, and a name
  5. one with only a name.
