if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "PlayerPositionChanged"|"Key"|"Manual":
        if __name__ == "": event: EventCustom
        x,y,z = (event.getInt("x"),event.getInt("y"),event.getInt("z"))
        if (x == -573 and y == -25 and z in range(-46, -49)): # X: -572.3 Y: -25.0 Z: -48.45
            Chat.log("You found the monster farm!")
            # Chat.log(Client.getGameOptions().getVolumes())
            Client.getGameOptions().setVolume("hostile", .1)
