import dropbox
import time

dbx = dropbox.Dropbox("API-KEY-HERE")
dbx.users_get_current_account()

def lights_on():
    print("on")

def lights_off():
    print("off")

while True:
    for entry in dbx.files_list_folder('/ifttt').entries:
        if "on" in entry.name:
            lights_on()
        elif "off" in entry.name:
            lights_off()
        dbx.files_delete("/ifttt/"+entry.name)
    time.sleep(5)
