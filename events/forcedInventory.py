from threading import local
from typing import List
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
def checkItem(slot: int):
    inv = Player.openInventory()
    item = inv.getSlot(slot)
    map = inv.getMap()
    # def getSlot(type: str, slot): return map[type][slot]
    def getItemSlot(item):
        id = item.getItemID().lower()
        tab = item.getCreativeTab()
        if id.endswith("sword"): return map["hotbar"][0]
        elif id.endswith("pickaxe"): return map["hotbar"][1]
        elif id.endswith("axe"): return map["hotbar"][2]
        elif id.endswith("shovel"): return map["hotbar"][3]
        elif id.endswith("bow"): return map["hotbar"][4]
        elif id.endswith("spyglass"): return map["hotbar"][5]
        elif id.endswith("torch"): return map["hotbar"][6]
        elif tab == "food": return map["hotbar"][7]
        elif tab == "building_blocks": return map["hotbar"][8]
        elif id.endswith("shield"): return map["offhand"][0]
    correct_slot = getItemSlot(item)
    if correct_slot:
        inslot = inv.getSlot(correct_slot)
        if inslot.isEmpty() or inslot.getItemID() != item.getItemID(): 
            Chat.log(f"{item.getItemID()} belongs into slot {correct_slot} (contained {inslot.getName().getString()})")
            inv.swap(slot, correct_slot)

match event_name:
    case "ClickSlot":
        if event.slot > 0:
            # event.screen	HandledScreen<?>	
            # event.mode	int
            # event.button	int
            # event.slot	int
            inv = Player.openInventory()
            # held = inv.getHeld()
            local_containers = ["craft_out","crafting_in","helmet","chestplate","leggings","boots","hotbar","main","offhand"]
            if event.mode == 1 and inv.getLocation(event.slot) not in local_containers: # or not held.isEmpty():
                slot = event.slot
                # def get_free_slots(range: List[int], first_only: bool = False):
                #     lst = list()
                #     for slot in range:
                #         # Chat.log(f"Slot #{slot}: {inv.getSlot(slot)}")
                #         if inv.getSlot(slot).isEmpty():
                #             if first_only: return slot
                #             lst.append(slot)
                # item = inv.getSlot(event.slot) if event.mode == 1 else held
                # Chat.log(f"Slot #{event.slot}: {item}")
                # if event.mode != 1:
                #     first_free_slot = get_free_slots(range(0, inv.getTotalSlots()), True)
                #     inv.click(first_free_slot)
                #     slot = first_free_slot
                checkItem(slot)
    case "ItemPickup":
        # event.item	ItemStack
        inv = Player.openInventory()
        def get_event_item_slot():
            for slot in range(inv.getTotalSlots()-1, -1, -1):
                item = inv.getSlot(slot)
                if item.isEmpty(): continue
                if item.isItemEqual(event.item): return slot
        checkItem(get_event_item_slot())