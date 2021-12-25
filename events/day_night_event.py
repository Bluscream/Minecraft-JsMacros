if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary

if event.getEventName() == "ProfileLoad":
    if not GlobalVars.getBoolean("day_night_event.py"):
        Chat.log(f"Executing {file.getName()}")
        GlobalVars.putBoolean('day_night_event.py', True)
        def sleep(sec: int): Client.waitTick(sec * 20)

        from math import floor
        def timeOfDayT(tod: int): return tod % 24000 #  round(((tod / 24000) - floor(tod / 24000)) * 24000)

        def task(night: bool = False):
            type = ("task_night" if night else "task_day")
            task = GlobalVars.getString(type)
            if not task: return
            for cmd in task.split(";"):
                if cmd and cmd != "":
                    Chat.log(f"[{type}] Executing {cmd}")
                    if (cmd.startswith("/sleep ")):
                        slp_time = cmd.replace("/sleep ", "")
                        sleep(int(slp_time))
                    else: Chat.say(cmd)


        events = {
            "DAY_START": None,
            "NIGHT_START":None,
            "BED_START":None,
            "BED_END":None
        }

        for event in events:
            events[event] = JsMacros.createCustomEvent(event)
            events[event].registerEvent()

        timer = True
        while timer:
            try:
                todt = timeOfDayT(World.getTimeOfDay())
                wasBedTime = GlobalVars.getBoolean("is_bed_time")
                if 12542 <= todt <= 12600 and not wasBedTime:
                    GlobalVars.putBoolean('is_bed_time', True)
                    events["BED_START"].trigger()
                elif 23460 <= todt <= 23500 and wasBedTime:
                    GlobalVars.putBoolean('is_bed_time', False)
                    events["BED_END"].trigger()
                wasNight = GlobalVars.getBoolean('is_night')
                if todt >= 13000 and not wasNight:
                    GlobalVars.putBoolean('is_night', True)
                    events["NIGHT_START"].trigger()
                    Chat.toast("Good night", "Zzzzz")
                    task(True)
                elif todt < 13000 and wasNight:
                    GlobalVars.putBoolean('is_night', False)
                    events["DAY_START"].trigger()
                    Chat.log("Good morning", "")
                    task(False)
                sleep(1)
            except Exception as e:
                Chat.log(f"Error: {e}")
                sleep(5)
