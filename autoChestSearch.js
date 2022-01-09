const ChestType = Java.type("net.minecraft.class_2745");
const ChestBlock = Java.type("net.minecraft.class_2281");
const player = Player.getPlayer();
var posX = Math.floor(player.getX());
var posY = Math.floor(player.getY()) + 1; //plus 1 to get the head position, used for the reach
var posZ = Math.floor(player.getZ());
const range = 4; //can technically go up to 7, but 3 to 4 is the vanilla range
const containers = [
    "minecraft:chest", "minecraft:trapped_chest" , "minecraft:barrel", "minecraft:chest_minecart"
    // "minecraft:furnace","minecraft:furnace_minecart","minecraft:blast_furnace"
];
const double_containers = [ "minecraft:chest", "minecraft:trapped_chest" ]
const chest_types = [ ChestType.field_12569/*single*/, ChestType.field_12574/*left*/]
//https://jsmacros.wagyourtail.xyz/?/examples/toggle.html
//run this loop every time the player position changes or if GlobalVar is false
// let looking_at = Player.rayTraceBlock(4, false);
// Chat.log("Looking at: " + looking_at?.toString());
// Player.getPlayer().interact()
for (let x = posX - range; x < posX + range; x++) {
  for (let y = posY - range; y < posY + range; y++) {
    for (let z = posZ - range; z < posZ + range; z++) {
      let block = World.getBlock(x, y, z);
      let block_id = block.getId();
      if (containers.includes(block_id)) {
        if (double_containers.includes(block_id)) {
          let state = block.getRawBlockState()
          // if (state.get(ChestBlock.ChestType) == ChestType.LEFT) {
          if (!chest_types.includes(state.method_11654(ChestBlock.field_10770))) continue;
        }
        Chat.log("Interacting with: " + block.toString());
        const yaw = player.getYaw();
        const pitch = player.getPitch();
        //look at
        player.lookAt(x + .5, y + .5, z + .5);
        Client.waitTick();
        let looking_at = Player.rayTraceBlock(4, false);
        if (!looking_at) continue;
        player.interact();
        // for (let i = 0; i < 6; i++) {
        //   Chat.log("Interacting at face: " + i);
        //   player.interactBlock(x, y, z, i, false); //need to check if block above is solid for chests
        //   Client.waitTick();
        // }
        //can be used with a counter to continue if the inventory doesn't open (chest is locked by a plugin or something like this
        while (!Hud.isContainer()) {
          Client.waitTick();
        }
        let inv = Player.openInventory();
        //JsMacros.waitForEvent("OpenScreen") //can be problematic if the chest just doesn't open
        let map = inv.getMap().get("container");
        Chat.log(
          "Opened inventory: " +
            inv.getContainerTitle() +
            " (" +
            map.length +
            " slots)"
        );
        for (let i = 0; i < map.length; i++) {
          let item = inv.getSlot(map[i]);
          if (item.getItemID() !== "minecraft:air") {
            Chat.log("[" + i.toString() + "] " + item.toString());
          }
        }
        Client.waitTick();
        inv.close();
        while (Hud.isContainer()) {
          Client.waitTick();
        }
        //look back
        player.lookAt(yaw, pitch)
      }
    }
  }
}
