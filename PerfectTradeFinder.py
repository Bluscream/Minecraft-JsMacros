if __name__ == "": from JsMacrosAC import * # Autocomplete, not necessary
from math import sqrt, round, floor
logger = Chat.getLogger()
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
logger.info(f"Executing {file.getName()} on event {event_name}")

toggledOff = GlobalVars.getBoolean("VanillaScripts.PefectTradeFinder")
if toggledOff:
    GlobalVars.remove("VanillaScripts.PefectTradeFinder") 
    Chat.log(Chat.createTextBuilder()
        .append("[").withColor(0x7)
        .append("MendingFinder").withColor(0x5)
        .append("]").withColor(0x7)
        .append(" disabled").withColor(0xc)
        .build())
else:
    GlobalVars.putBoolean("VanillaScripts.PefectTradeFinder", True)
    Chat.log(Chat.createTextBuilder()
        .append("[").withColor(0x7)
        .append("MendingFinder").withColor(0x5)
        .append("]").withColor(0x7)
        .append(" enabled").withColor(0xc)
        .build())

while (GlobalVars.getBoolean("VanillaScripts.PefectTradeFinder")):
    playerOBJ = Player.getPlayer()
    villagerOBJ = nearestVillager()
    
    # Check if nearestVillager() returned a villager
    if villagerOBJ is not None:
    
        # tiggers task to refresh villager
        foundEnchant = False
    
        # Open Villager GUI
        Player.getPlayer().interactEntity(villagerOBJ, True)
        
        # Get Villager inventory handle
        villagerInv = Player.openInventory()
        while GlobalVars.getBoolean("VanillaScripts.PefectTradeFinder") and  not villagerInv.getType().includes("Villager"):
            Player.getPlayer().interactEntity(villagerOBJ, True)
            villagerInv = Player.openInventory()
            Client.waitTick(5)
        
        if not GlobalVars.getBoolean("VanillaScripts.PefectTradeFinder"): break
        
        # Get all trades
        for tradeOffer in villagerInv.getTrades():
            itemOut = tradeOffer.getOutput()
            
            # Used to determine if we want to save this trade
            trade = {}
            trade.enchId
            trade.enchLvl
            trade.price = tradeOffer.getInput()[0].getCount()
            
            # search for trade Item ID
            if itemOut.getItemID().includes("enchanted_book"):
                # Search Item NBT
                nbt = itemOut.getNBT()
                if nbt is not None:
                    for i in range(0, nbt.asCompoundHelper().get("StoredEnchantments").asListHelper().length()):
                        storedEnchants = nbt.asCompoundHelper().get("StoredEnchantments").asListHelper().get(i).asCompoundHelper()
                        trade.enchId = storedEnchants.get("id").asString().replace('minecraft:', '')
                        trade.enchLvl = storedEnchants.get("lvl").asString().replace('s', '')
                        foundEnchant = perfectTrade(trade)
                        if (foundEnchant):
                            break
        villagerInv.close()
        # Wait for Villager hud to close
        while(GlobalVars.getBoolean("VanillaScripts.PefectTradeFinder") and Hud.isContainer()):
            Client.waitTick(10)
        if foundEnchant:
            Chat.log("Found Specifed a Perfect Trade...")
            # Turn off script
            GlobalVars.remove("VanillaScripts.PefectTradeFinder")
            break
        else:
            Chat.log("Refreshing Trades")
            refreshTrades()
    Client.waitTick(20) # wait 1 second (synchronized to client ticks)

def perfectTrade(trade):
    # List containg all "Tressure" enchantments
    tressure = ["frost_walker", "soul_speed", "mending", "binding_curse", "vanishing_curse"]
    
    # List containg the Enchantment id and thier best level
    bestLevel = [
        {"id": "aqua_affinity", "lvl": 1}, {"id": "channeling", "lvl": 1}, {"id": "binding_curse", "lvl": 1},
        {"id": "vanishing_curse", "lvl": 1}, {"id": "flame", "lvl": 1}, {"id": "infinity", "lvl": 1},
        {"id": "mending", "lvl": 1}, {"id": "multishot", "lvl": 1}, {"id": "silk_touch", "lvl": 1},

        {"id": "fire_aspect", "lvl": 2}, {"id": "frost_walker", "lvl": 2}, {"id": "knockback", "lvl": 2}, 
        {"id": "punch", "lvl": 2},

        {"id": "cleaving", "lvl": 3}, {"id": "depth_str"id"er", "lvl": 3}, {"id": "fortune", "lvl": 3},
        {"id": "looting", "lvl": 3}, {"id": "loyalty", "lvl": 3}, {"id": "luck_of_the_sea", "lvl": 3},
        {"id": "lure", "lvl": 3}, {"id": "quick_charge", "lvl": 3}, {"id": "respiration", "lvl": 3},
        {"id": "ript"id"e", "lvl": 3}, {"id": "soul_speed", "lvl": 3}, {"id": "sweeping", "lvl": 3},
        {"id": "thorns", "lvl": 3}, {"id": "unbreaking", "lvl": 3},

        {"id": "blast_protection", "lvl": 4}, {"id": "feather_falling", "lvl": 4}, {"id": "fire_protection", "lvl": 4},
        {"id": "piercing", "lvl": 4}, {"id": "projectile_protection", "lvl": 4}, {"id": "protection", "lvl": 4},

        {"id": "bane_of_arthropods", "lvl": 5}, {"id": "efficiency", "lvl": 5}, {"id": "impaling", "lvl": 5},
        {"id": "power", "lvl": 5}, {"id": "sharpness", "lvl": 5}, {"id": "smite", "lvl": 5}
    ]
        
    # List containg the lowest price per Level
    costLevel = [ 5, 8, 11, 14, 17]
    
    
    isTreasure = tressure.includes(trade.enchId)
    isMaxLevel = None
    for i in range(0, bestLevel.length):
        if bestLevel[i].id == trade.enchId:
            isMaxLevel = (bestLevel[i].lvl == trade.enchLvl)
            break
    isBestPrice = ((costLevel[trade.enchLvl-1] *2 ) >= trade.price) if isTreasure else (costLevel[trade.enchLvl-1] >= trade.price)
    return (isBestPrice and isMaxLevel)

