if __name__ == "": from JsMacrosAC import * #Autocomplete, not necessary
Chat.log(f"Executing {file.getName()}")

Chat.log(str(event.getEventName()))

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