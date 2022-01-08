const player = Player.getPlayer();
var posX = Math.floor(player.getX());
var posY = Math.floor(player.getY()) + 1; //plus 1 to get the head position, used for the reach
var posZ = Math.floor(player.getZ());
const range = 4; //can technically go up to 7, but 3 to 4 is the vanilla range
const containers = [
  "minecraft:chest",
  "minecraft:barrel",
  "minecraft:redstone_chest",
  "minecraft:trapped_chest",
  "minecraft:furnace",
  "minecraft:furnace_minecart",
  "minecraft:blast_furnace",
];
//https://jsmacros.wagyourtail.xyz/?/examples/toggle.html
//run this loop every time the player position changes or if GlobalVar is false
let looking_at = Player.rayTraceBlock(4, false);
Chat.log("Looking at: " + looking_at.toString());
// Player.getPlayer().interact()
for (let x = posX - range; x < posX + range; x++) {
  for (let y = posY - range; y < posY + range; y++) {
    for (let z = posZ - range; z < posZ + range; z++) {
      let block = World.getBlock(x, y, z);
      if (containers.includes(block.getId())) {
        Chat.log("Interacting with: " + block.toString());
        player.interactBlock(x, y, z, 0, false); //need to check if block above is solid for chests
        //can be used with a counter to continue if the inventory doesn't open (chest is locked by a plugin or something like this
        while (!Hud.isContainer()) {
          Client.waitTick(2);
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
        Client.waitTick(2);
        inv.close();
        while (Hud.isContainer()) {
          Client.waitTick(2);
        }
      }
    }
  }
}
