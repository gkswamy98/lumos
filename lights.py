import dropbox
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

dbx = dropbox.Dropbox("API-KEY-HERE")
dbx.users_get_current_account()

def lights_on():
    GPIO.output(4, GPIO.HIGH)
    sleep(5)
    GPIO.output(4, GPIO.LOW)

def lights_off():
    GPIO.output(4, GPIO.HIGH)
    sleep(5)
    GPIO.output(4, GPIO.LOW)

while True:
    try:
        for entry in dbx.files_list_folder('/ifttt').entries:
            if "on" in entry.name:
                lights_on()
            elif "off" in entry.name:
                lights_off()
            dbx.files_delete("/ifttt/"+entry.name)
        sleep(5)
    except:
        print("error, trying again")
