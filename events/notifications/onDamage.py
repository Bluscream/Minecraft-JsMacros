
if __name__ == "":
    from JsMacrosAC import *  # Autocomplete, not necessary
    event.attacker = EntityHelper()
    event.source = str()
    event.health = float()
    event.change = float()
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "Damage"|"Key"|"Manual":
        from os import environ
        from datetime import datetime
        from urllib.parse import quote_plus
        def AutoMagic(path: str, params = {}):
            try: Request.get(f"http://{environ.get('IP_Timo-Tablet')}:1122/{path}?{'&'.join([k+'='+quote_plus(v) for (k,v) in params.items()])}&password={environ.get('AMAPI_PW')}")
            except Exception as ex: Chat.getLogger().error(f"Could not send AutoMagic request: {ex}")
        AutoMagic("screen/on")
        Client.waitTick(10)
        player = Player.getPlayer()
        remaining_hearts = int(player.getHealth()/2)+1
        max_health = 20
        try:
            from net.minecraft import class_5134 as EntityAttributes
            max_health = player.asLiving().getRaw().method_26825(EntityAttributes.field_23716) # GENERIC_MAX_HEALTH
        except: pass
        missing_hearts = int((max_health/2)-remaining_hearts)
        msg = f"{event.source.title()} damaged you!\n\n{remaining_hearts*'♥'}{missing_hearts*'🖤'}"
        AutoMagic("toast/create", {"msg": msg, "long": "1"})
        AutoMagic("logger/log", {"message": msg})