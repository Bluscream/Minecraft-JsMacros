const player = Player.getPlayer();
var posX = Math.floor(player.getX());
var posY = Math.floor(player.getY()) + 1; //plus 1 to get the head position, used for the reach
var posZ = Math.floor(player.getZ());
const range = 4; //can technically go up to 7, but 3 to 4 is the vanilla range
const containers = ["minecraft:chest", "minecraft:barrel", "minecraft:redstone_chest","minecraft:trapped_chest","minecraft:furnace","minecraft:blas"];

//https://jsmacros.wagyourtail.xyz/?/examples/toggle.html
//run this loop every time the player position changes or if GlobalVar is false
for (let x = posX - range; x < posX + range; x++) {
  for (let y = posY - range; y < posY + range; y++) {
    for (let z = posZ - range; z < posZ + range; z++) {
      let block = World.getBlock(x, y, z);
      if (containers.includes(block.getId())) {
        player.interactBlock(x, y, z, 0, false); //need to check if block above is solid for chests
        //can be used with a counter to continue if the inventory doesn't open (chest is locked by a plugin or something like this
        while (!Hud.isContainer()) {
          Client.waitTick(1);
        } 
        //JsMacros.waitForEvent("OpenScreen") //can be problematic if the chest just doesn't open
        Player.openInventory().close();
      }
    }
  }
}