if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
# Hud.clearDraw2Ds()
# overlay = Hud.createDraw2D()

# mappings = Reflection.loadMappingHelper("https://maven.fabricmc.net/net/fabricmc/yarn/1.19+build.4/yarn-1.19+build.4-v2.jar")
# minecraft = mappings.remapClass(Client.getMinecraft())
# window = minecraft.getClass("client.util.Window") # net.minecraft.

window = Client.getMinecraft().method_22683()
# handle = window.method_4490()

# from net.minecraft import class_1041 as Window
# handle = Window.field_5187

text = None
def fps(): return Client.getFPS().split(' fps')[0]
def tps(): return round(World.getServerInstantTPS())
# def onInit(ovly):
#     global text
#     text = ovly.addText(f"",  3, 3, 0xFFFFFF, True) # int(ovly.getWidth()-35)
# overlay.setOnInit(JavaWrapper.methodToJavaAsync(onInit))
def onTick(arg1, arg2):
    txt=f"{fps()} | {tps()}"
    window.method_24286(txt)
    # window.invokeMethod("setTitle", [txt])
    # Java.type("org.lwjgl.glfw.GLFW").glfwSetWindowTitle(handle, "Title")
    # if text: text.setText(txt)
JsMacros.on("Tick", JavaWrapper.methodToJavaAsync(onTick))
# Hud.registerDraw2D(overlay)