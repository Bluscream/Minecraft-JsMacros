# coding=utf8
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary

from re import search

regex = r"<<\w{8}-\w{4}-\w{4}-\w{4}-\w{12}>>"

message = event.text.getString()
if search(regex, message):
    command = message.split(">>")[1]
    cmd = command.split(" ")
    args = cmd[1:]
    cmd = cmd[0].lower()
    Chat.say(".clear")
    match cmd:
        case "wp"|"waypoint":
            match args[0]:
                case "delete":
                    Chat.say(f"#{command}")
                    Chat.say("#wp list")
                case _:
                    Chat.say(f"#{command}")
        case _:
            Chat.say(f"#{command}")