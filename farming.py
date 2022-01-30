if __name__=="": from JsMacrosAC import * # Script by Hasenzahn1

RADIUS = 4
WAIT_AMOUNT = 2
ENABLE_FLOWERS = True
AUTO_SWITCH = True
USE_INVENTORY = True

BREAK = {
    "minecraft:wheat": 7,
    "minecraft:beetroots": 3,
    "minecraft:carrots": 7,
    "minecraft:potatoes": 7,
    "minecraft:nether_wart": 3,
    "minecraft:sweet_berry_bush": 3,
    "minecraft:grass": 0,
    "minecraft:tall_grass": 0,
    "minecraft:azure_bluet": 0,
    "minecraft:oxeye_daisy": 0,
    "minecraft:poppy": 0,
    "minecraft:dandelion": 0,
    "minecraft:cornflower": 0,
    "minecraft:allium": 0,
    "minecraft:blue_orchid": 0,
    "minecraft:white_tulip": 0,
    "minecraft:pink_tulip": 0,
    "minecraft:orange_tulip": 0,
    "minecraft:red_tulip": 0,
    "minecraft:fern": 0,
    "minecraft:large_fern": 0,
    "minecraft:cocoa": 2,
    "minecraft:sugar_cane": 0,
    "minecraft:kelp": 0,
    "minecraft:kelp_plant": 0,
    "minecraft:bamboo": 0
}

BREAKABLE_BLOCKS = [
    "minecraft:pumpkin",
    "minecraft:melon"
]

BREAK_NO_FIRST = [
    "minecraft:sugar_cane",
    "minecraft:kelp",
    "minecraft:kelp_plant",
    "minecraft:bamboo"
]

BONEMEALABLE = [
    # "minecraft:wheat",
    # "minecraft:beetroots",
    # "minecraft:carrots",
    # "minecraft:potatoes",
    # "minecraft:melon_stem",
    # "minecraft:pumpkin_stem",
    # "minecraft:oak_sapling", 
    # "minecraft:birch_sapling",
    # "minecraft:jungle_sapling",
    # "minecraft:spruce_sapling",
    # "minecraft:acacia_sapling",
    # "minecraft:dark_oak_sapling" ,
    # "minecraft:kelp",
    # "minecraft:kelp_plant",
    # "minecraft:bamboo",
    # "minecraft:bamboo_sapling",
    # "minecraft:sweet_berry_bush"
]

LOG_TYPES = [
    "minecraft:oak_log",
    "minecraft:spruce_log",
    "minecraft:birch_log",
    "minecraft:jungle_log",
    "minecraft:acacia_log",
    "minecraft:dark_oak_log",
    "minecraft:stripped_oak_log",
    "minecraft:stripped_spruce_log",
    "minecraft:stripped_birch_log",
    "minecraft:stripped_jungle_log",
    "minecraft:stripped_acacia_log",
    "minecraft:stripped_dark_oak_log",
    "minecraft:oak_wood",
    "minecraft:spruce_wood",
    "minecraft:birch_wood",
    "minecraft:jungle_wood",
    "minecraft:acacia_wood",
    "minecraft:dark_oak_wood"
]

PLACE = {
    "minecraft:wheat_seeds": ["minecraft:farmland"], 
    "minecraft:beetroot_seeds": ["minecraft:farmland"],
    "minecraft:carrot": ["minecraft:farmland"],
    "minecraft:potato": ["minecraft:farmland"],
    "minecraft:nether_wart": ["minecraft:soul_sand"],
    "minecraft:sugar_cane": ["minecraft:sand", "minecraft:dirt", "minecraft:grass_block", "minecraft:farmland"],
    "minecraft:melon_seeds": ["minecraft:farmland"],
    "minecraft:pumpkin_seeds": ["minecraft:farmland"],
    "minecraft:oak_sapling": ["minecraft:coarse_dirt", "minecraft:dirt", "minecraft:grass_block", "minecraft:podzol"], 
    "minecraft:birch_sapling": ["minecraft:coarse_dirt", "minecraft:dirt", "minecraft:grass_block", "minecraft:podzol"],
    "minecraft:jungle_sapling": ["minecraft:coarse_dirt", "minecraft:dirt", "minecraft:grass_block", "minecraft:podzol"],
    "minecraft:spruce_sapling": ["minecraft:coarse_dirt", "minecraft:dirt", "minecraft:grass_block", "minecraft:podzol"],
    "minecraft:acacia_sapling": ["minecraft:coarse_dirt", "minecraft:dirt", "minecraft:grass_block", "minecraft:podzol"],
    "minecraft:dark_oak_sapling": ["minecraft:coarse_dirt", "minecraft:dirt", "minecraft:grass_block", "minecraft:podzol"],
    "minecraft:kelp": [],
    "minecraft:bamboo": ["minecraft:coarse_dirt", "minecraft:dirt", "minecraft:grass_block", "minecraft:podzol", "minecraft:gravel", "minecraft:mycelium", "minecraft:red_sand"], # grass blocks, dirt, coarse dirt, gravel, mycelium, podzol, sand, or red sand.
    "minecraft:sweet_berries": ["minecraft:coarse_dirt", "minecraft:dirt", "minecraft:grass_block", "minecraft:podzol", "minecraft:farmland"],
    "minecraft:cocoa_beans": []
}

player = Player.getPlayer()

from net.minecraft import class_2350 as Direction
from net.minecraft import class_1268 as Hand
DOWN = Direction.field_11033
MAIN_HAND = Hand.field_5808

from net.minecraft import class_2338 as BlockPos
def breakBlock(x, y, z):
    blockId = World.getBlock(x, y, z).getId()
    if blockId not in ["minecraft:air", "minecraft:bedrock"]:
        pos = BlockPos(x, y, z)
        while Client.getMinecraft().field_1761.method_2902(pos, DOWN): #Break Block
            player.getRaw().method_6104(player.getRaw().field_6266) # Swing Hand
            Client.waitTick()

