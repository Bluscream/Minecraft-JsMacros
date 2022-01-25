let isFirstVillager = true;


// List containg all "Tressure" enchantments
const tressure = ["soul_speed", "mending", "binding_curse", "vanishing_curse"]; // "frost_walker", 

// List containg the best level for each enchantment
const bestEnchants = [{ id: "aqua_affinity", lvl: 1 }, { id: "channeling", lvl: 1 }, { id: "binding_curse", lvl: 1 },
    { id: "vanishing_curse", lvl: 1 }, { id: "flame", lvl: 1 }, { id: "infinity", lvl: 1 },
    { id: "mending", lvl: 1 }, { id: "multishot", lvl: 1 }, { id: "silk_touch", lvl: 1 },

    { id: "fire_aspect", lvl: 2 }, { id: "frost_walker", lvl: 2 }, { id: "knockback", lvl: 2 },
    { id: "punch", lvl: 2 },

    { id: "cleaving", lvl: 3 }, { id: "depth_strider", lvl: 3 }, { id: "fortune", lvl: 3 },
    { id: "looting", lvl: 3 }, { id: "loyalty", lvl: 3 }, { id: "luck_of_the_sea", lvl: 3 },
    { id: "lure", lvl: 3 }, { id: "quick_charge", lvl: 3 }, { id: "respiration", lvl: 3 },
    { id: "riptide", lvl: 4 }, { id: "soul_speed", lvl: 3 }, { id: "sweeping", lvl: 3 },
    { id: "thorns", lvl: 3 }, { id: "unbreaking", lvl: 3 },

    { id: "blast_protection", lvl: 4 }, { id: "feather_falling", lvl: 4 }, { id: "fire_protection", lvl: 4 },
    { id: "piercing", lvl: 4 }, { id: "projectile_protection", lvl: 4 }, { id: "protection", lvl: 4 },

    { id: "bane_of_arthropods", lvl: 5 }, { id: "efficiency", lvl: 5 }, { id: "impaling", lvl: 5 },
    { id: "power", lvl: 5 }, { id: "sharpness", lvl: 5 }, { id: "smite", lvl: 5 }
];

// List containg the lowest price per Level
const costLevel = [5, 8, 11, 14, 17];

// On/Off Code
toggledOff = GlobalVars.getBoolean("VanillaScripts.PefectTradeFinder");
if(toggledOff){
    GlobalVars.remove("VanillaScripts.PefectTradeFinder");
    Chat.log(Chat.createTextBuilder()
        .append("[").withColor(0x7)
        .append("EnchFinder").withColor(0x5)
        .append("]").withColor(0x7)
        .append(" disabled").withColor(0xc)
        .build());
} else {
    GlobalVars.putBoolean("VanillaScripts.PefectTradeFinder", true);
    Chat.log(Chat.createTextBuilder()
        .append("[").withColor(0x7)
        .append("EnchFinder").withColor(0x5)
        .append("]").withColor(0x7)
        .append(" enabled").withColor(0xc)
        .build());

        
    // list of enchantments not found
    let missingEnchants = "[smite, sharpness, power, impaling, efficiency, bane_of_arthropods, protection, projectile_protection, piercing, fire_protection, feather_falling, blast_protection, unbreaking, thorns, sweeping, soul_speed, respiration, quick_charge, lure, luck_of_the_sea, loyalty, looting, fortune, depth_strider, cleaving, punch, knockback, frost_walker, fire_aspect, silk_touch, multishot, mending, infinity, flame, vanishing_curse, binding_curse, channeling]"
     // GlobalVars.getString("VanillaScripts.PefectTradeFinder.Enchants");

    // Checks if we got a list
    if (missingEnchants === null || missingEnchants == "[]") {
        Chat.log(Chat.createTextBuilder()
            .append("[").withColor(0x7)
            .append("EnchFinder").withColor(0x5)
            .append("]").withColor(0x7)
            .append(" List of wanted enchantments is empty...").withColor(0xc)
            .build());

        // set String to be "Empty"
        missingEnchants = "[]";
        let addEnchants = true;
        // Waits for chat input
        while(addEnchants){
            missingEnchants = addEnchant(missingEnchants);
            Chat.log("Current: " + missingEnchants);
            Chat.log(Chat.createTextBuilder()
                .append("[").withColor(0x7)
                .append("EnchFinder").withColor(0x5)
                .append("]").withColor(0x7)
                .append(" Do you want to add another? yes/no").withColor(0xc)
                .build());
            // Waits for chat input
            context.releaseLock();
            const ctx = JsMacros.waitForEvent("SendMessage");
            const evt = ctx.event;
            if(evt.message.toLowerCase() == "no"){
                addEnchants = false;
                GlobalVars.putString("VanillaScripts.PefectTradeFinder.Enchants", missingEnchants);
            }
            evt.message = null;
            ctx.context.releaseLock();
        }
        
        Chat.log("Now Searching for these enchantments: " + missingEnchants);
        // Save the reseted List
        GlobalVars.putString("VanillaScripts.PefectTradeFinder.Enchants", missingEnchants);
    } else {
        Chat.log(Chat.createTextBuilder()
            .append("[").withColor(0x7)
            .append("EnchFinder").withColor(0x5)
            .append("]").withColor(0x7)
            .append(" Found list of wanted enchantments: \n").withColor(0xc)
            .append(missingEnchants).withColor(0x7)
            .build());
    }
}

