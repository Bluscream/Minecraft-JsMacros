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
        def get_first_free_slot():
            for slot in range(0, inv.getTotalSlots()):
                if inv.getSlot(slot).isEmpty(): return slot
        def get_worst_condition_item_slot(id, compare):
            slots = inv.getTotalSlots()
            highest= [compare, 0]
            for slot in range(-1, slots):
                stack = inv.getHeld() if (slot == -1) else inv.getSlot(slot)
                if stack.getItemID() == id and stack.isDamageable():
                    nbt = stack.getNBT()
                    if nbt.isCompound():
                        nbt = nbt.asCompoundHelper()
                        if nbt.has("Enchantments"):
                            enchantments = nbt.get("Enchantments")
                            for enchantment in range(0, enchantments.length()):
                                enchantment = enchantments.get(enchantment)
                                if enchantment.get("id").asString() == "minecraft:mending":
                                    damage_percent = percent(stack.getDamage(), stack.getMaxDamage())
                                    # Chat.log(f"Current Highest {highest[0]}% vs new {damage_percent}%")
                                    if damage_percent > highest[0]:
                                        # Chat.log(f"Got new highest: {highest[0]}% -> {damage_percent}%")
                                        highest = [damage_percent, slot]
                                    break
            return highest
        def swap_slots(slot1, slot2):
            # Chat.log(f"Slot {slot1} -> {slot2}")
            global inv
            held_item = inv.getHeld()
            # held_item_id = held_item.getItemID()
            # Chat.log(f"Held: {held_item}")
            if held_item and not held_item.isEmpty():
                if held_item.getItemID() == "minecraft:fishing_rod":
                    Chat.log(f"Already holding {held_item.getName()}, using that")
                    inv = inv.click(slot2)
                else:
                    first_free_slot = get_first_free_slot()
                    Chat.log(f"Already holding {held_item.getName()}, dropping at #{first_free_slot}")
                    inv.click(first_free_slot)
                return
            _slot1 = inv.getSlot(slot1)
            slot1IsEmpty = _slot1.isEmpty()
            _slot2 = inv.getSlot(slot2)
            slot2IsEmpty = _slot2.isEmpty()
            if slot1IsEmpty:
                inv = inv.click(slot2)
                Client.waitTick(10)
                inv = inv.click(slot1)
                Client.waitTick(10)
            elif slot2IsEmpty:
                inv = inv.click(slot1)
                Client.waitTick(10)
                inv = inv.click(slot2)
                Client.waitTick(10)
            elif slot1IsEmpty and slot2IsEmpty: return
            else:
                inv = inv.click(slot1)
                Client.waitTick(10)
                inv = inv.click(slot2)
                Client.waitTick(10)
                inv = inv.click(slot1)
                Client.waitTick(10)
        held_item = Player.getPlayer().getMainHand()
        held_item_index = inv.getSelectedHotbarSlotIndex()+36
        if held_item.getItemID() == "minecraft:fishing_rod":
            held_item_damage = held_item.getDamage()
            held_item_max_damage = held_item.getMaxDamage()
            held_item_damage_percent = percent(held_item_damage, held_item_max_damage)
            fully_repaired = held_item_damage < 1
            worst_rod = get_worst_condition_item_slot("minecraft:fishing_rod", held_item_damage_percent)
            if worst_rod[0] > held_item_damage_percent:
                Chat.log(f"Switching to more broken fishing rod: #{worst_rod[1]} ({worst_rod[0]}% damage) to {held_item_index}")
                swap_slots(worst_rod[1], held_item_index)
            new_item_nbt = event.item.getNBT()
            new_item_nbt = '\n'+str(new_item_nbt) if new_item_nbt else ""
        else: pass