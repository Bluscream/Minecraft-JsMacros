if __name__ == "": 
    from JsMacrosAC import *  # Autocomplete, not necessary
    event.item = ItemStackHelper()
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "ItemPickup"|"Key"|"Manual":
        inv = Player.openInventory()
        from os import environ
        from datetime import datetime
        from urllib.parse import quote_plus
        def AutoMagic(path: str, params = {}):
            try: Request.get(f"http://{environ.get('IP_Timo-Tablet')}:1122/{path}?{'&'.join([k+'='+quote_plus(v) for (k,v) in params.items()])}&password={environ.get('AMAPI_PW')}")
            except Exception as ex: Chat.getLogger().error(f"Could not send AutoMagic request: {ex}")
        def percent(num, den): return int((num / den) * 100)
        def get_first_free_slot():
            for slot in range(0, inv.getTotalSlots()):
                if inv.getSlot(slot).isEmpty(): return slot
        def get_best_rod():
            slots = inv.getTotalSlots()
            best_rod = { "slot": -1, "has_mending": False, "luck_of_the_sea": 0, "lure": 0, "unbreaking": 0}
            for slot in range(-1, slots):
                stack = inv.getHeld() if (slot == -1) else inv.getSlot(slot)
                if stack.getItemID() == "minecraft:fishing_rod":
                    nbt = stack.getNBT()
                    if nbt.isCompound():
                        nbt = nbt.asCompoundHelper()
                        if nbt.has("Enchantments"):
                            enchantments = nbt.get("Enchantments")
                            current_rod = { "slot": slot, "has_mending": False, "luck_of_the_sea": 0, "lure": 0, "unbreaking": 0}
                            is_better = False
                            for enchantment in range(0, enchantments.length()):
                                enchantment = enchantments.get(enchantment)
                                enchantment_id = enchantment.get("id").asString()
                                lvl = 0
                                if enchantment.has("lvl"): lvl = int(enchantment.get("lvl").asString().split("s")[0])
                                if enchantment_id == "minecraft:mending": current_rod["has_mending"] = True
                                elif enchantment_id == "minecraft:luck_of_the_sea": current_rod["luck_of_the_sea"] = lvl
                                elif enchantment_id == "minecraft:lure": current_rod["lure"] = lvl
                                elif enchantment_id == "minecraft:unbreaking": current_rod["unbreaking"] = lvl
                            if current_rod["has_mending"] and not best_rod["has_mending"]: is_better = True
                            if current_rod["luck_of_the_sea"] > best_rod["luck_of_the_sea"]: is_better = True
                            if current_rod["lure"] > best_rod["lure"]: is_better = True
                            # if current_rod["unbreaking"] > best_rod["unbreaking"]: is_better = True
                            if is_better: best_rod = current_rod
            return best_rod
        def get_best_worst_condition_item_slot(id, compare, mode: str):
            slots = inv.getTotalSlots()
            worst_item = [compare, 0]
            best_item = [compare, 0]
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
                                    if damage_percent > worst_item[0]:
                                        # Chat.log(f"Got new worst: {worst_item[0]}% -> {damage_percent}% damage")
                                        worst_item = [damage_percent, slot]
                                    if damage_percent < best_item[0]:
                                        # Chat.log(f"Got new best: {best_item[0]}% -> {damage_percent}% damage")
                                        best_item = [damage_percent, slot]
                                    break
            return best_item if mode == "best" else worst_item
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
            worst_rod = get_best_worst_condition_item_slot("minecraft:fishing_rod", held_item_damage_percent, "worst")
            # Chat.log(f"Worst: {worst_rod[0]} Current: {held_item_damage_percent}")
            if held_item_damage_percent < 2:
                if worst_rod[0] > held_item_damage_percent:
                    msg = f"Switching to more broken fishing rod: #{worst_rod[1]} ({worst_rod[0]}% damage) to {held_item_index}"
                    Chat.log(msg)
                    AutoMagic("logger/log", {"message": msg})
                    swap_slots(worst_rod[1], held_item_index)
                else:
                    best_rod = get_best_rod()
                    if best_rod["slot"] != -1 and best_rod["slot"] != held_item_index:
                        msg = f"Switching to better fishing rod in slot #{best_rod['slot']}\n{'Mending' if best_rod['has_mending'] else ''} Luck of the Sea: {best_rod['luck_of_the_sea']} Lure: {best_rod['lure']} Unbreaking: {best_rod['unbreaking']}"
                        Chat.log(msg)
                        AutoMagic("logger/log", {"message": msg})
                        swap_slots(best_rod["slot"], held_item_index)