function addEnchant(missingEnchants){
    const bestEnchants = [{ id: "aqua_affinity", lvl: 1 }, { id: "channeling", lvl: 1 }, { id: "binding_curse", lvl: 1 },
        { id: "vanishing_curse", lvl: 1 }, { id: "flame", lvl: 1 }, { id: "infinity", lvl: 1 },
        { id: "mending", lvl: 1 }, { id: "multishot", lvl: 1 }, { id: "silk_touch", lvl: 1 },

        { id: "fire_aspect", lvl: 2 }, { id: "frost_walker", lvl: 2 }, { id: "knockback", lvl: 2 },
        { id: "punch", lvl: 2 },

        { id: "cleaving", lvl: 3 }, { id: "depth_strider", lvl: 3 }, { id: "fortune", lvl: 3 },
        { id: "looting", lvl: 3 }, { id: "loyalty", lvl: 3 }, { id: "luck_of_the_sea", lvl: 3 },
        { id: "lure", lvl: 3 }, { id: "quick_charge", lvl: 3 }, { id: "respiration", lvl: 3 },
        { id: "riptide", lvl: 4 }, { id: "soul_speed", lvl: 3 }, { id: "sweeping", lvl: 3 },
        { id: "thorns", lvl: 3 }, { id: "unbreaking", lvl: 3 },

        { id: "blast_protection", lvl: 4 }, { id: "feather_falling", lvl: 4 }, { id: "fire_protection", lvl: 4 },
        { id: "piercing", lvl: 4 }, { id: "projectile_protection", lvl: 4 }, { id: "protection", lvl: 4 },

        { id: "bane_of_arthropods", lvl: 5 }, { id: "efficiency", lvl: 5 }, { id: "impaling", lvl: 5 },
        { id: "power", lvl: 5 }, { id: "sharpness", lvl: 5 }, { id: "smite", lvl: 5 }
    ];

    let addEnchants = true;
    add:
    while(addEnchants) {
        Chat.log(Chat.createTextBuilder()
            .append("[").withColor(0x7)
            .append("EnchFinder").withColor(0x5)
            .append("]").withColor(0x7)
            .append(" Please enter enchantment id in chat to add it or \"all\" for all of them:").withColor(0xc)
            .build());

        // Waits for chat input
        context.releaseLock();
        const ctx = JsMacros.waitForEvent("SendMessage");
        const evt = ctx.event;

        if(evt.message === null) {
            evt.message = "";
        }
        Chat.log("You wrote: " + evt.message.toLowerCase())
        if(evt.message.toLowerCase() == "all") {
            missingEnchants = "[]";
            for(let i = 0; i< bestEnchants.length; i++) {
                if(missingEnchants.length==2) {
                    missingEnchants = missingEnchants.slice(0, 1) + bestEnchants[i].id + missingEnchants.slice(1)
                } else {
                    missingEnchants = missingEnchants.slice(0, 1) + bestEnchants[i].id + ", " + missingEnchants.slice(1)
                }
            }
            addEnchants = false;
        } else {
            for (let i = 0; i < bestEnchants.length; i++){
                if (bestEnchants[i].id.toLowerCase() == evt.message.toLowerCase()) {
                    if(!missingEnchants.includes(evt.message.toLowerCase())){
                        if(missingEnchants.length==2) {// Empty
                            missingEnchants = missingEnchants.slice(0, 1) + evt.message.toLowerCase() + missingEnchants.slice(1)
                        } else {
                            missingEnchants = missingEnchants.slice(0, 1) + evt.message.toLowerCase() + ", " + missingEnchants.slice(1)
                        }
                        Chat.log(Chat.createTextBuilder()
                            .append("[").withColor(0x7)
                            .append("EnchFinder").withColor(0x5)
                            .append("]").withColor(0x7)
                            .append(" Added enchant to list: " + evt.message.toLowerCase()).withColor(0xc)
                            .build());

                        addEnchants = false;
                    }
                }
            }
            if(addEnchants) {
                Chat.log(Chat.createTextBuilder()
                    .append("[").withColor(0x7)
                    .append("EnchFinder").withColor(0x5)
                    .append("]").withColor(0x7)
                    .append(" Cannot add enchantment: " + evt.message.toLowerCase()).withColor(0xc)
                    .build());
            }
        }
        evt.message = null;
        ctx.context.releaseLock();
    }
    return missingEnchants;
}

