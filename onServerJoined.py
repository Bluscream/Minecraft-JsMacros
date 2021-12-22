from datetime import datetime

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
        JsMacros.runScript("wurst_altoclef.py")
        Chat.say("#set censorCoordinates true")
        Chat.say("#set renderCachedChunks true")
        if GlobalVars.getString("crashed"):
            Chat.getLogger().warn(f"Was crashed: {GlobalVars.getString('crashed')}")
            GlobalVars.remove("crashed")
        else:
            # Chat.say("@gamer")
            GlobalVars.putString("task_night", "#set allowBreak false;#set allowPlace false;#set disconnectOnArrival false;@goto 8958 71 -12434")
            Chat.log(f"Set task_night to {GlobalVars.getString('task_night')}")
            GlobalVars.putString("task_day", "#set allowBreak true;#set allowPlace true")
            Chat.log(f"Set task_day to {GlobalVars.getString('task_day')}")
        pass
    case _:
        pass

def sleep(sec: int): Client.waitTick(sec * 20)
sleep(1)
players = World.getPlayers()
player_count = len(players)
Chat.log(f"Online Players: \u00A7l{player_count}")
if player_count > 1:
    greeting = choice(["Hello, %s", "Hi, %s", "Hey, %s", "Greetings, %s"])
    if player_count > 2: Chat.say(greeting.replace(", %s", ""))
    else: Chat.say(greeting % choice(players).getName())



# Chat.toast("onServerJoined", "Server Joined")