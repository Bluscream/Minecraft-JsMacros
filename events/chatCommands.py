
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "SendMessage":
        import platform
        from sys import exit
        from os import name as os_name
        from subprocess import check_call, Popen, PIPE
        from copy import copy

        prefix = ","
        c = "\u00A7"

        def Respond(msg: str, log: bool = False):
            Chat.log(f"[{c}2JsMacros{c}r] {msg}")
            if log: Chat.getLogger().info(f"[JsMacros] {msg}")

        def sleep(sec: int):
            for i in range(sec * 20):
                Client.waitTick()

        def copy2clip(txt):
            if os_name == 'nt': return
            return check_call('echo '+txt.strip()+'|clip', shell=True)

        def var(name: str):
            type_ = GlobalVars.getType(name)
            if type_ is str:
                match type_.lower():
                    case "int": return GlobalVars.getInt(name)
                    case "float": return GlobalVars.getFloat(name)
                    case "string": return GlobalVars.getString(name)
                    case "boolean": return GlobalVars.getBoolean(name)
                    case None: return None
                    case _: return GlobalVars.getObject(name)
            return None

        message = copy(event.message)
        if message.startswith(prefix):
            event.message = ""
            history = Chat.getHistory()
            history.getSent().add(message)
            # history.insertRecvText(message)
            # history.refreshVisible()

            Chat.log(f"> {message}")
            try:
                copy2clip(message)
                command = message[1:].split(" ")
                cmd = command[0]
                args = command[1:]
                GlobalVars.putString('last_command', ' '.join(command))
                arg_str = ' '.join(args)
                match cmd.lower():
                    case "help":
                        Respond(f"Commands:")
                        Respond(f"{prefix}help - Shows this message")
                        Respond(f"{prefix}about - Shows info about the script")
                        Respond(f"{prefix}rejoin - Rejoins the current server")
                        Respond(f"{prefix}disconnect - Disconnects from the current server")
                        Respond(f"{prefix}exit|quit - Closes the client")
                        Respond(f"{prefix}players - Lists all players on the server")
                        Respond(f"{prefix}coords - Converts overworld coords to nether and vice versa")
                        Respond(f"{prefix}exec - Executes a chain of commands (separated by ;). Use /sleep for delays")
                        Respond(f"{prefix}os - Executes commands on the OS level")
                        Respond(f"{prefix}eval - Executes python code")
                        Respond(f"{prefix}echo|print - duh")
                        Respond(f"{prefix}get - Get the value of a global variable")
                        Respond(f"{prefix}set - Set the value of a global variable")
                        Respond(f"{prefix}gamemode|gm - Gets or sets gamemode")
                        # Respond(f"{prefix}screen|gui|ui - Opens")
                        Respond(f"{prefix}fps - Gets client frames per second")
                        Respond(f"{prefix}tps - Gets server ticks per second")
                        Respond(f"{prefix}baritone|bt|altoclef|ac")
                        Respond(f"{prefix}gohome|home|night")
                        Respond(f"{prefix}dotask|task|day")
                        Respond(f"{prefix}cleartasks|ct")
                    case "about":
                        Respond(f"""JsMacros:
            OS: {platform.system()} {platform.release()}
            Python: {platform.python_version()}
            Minecraft: {Client.mcVersion()}
                        """)
                    case "rejoin":
                        server = World.getCurrentServerAddress().split("/")[1]
                        Respond(f"Reconnecting to {server}...")
                        Client.disconnect()
                        Client.waitTick(5000)
                        address = server.split(":")
                        Client.connect(address[0], int(address[1]))
                    case "disconnect":
                        Client.disconnect()
                    case "quit" | "exit":
                        Client.shutdown() # exit()
                    case "players":
                        players = World.getPlayers()
                        Respond(f"{len(players)} players:")
                        for num, player in enumerate(players, start=1):
                            Chat.log(f"#{num:02} {player.getName()} ({player.getUUID()})")
                    case "coords":
                        dim = World.getDimension().split(":")[-1]
                        pos = Player.getPlayer().getPos()
                        if len(args) == 4: dim = args[3]
                        if len(args) > 2: pos.x = float(args[0]); pos.y = float(args[1]); pos.z = float(args[2])
                        elif len(args) == 2: pos.x = float(args[0]);pos.y = 0; pos.z = float(args[1])
                        pos.x = round(pos.x, 2); pos.y = round(pos.y, 2); pos.z = round(pos.z, 2)
                        match dim:
                            case "nether":
                                Respond(f"[{c}5Nether{c}r] X: {pos.x} Y: {pos.y} Z: {pos.z}")
                                Respond(f"[Overworld] X: {pos.x*8} Y: {pos.y} Z: {pos.z*8}")
                            case _:
                                Respond(f"[Overworld] X: {pos.x} Y: {pos.y} Z: {pos.z}")
                                Respond(f"[{c}5Nether{c}r] X: {pos.x/8} Y: {pos.y} Z: {pos.z/8}")
                    case "exec":
                        for command in arg_str.split(";"):
                            Respond(f"Executing {command}")
                            if (command.startswith("/sleep ")):
                                slp_time = command.replace("/sleep ", "")
                                sleep(int(slp_time))
                            else: Chat.say(command)
                    case "os":
                        Respond(f"Executing {' '.join(args)}")
                        Respond(Popen(args, stdout=PIPE).stdout.read().decode('utf-8'))
                    case "eval":
                        Respond(f"Evaluating {arg_str}")
                        Chat.say(eval(arg_str))
                    case "echo" | "print":
                        Respond(f"{arg_str}")
                    case "get":
                        var_ = var(arg_str)
                        if var_ is not None: Respond(f"{arg_str}: {var_} ({GlobalVars.getType(arg_str)})")
                        else: Respond(f"{c}4Variable {c}r{arg_str} {c}4does not exist{c}r")
                    case "set":
                        old = var(args[0])
                        GlobalVars.putString(args[0], ' '.join(args[1:]))
                        Respond(f"{args[0]}: {old} -> {var(args[0])}")
                    case "gamemode"|"gm":
                        if len(args) == 0: Respond(f"Current Gamemode: {Player.getGameMode()}")
                        else:
                            if args[0] == "0" or args[0].lower() == "s": args[0] = "survival"
                            elif args[0] == "1" or args[0].lower() == "c": args[0] = "creative"
                            elif args[0] == "2" or args[0].lower() == "ss": args[0] = "spectator"
                            elif args[0] == "3" or args[0].lower() == "a": args[0] = "adventure"
                            Chat.say(f"/gamemode {args[0]}")
                    case "screen"|"gui"|"ui":
                        Hud.openScreen(arg_str)
                    case "fps": Respond(f"FPS: {Client.getFPS()}")
                    case "tps": Respond(f"TPS: {World.getServerTPS()}")
                    case "time":
                        Respond(f"getTime: {World.getTime()}")
                        tod = World.getTimeOfDay()
                        Respond(f"getTimeOfDay: {tod}")
                        from math import floor
                        Respond(f"getDayTimeT: {round(((tod / 24000) - floor(tod / 24000)) * 24000)}")
                        Respond(f"is_night: {GlobalVars.getBoolean('is_night')}")
                        Respond(f"task_night: {GlobalVars.getString('task_night')}")
                        Respond(f"task_day: {GlobalVars.getString('task_day')}")
                    case "baritone"|"bt"|"altoclef"|"ac":
                        Respond(f"last_baritone_task: {GlobalVars.getString('last_baritone_task')}")
                        Respond(f"last_altoclef_task: {GlobalVars.getString('last_altoclef_task')}")
                    case "gohome"|"home"|"night":
                        if len(args) > 0: GlobalVars.putString("task_night", ' '.join(args))
                        else: GlobalVars.putString("task_now", GlobalVars.getString('task_night'))
                    case "dotask"|"day":
                        if len(args) > 0: GlobalVars.putString("task_day", ' '.join(args))
                        else: GlobalVars.putString("task_now", GlobalVars.getString('task_day'))
                    case "task":
                        if len(args) > 0: GlobalVars.putString("task_now", ' '.join(args))
                        else: Chat.log(GlobalVars.getString('task_now'))
                    case "repeat":
                        times = int(args.pop(0))
                        Chat.log(f"Repeating task {times} times")
                        Chat.log(' '.join(args))
                        GlobalVars.putString("task_now", ' '.join(args) * times)
                    case "cleartasks"|"ct":
                        for t in ["task_now","task_day","task_night","task_now","task_bed_start","task_bed_end","task_monster_spawn_start","task_monster_spawn_end"]: GlobalVars.remove(t)
                        Respond("Cleared tasks")
                    case _:
                        Respond("Unknown command")
            except Exception as e:
                Respond(f"{c}4Error§r: {c}c{e}")