// Code
main:
while (GlobalVars.getBoolean("VanillaScripts.PefectTradeFinder")) {
    playerOBJ = Player.getPlayer();
    villagerOBJ = nearestVillager()
    
    // Check if nearestVillager() returned a villager
    if( !(villagerOBJ === null) ){
    
        // tiggers task to refresh villager
        var foundEnchant = false;
        
        // Open Villager GUI
        Player.getPlayer().interactEntity(villagerOBJ, false)
        
        // Get Villager inventory handle
        let villagerInv = Player.openInventory();
        while (!villagerInv.getType().includes("Villager")) {
            if (!GlobalVars.getBoolean("VanillaScripts.PefectTradeFinder")) {
                break main;
            }
            Player.getPlayer().interactEntity(villagerOBJ, false)
            villagerInv = Player.openInventory();
            Client.waitTick(5);
        }
        if (!GlobalVars.getBoolean("VanillaScripts.PefectTradeFinder")) {
            break main;
        }
        
        // Get all trades
        for (const tradeOffer of villagerInv.getTrades()){
            let itemOut = tradeOffer.getOutput();
            
            // Used to determine if we want to save this trade
            const trade = {}
            trade.enchId;
            trade.enchLvl;
            trade.price = tradeOffer.getInput()[0].getCount()
            
            // search for trade Item ID
            if(itemOut.getItemID().includes("enchanted_book")){
                // Search Item NBT
                let nbt = itemOut.getNBT()
                if( !(nbt === null) ) {
                    for (let i=0; i < nbt.asCompoundHelper().get("StoredEnchantments").asListHelper().length(); i++){
                        let storedEnchants = nbt.asCompoundHelper().get("StoredEnchantments").asListHelper().get(i).asCompoundHelper();
                        trade.enchId = storedEnchants.get("id").asString().replace(/minecraft:/, '');
                        trade.enchLvl = storedEnchants.get("lvl").asString().replace(/s/, '');
                        foundEnchant = perfectTrade(trade);
                        Chat.log("Got " + trade.enchId + " " + trade.enchLvl + " for " + trade.price + " emeralds");
                        if(foundEnchant){
                            break;
                        }
                    }
                }
            } 
        }
        villagerInv.close()
        // Wait for Villager hud to close
        while (Hud.isContainer() && GlobalVars.getBoolean("VanillaScripts.PefectTradeFinder")) {
            Client.waitTick(1);
        }
        
        if (foundEnchant) {
            // Log in chat
            Chat.log(Chat.createTextBuilder()
                .append("[").withColor(0x7)
                .append("EnchFinder").withColor(0x5)
                .append("]").withColor(0x7)
                .append(" Found a ").withColor(0xa)
                .append(" Perfect ").withColor(0x6)
                .append(" Trade").withColor(0xa)
                .build());

            //Play sound to get players attention
            World.playSound("ui.toast.challenge_complete");

            // Exit While loop
            break main;
        } else {
            Chat.actionbar(Chat.createTextBuilder()
                .append("[").withColor(0x7)
                .append("EnchFinder").withColor(0x5)
                .append("]").withColor(0x7)
                .append(" Refreshing Trades").withColor(0x8)
                .build(), false);
            refreshTrades();
        }
    }
    
    Client.waitTick(5); // wait 1 second (synchronized to client ticks)
}

// Turns off script
GlobalVars.remove("VanillaScripts.PefectTradeFinder");


