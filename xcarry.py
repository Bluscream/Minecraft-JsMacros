from operator import is_


if __name__ == "": 
    from JsMacrosAC import *  # Autocomplete, not necessary
    event.item = ItemStackHelper()
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "ItemPickup"|"Key"|"Manual":
        inv = Player.openInventory()
        inv_slot_count = inv.getTotalSlots()
        def percent(num, den): return int((num / den) * 100)
        from os import environ
        from datetime import datetime
        from urllib.parse import quote_plus
        def AutoMagic(path: str, params = {}):
            try: Request.get(f"http://{environ.get('IP_Timo-Tablet')}:1122/{path}?{'&'.join([k+'='+quote_plus(v) for (k,v) in params.items()])}&password={environ.get('AMAPI_PW')}")
            except Exception as ex: Chat.getLogger().error(f"Could not send AutoMagic request: {ex}")
        from typing import Optional, List
        def get_free_slot_count() -> List[int]:
            empty = 0
            for slot in range(10, inv_slot_count):
                if inv.getSlot(slot).isEmpty(): empty += 1
            return [empty, inv_slot_count-10]
        def get_free_slots(range: List[int], first_only: bool = False):
            lst = list()
            for slot in range:
                # Chat.log(f"Slot #{slot}: {inv.getSlot(slot)}")
                if inv.getSlot(slot).isEmpty():
                    if first_only: return slot
                    lst.append(slot)
            return lst
        def swap_slots(slot1, slot2):
            global inv
            held_item = inv.getHeld()
            if held_item and not held_item.isEmpty():
                if held_item.getItemID() == "minecraft:fishing_rod":
                    Chat.log(f"Already holding {held_item.getName()}, using that")
                    inv = inv.click(slot2)
                else:
                    first_free_slot = get_free_slots(range(0, inv_slot_count), True)
                    Chat.log(f"Already holding {held_item.getName()}, dropping at #{first_free_slot}")
                    inv.click(first_free_slot)
                return
            _slot1 = inv.getSlot(slot1)
            slot1IsEmpty = _slot1.isEmpty()
            _slot2 = inv.getSlot(slot2)
            slot2IsEmpty = _slot2.isEmpty()
            if slot1IsEmpty:
                inv = inv.click(slot2)
                Client.waitTick(5)
                inv = inv.click(slot1)
                Client.waitTick(5)
            elif slot2IsEmpty:
                inv = inv.click(slot1)
                Client.waitTick(5)
                inv = inv.click(slot2)
                Client.waitTick(5)
            elif slot1IsEmpty and slot2IsEmpty: return
            else:
                inv = inv.click(slot1)
                Client.waitTick(5)
                inv = inv.click(slot2)
                Client.waitTick(5)
                inv = inv.click(slot1)
                Client.waitTick(5)
        empty, total = get_free_slot_count()
        is_damagable = event.item.isDamageable()
        is_stackable = event.item.getMaxCount() > 1
        if not is_damagable and not is_stackable:
            def get_event_item_slot():
                for slot in range(inv_slot_count-1, -1, -1):
                    item = inv.getSlot(slot)
                    if item.isEmpty(): continue
                    if item.isItemEqual(event.item): return slot
            event_item_slot = get_event_item_slot()
            free_crafting_offhand_slot = get_free_slots([1,2,3,4,45], True)
            if free_crafting_offhand_slot:
                Chat.log(f"Picked up {event.item.getName()} in slot #{event_item_slot}, moving to #{free_crafting_offhand_slot}")
                swap_slots(event_item_slot, free_crafting_offhand_slot)
            elif empty < 1:
                Chat.log(f"Inventory full, holding onto {}")
                inv.click(event_item_slot)