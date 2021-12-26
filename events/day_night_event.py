# coding=utf8
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = event.getEventName()
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "ProfileLoad":
        if not GlobalVars.getBoolean("day_night_event.py"):
            Chat.log(f"Executing {file.getName()}")
            GlobalVars.putBoolean('day_night_event.py', True)
            def sleep(sec: int): Client.waitTick(sec * 20)

            from math import floor
            def timeOfDayT(tod: int): return tod % 24000 #  round(((tod / 24000) - floor(tod / 24000)) * 24000)

            def task(task: str):
                _task = GlobalVars.getString(task)
                if not _task: return
                for cmd in _task.split(";"):
                    if cmd and cmd != "":
                        Chat.log(f"[{_task}] Executing {cmd}")
                        if (cmd.startswith("/sleep ")):
                            slp_time = cmd.replace("/sleep ", "")
                            sleep(int(slp_time))
                        else: Chat.say(cmd)


            events = {
                "DAY_START": None,
                "NIGHT_START":None,
                "BED_START":None,
                "BED_END":None,
                "MONSTER_SPAWN_START":None,
                "MONSTER_SPAWN_END":None
            }

            for event in events:
                events[event] = JsMacros.createCustomEvent(event)
                events[event].registerEvent()

            timer = True
            while timer:
                try:
                    todt = timeOfDayT(World.getTimeOfDay())
                    wasBedTime = GlobalVars.getBoolean("is_bed_time")
                    if 12542 <= todt <= 12642 and not wasBedTime:
                        GlobalVars.putBoolean('is_bed_time', True)
                        events["BED_START"].trigger()
                        task("task_bed_start")
                    elif 23460 <= todt <= 23500 and wasBedTime:
                        GlobalVars.putBoolean('is_bed_time', False)
                        events["BED_END"].trigger()
                        task("tast_bed_end")
                    wasMonsterSpawnTime = GlobalVars.getBoolean("is_monster_spawn_time")
                    if 12869 <= todt <= 13069 and not wasMonsterSpawnTime:
                        GlobalVars.putBoolean('is_monster_spawn_time', True)
                        events["MONSTER_SPAWN_START"].trigger()
                        task("task_monster_spawn_start")
                    elif 22931 <= todt <= 23131 and wasMonsterSpawnTime:
                        GlobalVars.putBoolean('is_monster_spawn_time', False)
                        events["MONSTER_SPAWN_END"].trigger()
                        task("task_monster_spawn_end")
                    wasNight = GlobalVars.getBoolean('is_night')
                    if todt >= 13000 and not wasNight:
                        GlobalVars.putBoolean('is_night', True)
                        events["NIGHT_START"].trigger()
                        Chat.toast("Good night", "Zzzzz")
                        task("task_night")
                    elif todt < 13000 and wasNight:
                        GlobalVars.putBoolean('is_night', False)
                        events["DAY_START"].trigger()
                        Chat.log("Good morning", "")
                        task("task_day")
                    sleep(1)
                except Exception as e:
                    Chat.log(f"Error: {e}")
                    sleep(5)
