
if __name__ == "":
    from JsMacrosAC import *  # Autocomplete, not necessary
    event = EventDeath
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "Death"|"Key"|"Manual":
        from os import environ
        from datetime import datetime
        from urllib.parse import quote_plus
        def AutoMagic(path: str, params = {}):
            try: Request.get(f"http://{environ.get('IP_Timo-Tablet')}:1122/{path}?{'&'.join([k+'='+quote_plus(v) for (k,v) in params.items()])}&password={environ.get('AMAPI_PW')}")
            except Exception as ex: Chat.getLogger().error(f"Could not send AutoMagic request: {ex}")
        AutoMagic("screen/on")
        Client.waitTick(10)
        AutoMagic("screen/unlock")
        msg = f"{Player.getPlayer().getName().getString()} died at {datetime.now()}"
        AutoMagic("notification/create", {"title": "Death" , "bigmessage": msg, "icon": "app.icon://com.mojang.minecraftpe"})
        AutoMagic("popup/show", {"title": "Minecraft JsMacros", "message": msg, "button": "OK", "icon": "app.icon://com.mojang.minecraftpe"})