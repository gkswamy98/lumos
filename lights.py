import dropbox
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
motor_pin = 4
GPIO.setup(motor_pin, GPIO.OUT)

dbx = dropbox.Dropbox("API-KEY-HERE")
dbx.users_get_current_account()

def lights_on():
    GPIO.output(motor_pin, GPIO.HIGH)
    sleep(5)
    GPIO.output(motor_pin, GPIO.LOW)

def lights_off():
    GPIO.output(motor_pin, GPIO.HIGH)
    sleep(5)
    GPIO.output(motor_pin, GPIO.LOW)

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
