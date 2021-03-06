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
        def AutoMagic(path: str, params = {}):
            try: Request.get(f"http://{environ.get('IP_Timo-Tablet')}:1122/{path}?{'&'.join([k+'='+quote_plus(v) for (k,v) in params.items()])}&password={environ.get('AMAPI_PW')}")
            except Exception as ex: Chat.getLogger().error(f"Could not send AutoMagic request: {ex}")
        from typing import Optional, List
        def get_free_slots() -> List[int]:
            total = inv.getTotalSlots()
            empty = 0
            for slot in range(10, total):
                if inv.getSlot(slot).isEmpty(): empty += 1
            return [empty, total-10]
        
        empty, total = get_free_slots()
        if total - empty == 2: AutoMagic("logger/clear")
        toast = f"Picked up Item ({total-empty}/{total})\n{event.item.getName()}"
        player = Player.getPlayer()
        msg = f"{player.getName().getString()} picked up {event.item.getName()}"
        if event.item.isDamageable(): _msg = f" ({percent(event.item.getDamage(), event.item.getMaxDamage())}% damaged)"; toast += _msg;msg += _msg
        nbt = event.item.getNBT()
        if nbt:
            if nbt.isCompound():
                nbt = nbt.asCompoundHelper()
                def get_enchantment_strings(nbt):
                    enchantments = None
                    _enchantments = list()
                    if nbt.has("Enchantments"): enchantments = nbt.get("Enchantments")
                    elif nbt.has("StoredEnchantments"): enchantments = nbt.get("StoredEnchantments")
                    if enchantments:
                        enchantments_count = enchantments.length()
                        if enchantments_count > 0:
                            for enchantment in range(0, enchantments_count):
                                enchantment = enchantments.get(enchantment)
                                _msg = enchantment.get("id").asString().split(":")[1].replace("_"," ").title()
                                if enchantment.has("lvl"): _msg += " " + enchantment.get("lvl").asString().split("s")[0]
                                _enchantments.append(_msg)
                    return _enchantments
                enchantments = get_enchantment_strings(nbt)
                toast +="\n"+"\n".join(enchantments); msg += " (" + ", ".join(enchantments)+")"
            else: toast += '\n'+nbt.toString(); msg += ' '+nbt.toString()
        else: toast += f"\n{nbt}"; msg += f" {nbt}"
        
        holding_fishing_rod = player.getMainHand().getItemID() == "minecraft:fishing_rod"
        if holding_fishing_rod:
            AutoMagic("toast/create", {"msg": toast, "long": "1"})
            if nbt and enchantments: AutoMagic("logger/log", {"message": msg})
            if empty < 1:
                msg =  "Inventory is Full!"
                AutoMagic("toast/create", {"msg":msg, "long": "1"})
                AutoMagic("notification/create", {"title": msg, "bigmessage": str(datetime.now()), "icon": "app.icon://com.mojang.minecraftpe"})
                AutoMagic("logger/log", {"message": msg})