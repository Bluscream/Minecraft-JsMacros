if __name__ == "": from JsMacrosAC import *

from net.minecraft import class_2745 as ChestType
from net.minecraft import class_2281 as ChestBlock

radius = 5
px = int(Player.getPlayer().getX())
py = int(Player.getPlayer().getY())
pz = int(Player.getPlayer().getZ())

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
                    Player.getPlayer().lookAt(x + .5, y + .5, z + .5)
                    Client.waitTick(2)
                    
                    if Player.rayTraceBlock(4, False) != None and Player.rayTraceBlock(4, False).getId() in container:
                        Chat.log(f"Interacting with {block.getName()} at [{x}, {y}, {z}]")
                        Player.getPlayer().interact()
                        Client.waitTick(8)
                        Player.openInventory().close()
                        #Player.getPlayer().interactBlock(x, y, z, 0, False)
                        #Client.waitTick(2)