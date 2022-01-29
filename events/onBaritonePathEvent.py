
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
            case "AT_GOAL": pass
            case "CALC_FAILED": pass
            case "CONTINUING_ONTO_PLANNED_NEXT": pass
            case "DISCARD_NEXT": pass
            case "NEXT_CALC_FAILED": pass
            case "NEXT_SEGMENT_CALC_FINISHED": pass
            case "NEXT_SEGMENT_CALC_STARTED": pass
            case "PATH_FINISHED_NEXT_STILL_CALCULATING": pass
            case "SPLICING_ONTO_NEXT_EARLY": pass
            case _: pass
        Chat.log(f"BaritonePathEvent: {status}")