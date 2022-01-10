if __name__ == "": from JsMacrosAC import *
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "JoinServer":
        GlobalVars.putBoolean("server_joining", True)
        GlobalVars.putString("server", event.address)

        def sleep(sec: int): Client.waitTick(sec * 20)

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

        Chat.say(".t SpeedNuker off", True)
        Chat.say(".t Nuker off", True)
        Chat.say(".t NukerLegit off", True)
        Chat.say(".t AutoMine off", True)
        Chat.say("#set renderCachedChunks false", True)

        match hostname.lower():
            case "play.tasmantismc.com":
                GlobalVars.putString("homedimension", "overworld")
                GlobalVars.putString("home", "8957 71 -12439") # 1148 63 -1525
                Chat.log(f"Set home to {GlobalVars.getString('home')} {GlobalVars.getString('homedimension')}")
                JsMacros.runScript("wurst_altoclef.py")
                Chat.say("#set censorCoordinates true", True)
                if GlobalVars.getString("crashed"):
                    Chat.getLogger().warn(f"Was crashed: {GlobalVars.getString('crashed')}")
                    GlobalVars.remove("crashed")
                else:
                    sleep(5)
                    GlobalVars.putString("task_day", f"#set allowBreak false;#set allowPlace false;@goto 9068 -12401 overworld;wait;#set allowBreak true;#set allowPlace true;@get log 2000")
                    Chat.log(f"Set task_day to {GlobalVars.getString('task_day')}")
                    homestr = GlobalVars.getString('home').split(" ")
                    homestr = f"{homestr[0]} {homestr[2]} {GlobalVars.getString('homedimension')}"
                    # GlobalVars.putString("task_bed_start", 
                    # Chat.log(f"Set task_bed_start to {GlobalVars.getString('task_bed_start')}")
                    # GlobalVars.putString("task_night", f"#set allowBreak false;#set allowPlace true;@test bed;wait;#set allowPlace false;@goto {homestr}")
                    GlobalVars.putString("task_night", f"#set allowBreak false;#set allowPlace false;@goto {homestr}")
                    Chat.log(f"Set task_night to {GlobalVars.getString('task_night')}")
                    # GlobalVars.putString("task_now", GlobalVars.getString('task_day'))
                pass
            case _:
                pass # @get logs 512;@wait;@test bed
        GlobalVars.putBoolean("server_joining", False)
