if __name__ == "": from JsMacrosAC import *
Vec3D = Reflection.getClass("xyz.wagyourtail.jsmacros.client.api.sharedclasses.PositionCommon$Vec3D")
def distance(pos1, pos2): return Vec3D(pos1, pos2).getMagnitude()
playerPos = Player.getPlayer().getPos()
def inRange(entity, range): return distance(playerPos, entity.getPos()) < range
def simplePos(pos): return f"{int(pos.getX())} {int(pos.getY())} {int(pos.getZ())}"

range = 0

items = []

for entity in World.getEntities():
    if entity.getType() != "minecraft:item": continue
    if not range or inRange(entity, range): items.append(entity)

item_count = len(items)
Chat.log(f"Found {item_count} dropped items within {range if range else 'infinity'} blocks")

task = ""
for item in items:
    task += f"@goto {simplePos(item.getPos())};@@wait;"
    
Chat.log(f"Task: {task}")
GlobalVars.putString("task_now", task)