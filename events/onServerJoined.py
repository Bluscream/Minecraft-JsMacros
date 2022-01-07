# coding=utf8
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = event.getEventName()
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "JoinServer":
        GlobalVars.putBoolean("server_joining", True)
        GlobalVars.putString("server", event.address)

        def sleep(sec: int): Client.waitTick(sec * 20)
        def task(task: str):
            if not task: return
            for cmd in task.split(";"):
                if cmd and cmd != "":
                    Chat.log(f"[{type}] Executing {cmd}")
                    if (cmd.startswith("/sleep ")):
                        slp_time = cmd.replace("/sleep ", "")
                        sleep(int(slp_time))
                    else: Chat.say(cmd)

        server = event.address.split("/")
        hostname = server[0]
        address = server[1].split(":")

        Chat.log(f"[JsMacros] Joined server {hostname} ({':'.join(address)})")
        sleep(1)
        players = World.getPlayers()
        player_count = len(players)
        Chat.log(f"[JsMacros] Online Players: \u00A7l{player_count}")
        if player_count > 1:
            from random import choice
            greeting = choice(["Hello, %s", "Hi, %s", "Hey, %s", "Greetings, %s"])
            if player_count > 2: Chat.say(greeting.replace(", %s", ""))
            else: Chat.say(greeting % choice(players).getName())

        Chat.say(".t SpeedNuker off")
        Chat.say(".t Nuker off")
        Chat.say(".t NukerLegit off")
        Chat.say(".t AutoMine off")
        Chat.say("#set renderCachedChunks false")

        match hostname.lower():
            case "play.tasmantismc.com":
                GlobalVars.putString("home", "9191 63 -12202") # 8958 -12434
                JsMacros.runScript("wurst_altoclef.py")
                Chat.say("#set censorCoordinates true")
                if GlobalVars.getString("crashed"):
                    Chat.getLogger().warn(f"Was crashed: {GlobalVars.getString('crashed')}")
                    GlobalVars.remove("crashed")
                else:
                    # Chat.say("@gamer") #
                    GlobalVars.putString("task_bed_start", "@stop;#set disconnectOnArrival false;@test bed") # f"#set allowBreak false;#set allowPlace false;@goto {GlobalVars.getString('home')}"
                    Chat.log(f"Set task_bed_start to {GlobalVars.getString('task_bed_start')}")
                    GlobalVars.putString("task_day", "@stop;#set allowBreak true;#set allowPlace true;@test stacked")
                    Chat.log(f"Set task_day to {GlobalVars.getString('task_day')}")
                    # sleep(10)
                    # if GlobalVars.getBoolean('is_night'): task(GlobalVars.getString('task_night'))
                    # else:
                    # task(GlobalVars.getString('task_day'))
                pass
            case _:
                pass



        # Chat.toast("onServerJoined", "Server Joined")
        GlobalVars.putBoolean("server_joining", False)