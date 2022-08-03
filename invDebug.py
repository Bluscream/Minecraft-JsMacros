if __name__ == "": 
    from JsMacrosAC import *  # Autocomplete, not necessary
    event.item = ItemStackHelper()
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "Key"|"Manual":
        if Hud.isContainer():
            def big(msg):
                Chat.log("==============================")
                Chat.log(msg)
                Chat.log("==============================")
            inv = Player.openInventory()
            big(f"Inventory Debug: {inv.getType()}")
            inv = Player.openInventory()
            inv_slot_count = inv.getTotalSlots()
            for slot in range(0, inv_slot_count):
                Chat.log(f"Slot #{slot}: {inv.getSlot(slot).getName()}")
            big(f"Inventory Debug: {inv.getContainerTitle()}")