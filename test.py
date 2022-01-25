if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
logger = Chat.getLogger()
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
logger.info(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "Key"|"Manual":
        def getBlockPos():
            
            pass