if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "PlayerPositionChanged"|"Key"|"Manual":
        from java.util import ArrayList
        from net.minecraft import class_2745 as ChestType
        from net.minecraft import class_2281 as ChestBlock

        radius = 5
        player = Player.getPlayer()
        px = int(player.getX())
        py = int(player.getY())
        pz = int(player.getZ())

        chests = ["minecraft:chest", "minecraft:trapped_chest"]
        container = chests + [
            "minecraft:ender_chest",
            "minecraft:barrel",
            "minecraft:shulker_box",
            "minecraft:dispenser",
            "minecraft:dropper",
            "minecraft:hopper",
            "minecraft:furnace",
            "minecraft:lit_furnace",
            "minecraft:blast_furnace",
            "minecraft:smoker",
            "minecraft:lit_smoker",
            "minecraft:campfire",
            "minecraft:lit_campfire",
            "minecraft:chest_minecart",
            "minecraft:brewing_stand"
        ]

        container2 = [
            "AbstractBannerBlock",
            "AbstractChestBlock",
            "AbstractFurnaceBlock",
            "AbstractSignBlock",
            "AbstractSkullBlock",
            "BarrelBlock",
            "BeaconBlock",
            "BeehiveBlock",
            "BellBlock",
            "BrewingStandBlock",
            "CampfireBlock",
            "CommandBlock",
            "ConduitBlock",
            "DaylightDetectorBlock",
            "DispenserBlock",
            "EnchantingTableBlock",
            "EndGatewayBlock",
            "EndPortalBlock",
            "HopperBlock",
            "JukeboxBlock",
            "LecternBlock",
            "PistonExtensionBlock",
            "SculkSensorBlock",
            "ShulkerBoxBlock",
            "SpawnerBlock",
            "StructureBlock"
        ]

        sides = [ChestType.field_12574]

        alreadyChecked = GlobalVars.getObject("chestCheck:alreadyChecked")
        if not alreadyChecked: alreadyChecked = ArrayList()
        Chat.log(f"Already checked {len(alreadyChecked)} chests")
        directions = list(range(-1, 6))
        for x in range(px - radius, px + radius):
            for y in range(py - radius, py + radius):
                for z in range(pz - radius, pz + radius):
                        block = World.getBlock(x, y, z)
                        # if isinstance(block, ChestBlock.getClass()):
                        if block != None:
                            block_id = block.getId()
                            if block_id in container:
                                    if block_id in chests:
                                        blockState = block.getRawBlockState()
                                        if blockState.method_11654(ChestBlock.field_10770) in sides:
                                            continue
                                    player.lookAt(x + .5, y + .5, z + .5)
                                    Client.waitTick()
                                    looking_at = Player.rayTraceBlock(4, False)
                                    if looking_at and looking_at.getId() == block_id:
                                        pos = [x,y,z]
                                        if not alreadyChecked.contains(pos):
                                            Chat.log(f"Interacting with {block.getName()} at {pos}")
                                            Player.getPlayer().interact()
                                            i = 0
                                            while not Hud.isContainer():
                                                if i > 4: break
                                                Client.waitTick()
                                                i += 1
                                            # for direction in directions:
                                            #     Chat.log(f"Trying direction {direction}")
                                            #     player.interactBlock(x, y, z, direction, False, False)
                                            #     Client.waitTick(20)
                                            # Client.waitTick(8)
                                            Player.openInventory().close()
                                            i = 0
                                            while Hud.isContainer():
                                                if i > 4: break
                                                Client.waitTick()
                                                i += 1
                                            alreadyChecked.add([x,y,z])
        if len(alreadyChecked): GlobalVars.putObject("chestCheck:alreadyChecked", alreadyChecked)
        Chat.log(f"Finished chest check: {len(alreadyChecked)}")