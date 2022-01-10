const Vec3D = Java.type("xyz.wagyourtail.jsmacros.client.api.sharedclasses.PositionCommon$Vec3D");
const range = 10;

var entities = World.getEntities();
var playerPos = Player.getPlayer().getPos();

for (let entity of entities) {
    if (entity.getType() != "minecraft:item")
        continue;
    if (distance(playerPos, entity.getPos()) < range) {
        Chat.log(entity);
    }
}

function distance(pos1, pos2) {
    return new Vec3D(pos1, pos2).getMagnitude();
}