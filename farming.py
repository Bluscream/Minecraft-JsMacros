# Script by Hasenzahn1


if __name__=="": 
    from JsMacrosAC import *


from net.minecraft import class_2338 as BlockPos
from net.minecraft import class_2350 as Direction
from net.minecraft import class_1268 as Hand

DOWN = Direction.field_11033
MAIN_HAND = Hand.field_5808

def breakBlock(x, y, z):
    if World.getBlock(x, y, z).getId() != "minecraft:air" and World.getBlock(x, y, z).getId() != "minecraft:bedrock":
        pos = BlockPos(x, y, z)
        while Client.getMinecraft().field_1761.method_2902(pos, DOWN): #Break Block
            Player.getPlayer().getRaw().method_6104(Player.getPlayer().getRaw().field_6266) # Swing Hand
            Client.waitTick()

RADIUS = 4
WAIT_AMOUNT = 1
ENABLE_FLOWERS = True

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
     "minecraft:cocoa": 2
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
    "minecraft:wheat",
    "minecraft:beetroots",
    "minecraft:carrots",
    "minecraft:potatoes",
    "minecraft:melon_stem",
    "minecraft:pumpkin_stem",
    "minecraft:oak_sapling", 
    "minecraft:birch_sapling",
    "minecraft:jungle_sapling",
    "minecraft:spruce_sapling",
    "minecraft:acacia_sapling",
    "minecraft:dark_oak_sapling" ,
    "minecraft:kelp",
    "minecraft:kelp_plant",
    "minecraft:bamboo",
    "minecraft:bamboo_sapling",
    "minecraft:sweet_berry_bush"
]



PLACE = {
    "minecraft:wheat_seeds": ["minecraft:farmland"], 
    "minecraft:beetroot_seeds": ["minecraft:farmland"],
    "minecraft:carrot": ["minecraft:farmland"],
    "minecraft:potato": ["minecraft:farmland"],
    "minecraft:nether_wart": ["minecraft:soul_sand"],
    "minecraft:sugar_cane": ["minecraft:sand", "minecraft:dirt", "minecraft_grass_block", "minecraft:farmland"],
    "minecraft:melon_seeds": ["minecraft:farmland"],
    "minecraft:pumpkin_seeds": ["minecraft:farmland"],
    # "minecraft:oak_sapling": ["minecraft:coarse_dirt", "minecraft:dirt", "minecraft_grass_block", "minecraft:podzol"], 
    # "minecraft:birch_sapling": ["minecraft:coarse_dirt", "minecraft:dirt", "minecraft_grass_block", "minecraft:podzol"],
    # "minecraft:jungle_sapling": ["minecraft:coarse_dirt", "minecraft:dirt", "minecraft_grass_block", "minecraft:podzol"],
    # "minecraft:spruce_sapling": ["minecraft:coarse_dirt", "minecraft:dirt", "minecraft_grass_block", "minecraft:podzol"],
    # "minecraft:acacia_sapling": ["minecraft:coarse_dirt", "minecraft:dirt", "minecraft_grass_block", "minecraft:podzol"],
    # "minecraft:dark_oak_sapling": ["minecraft:coarse_dirt", "minecraft:dirt", "minecraft_grass_block", "minecraft:podzol"],
    "minecraft:kelp": [],
    "minecraft:bamboo": ["minecraft:coarse_dirt", "minecraft:dirt", "minecraft_grass_block", "minecraft:podzol", "minecraft:gravel", "minecraft:mycelium", "minecraft:red_sand"], # grass blocks, dirt, coarse dirt, gravel, mycelium, podzol, sand, or red sand.
    "minecraft:sweet_berries": ["minecraft:coarse_dirt", "minecraft:dirt", "minecraft_grass_block", "minecraft:podzol", "minecraft:farmland"]
}

