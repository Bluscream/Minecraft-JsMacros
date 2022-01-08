
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = event.getEventName()
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "Disconnect":
        server = ""
        if (GlobalVars.getString("server")):
            server = GlobalVars.getString("server").split("/")[0]

        Chat.toast("Disconnected", server)