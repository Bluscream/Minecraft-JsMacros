if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
Hud.clearDraw2Ds()
overlay = Hud.createDraw2D()
text = None
def fps(): return Client.getFPS().split(' fps')[0]
def onInit(ovly):
    global text
    text = ovly.addText(f"{fps()} fps!",  3, 10, 0xFFFFFF, True) # int(ovly.getWidth()-35)
overlay.setOnInit(JavaWrapper.methodToJavaAsync(onInit))
def onTick(arg1, arg2):
    if text: text.setText(f"{fps()} fps")
JsMacros.on("Tick", JavaWrapper.methodToJavaAsync(onTick))
Hud.registerDraw2D(overlay)