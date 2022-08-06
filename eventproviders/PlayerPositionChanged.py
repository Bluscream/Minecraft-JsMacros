if __name__ == "": from JsMacrosAC import *
event = JsMacros.createCustomEvent("PlayerPositionChanged")
event.registerEvent()
l = [0,0,0]
while not World.isWorldLoaded(): Client.waitTick(10)
player = Player.getPlayer()
while True:
    pos = player.getBlockPos()
    x,y,z = (int(pos.getX()),int(pos.getY()),int(pos.getZ()))
    jumping = l[1] == y-1
    if (l[0]!=x or l[1]!=y or l[2]!=z) and not jumping:
        l = [x,y,z]
        event.putInt("x", x)
        event.putInt("y", y)
        event.putInt("z", z)
        event.trigger()
    Client.waitTick(3)
