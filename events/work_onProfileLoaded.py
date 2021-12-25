# coding=utf8
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = event.getEventName()
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "ProfileLoad":
        Client.waitTick()
        Chat.toast("EventProfileLoad", event.profileName)
        # Client.connect("play.tasmantismc.com")