from datetime import datetime

if __name__ == "":
    from JsMacrosAC import *
    button: ButtonWidgetHelper
    screen: IScreen
screen = event.screen
screen_name = event.screenName
screen_class = ""
try: screen_class = screen.getScreenClassName()
except: pass

Chat.getLogger().info(f"EventOpenScreen {screen_name} ({screen_class})")
try:
    screen_buttons = screen.getButtonWidgets()
    for num, button in enumerate(screen_buttons, start=0):
        Chat.getLogger().warn(f"screen.getButtonWidgets()[{num}] = {button.getLabel()}","")
except: pass

def sleep(sec: float=0): Client.waitTick(sec * 20)
if screen_name is not None and screen_name != "unknown":
    # Chat.toast("EventOpenScreen", screen_name)
    match screen_name:
        case "Title Screen": # Title Screen # class: t.minecraft.class_442 # button: Multiplayer ID: 400310
            sleep(10)
            event.screen.getButtonWidgets()[1].click(True) # click Multiplayer
        case "Play Multiplayer": # Play Multiplayer # class: net.minecraft.class_500 # button: Join Server ID: 348948
            sleep(1)
            event.screen.getButtonWidgets()[1].click(True)  # click Direct connect
        case "Direct Connection": # Direct Connection # class: net.minecraft.class_ # button: Connect ID:
            sleep(1)
            event.screen.getTextFields()[0].setText("play.tasmantismc.com") # set address
            sleep(1)
            event.screen.getButtonWidgets()[0].click(True)  # click connect
        case "Saving World":
            sleep(0)
            Chat.getLogger().info(f">>> Saving World")
            GlobalVars.putString("crashed", str(datetime.now()))
        case "unknown":
            sleep(0)
            Chat.getLogger().info(f">>> unknown")
        case "Failed to connect to the server":
            sleep(0)
            Chat.getLogger().info(f">>> Failed to connect to the server")
            # event.screen.getButtonWidgets()[1].click(True)  # click Reconnect

elif screen:
    if screen_class == "fudge.notenoughcrashes.gui.CrashScreen":
        sleep(15)
        event.screen.getButtonWidgets()[2].click(True)
        event.screen.getButtonWidgets()[3].click(True)

"""
[08:49:29] [Script:{"trigger":"EVENT", "event":"OpenScreen", "file":"work\onScreen.py"}/INFO]: EventOpenScreen unknown ()
[08:49:29] [Script:{"trigger":"EVENT", "event":"OpenScreen", "file":"work\onScreen.py"}/WARN]: screen.getButtonWidgets()[0] = TextHelper:{"text": "Get link"}
[08:49:29] [Script:{"trigger":"EVENT", "event":"OpenScreen", "file":"work\onScreen.py"}/WARN]: screen.getButtonWidgets()[1] = TextHelper:{"text": "Show on Crashy [Beta]"}
[08:49:29] [Script:{"trigger":"EVENT", "event":"OpenScreen", "file":"work\onScreen.py"}/WARN]: screen.getButtonWidgets()[2] = TextHelper:{"text": "Back to Title Screen"}

[09:26:52] [Script:{"trigger":"EVENT", "event":"OpenScreen", "file":"work\onScreen.py"}/INFO]: EventOpenScreen Failed to connect to the server ()
[09:26:52] [Script:{"trigger":"EVENT", "event":"OpenScreen", "file":"work\onScreen.py"}/WARN]: p.getButtonWidgets()[0] = TextHelper:{"text": "Back to Server List"}
[09:26:52] [Script:{"trigger":"EVENT", "event":"OpenScreen", "file":"work\onScreen.py"}/WARN]: screen.getButtonWidgets()[1] = TextHelper:{"text": "Reconnect"}
"""