function perfectTrade(trade) {

    // list of enchantments not found
    let missingEnchants = GlobalVars.getString("VanillaScripts.PefectTradeFinder.Enchants");
    
    let isTreasure = tressure.includes(trade.enchId);
    let isMaxLevel;
    let bestLevelIndex;
    for (let i = 0; i < bestEnchants.length; i++){
        if (bestEnchants[i].id == trade.enchId) {
            isMaxLevel = (bestEnchants[i].lvl == trade.enchLvl);
            bestLevelIndex = i;
            break;
        }
    }

    let isBestPrice = isTreasure ? ((costLevel[trade.enchLvl - 1] * 2) >= trade.price) : (costLevel[trade.enchLvl - 1] >= trade.price);
    if (isBestPrice && isMaxLevel) {

        // Has Enchant NOT been found before
        let hasNOTBeenFound = missingEnchants.includes(trade.enchId) || isFirstVillager;

        // Remove from list
        // Remove from front-back
        missingEnchants = missingEnchants.replace(trade.enchId + ", ", '');
        // Remove from back-front
        missingEnchants = missingEnchants.replace(", " + trade.enchId, '');

        if (hasNOTBeenFound) {

            // Save list
            GlobalVars.putString("VanillaScripts.PefectTradeFinder.Enchants", missingEnchants);
            Chat.log(Chat.createTextBuilder()
                .append("[").withColor(0x7)
                .append("EnchFinder").withColor(0x5)
                .append("]").withColor(0x7)
                .append(" Found ").withColor(0xc)
                .append(trade.enchId).withColor(0xc)
                .append(" and Removed it from list ").withColor(0xc)
                .build());
            Chat.log("Missing List: " + missingEnchants);

        }
        return hasNOTBeenFound;
    }
    return false;
}


function getBlockId(){
    let jobbBlock = getBlockPos();
    return World.getBlock(Math.floor(jobbBlock.x), Math.floor(jobbBlock.y), Math.floor(jobbBlock.z)).getId();
}

/**
 * This functions assumes that the jobbBlock is directly infront of your feet
 */
function getBlockPos() {
    // player
    let playerOBJ = Player.getPlayer();
    let jobbBlock;
    let yaw = Player.getPlayer().getYaw()
    
    if( ( yaw >135 && yaw <= 180) || (yaw >= -180 && yaw <= -135) ){
        // Facing North
        Player.getPlayer().lookAt(180, playerOBJ.getPitch());
        jobbBlock = {x: playerOBJ.getX() , y: playerOBJ.getY() , z: playerOBJ.getZ()-1}
    } else if( (yaw <= 135 && yaw >45) ) {
        // Facing West
        Player.getPlayer().lookAt(90, playerOBJ.getPitch());
        jobbBlock = {x: Math.floor(playerOBJ.getX()-1) , y: Math.floor(playerOBJ.getY()) , z: Math.floor(playerOBJ.getZ())}
    } else if( (yaw <= 45 && yaw >-45) ) {
        // Facing South
        Player.getPlayer().lookAt(0, playerOBJ.getPitch());
        jobbBlock = {x: Math.floor(playerOBJ.getX()) , y: Math.floor(playerOBJ.getY()) , z: Math.floor(playerOBJ.getZ()+1)}
    } else {
        // Facing East
        Player.getPlayer().lookAt(-90, playerOBJ.getPitch());
        jobbBlock = {x: Math.floor(playerOBJ.getX()+1) , y: Math.floor(playerOBJ.getY()) , z: Math.floor(playerOBJ.getZ())}
    }
    return jobbBlock;
}

/**
 * Tricks Minecraft into thinking that the mouse is grabbed
 * This allows for script to break block when minecraft is minimized
 */
function grabMouse() {
    // Client Class
    let minecraftClass = Reflection.getClass("net.minecraft.class_310");

    // Mouse Handler Field
    let mouseHandlerField = Reflection.getDeclaredField(minecraftClass, "field_1729");
    mouseHandlerField.setAccessible(true);

    //Use reflection to grab mouse:
    let clientInstance = Client.getMinecraft();

    // Mouse Handler
    let mouseHandlerObj = mouseHandlerField.get(clientInstance);

    // Mouse Handelr Class
    let mouseClass = Reflection.getClass("net.minecraft.class_312");

    // Lock Mouse / grab Mouse Boolean Field
    let lockMouse = Reflection.getDeclaredField(mouseClass, "field_1783");
    lockMouse.setAccessible(true);

    // Grab mouse
    lockMouse.setBoolean(mouseHandlerObj, true);
}


