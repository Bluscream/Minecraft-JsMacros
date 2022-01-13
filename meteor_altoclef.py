if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
def sleep(sec: int): Client.waitTick(sec * 20)
sleep(2)

fabricInstance = Java.type("net.fabricmc.loader.api.FabricLoader").getInstance()
meteorLoaded = fabricInstance.isModLoaded("meteor-client")
wurstLoaded = fabricInstance.isModLoaded("wurst")

cheat = True
speed = 0

# sJsMacros.runScript("workDirFix.py")
import json
altoclef_settings_file = r'G:\OneDrive\Games\Minecraft\altoclef_settings.json'
f = open(altoclef_settings_file, "r")
ac = json.load(f)
f.close()

ac["bluscream"] = True
Chat.say(".profiles altoclef load", True)

ac["speedHack"] = speed
if speed:
    # Chat.say(f".setslider timer speed {speed}")
    Chat.say(".t timer on", True)
else: Chat.say(".t timer off", True)

Chat.say(".t kill-aura on", True)

# Chat.say(".setslider nuker range 2.1", True)
# Chat.say(".setmode nuker mode multiid", True)
# Chat.say(".t nuker on", True)

Chat.say(".setcheckbox autoeat eat_while_walking on", True)
Chat.say(".t auto-eat on", True)
Chat.say(".t criticals on", True)
Chat.say(".t auto-armor on", True)
Chat.say(".t fullbright on", True)
# Chat.say(".t auto-log on", True)
Chat.say(f'.t no-fall {"on" if cheat else "off"}')
# if not cheat: Chat.toast(f"Cheat is off!", "!!! NOFALL DISABLED !!!")

Chat.say("#set antiCheatCompatibility false", True)
Chat.say(f"#set allowOnlyExposedOres {not cheat}")
Chat.say("#set allowBreak true", True)
Chat.say("#set allowPlace true", True)
Chat.say("#set disconnectOnArrival false", True)
Chat.say("#set freeLook false", True)
Chat.say(f"#set legitMine {not cheat}")
Chat.say(f"#set legitMineIncludeDiagonals {not cheat}")

Chat.say(".t auto-respawn on", True)
ac["autoRespawn"] = False

Chat.say(".t auto-reconnect on", True)
ac["autoReconnect"] = False

Chat.say(".t auto-eat on", True)
ac["autoEat"] = True

Chat.say(".t sprint off", True)
Chat.say("#set allowSprint true", True)
Chat.say("#set sprintInWater true", True)

Chat.say(".t auto-weapon on", True)
Chat.say(".t auto-tool on", True)
# Chat.say(".setcheckbox autotool switch_back off", True)
Chat.say("#set disableAutoTool true", True)
Chat.say("#set assumeExternalAutoTool false", True)

Chat.say(".t safe-walk off", True)
Chat.say("#set assumeSafeWalk false", True)

# Chat.say(".t step on", True)
# Chat.say(".setmode step mode simple", True)
# Chat.say(".setslider step height 1", True)
# Chat.say("#set assumeStep true", True)

Chat.say(".t jesus on", True)
Chat.say("#set assumeWalkOnLava true", True)
Chat.say("#set assumeWalkOnWater true", True)
radius = 17
ac["areasToProtect"] = [{"start": f"-{radius}, 0, -{radius}", "end": f"{radius}, 255, {radius}"}]
Chat.log(f"Altoclef protection area set to {radius} blocks around spawn.")
home = GlobalVars.getString("home")
if home:
    # Chat.log("Home is set to " + home)
    ac["homeBasePosition"] = home.replace(" ", ",")
    radius = 50
    home = [int(x) for x in home.split(" ")]
    ac["areasToProtect"].append({"start": f"{home[0]-radius}, 0, {home[2]-radius}","end": f"{home[0]+radius}, 255, {home[2]+radius}"})
    Chat.log(f"Altoclef protection area set to {radius} blocks around home.")

with open(altoclef_settings_file, "w") as f:
    json.dump(ac, f, indent=4)
Client.waitTick()
JsMacros.runScript("workDirFix.py") # Chat.say("@reload_settings", True)
