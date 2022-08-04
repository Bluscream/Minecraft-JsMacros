if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "Key":
        try:
            Baritone = Reflection.getClass("baritone.api.BaritoneAPI").getProvider().getPrimaryBaritone()
            if (GlobalVars.getBoolean("baritone_paused")):
                GlobalVars.putBoolean("baritone_paused", False)
                Baritone.getCommandManager().execute("resume")
            else:
                GlobalVars.putBoolean("baritone_paused", True)
                Baritone.getCommandManager().execute("pause")
        except Exception as e: Chat.log("Baritone not installed: "+str(e))