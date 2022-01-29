if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
player = Player.getPlayer()
x = int(player.getX())
y = int(player.getY())
z = int(player.getZ())
Chat.log(f"Player position changed: {[x,y,z]}")