def getPlaceSide(x,y,z):
    #[DOWN, UP, NORTH, SOUTH, WEST, EAST] 0-5
    for i in [(0, -1, 0, 0), (0, 1, 0, 1), (0, 0, 1, 3), (0, 0, -1, 2), (-1, 0, 0, 4), (1, 0, 0, 5)]:
        if World.getBlock(x+i[0], y+i[1], z+i[2]).getId() != "minecraft:air":
            return i[3]

def place(x,y,z, block=True):
    side = getPlaceSide(x,y,z)
    if block: player.interactBlock(x,y,z, side, False)
    else: player.interactItem(x, y, z, side, False)

def onTick(event, args):
    if GlobalVars.getBoolean("NEXT_TICK"):
        GlobalVars.putBoolean("NEXT_TICK", False)
        pX = int(player.getX())
        pY = int(player.getY())
        pZ = int(player.getZ())
        ignore = []
        for x in range(-RADIUS, RADIUS + 1):
            for y in range(-RADIUS, RADIUS + 1):
                for z in range(-RADIUS, RADIUS + 1):
                    xyz = [pX + x, pY + y + 1, pZ + z]
                    if xyz not in ignore:
                        if GlobalVars.getObject("FARMER_RUNNING") != None:
                            block = World.getBlock(xyz[0],xyz[1],xyz[2])
                            blockID = block.getId()
                            mainHandItemId = player.getMainHand().getItemID() # Player.openInventory().getSlot(Player.openInventory().getSelectedHotbarSlotIndex() + 36).getItemID()
                            blockUnderID = World.getBlock(xyz[0],xyz[1]- 1, xyz[2]).getId()
                            if blockID in BREAK.keys() or blockID in BREAKABLE_BLOCKS:
                                if blockID in BREAK_NO_FIRST:
                                    if blockUnderID in BREAK_NO_FIRST:
                                        if blockID == "minecraft:bamboo":
                                            breakBlock(xyz[0],xyz[1],xyz[2])
                                            Client.waitTick(WAIT_AMOUNT)
                                        else:
                                            breakBlock(xyz[0],xyz[1],xyz[2])
                                            Client.waitTick(WAIT_AMOUNT)
                                else:
                                    state = block.getBlockState()
                                    if "age" in state.keySet():
                                        if int(state["age"]) == BREAK[blockID]:
                                            if blockID == "minecraft:sweet_berry_bush": place(xyz[0],xyz[1],xyz[2], False)
                                            else: breakBlock(xyz[0],xyz[1],xyz[2])
                                            Client.waitTick(WAIT_AMOUNT)
                                    elif blockID in BREAKABLE_BLOCKS:
                                        breakBlock(xyz[0],xyz[1],xyz[2])
                                        Client.waitTick(WAIT_AMOUNT)
                                    elif ENABLE_FLOWERS:
                                        breakBlock(xyz[0],xyz[1],xyz[2])
                                        Client.waitTick(WAIT_AMOUNT)

                            #Bonemeal
                            if blockID in BONEMEALABLE:
                                if Player.openInventory().getSlot(45).getItemID() == "minecraft:bone_meal":
                                    place(xyz[0],xyz[1],xyz[2], False)

                            #Place
                            if mainHandItemId in PLACE.keys():
                                if mainHandItemId == "minecraft:kelp":
                                    if blockID in ["minecraft:water", "minecraft:flowing_water"] and blockUnderID not in ["minecraft:kelp", "minecraft:kelp_plant"]:
                                        place(xyz[0],xyz[1],xyz[2])
                                        Client.waitTick(WAIT_AMOUNT)
                                elif mainHandItemId == "minecraft:cocoa_beans":
                                    if blockID in LOG_TYPES:
                                        surrounding = [
                                            # [xyz[0], xyz[1] + 1, xyz[2]], # above
                                            # [xyz[0], xyz[1] - 1, xyz[2]], # below
                                            [xyz[0],xyz[1],xyz[2] + 1], # north
                                            [xyz[0],xyz[1],xyz[2] - 1], # south
                                            [xyz[0] - 1, xyz[1], xyz[2]], # west
                                            [xyz[0] + 1, xyz[1], xyz[2]] # east
                                        ]
                                        for pos in surrounding:
                                            block = World.getBlock(pos[0],pos[1],pos[2])
                                            if block.getId() == "minecraft:air":
                                                ignore.append(pos)
                                                place(pos[0],pos[1],pos[2])
                                                Client.waitTick(WAIT_AMOUNT * 2)
                                elif blockID == "minecraft:air":
                                    if blockUnderID in PLACE[mainHandItemId]:
                                        place(xyz[0],xyz[1],xyz[2])
                                        Client.waitTick(WAIT_AMOUNT * 2)
                                continue
                            GlobalVars.putBoolean("NEXT_TICK", True)

if __name__ == "__main__":
    ON_PROGRAM_RUN = GlobalVars.getObject("FARMER_RUNNING")
    if ON_PROGRAM_RUN == None:
        Chat.log("[JSMacros] AutoFarm enabled")
        GlobalVars.putBoolean("NEXT_TICK", True)
        ON_PROGRAM_RUN = JsMacros.on("Tick", JavaWrapper.methodToJava(onTick))
        GlobalVars.putObject("FARMER_RUNNING", ON_PROGRAM_RUN)
    else:
        Chat.log("[JSMacros] AutoFarm disabled")
        JsMacros.off("Tick", ON_PROGRAM_RUN)
        GlobalVars.remove("FARMER_RUNNING")

