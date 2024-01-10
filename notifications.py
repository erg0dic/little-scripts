import os
import time

# print "get off your ass" every 20 minutes
def eye_rest_notification():
    while True:
        os.system("notify-send 'Its been 20 min. Look away for 20 seconds.'")
        time.sleep(20*60) # sleep for 20*60 seconds


if __name__ == '__main__':
    eye_rest_notification()
