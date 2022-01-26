
from email import message


if __name__ == "":
    from JsMacrosAC import *  # Autocomplete, not necessary
    event = EventRecvMessage
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "RecvMessage"|"Key"|"Manual":
        if event is not None:
            player_name = Player.getPlayer().getName().getString()
            event_text = event.text.getString()
            if player_name in event_text:
                context.releaseLock()
                from os import environ
                from datetime import datetime
                from urllib.parse import quote_plus
                def AutoMagic(path: str, params = {}):
                    try: Request.get(f"http://{environ.get('IP_Timo-Tablet')}:1122/{path}?{'&'.join([k+'='+quote_plus(v) for (k,v) in params.items()])}&password={environ.get('AMAPI_PW')}")
                    except Exception as ex: Chat.getLogger().error(f"Could not send AutoMagic request: {ex}")
                AutoMagic("screen/on")
                Client.waitTick(10)
                AutoMagic("screen/unlock")
                msg = f"[{datetime.now()}] {event_text}"
                AutoMagic("notification/create", {"title": "You were mentioned" , "bigmessage": msg, "icon": "app.icon://com.mojang.minecraftpe"})
                AutoMagic("popup/show", {"title": "Minecraft: Someone mentioned you", "message": msg, "timeout": "30s", "button": "OK", "icon": "app.icon://com.mojang.minecraftpe"})