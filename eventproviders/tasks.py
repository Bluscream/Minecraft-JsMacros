
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "ProfileLoad"|"Key"|"JoinServer"|"Manual":
        was_run = GlobalVars.getBoolean(file.getName())
        Chat.log(f"Was run: {was_run}"); GlobalVars.putBoolean(file.getName(), False)
        if not was_run or event_name in ["Key","Manual"]:
            GlobalVars.putBoolean(file.getName(), True)
            def sleep(sec: float): Client.waitTick(int(sec * 20.0))
            # def updateTask(new):
            #     task_first = GlobalVars.getString("task_first")
            #     task_previous = GlobalVars.getString("task_previous")
            #     task_current = GlobalVars.getString("task_current")
            #     task_next = GlobalVars.getString("task_next")
            #     task_last = GlobalVars.getString("task_last")
            event = JsMacros.createCustomEvent("TASK_CHANGED")
            event.registerEvent()
            while not World.isWorldLoaded(): sleep(5)
            from traceback import format_exc
            last_task_now = GlobalVars.getString("task_now")
            Chat.log("Task system initialized")
            while True:
                try:
                    taskNow = GlobalVars.getString("task_now")
                    if taskNow != last_task_now:
                        last_task_now = taskNow
                        Chat.log("task_now changed to: "+taskNow+" triggering TASK_CHANGED")
                        event.trigger()
                    sleep(1)
                except Exception as e:
                    Chat.getLogger().error(format_exc())
                    sleep(5)
