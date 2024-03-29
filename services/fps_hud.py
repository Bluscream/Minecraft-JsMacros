if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
Hud.clearDraw2Ds()
overlay = Hud.createDraw2D()
text = None
def fps(): return Client.getFPS().split(' fps')[0]
def tps(): return round(World.getServerInstantTPS())
def onInit(ovly):
    global text
    text = ovly.addText(f"",  3, 3, 0xFFFFFF, True) # int(ovly.getWidth()-35)
overlay.setOnInit(JavaWrapper.methodToJavaAsync(onInit))
def onTick(arg1, arg2):
    if text: text.setText(f"{fps()} | {tps()}")
JsMacros.on("Tick", JavaWrapper.methodToJavaAsync(onTick))
Hud.registerDraw2D(overlay)