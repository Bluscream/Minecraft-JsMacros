# coding=utf8
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = event.getEventName()
Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "BED_START":
        Chat.toast("Bed Start","Bed Start")
    case "BED_END":
        Chat.toast("Bed End","Bed End")

"""
last = GlobalVars.getBoolean('is_night')
timer = True
while timer:
    is_night = GlobalVars.getBoolean('is_night')
    if (is_night != last):
        last = is_night
        if (is_night): Chat.log("is_night changed to true")
        else: Chat.log("is_night changed to false")
    Client.waitTick(20)
"""