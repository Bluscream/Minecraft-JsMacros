if __name__ == "": from JsMacrosAC import *
if event.screenName is not None and event.screenName != "unknown":
    Chat.getLogger().info(f"EventOpenScreen {event.screenName}")
    # Chat.toast("EventOpenScreen", event.screenName)

    def sleep(sec: float=0): Client.waitTick(sec * 20)

    match event.screenName:
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
        case "Saving World": # fudge.notenoughcrashes.gui.CrashScreen
            sleep(1)
            event.screen.getButtonWidgets()[0].click(True)