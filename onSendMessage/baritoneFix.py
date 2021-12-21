if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary

broken_prefix = "<<70e4ada0-c1d8-40a2-8df1-e249cf125202>>"
message = event.text.getString()
if broken_prefix in message:
    command = message.split(broken_prefix)[1]
    cmd = command.split(" ")
    args = cmd[1:]
    cmd = cmd[0].lower()
    match cmd:
        case "wp"|"waypoint":
            match args[0]:
                case "delete":
                    Chat.say(".clear")
                    Chat.say(f"#{command}")
                    Chat.say("#wp list")
                case _:
                    Chat.say(".clear")
                    Chat.say(f"#{command}")
        case _:
            Chat.say(f"#{command}")
