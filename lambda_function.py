import pyotp
import datetime
import time

def lambda_handler(event, context):
    
    test = pyotp.TOTP('base32secret3232')
    print(test.now())
    print(int(time.mktime(datetime.datetime.now().timetuple())%30))
