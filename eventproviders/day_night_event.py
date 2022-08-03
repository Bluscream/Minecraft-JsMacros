
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "ProfileLoad"|"Key"|"JoinServer"|"Manual":
        was_run = GlobalVars.getBoolean(file.getName())
        if not was_run or event_name in ["Key","Manual"]:
            GlobalVars.putBoolean(file.getName(), True)
            def sleep(sec: float): Client.waitTick(int(sec * 20.0))
            def timeOfDayT(tod: int): return tod % 24000
            events = {
                "DAY_START": None,
                "NIGHT_START":None,
                "BED_START":None,
                "BED_END":None,
                "MONSTER_SPAWN_START":None,
                "MONSTER_SPAWN_END":None,
                "TASK_NOW_CHANGED":None
            }

            for event in events:
                events[event] = JsMacros.createCustomEvent(event)
                events[event].registerEvent()

            import traceback
            while not World.isWorldLoaded(): sleep(5)
            while True:
                try:
                    todt = timeOfDayT(World.getTimeOfDay())
                    wasBedTime = GlobalVars.getBoolean("is_bed_time")
                    if 12542 <= todt <= 12642 and not wasBedTime:
                        GlobalVars.putBoolean("is_bed_time", True)
                        events["BED_START"].trigger()
                        Chat.log("BED_START"+": "+f"is_bed_time: {GlobalVars.getBoolean('is_bed_time')}")
                    elif 23460 <= todt <= 23500 and wasBedTime: # 5:30
                        GlobalVars.putBoolean("is_bed_time", False)
                        events["BED_END"].trigger()
                        Chat.log("BED_END"+": "+f"is_bed_time: {GlobalVars.getBoolean('is_bed_time')}")
                    wasMonsterSpawnTime = GlobalVars.getBoolean("is_monster_spawn_time")
                    if 12869 <= todt <= 13069 and not wasMonsterSpawnTime:
                        GlobalVars.putBoolean('is_monster_spawn_time', True)
                        events["MONSTER_SPAWN_START"].trigger()
                        Chat.log("MONSTER_SPAWN_START"+": "+f"is_monster_spawn_time: {GlobalVars.getBoolean('is_monster_spawn_time')}")
                    elif 22931 <= todt <= 23131 and wasMonsterSpawnTime:
                        GlobalVars.putBoolean('is_monster_spawn_time', False)
                        events["MONSTER_SPAWN_END"].trigger()
                        Chat.log("MONSTER_SPAWN_END"+": "+f"is_monster_spawn_time: {GlobalVars.getBoolean('is_monster_spawn_time')}")
                    wasNight = GlobalVars.getBoolean('is_night')
                    if todt >= 13000 and not wasNight:
                        GlobalVars.putBoolean('is_night', True)
                        events["NIGHT_START"].trigger()
                        Chat.log("NIGHT_START"+": "+f"is_night: {GlobalVars.getBoolean('is_night')}")
                    elif todt < 13000 and wasNight:
                        GlobalVars.putBoolean('is_night', False)
                        events["DAY_START"].trigger()
                        Chat.log("DAY_START"+": "+f"is_night: {GlobalVars.getBoolean('is_night')}")
                    sleep(.25)
                except Exception as e:
                    # Chat.log(f"day_night_event Error: {e}")
                    # Chat.getLogger().error(traceback.format_exc())
                    sleep(5)
