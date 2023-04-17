from threading import local
from typing import List
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
saved = {
    'item.getItemID().lower().endswith("_sword")': { "type": "hotbar", "slot": 1 },
    'item.getItemID().lower().endswith("_pickaxe")': { "type": "hotbar", "slot": 2 },
    'item.getItemID().lower().endswith("_axe")': { "type": "hotbar", "slot": 3 },
    'item.getItemID().lower().endswith("_shovel")': { "type": "hotbar", "slot": 4 },
    'item.getItemID().lower().endswith("bow")': { "type": "hotbar", "slot": 5 },
    'item.getItemID().lower().endswith("spyglass")': { "type": "hotbar", "slot": 6 },
    'item.getItemID().lower().endswith("torch")': { "type": "hotbar", "slot": 7 },
    'item.getRaw().method_19267()': { "type": "hotbar", "slot": 8 }, # isFood() -> bool
    'item.getCreativeTab()=="building_blocks"': { "type": "hotbar", "slot": 9 },
    'item.getItemID().lower().endswith("shield")': { "type": "offhand", "slot": 1 },
}
def checkItem(slot: int):
    if slot is None: return
    inv = Player.openInventory()
    item = inv.getSlot(slot)
    map = inv.getMap()
    # def getSlot(type: str, slot): return map[type][slot]
    def getItemSlot(item):
        for condition, data in saved.items():
            if eval(condition, globals(), locals()):
                slot = map[data["type"]][data["slot"]-1]
                item = inv.getSlot(slot)
                if eval(condition, globals(), locals()):
                    # Chat.log(f"{item.getName().getString()} in slot {slot} already satisfies condition {condition}")
                    return None
                return slot
    correct_slot = getItemSlot(item)
    if correct_slot:
        inslot = inv.getSlot(correct_slot)
        if inslot.isEmpty() or inslot.getItemID() != item.getItemID(): 
            # Chat.log(f"{item.getItemID()} belongs into slot {correct_slot} (contained {inslot.getName().getString()})")
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
                if slot is None: Chat.log(f"event.slot is None")
                checkItem(slot)
    case "ItemPickup":
        # event.item	ItemStack
        inv = Player.openInventory()
        def get_event_item_slot():
            for slot in range(inv.getTotalSlots()-1, -1, -1):
                item = inv.getSlot(slot)
                if item.isEmpty(): continue
                if item.isItemEqual(event.item): return slot
        event_item_slot = get_event_item_slot()
        if event_item_slot is None: Chat.log(f"event_item_slot is None")
        checkItem(event_item_slot)