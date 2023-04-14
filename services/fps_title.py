if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
title = f"MC | FPS: {{fps}} | TPS: {{tps}} | {Client.mcVersion()} | {{address}} | {{dimension}} | {{biome}} | {{time}}"
def fps(): return Client.getFPS().split(' fps')[0]
def tps(): return round(World.getServerInstantTPS())
def time(): return ""
    # tick = World.getTimeOfDay()
    # second = tick // 20
    # minute = second // 60
    # hour = (minute // 60 + 6) % 24
    # minute = minute % 60
    # return f"{hour:02}:{minute:02}"
def str(a): return a.split(":")[1].title()
def onTick(_1,_2):
    address = World.getCurrentServerAddress()
    if address: window.method_24286(title.format(
        fps=fps(),
        tps=tps(),
        address=World.getCurrentServerAddress().split(".")[0],
        dimension=str(World.getDimension()),
        biome=str(World.getBiome()),
        time=time()
    ))
window = Client.getMinecraft().method_22683()
JsMacros.on("Tick", JavaWrapper.methodToJavaAsync(onTick))