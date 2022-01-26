
if __name__ == "":
    from JsMacrosAC import *  # Autocomplete, not necessary
    event.progress =float()
    event.total = int()
    event.level	= int()
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "EXPChange"|"Key"|"Manual":
        context.releaseLock()
        from os import environ
        from datetime import datetime
        from urllib.parse import quote_plus
        def AutoMagic(path: str, params = {}):
            try: Request.get(f"http://{environ.get('IP_Timo-Tablet')}:1122/{path}?{'&'.join([k+'='+quote_plus(v) for (k,v) in params.items()])}&password={environ.get('AMAPI_PW')}")
            except Exception as ex: Chat.getLogger().error(f"Could not send AutoMagic request: {ex}")
        last_level = GlobalVars.getInt("last_level")
        if last_level != event.level:
            if last_level:
                msg = f"⇪ {Player.getPlayer().getName().getString()} leveled up to {event.level} ({event.total} XP)"
                AutoMagic("toast/create", {"msg": msg, "long": "0"})
                AutoMagic("logger/log", {"message": msg})
                Chat.log(msg)
            GlobalVars.putInt("last_level", event.level)