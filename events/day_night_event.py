
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = event.getEventName()
Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "ProfileLoad"|"Key"|"JoinServer":
        if not GlobalVars.getBoolean("day_night_event.py"):
            Chat.log(f"Executing {file.getName()}")
            GlobalVars.putBoolean('day_night_event.py', True)
            def sleep(sec: float): Client.waitTick(sec * 20.0)
            def timeOfDayT(tod: int): return tod % 24000
            def is_altoclef_finished(RecvMessage_event): return any(x in RecvMessage_event.text.getString() for x in ["§rUser task FINISHED","§rStopped"])
            def is_baritone_finished(RecvMessage_event): return any(x in RecvMessage_event.text.getString() for x in [""])
            def task(task: str):
                if not task: return
                for cmd in task.split(";"):
                    if cmd and cmd != "":
                        Chat.log(f"[TASK] Executing {cmd}")
                        lower = cmd.lower()
                        if lower.startswith("/sleep "):
                            slp_time = cmd.replace("/sleep ", "")
                            sleep(float(slp_time))
                        elif lower == "@wait":
                            JsMacros.waitForEvent("RecvMessage", JavaWrapper.methodToJava(is_altoclef_finished)).context.releaseLock()
                            context.releaseLock()
                            Client.waitTick()
                        elif lower == "#wait":
                            Chat.log("ERROR: #wait is not implemented")
                            # JsMacros.waitForEvent("RecvMessage", JavaWrapper.methodToJava(is_baritone_finished)).context.releaseLock()
                            context.releaseLock()
                            Client.waitTick()
                        else: Chat.say(cmd, True)


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
            import traceback
            while timer:
                try:
                    todt = timeOfDayT(World.getTimeOfDay())
                    wasBedTime = GlobalVars.getBoolean("is_bed_time")
                    if 12542 <= todt <= 12642 and not wasBedTime:
                        GlobalVars.putBoolean("is_bed_time", True)
                        events["BED_START"].trigger()
                        Chat.toast("BED_START", f"is_bed_time: {GlobalVars.getBoolean('is_bed_time')}")
                        task(GlobalVars.getString("task_bed_start"))
                    elif 23460 <= todt <= 23500 and wasBedTime: # 5:30
                        GlobalVars.putBoolean("is_bed_time", False)
                        events["BED_END"].trigger()
                        Chat.toast("BED_END", f"is_bed_time: {GlobalVars.getBoolean('is_bed_time')}")
                        task(GlobalVars.getString("task_bed_end"))
                    wasMonsterSpawnTime = GlobalVars.getBoolean("is_monster_spawn_time")
                    if 12869 <= todt <= 13069 and not wasMonsterSpawnTime:
                        GlobalVars.putBoolean('is_monster_spawn_time', True)
                        events["MONSTER_SPAWN_START"].trigger()
                        Chat.toast("MONSTER_SPAWN_START", f"is_monster_spawn_time: {GlobalVars.getBoolean('is_monster_spawn_time')}")
                        task(GlobalVars.getString("task_monster_spawn_start"))
                    elif 22931 <= todt <= 23131 and wasMonsterSpawnTime:
                        GlobalVars.putBoolean('is_monster_spawn_time', False)
                        events["MONSTER_SPAWN_END"].trigger()
                        Chat.toast("MONSTER_SPAWN_END", f"is_monster_spawn_time: {GlobalVars.getBoolean('is_monster_spawn_time')}")
                        task(GlobalVars.getString("task_monster_spawn_end"))
                    wasNight = GlobalVars.getBoolean('is_night')
                    if todt >= 13000 and not wasNight:
                        GlobalVars.putBoolean('is_night', True)
                        events["NIGHT_START"].trigger()
                        Chat.toast("NIGHT_START", f"is_night: {GlobalVars.getBoolean('is_night')}")
                        task(GlobalVars.getString("task_night"))
                    elif todt < 13000 and wasNight:
                        GlobalVars.putBoolean('is_night', False)
                        events["DAY_START"].trigger()
                        Chat.toast("DAY_START", f"is_night: {GlobalVars.getBoolean('is_night')}")
                        task(GlobalVars.getString("task_day"))
                    sleep(.25)
                except Exception as e:
                    # Chat.log(f"day_night_event Error: {e}")
                    Chat.getLogger().error(traceback.format_exc())
                    sleep(5)
