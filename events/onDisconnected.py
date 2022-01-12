
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "Disconnect"|"Key"|"Manual":
        Client.waitTick()
        if (GlobalVars.getString("server")): server = GlobalVars.getString("server").split("/")[0]
        Chat.toast("Disconnected", server)
        from os import environ
        from datetime import datetime
        from urllib.parse import quote_plus
        def AutoMagic(path: str, params = {}): Request.get(f"http://192.168.2.145:1122/{path}?{'&'.join([k+'='+quote_plus(v) for (k,v) in params.items()])}&password={environ.get('AMAPI_PW')}")
        AutoMagic("screen/on")
        Client.waitTick(10)
        AutoMagic("notification/create", {"title": f"Disconnected from {server}", "bigmessage": str(datetime.now()), "icon": "app.icon://com.mojang.minecraftpe"})