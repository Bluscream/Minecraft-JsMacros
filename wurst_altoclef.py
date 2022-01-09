if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
def sleep(sec: int): Client.waitTick(sec * 20)
sleep(2)

cheat = True
speed = 0

# sJsMacros.runScript("workDirFix.py")
import json
altoclef_settings_file = r'G:\OneDrive\Games\Minecraft\altoclef_settings.json'
f = open(altoclef_settings_file, "r")
ac = json.load(f)
f.close()

ac["bluscream"] = True
Chat.say(".enabledhax load-profile altoclef", true)

ac["speedHack"] = speed
if speed:
    Chat.say(f".setslider timer speed {speed}")
    Chat.say(".t timer on", true)
else: Chat.say(".t timer off", true)

Chat.say(".t autofarm on", true)
Chat.say(".t multiaura on", true)
Chat.say(".t snowshoe off", true)

Chat.say(".setslider nuker range 2.1", true)
Chat.say(".setmode nuker mode multiid", true)
Chat.say(".t nuker on", true)

Chat.say(".setcheckbox autoeat eat_while_walking on", true)
Chat.say(".t autoeat on", true)
Chat.say(".t criticals on", true)
Chat.say(".t autoarmor on", true)
Chat.say(".t fullbright on", true)
Chat.say(".t AutoLeave off", true)
# Chat.say(f'.t nofall {"on" if cheat else "off"}')
# if not cheat: Chat.toast(f"Cheat is off!", "!!! NOFALL DISABLED !!!")
Chat.say(".t creativeflight on", true)

Chat.say("#set antiCheatCompatibility false", true)
Chat.say(f"#set allowOnlyExposedOres {not cheat}")
Chat.say("#set allowBreak true", true)
Chat.say("#set allowPlace true", true)
Chat.say("#set disconnectOnArrival false", true)
Chat.say("#set freeLook false", true)
Chat.say(f"#set legitMine {not cheat}")
Chat.say(f"#set legitMineIncludeDiagonals {not cheat}")

Chat.say(".t autorespawn on", true)
ac["autoRespawn"] = False

Chat.say(".t autoreconnect on", true)
ac["autoReconnect"] = False

Chat.say(".t autoeat on", true)
ac["autoEat"] = True

Chat.say(".t autosprint off", true)
Chat.say("#set allowSprint true", true)
Chat.say("#set sprintInWater true", true)

Chat.say(".t autotool on", true)
Chat.say(".setcheckbox autotool switch_back off", true)
Chat.say(".t autosword on", true)
Chat.say("#set disableAutoTool false", true)
Chat.say("#set assumeExternalAutoTool false", true)

Chat.say(".t safewalk off", true)
Chat.say("#set assumeSafeWalk false", true)

# Chat.say(".t step on", true)
# Chat.say(".setmode step mode simple", true)
# Chat.say(".setslider step height 1", true)
# Chat.say("#set assumeStep true", true)

Chat.say(".t jesus on", true)
Chat.say("#set assumeWalkOnLava true", true)
Chat.say("#set assumeWalkOnWater true", true)
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
JsMacros.runScript("workDirFix.py") # Chat.say("@reload_settings", true)
