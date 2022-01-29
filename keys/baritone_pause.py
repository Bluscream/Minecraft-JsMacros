if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "Key":
        if (GlobalVars.getBoolean("baritone_paused")):
            Chat.say("#resume")
            GlobalVars.putBoolean("baritone_paused", False)
        else:
            Chat.say("#pause")
            GlobalVars.putBoolean("baritone_paused", True)