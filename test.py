if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
logger = Chat.getLogger()
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
logger.info(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "Key"|"Manual":
        inv = Player.openInventory()
        def get_free_slots():
            total = inv.getTotalSlots()
            for slot in range(0, total):
                if not inv.getSlot(slot).isEmpty():
                    stack = inv.getSlot(slot)
                    Chat.log(f"[{slot}]  {stack} {stack.getNBT()}")
        get_free_slots()