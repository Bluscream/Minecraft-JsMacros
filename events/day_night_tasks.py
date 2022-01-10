
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
events={"DAY_START":"task_day","NIGHT_START":"task_night","BED_START":"task_bed_start","BED_END":"task_bed_end","MONSTER_SPAWN_START":"task_monster_spawn_start","MONSTER_SPAWN_END":"task_monster_spawn_end","TASK_NOW_CHANGED":"task_now"}
if event_name in events:
    GlobalVars.putString("task_now", (GlobalVars.getString(events[event_name])))