function refreshTrades() {
    isFirstVillager = false;
    
    grabMouse();
    
    // NEW METHOD: PISTON
    
    // get player shortcut
    let playerOBJ = Player.getPlayer();
    
    // Look at button at players feet
    //Player.getPlayer().lookAt(playerOBJ.getYaw(), 90);

    workStation=getBlockPos();

    // Look at Work Station
    playerOBJ.lookAt(workStation.x, workStation.y, workStation.z);

    // Work Station
    let workstation = getBlockId();

    // Work Station - Soon to be replaced with piston head
    let workstationReplacement = getBlockId();
    
    // Press button
    KeyBind.keyBind("key.attack", true);
    
    // continue breaking untill it changes block OR Script is toggled off
    while ((workstation == workstationReplacement) && GlobalVars.getBoolean("VanillaScripts.PefectTradeFinder")) {
        workstationReplacement = getBlockId();
        Client.waitTick(1);
    }
    
    // stop rigth clicking button
    KeyBind.keyBind("key.attack", false);
    
    Client.waitTick(1);
    KeyBind.keyBind("key.use", true);
    
    // continue breaking untill it changes block OR Script is toggled off
    while ((workstation != workstationReplacement) && GlobalVars.getBoolean("VanillaScripts.PefectTradeFinder")) {
        workstationReplacement = getBlockId();
        Client.waitTick(1);
    }
    KeyBind.keyBind("key.use", false);
    
    // Look at villager
    playerOBJ.lookAt(Player.getPlayer().getYaw(), 0);
}

function refreshTradesNew() {
    
    let jobbBlock = getBlockPos();
    
    // Look at targeted block
    playerOBJ = Player.getPlayer();

    playerOBJ.lookAt(jobbBlock.x, jobbBlock.y, jobbBlock.z);
    breakBlock(jobbBlock.x, jobbBlock.y, jobbBlock.z)
    
    /* Start to break
    let oldJobbBlockId = getBlockId();
    KeyBind.keyBind("key.attack", true);    
    let newJobbBlockId = getBlockId();    
    // continue breaking untill it changes block
    while( (oldJobbBlockId == newJobbBlockId) && GlobalVars.getBoolean("VanillaScripts.PefectTradeFinder") ) {
        newJobbBlockId = getBlockId();
        Client.waitTick(10);
    }
    // Stop breaking
    KeyBind.keyBind("key.attack", false);*/
    
    // Add Delay
    Client.waitTick(10);
    
    // Place from of-hand
    KeyBind.keyBind("key.use", true);
    Client.waitTick(10);
    KeyBind.keyBind("key.use", false);
    
    // Look at villager
    playerOBJ.lookAt(Player.getPlayer().getYaw(), 0);
}
BlockPos = Reflection.getClass("net.minecraft.class_2338");
Direction = Reflection.getClass("net.minecraft.class_2350");
function breakBlock(x, y, z) {
    Chat.log("breakBlock x: " + x.toString() + " " + y.toString() + " " + z.toString())
    x = x|0;y = y|0;z = z|0
    block = World.getBlock(x,y,z)
    Chat.log("breakBlock: " + block.getId() + " x: " + x.toString() + " " + y.toString() + " " + z.toString())
    if (block.getId() != "minecraft:air" && block.getId() != "minecraft:bedrock") {
        // block.setGlowing(True)
        while (Client.getMinecraft().field_1761.method_2902(BlockPos(x,y,z), Direction.field_11033)) {
            Player.getPlayer().getRaw().method_6104(Player.getPlayer().getRaw().field_6266)
            Client.waitTick()
        }
    }
}

function nearestVillager(){
    // player
    playerOBJ = Player.getPlayer();
    let p1 = {x: playerOBJ.getX(), y: playerOBJ.getY(), z: playerOBJ.getZ()};
    
    // list of villagers
    let villagers = []
    
    // entity
    let p2;
    for (const entity of World.getEntities()){
        if(entity.getType().includes("villager")){
            p2 = {x: entity.getX(), y: entity.getY(), z: entity.getZ()};
            villagers.push([calculateDistance(p1, p2), entity])
        }
    }
    
    if( villagers.length == 0 ) {
        // return null becuse requierments where not met
        return null;
    }
    
    // Custom sort function
    // lowest distance first
    villagers.sort(
            function(a,b){
                return a[0] - b[0];
            }
        );
        
    if( villagers[0][0]<=5 ) {
        // return the closest villager
        return villagers[0][1];
    }
    
    // return null becuse requierments where not met
    return null;
}


function calculateDistance(p1, p2) {
    let a = p2.x - p1.x;
    let b = p2.y - p1.y;
    let c = p2.z - p1.z;

    return Math.round(Math.sqrt(a * a + b * b + c * c)*100)/100;
}