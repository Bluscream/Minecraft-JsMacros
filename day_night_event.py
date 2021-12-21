if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
Chat.log(f"Executing {file.getName()}")
from math import floor


def sleep(sec: int): Client.waitTick(sec * 20)

def timeOfDayT(tod: int): return round(((tod / 24000) - floor(tod / 24000)) * 24000)

def task(night: bool = False):
    type = ("task_night" if night else "task_day")
    task = GlobalVars.getString(type)
    if not task: return
    for cmd in task.split(";"):
        Chat.log(f"[{type}] Executing {cmd}")
        if (cmd.startswith("/sleep ")):
            slp_time = cmd.replace("/sleep ", "")
            sleep(int(slp_time))
        else: Chat.say(cmd)

# profile = JsMacros.getProfile()
# profile.getRegistry().addEvent("DAY_START")
# profile.getRegistry().addEvent("NIGHT_START")

wasNight = False
timer = True
while timer:
    try:
        todt = timeOfDayT(World.getTimeOfDay())
        if todt >= 13000 and not wasNight:
            wasNight = True
            GlobalVars.putBoolean('is_night', True)
            # profile.triggerEvent("NIGHT_START")
            Chat.toast("Good night", "Zzzzz")
            task(wasNight)
            sleep(5)
        elif todt < 13000 and wasNight:
            wasNight = False
            GlobalVars.putBoolean('is_night', False)
            # profile.triggerEvent("DAY_START")
            Chat.log("Good morning", "")
            task(wasNight)
            sleep(5)
        sleep(1)
    except Exception as e:
        Chat.log(f"Error: {e}")
        sleep(5)
