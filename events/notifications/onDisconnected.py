
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "Disconnect"|"Key"|"Manual":
        Client.waitTick()
        if (GlobalVars.getString("server")): server = GlobalVars.getString("server").split("/")[0]
        from os import environ
        from datetime import datetime
        from urllib.parse import quote_plus
        def AutoMagic(path: str, params = {}):
            try: Request.get(f"http://{environ.get('IP_Timo-Tablet')}:1122/{path}?{'&'.join([k+'='+quote_plus(v) for (k,v) in params.items()])}&password={environ.get('AMAPI_PW')}")
            except Exception as ex: Chat.getLogger().error(f"Could not send AutoMagic request: {ex}")
        AutoMagic("screen/on")
        Client.waitTick(10)
        AutoMagic("notification/create", {"title": f"Disconnected from {server}", "bigmessage": str(datetime.now()), "icon": "app.icon://com.mojang.minecraftpe"})