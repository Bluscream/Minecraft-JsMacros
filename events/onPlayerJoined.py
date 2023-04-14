
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "PlayerJoin":
        if not GlobalVars.getBoolean("server_joining"):
            player_name = event.player.getName()
            if player_name.strip() and not player_name.startswith("CIT-"):
                builder = Chat.createTextBuilder()\
                    .append("[\u00A7l\u00A7a+\u00A7r] ")\
                    .append(player_name).withColor(7)\
                    .withShowTextHover(Chat.createTextHelperFromString(event.player.getUUID()))
                Chat.log(builder.build())

                hostname = World.getCurrentServerAddress().split("/")[0]
                match hostname.lower():
                    case "play.tasmantismc.com":
                        from random import choice
                        Chat.say(choice(["Hello, %s", "Hi, %s", "Hey, %s", "Greetings, %s"]) % player_name)
                    case "golitron.aternos.me":
                        from random import choice
                        Chat.say(choice(["Hallo, %s", "Hi, %s", "Hey, %s", "Wie gehts, %s?"]) % player_name)
