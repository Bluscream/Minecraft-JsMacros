if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "ProfileLoad"|"Key"|"JoinServer"|"Manual":
        done = GlobalVars.getBoolean("startup_done")
        if not done:
            GlobalVars.putBoolean("startup_done", True)
            # Client.waitTick(20)
            evt = JsMacros.createCustomEvent("Startup")
            evt.registerEvent()
            evt.trigger()
            # Chat.toast("Startup done","")