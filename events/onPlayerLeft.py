
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "PlayerLeave":

        builder = Chat.createTextBuilder()\
            .append("[\u00A7l\u00A7c-\u00A7r] \u00A77")\
            .append(event.player.getName())\
            .withShowTextHover(Chat.createTextHelperFromString(event.player.getUUID()))
        Chat.log(builder.build())

        hostname = World.getCurrentServerAddress().split("/")[0]
        match hostname.lower():
            case "play.tasmantismc.com":
                from random import choice
                Chat.say(choice(["Ciao, %s", "Bye, %s", "Tschüss, %s", "gtfo, %s"]) % event.player.getName())