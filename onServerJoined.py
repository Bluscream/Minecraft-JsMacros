if __name__ == "": from JsMacrosAC import *
Chat.log(f"Executing {file.getName()}")

import sys
from random import choice

if file.getParent() not in sys.path:
    sys.path.append(file.getParent())

server = event.address.split("/")
hostname = server[0]
address = server[1].split(":")

Chat.say(".t SpeedNuker off")
Chat.say(".t Nuker off")
Chat.say(".t NukerLegit off")
Chat.say(".t AutoMine off")

match hostname.lower():
    case "play.tasmantismc.com":
        Chat.log("ANARCHY!")
    case _:
        Chat.log(f"[JsMacros] Joined server {hostname} ({':'.join(address)})")

players = World.getPlayers()
player_count = len(players)
if player_count > 0:
    # get random greeting
    greeting = choice(["Hello, %s", "Hi, %s", "Hey, %s", "Greetings, %s"])
    if player_count == 1: Chat.say(greeting % choice(players).name)
    else: Chat.say(greeting.replace(", %s", ""))



# Chat.toast("onServerJoined", "Server Joined")