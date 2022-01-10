
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = event.getEventName()
match event_name:
    case "TASK_CHANGED":
        def is_altoclef_finished(RecvMessage_event): return any(x in RecvMessage_event.text.getString() for x in ["§rUser task FINISHED","§rStopped"])
        def task(task: str):
            if not task: return
            for cmd in task.split(";"):
                if cmd and cmd != "":
                    Chat.log(f"[TASK] Executing {cmd}")
                    lower = cmd.lower()
                    if lower.startswith("/sleep "):
                        slp_time = cmd.replace("/sleep ", "")
                        sleep(float(slp_time))
                    elif lower == "@@wait":
                        Chat.log("Waiting for Altoclef to finish task...")
                        JsMacros.waitForEvent("RecvMessage", JavaWrapper.methodToJava(is_altoclef_finished)).context.releaseLock()
                        context.releaseLock()
                        Client.waitTick()
                    else: Chat.say(cmd, True)
        task(GlobalVars.getString("task_now"))
        Chat.log("[JSMacros] Task Finished!")
        GlobalVars.remove("task_now")
    case "ProfileLoad"|"Key"|"JoinServer":
        if not GlobalVars.getBoolean("task_now.py"):
            GlobalVars.putBoolean('task_now.py', True)
            def sleep(sec: float): Client.waitTick(int(sec * 20.0))
            # def updateTask(new):
            #     task_first = GlobalVars.getString("task_first")
            #     task_previous = GlobalVars.getString("task_previous")
            #     task_current = GlobalVars.getString("task_current")
            #     task_next = GlobalVars.getString("task_next")
            #     task_last = GlobalVars.getString("task_last")
            events = { "TASK_CHANGED":None }
            for event in events:
                events[event] = JsMacros.createCustomEvent(event)
                events[event].registerEvent()
            timer = True
            import traceback
            last_task_now = GlobalVars.getString("task_now")
            while timer:
                try:
                    taskNow = GlobalVars.getString("task_now")
                    if taskNow and taskNow != last_task_now:
                        last_task_now = taskNow
                        events["TASK_CHANGED"].trigger()
                    sleep(1)
                except Exception as e:
                    # Chat.log(f"day_night_event Error: {e}")
                    Chat.getLogger().error(traceback.format_exc())
                    sleep(5)
