
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "BaritonePathEvent"|"Key"|"Manual":
        status = event.getString("status")
        paused = GlobalVars.getBoolean("baritone_paused")
        match status:
            case "CALC_STARTED"|"CALC_FINISHED_NOW_EXECUTING":
                if paused: GlobalVars.putBoolean("baritone_paused", False)
            case "CANCELED":
                if not paused: GlobalVars.putBoolean("baritone_paused", True)
            case _:
                Chat.log(f"BaritonePathEvent: {status}")