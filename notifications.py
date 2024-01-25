import os
import time
import sys
import logging

logging.basicConfig(level=logging.INFO)

def eye_rest_notification(mins=20):
    # print "rest" every `min` minutes
    message = "Its been 20 min. Look away for 20 seconds."
    if 'linux' in sys.platform: 
        logging.info('booting up in linux 😊/💀')
        while True:
            os.system(f"notify-send '{message}'")
            time.sleep(mins*60) # sleep for 20*60 seconds
    elif 'win' in sys.platform:
        try:
            import win10toast
        except ModuleNotFoundError as e:
            logging.info("Attempting to install win10toast using pip.")
            os.system("pip install win10toast")
        # try a second time
        try:
            import win10toast
        except ModuleNotFoundError as e:
            logging.error("Failed to install win10toast. If this fails, just do it manually using privileged pip.")
            raise e
        logging.info('booting up in linux 😊/💀')
        toaster = win10toast.ToastNotifier()
        while True:
            toaster.show_toast(title="Rest Notification", msg=message, duration=5)
            time.sleep(mins*60) # sleep for mins*60 seconds
    else:
        raise NotImplementedError(f"App doesn't support {sys.platform}.")

if __name__ == '__main__':
    eye_rest_notification()
