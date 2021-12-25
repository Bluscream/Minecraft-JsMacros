# coding=utf8
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = event.getEventName()
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case _:
        def sleep(sec: int): Client.waitTick(sec * 20)
        sleep(2)

        cheat = True

        # sJsMacros.runScript("workDirFix.py")
        import json
        altoclef_settings_file = r"S:\multimc\instances\Fabric 1.18.1\minecraft\altoclef_settings.json"
        f = open(altoclef_settings_file, "r")
        ac = json.load(f)
        f.close()

        ac["bluscream"] = True

        ac["speedHack"] = 1.5 if cheat else 0.0

        Chat.say(".enabledhax load-profile blu")

        Chat.say(".t multiaura on")
        Chat.say(".t criticals on")
        Chat.say(".t autoarmor on")
        Chat.say(".t fullbright on")
        Chat.say(".t AutoLeave off")
        # Chat.say(f'.t nofall {"on" if cheat else "off"}')
        # if not cheat: Chat.toast(f"Cheat is off!", "!!! NOFALL DISABLED !!!")
        Chat.say(".t creativeflight on")

        Chat.say("#set antiCheatCompatibility false")
        Chat.say(f"#set allowOnlyExposedOres {not cheat}")
        Chat.say("#set allowBreak true")
        Chat.say("#set allowPlace true")
        Chat.say("#set disconnectOnArrival false")
        Chat.say("#set freeLook false")
        Chat.say(f"#set legitMine {not cheat}")
        Chat.say(f"#set legitMineIncludeDiagonals {not cheat}")

        Chat.say(".t autorespawn on")
        ac["autoRespawn"] = False

        Chat.say(".t autoreconnect on")
        ac["autoReconnect"] = False

        Chat.say(".t autoeat on")
        ac["autoEat"] = True

        Chat.say(".t autosprint off")
        Chat.say("#set allowSprint true")
        Chat.say("#set sprintInWater true")

        Chat.say(".t autotool off")
        Chat.say(".setcheckbox autotool switch_back off")
        Chat.say(".t autosword off")
        Chat.say("#set disableAutoTool false")
        Chat.say("#set assumeExternalAutoTool false")

        Chat.say(".t safewalk off")
        Chat.say("#set assumeSafeWalk false")

        # Chat.say(".t step on")
        # Chat.say(".setmode step mode simple")
        # Chat.say(".setslider step height 1")
        # Chat.say("#set assumeStep true")

        Chat.say(".t jesus on")
        Chat.say("#set assumeWalkOnLava true")
        Chat.say("#set assumeWalkOnWater true")

        home = GlobalVars.getString("home")
        if home: ac["homeBasePosition"] = home.replace(" ", ",")

        with open(altoclef_settings_file, "w") as f:
            json.dump(ac, f, indent=4)
        JsMacros.runScript("workDirFix.py")
        Chat.say("@reload_settings")

