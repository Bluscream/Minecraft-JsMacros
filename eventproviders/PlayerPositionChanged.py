if __name__ == "": from JsMacrosAC import *
    
event = JsMacros.createCustomEvent("PlayerPositionChanged")
event.registerEvent()
while not World.isWorldLoaded(): Client.waitTick(10)
lastPos = [0,0,0]
player = Player.getPlayer()
while True:
    x = int(player.getX())
    y = int(player.getY())
    z = int(player.getZ())
    xyz = [x,y,z]
    if lastPos != xyz:
        lastPos = xyz
        event.trigger()
    Client.waitTick(3)
