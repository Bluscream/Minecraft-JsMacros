# coding=utf8
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = event.getEventName()
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "PlayerJoin":
        if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary

        builder = Chat.createTextBuilder()\
            .append("[\u00A7l\u00A7a+\u00A7r] ")\
            .append(event.player.getName()).withColor(7)\
            .withShowTextHover(Chat.createTextHelperFromString(event.player.getUUID()))
        Chat.log(builder.build())

        hostname = World.getCurrentServerAddress().split("/")[0]
        match hostname.lower():
            case "play.tasmantismc.com":
                pass # Chat.say(choice(["Hello, %s", "Hi, %s", "Hey, %s", "Greetings, %s"]) % event.player.getName())