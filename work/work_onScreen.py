
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "OpenScreen":
        if __name__ == "":
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
            # Chat.log("EventOpenScreen"+": "+screen_name)
            # day_task = GlobalVars.getString("task_day")
            # if day_task and day_task != "#set allowBreak true;#set allowPlace true":
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
                    from datetime import datetime
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