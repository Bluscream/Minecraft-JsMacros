
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "Death":
        Client.waitTick()
        Chat.toast("EventDeath", event.toString())

        def sleep(sec: int): Client.waitTick(sec * 20)
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
        if GlobalVars.getBoolean('is_bed_time'):
            task("task_bed_start")
        elif not GlobalVars.getBoolean('is_night'):
            task("task_day")