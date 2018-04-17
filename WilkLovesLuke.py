import twitter
import time
from random import *

consumersecret1 = "ZLiUZgSKU9u70J5iHuSifmVgFt44FBdJSxAnpfwD6Unt1ipmqk"
consumerkey1 = "ydLcS0vefHo3GF2VcJuCcLiy1"
accesstoken1 = "986081091520954369-9Eg4qoG5xxQuN87zIxxFlQgYI9IJgVq"
accesstokensecret1 = "3OCXgQ0vhfup7UThqsf1gItbFPbMJOWR0jA9KVVBOPlGM"

   

#authenticate I love LUuke
api = twitter.Api(consumer_key=consumerkey1,consumer_secret=consumersecret1,access_token_key=accesstoken1, access_token_secret=accesstokensecret1)
users = api.GetFriends()
counter = 5
while(True):
   rand = randint(1, 40)
   if counter % 5 != 0:
      status = api.PostUpdate('I LOVE LUKE @haus_of_pain15 ' + '!'*rand, media="Wilk.PNG")
   else:
      status = api.PostUpdate('I LOVE LUKE @haus_of_pain15 ' + 'and I LOVE THE STIFFY @WiffieStiffie17'+ '!'*rand, media="Stiffy.jpg")
   time.sleep(300)
   counter+=1



   
   


