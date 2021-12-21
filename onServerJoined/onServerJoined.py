if __name__ == "": from JsMacrosAC import *
GlobalVars.putString("server", event.address)

from random import choice


server = event.address.split("/")
hostname = server[0]
address = server[1].split(":")

Chat.say(".t SpeedNuker off")
Chat.say(".t Nuker off")
Chat.say(".t NukerLegit off")
Chat.say(".t AutoMine off")

Chat.log(f"[JsMacros] Joined server {hostname} ({':'.join(address)})")
match hostname.lower():
    case "play.tasmantismc.com":
        GlobalVars.putString("task_night", "@goto 8958 71 -12434")
        Chat.log(f"Set task_night to {GlobalVars.getString('task_night')}")
    case _:
        pass

players = World.getPlayers()
player_count = len(players)
if player_count > 0:
    # get random greeting
    greeting = choice(["Hello, %s", "Hi, %s", "Hey, %s", "Greetings, %s"])
    if player_count == 1: Chat.say(greeting % choice(players).name)
    else: Chat.say(greeting.replace(", %s", ""))



# Chat.toast("onServerJoined", "Server Joined")