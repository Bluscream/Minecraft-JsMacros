from operator import is_
if __name__ == "": 
    from JsMacrosAC import *  # Autocomplete, not necessary
    event.item = ItemStackHelper()
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "ItemPickup"|"Key"|"Manual":
        def autoArmor():
            inventory = Player.getInventory()
            armor_slots = [5, 6, 7, 8] # Helmet, Chestplate, Leggings, Boots
            armor_items = [
                'minecraft:leather_helmet',
                'minecraft:leather_chestplate',
                'minecraft:leather_leggings',
                'minecraft:leather_boots',
                'minecraft:chainmail_helmet',
                'minecraft:chainmail_chestplate',
                'minecraft:chainmail_leggings',
                'minecraft:chainmail_boots',
                'minecraft:iron_helmet',
                'minecraft:iron_chestplate',
                'minecraft:iron_leggings',
                'minecraft:iron_boots',
                'minecraft:golden_helmet',
                'minecraft:golden_chestplate',
                'minecraft:golden_leggings',
                'minecraft:golden_boots',
                'minecraft:diamond_helmet',
                'minecraft:diamond_chestplate',
                'minecraft:diamond_leggings',
                'minecraft:diamond_boots',
                'minecraft:netherite_helmet',
                'minecraft:netherite_chestplate',
                'minecraft:netherite_leggings',
                'minecraft:netherite_boots'
            ]
            for i in range(len(armor_slots)):
                slot = armor_slots[i]
                item = inventory[slot]
                if not item or not item['id'] in armor_items:
                    # Find the first available armor item in inventory
                    for j in range(36):
                        inv_item = inventory[j]
                        if inv_item and inv_item['id'] == armor_items[i]:
                            # Swap the item with the armor slot
                            Player.swapInventorySlots(j, slot)
                            break
        autoArmor()
# JsMacros.scheduleRepeat(autoArmor, 50)