def getBlockId():
    jobbBlock = getBlockPos()
    return World.getBlock(floor(jobbBlock.x), floor(jobbBlock.y), floor(jobbBlock.z)).getId()

def getBlockPos():
    # player
    playerOBJ = Player.getPlayer()
    jobbBlock = None
    yaw = Player.getPlayer().getYaw()
    
    if (yaw <= 180 and yaw >135) or (yaw >= -180 and yaw <= 135): # Facing North
        jobbBlock = { "x": playerOBJ.getX() , "y": playerOBJ.getY() , "z": playerOBJ.getZ()-1 }
    elif (yaw <= 135 and yaw >45): # Facing West
        jobbBlock = { "x": floor(playerOBJ.getX()-1) , "y": floor(playerOBJ.getY()) , "z": floor(playerOBJ.getZ()) }
    elif (yaw <= 45 and yaw >-45): # Facing South
        jobbBlock = { "x": floor(playerOBJ.getX()) , "y": floor(playerOBJ.getY()) , "z": floor(playerOBJ.getZ()+1)}
    else: # Facing East
        jobbBlock = { "x": floor(playerOBJ.getX()+1) , "y": floor(playerOBJ.getY()) , "z": floor(playerOBJ.getZ()) }
    
    return jobbBlock

def refreshTrades():
    jobbBlock = getBlockPos()
    # Look at targeted block
    playerOBJ = Player.getPlayer()
    playerOBJ.lookAt(jobbBlock.x, jobbBlock.y, jobbBlock.z)
    breakBlock(jobbBlock.x, jobbBlock.y, jobbBlock.z)    
    # Add Delay
    Client.waitTick(10)
    # Place from of-hand
    KeyBind.keyBind("key.use", True)
    Client.waitTick(10)
    KeyBind.keyBind("key.use", False)
    # Look at villager
    playerOBJ.lookAt(Player.getPlayer().getYaw(), 0)

BlockPos = Reflection.getClass("net.minecraft.class_2338")
Direction = Reflection.getClass("net.minecraft.class_2350")
def breakBlock(x, y, z):
    Chat.log("breakBlock x: " + x.toString() + " " + y.toString() + " " + z.toString())
    x = int(x)
    y = int(y)
    z = int(z)
    block = World.getBlock(x,y,z)
    Chat.log("breakBlock: " + block.getId() + " x: " + x.toString() + " " + y.toString() + " " + z.toString())
    if block.getId()  != "minecraft:air" and block.getId()  != "minecraft:bedrock":
        block.setGlowing(True)
        while (Client.getMinecraft().field_1761.method_2902(BlockPos(x,y,z), Direction.field_11033)):
            Player.getPlayer().getRaw().method_6104(Player.getPlayer().getRaw().field_6266)
            Client.waitTick()


def nearestVillager():
    # player
    playerOBJ = Player.getPlayer()
    p1 = { "x": playerOBJ.getX(), "y": playerOBJ.getY(), "z": playerOBJ.getZ() }
    
    # list of villagers
    villagers = []
    
    # entity
    p2 = None
    for entity in World.getEntities():
        if entity.getType().includes("villager"):
            p2 = { "x": entity.getX(), "y": entity.getY(), "z": entity.getZ() }
            villagers.push([calculateDistance(p1, p2), entity])

    if villagers.length == 0 :
        # return null becuse requierments where not met
        return null

    # Custom sort function
    # lowest distance first
    villagers.sort( function(a,b): return a[0] - b[0])

    if villagers[0][0]<=5 :
        # return the closest villager
        return villagers[0][1]

    # return null becuse requierments where not met
    return null



def calculateDistance(p1, p2):
    a = p2.x - p1.x
    b = p2.y - p1.y
    c = p2.z - p1.z
    return round(sqrt(a * a + b * b + c * c)*100)/100

