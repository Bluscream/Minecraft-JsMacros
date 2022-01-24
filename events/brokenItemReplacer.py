if __name__ == "": 
    from JsMacrosAC import *  # Autocomplete, not necessary
    event.item = ItemStackHelper()
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "ItemDamage"|"Key"|"Manual":
        # def getPrivateField(sourceClass, source, field, name = ""):
            # field = Reflection.getDeclaredField(sourceClass, field, name)
            # field.setAccessible(True)
            # return field.get(source)
        itemStack = event.item
        itemID = itemStack.getItemID()
        if itemStack.isDamageable():
            def percent(num: int, den: int) -> float: return num / den if den else 0
            # Chat.log(f"last_damaged_item: {GlobalVars.getString('last_damaged_item')}")
            GlobalVars.putString("last_damaged_item", itemID)
            damage = event.damage
            maxdamage = itemStack.getMaxDamage()
            damage_percent = int(percent(damage, maxdamage) * 100)
            Chat.log(f"ItemDamage: {itemStack.getName()} {damage}/{maxdamage} ({damage_percent}%)")
            life = maxdamage - damage
            if life <= 4:
                inv = Player.openInventory()
                def pick(blockState):
                    best = 1
                    index = -1
                    optAirIndex = -1
                    for i in range(36, 44):
                        stack = inv.getSlot(i)
                        if stack.getItemID() == "minecraft:air": optAirIndex = i
                        s = stack.getRaw().method_7924(blockState) # getMiningSpeedMultiplier
                        if s > best: best = s; index = i
                    if index != -1:
                        inv.setSelectedHotbarSlotIndex(index - 36)
                    elif optAirIndex != -1:
                        inv.setSelectedHotbarSlotIndex(optAirIndex - 36)
                # def get_from_hotbar():
                #     for i in range(9):
                #         stack = inv.getSlot(i)
                #         if stack.getName() == itemStack.getName():
                #             return stack
                #     return None
                def get_from_inventory():
                    slots = inv.getTotalSlots()
                    Chat.log(f"Slots: {slots}")
                    for slot in range(0, slots):
                        stack = inv.getSlot(slot)
                        if stack.getItemID() != "minecraft:air": Chat.log(f"[{slot}]  {stack} {stack.getNBT()}")
                get_from_inventory() # get_from_hotbar()
            elif life < 1:
                Chat.log("Broken!")
                