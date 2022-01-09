context.releaseLock();
Client.waitTick(40);

const ChestType = Java.type("net.minecraft.class_2745");
const ChestBlock = Java.type("net.minecraft.class_2281");
const player = Player.getPlayer();
const range = 4; //can technically go up to 7, but 3 to 4 is the vanilla range
const containers = [
  "minecraft:chest",
  "minecraft:trapped_chest",
  "minecraft:barrel",
  "minecraft:chest_minecart",
  // "minecraft:furnace","minecraft:furnace_minecart","minecraft:blast_furnace"
];
const double_containers = ["minecraft:chest", "minecraft:trapped_chest"];
const chest_types = [
  ChestType.field_12569 /*single*/,
  ChestType.field_12574 /*left*/,
];
var searchedChests = [];

//https://jsmacros.wagyourtail.xyz/?/examples/toggle.html
//run this loop every time the player position changes or if GlobalVar is false
// let looking_at = Player.rayTraceBlock(4, false);
// Chat.log("Looking at: " + looking_at?.toString());
// Player.getPlayer().interact()
while (true) {
  var posX = Math.floor(player.getX());
  var posY = Math.floor(player.getY()) + 1; //plus 1 to get the head position, used for the reach
  var posZ = Math.floor(player.getZ());
  for (let x = posX - range; x < posX + range; x++) {
    for (let y = posY - range; y < posY + range; y++) {
      for (let z = posZ - range; z < posZ + range; z++) {
        let block = World.getBlock(x, y, z);
        let block_id = block.getId();
        if (containers.includes(block_id)) {
          if (double_containers.includes(block_id)) {
            let state = block.getRawBlockState();
            if (
              !chest_types.includes(state.method_11654(ChestBlock.field_10770))
            )
              continue; // state.get(ChestBlock.ChestType)
          }
          let pos_str = x + "," + y + "," + z;
          if (searchedChests.includes(pos_str)) continue;
          searchedChests.push(pos_str);
          // Chat.log("Interacting with: " + block.toString());
          const yaw = player.getYaw();
          const pitch = player.getPitch();
          let _ = player.lookAt(x + 0.5, y + 0.5, z + 0.5);
          // Client.waitTick();
          let looking_at = Player.rayTraceBlock(4, false);
          if (!looking_at || !containers.includes(looking_at.getId())) continue;
          player.interact();
          while (!Hud.isContainer()) {
            Client.waitTick();
          }
          let inv = Player.openInventory();
          Client.waitTick();
          inv.close();
          while (Hud.isContainer()) {
            Client.waitTick();
          }
          //look back
          player.lookAt(yaw, pitch);
        }
      }
    }
  }
  Client.waitTick(10);
}
