if __name__ == "": from JsMacrosAC import *
event = JsMacros.createCustomEvent("PlayerPositionChanged")
event.registerEvent()
while not World.isWorldLoaded(): Client.waitTick(10)
l = [0,0,0]
player = Player.getPlayer()
while True:
    x = int(player.getX())
    y = int(player.getY())
    z = int(player.getZ())
    jumping = l[1] == y-1
    if l[0]!=x and l[1]!=y and l[2]!=z and not jumping:
        l = [x,y,z]
        event.trigger()
    Client.waitTick(3)
