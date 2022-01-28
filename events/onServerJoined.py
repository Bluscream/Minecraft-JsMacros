if __name__ == "": from JsMacrosAC import *
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "JoinServer":
        GlobalVars.putBoolean("server_joining", True)
        GlobalVars.putString("server", event.address)

        def sleep(sec: int): Client.waitTick(sec * 20)
        def parsePos(i): return f"{i[0]} {i[1]} {i[2]}" if len(i) > 2 else f"{i[0]} {i[1]}"
        def toggleHacks(hacks: list, state: bool = None):
            if not isinstance(hacks, list): hacks = [ hacks ]
            if state == True: state = " on"
            elif state == False: state = " off"
            elif state == None: state = ""
            for hack in hacks: Chat.say(f".t {hack}{state}")
            

        server = event.address.split("/")
        if len(server) > 1:
            hostname = server[0]
            address = server[1].split(":")

            player_name = Player.getPlayer().getName().getString()
            Chat.log(f"[JsMacros] Joined server {hostname} ({':'.join(address)}) as {player_name}")
            sleep(1)
            players = World.getPlayers()
            player_count = len(players)
            players = [i for i in players if i.getName() != player_name]
            Chat.log(f"[JsMacros] Online Players: \u00A7l{player_count}")
            if player_count > 1:
                from random import choice
                greeting = choice(["Hello, %s", "Hi, %s", "Hey, %s", "Greetings, %s"])
                if player_count > 2: Chat.say(greeting.replace(", %s", ""))
                else: Chat.say(greeting % choice(players).getName())
                
            fabricInstance = Reflection.getClass("net.fabricmc.loader.api.FabricLoader").getInstance()
            meteorLoaded = fabricInstance.isModLoaded("meteor-client")
            wurstLoaded = fabricInstance.isModLoaded("wurst")
            bobbyLoaded = fabricInstance.isModLoaded("bobby")
            
            if bobbyLoaded: Chat.say("#set renderCachedChunks false")
            else: Chat.say("#set renderCachedChunks true")
            
            if meteorLoaded or wurstLoaded:
                toggleHacks("Nuker", False)
                if wurstLoaded: toggleHacks(["SpeedNuker","NukerLegit","AutoMine"], False)

            match hostname.lower():
                case "play.tasmantismc.com":
                    Chat.say("#set censorCoordinates true", True)
                    if GlobalVars.getString("crashed"):
                        Chat.getLogger().warn(f"Was crashed: {GlobalVars.getString('crashed')}")
                        GlobalVars.remove("crashed")
                    else:
                        sleep(5)
                        GlobalVars.putString("homedimension", "overworld")
                        GlobalVars.putString("home", "9067 69 -12399") # (1148 63 -1525) (base:8957 71 -12439) (woodbase:9067 69 -12399)
                        homestr = f"{parsePos(GlobalVars.getString('home').split(' '))} {GlobalVars.getString('homedimension')}"
                        Chat.log(f"Set home to {homestr}")
                        
                        GlobalVars.putString("workdimension", "overworld")
                        GlobalVars.putString("work", "9067 72 -12399")
                        workstr = f"{parsePos(GlobalVars.getString('work').split(' '))} {GlobalVars.getString('workdimension')}"
                        Chat.log(f"Set work to {workstr}")
                        
                        task_day = f"#set allowBreak false;#set allowPlace false;@goto {workstr};@@wait;#set allowBreak true;#set allowPlace true;@get log 1024;@@wait;@@pickup"
                        # GlobalVars.putString("task_day", task_day)
                        Chat.log(f"Set task_day to {task_day}")
                        task_night = f"#set allowBreak false;#set allowPlace true;@test bed;sleep 5;#set allowPlace false;@goto {homestr}"
                        # GlobalVars.putString("task_bed_start", task_night)
                        Chat.log(f"Set task_bed_start to {GlobalVars.getString('task_bed_start')}")
                        # GlobalVars.putString("task_night", task_night)
                        Chat.log(f"Set task_night to {GlobalVars.getString('task_night')}")
                        
                        match player_name:
                            # case "B1uscr34m": GlobalVars.putString("task_now", ".t auto-reconnect on;@get raw_iron 256;@@wait;,quit") # .t auto-reconnect on;@get baked_potato 1;@@wait;.t auto-reconnect off;,disconnect
                            case _: GlobalVars.putString("task_now", "")
                        
                        # JsMacros.runScript("meteor_altoclef.py")
                case "mc.hypixel.net":
                    pass
                case _:
                    Chat.say("#set censorCoordinates false", True)
            GlobalVars.putBoolean("server_joining", False)

    # [21:07:56] [Render thread/INFO]: [CHAT] Set home to 9067 69 -12399 overworld
    # [21:07:56] [Render thread/INFO]: [CHAT] Set work to 9067 72 -12399 overworld
    # [21:07:56] [Render thread/INFO]: [CHAT] Set task_day to #set allowBreak false;#set allowPlace false;@goto 9067 72 -12399 overworld;@@wait;#set allowBreak true;#set allowPlace true;@get log 1024;@@wait;@@pickup
    # [21:07:56] [Render thread/INFO]: [CHAT] Set task_bed_start to #set allowBreak false;#set allowPlace true;@test bed;sleep 5;#set allowPlace false;@goto 9067 69 -12399 overworld
