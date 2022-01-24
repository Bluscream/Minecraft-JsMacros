if __name__ == "": 
    from JsMacrosAC import *  # Autocomplete, not necessary
    event.item = ItemStackHelper()
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "ItemPickup"|"Key"|"Manual":
        inv = Player.openInventory()
        def percent(num, den): return int((num / den) * 100)
        from os import environ
        from datetime import datetime
        from urllib.parse import quote_plus
        from typing import Optional, List
        def AutoMagic(path: str, params = {}):
            try: Request.get(f"http://{environ.get('IP_Timo-Tablet')}:1122/{path}?{'&'.join([k+'='+quote_plus(v) for (k,v) in params.items()])}&password={environ.get('AMAPI_PW')}")
            except Exception as ex: Chat.getLogger().error(f"Could not send AutoMagic request: {ex}")
        def get_free_slots() -> List[int]:
            total = inv.getTotalSlots()
            empty = 0
            for slot in range(10, total):
                if inv.getSlot(slot).isEmpty(): empty += 1
            return [empty, total-10]
        
        empty, total = get_free_slots()
        msg = f"Picked up Item ({total-empty}/{total})\n[{event.item.getName()}]"
        nbt = event.item.getNBT()
        if nbt:
            if nbt.isCompound():
                nbt = nbt.asCompoundHelper()
                enchantments = None
                if nbt.has("Enchantments"): enchantments = nbt.get("Enchantments")
                elif nbt.has("StoredEnchantments"): enchantments = nbt.get("StoredEnchantments")
                if enchantments:
                    enchantments_count = enchantments.length()
                    if enchantments_count > 0:
                        # msg += "\n"
                        for enchantment in range(0, enchantments_count):
                            enchantment = enchantments.get(enchantment)
                            msg += "\n- "+enchantment.get("id").asString().split(":")[1].replace("_"," ").title()
                            if enchantment.has("lvl"):
                                msg += " " + enchantment.get("lvl").asString().split("s")[0]
                else: msg += '\n'+nbt.toString()
            else: msg += '\n'+str(nbt)
        AutoMagic("toast/create", {"msg": msg, "long": "1"})
        AutoMagic("logger/log", {"message": msg})

        if empty < 1:
            msg =  "Inventory is Full!"
            AutoMagic("toast/create", {"msg":msg, "long": "1"})
            AutoMagic("notification/create", {"title": msg, "bigmessage": str(datetime.now()), "icon": "app.icon://com.mojang.minecraftpe"})
            AutoMagic("logger/log", {"message": msg})