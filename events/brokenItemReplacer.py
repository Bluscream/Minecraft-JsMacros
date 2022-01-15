if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "ItemDamage"|"Manual":
        def percent(num: int, den: int) -> float: return num / den if den else 0
        itemStack = event.item
        itemID = itemStack.getItemID()
        if itemStack.isDamageable():
            Chat.log(f"last_damaged_item: {GlobalVars.getString('last_damaged_item')}")
            GlobalVars.putString("last_damaged_item", itemID)
            damage = event.damage
            maxdamage = itemStack.getMaxDamage()
            damage_percent = int(percent(damage, maxdamage) * 100)
            Chat.log(f"ItemDamage: {itemStack.getName()} {damage}/{maxdamage} ({damage_percent}%)")
            if maxdamage - damage <= 4:
                inv = Player.openInventory()
                def get_from_hotbar():
                    for i in range(9):
                        stack = inv.getSlot(i)
                        if stack.getName() == itemStack.getName():
                            return stack
                    return None
                def get_from_inventory():
                    slots = inv.getTotalSlots()
                    Chat.log(f"Slots: {slots}")
                    for slot in range(0, slots):
                        stack = inv.getSlot(slot)
                        if itemID != "minecraft:air": Chat.log(f"[{slot}] {stack.getNBT()}")
                    
                Chat.log("Broken!")
                # get_from_hotbar()
                get_from_inventory()