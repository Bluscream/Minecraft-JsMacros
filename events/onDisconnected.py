
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "Disconnect"|"Key"|"Manual":
        Client.waitTick()
        server = ""
        if (GlobalVars.getString("server")): server = GlobalVars.getString("server").split("/")[0]
        Chat.toast("Disconnected", server)