def onTick(event, args):
    if GlobalVars.getBoolean("NEXT_TICK"):
        GlobalVars.putBoolean("NEXT_TICK", False)
        pX = int(Player.getPlayer().getX())
        pY = int(Player.getPlayer().getY())
        pZ = int(Player.getPlayer().getZ())
        for x in range(-RADIUS, RADIUS + 1):
            for y in range(-RADIUS, RADIUS + 1):
                for z in range(-RADIUS, RADIUS + 1):
                    if GlobalVars.getObject("FARMER_RUNNING") != None:
                        block = World.getBlock(pX + x, pY + y, pZ + z)
                        blockID = block.getId()
                        #Chat.log(blockID)
                        blockUnderID = World.getBlock(pX + x, pY + y - 1, pZ + z).getId()
                        selectedSlotID = Player.openInventory().getSlot(Player.openInventory().getSelectedHotbarSlotIndex() + 36).getItemID()
                        #Break
                        if blockID in BREAK.keys() or blockID in BREAKABLE_BLOCKS:
                            # state = type(block.getBlockState())
                            # if not state: continue
                            # Chat.log(str(state))
                            state = block.getBlockState()
                            if "age" in state.keySet():
                                if int(state["age"]) == BREAK[blockID]:
                                    if blockID != "minecraft:sweet_berry_bush":
                                        breakBlock(pX + x, pY + y, pZ + z)
                                        Client.waitTick(WAIT_AMOUNT)
                                    else:
                                        Player.getPlayer().interact(pX + x, pY + y, pZ + z, 0, False)
                                        Client.waitTick(WAIT_AMOUNT)
                            elif blockID in BREAKABLE_BLOCKS:
                                breakBlock(pX + x, pY + y, pZ + z)
                                Client.waitTick(WAIT_AMOUNT)
                            elif ENABLE_FLOWERS:
                                breakBlock(pX + x, pY + y, pZ + z)
                                Client.waitTick(WAIT_AMOUNT)
                            


                        
                        #Break Not lowest Block
                        elif blockID in BREAK_NO_FIRST and blockUnderID in BREAK_NO_FIRST:
                            if blockID == "minecraft:bamboo":
                                #if "sword" in selectedSlotID:
                                breakBlock(pX + x, pY + y, pZ + z)
                                Client.waitTick(WAIT_AMOUNT)
                            else:
                                breakBlock(pX + x, pY + y, pZ + z)
                                Client.waitTick(WAIT_AMOUNT)


                        #Bonemeal
                        if blockID in BONEMEALABLE:
                            if Player.openInventory().getSlot(45).getItemID() == "minecraft:bone_meal":
                                Player.getPlayer().interact(pX + x, pY + y, pZ + z, 0, True)  

                        

                        #Place
                        if selectedSlotID in PLACE.keys():
                            if blockID == "minecraft:air":
                                #Chat.log("is air")
                                if blockUnderID in PLACE[selectedSlotID]:
                                    Player.getPlayer().interactBlock(pX + x, pY + y, pZ + z, 0, False)       
                                    Client.waitTick(WAIT_AMOUNT)
                            elif selectedSlotID == "minecraft:kelp":
                                if blockID in ["minecraft:water", "minecraft:flowing_water"] and blockUnderID not in ["minecraft:kelp", "minecraft:kelp_plant"]:
                                    Player.getPlayer().interactBlock(pX + x, pY + y, pZ + z, 0, False)       
                                    Client.waitTick(WAIT_AMOUNT)

                    else:
                        return
                            

        GlobalVars.putBoolean("NEXT_TICK", True)



if __name__ == "__main__":
    ON_PROGRAM_RUN = GlobalVars.getObject("FARMER_RUNNING")
    if ON_PROGRAM_RUN == None:
        Chat.log("on")
        GlobalVars.putBoolean("NEXT_TICK", True)
        ON_PROGRAM_RUN = JsMacros.on("Tick", JavaWrapper.methodToJava(onTick))
        GlobalVars.putObject("FARMER_RUNNING", ON_PROGRAM_RUN)
    else:
        Chat.log("off")
        JsMacros.off("Tick", ON_PROGRAM_RUN)
        GlobalVars.remove("FARMER_RUNNING")

