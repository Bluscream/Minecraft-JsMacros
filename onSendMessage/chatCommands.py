if __name__ == "": from JsMacrosAC import * #Autocomplete, not necessary

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
    type = GlobalVars.getType(name)
    if type is None:
        Respond(f"{c}4Variable {c}r{name} {c}4does not exist{c}r")
        return
    match type.lower():
        case "int": return GlobalVars.getInt(name)
        case "float": return GlobalVars.getFloat(name)
        case "string": return GlobalVars.getString(name)
        case "boolean": return GlobalVars.getBoolean(name)
        case _: return GlobalVars.getObject(name)

message = copy(event.message)
if message.startswith(prefix):
    event.message = ""
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
                Respond(f"{prefix}exec - Executes a chain of commands (separated by ;). Use /sleep for delays")
                Respond(f"{prefix}os - Executes commands on the OS level")
                Respond(f"{prefix}eval - Executes python code")
                Respond(f"{prefix}get - Get the value of a global variable")
                Respond(f"{prefix}set - Set the value of a global variable")
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
                exit()
            case "players":
                players = World.getPlayers()
                Respond(f"{len(players)} players:")
                for num, player in enumerate(players, start=1):
                    Chat.log(f"#{num:02} {player.getName()} ({player.getUUID()})")
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
                Respond(f"{arg_str}: {var(arg_str)} ({GlobalVars.getType(arg_str)})")
            case "set":
                GlobalVars.putString(args[0], ' '.join(args[1:]))
            case "gamemode"|"gm":
                if len(args) == 0: Respond(f"Current Gamemode: {Player.getGameMode()}")
                else: Chat.say(f".gm {args[0]}")
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
            case _:
                Respond("Unknown command")
    except Exception as e:
        Respond(f"{c}4Error§r: {c}c{e}")
