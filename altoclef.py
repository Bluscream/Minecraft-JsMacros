if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = event.getEventName()
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "RecvMessage":
        message = event.text.getString()
        from re import search
        srch = search(r"\[Alto Clef\].*§r(.*)", message)
        if srch:
            var = 'altoclef_tasks'
            def get(): return GlobalVars.getString(var)
            def clear(): GlobalVars.putString(var, "")
            def next():
                task = get()
                if not task: return
                split = task.split(";")
                first = split.pop(0)
                Chat.log("next: " + first)
                Chat.log("remaining: " + ";".join(split))
                GlobalVars.putString("altoclef_tasks", ";".join(split))
                return first

            msg = srch.groups()[0]
            if msg == "Stopped":
                Chat.log(f"Altoclef stopped") # , clearing tasks {get()}")
                # clear()
            elif msg.startswith("User task FINISHED"):
                nxt = next()
                if not nxt:
                    Chat.log("Altoclef finished all tasks")
                else:
                    Chat.log(f"Altoclef finished current task, starting next task: {nxt}")
                    Chat.say(nxt)
"""
,set altoclef_tasks @goto 8957 71 -12442 overworld;@goto 8957 71 -12445 overworld
[10:52:51] [Render thread/INFO]: [STDOUT]: ALTO CLEF: Task STOP: <Getting to (0,0) in dimension NETHER> Completing goal., interrupted by null
[10:52:51] [Render thread/INFO]: [CHAT] Â§2Â§lÂ§o[Alto Clef] Â§rStopped
[10:52:51] [Render thread/INFO]: [CHAT] Â§2Â§lÂ§o[Alto Clef] Â§rUser task FINISHED. Took 22,48 seconds.
[10:51:59] [Render thread/INFO]: [CHAT] Â§2Â§lÂ§o[Alto Clef] Â§rFailed exploring.
[10:52:03] [Render thread/INFO]: [CHAT] Â§2Â§lÂ§o[Alto Clef] Â§rRefreshed inventory...
[10:51:58] [Render thread/INFO]: [STDOUT]: ALTO CLEF: Task START: <Wander for 10.0 blocks> Plan B: Random direction.
[10:51:58] [Render thread/INFO]: [STDOUT]: ALTO CLEF: <Getting to block class_2338{x=1148, y=63, z=-1525} in dimension NETHER> Wandering...
[10:51:55] [Render thread/INFO]: [STDOUT]: ALTO CLEF: Task START: <Wander for 10.0 blocks> Plan B: Random direction.
[10:51:43] [Render thread/INFO]: [STDOUT]: ALTO CLEF: Task START: <Shimmying> 
[10:51:43] [Render thread/INFO]: [STDOUT]: ALTO CLEF: Chain Interrupted: Misc World Survival Chain by User Tasks
[10:51:43] [Render thread/INFO]: [STDOUT]: ALTO CLEF: Task STOP: <Shimmying> , interrupted by null
[10:51:41] [Render thread/INFO]: [STDOUT]: ALTO CLEF: Task START: <Going to dimension: NETHER (default version)> Going to nether portal
[10:51:41] [Render thread/INFO]: [STDOUT]: ALTO CLEF: Task START: <Entering nether portal> Waiting inside portal
[10:51:38] [Render thread/INFO]: [STDOUT]: ALTO CLEF: Task STOP: <Doing something to closest block...> , interrupted by null


[10:56:52] [Render thread/INFO]: [CHAT] [Baritone] Going to: GoalXZ{x=<censored>,z=<censored>}
"""