if __name__ == "": 
    from JsMacrosAC import *  # Autocomplete, not necessary
    event.item = ItemStackHelper()
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "Key"|"Manual":
        if Hud.isContainer():
            def big(msg, msg2 = None):
                Chat.log("==============================")
                Chat.log(msg)
                if msg2: Chat.log(msg2)
                Chat.log("==============================")
            inv = Player.openInventory()
            big(f"Inventory Debug: {inv.getType()}")
            inv = Player.openInventory()
            inv_slot_count = inv.getTotalSlots()
            for slot in range(0, inv_slot_count):
                Chat.log(f"Slot #{slot}: {inv.getSlot(slot).getName()}")
            map = inv.getMap()
            local_containers = ["craft_out","crafting_in","helmet","chestplate","leggings","boots","hotbar","main","offhand"]
            # local_slots = [map[container] for container in map if container in local_containers]
            big(f"Inventory Debug: {inv.getContainerTitle()} {inv_slot_count-len(map['container']) if 'container' in map else 0} slots ({inv_slot_count} total)",', '.join(map))