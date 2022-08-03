
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "Death"|"Key"|"Manual":
        Client.waitTick()
        Chat.log("Death: You died, looser"")