
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "Key":
        screen = Hud.getOpenScreen()
        Chat.toast(f"{Hud.getOpenScreenName()}","")
        for button in screen.getButtonWidgets():
            Chat.getLogger().warn(f"{button.getText()}","")