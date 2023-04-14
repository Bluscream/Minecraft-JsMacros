
from json import dumps
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "OpenScreen":
        if __name__ == "":
            button: ButtonWidgetHelper
            screen: IScreen
        screen = event.screen
        if screen is not None:
            screen_name = event.screenName
            screen_title = ""
            try: screen_title = screen.getTitleText()
            except: pass
            screen_class = ""
            try: screen_class = screen.getScreenClassName()
            except: pass

            Chat.getLogger().info(f"EventOpenScreen {screen_name} [{screen_title}] ({screen_class}): {type(screen)}")
            screen_buttons = screen.getButtonWidgets()
            for num, button in enumerate(screen_buttons, start=0):
                try: Chat.getLogger().warn(f"screen.getButtonWidgets()[{num}] = {button.getLabel()}","")
                except: Chat.getLogger().error(f"Unable to get label for button {num}")
            screen_texts = screen.getTextFields()
            for num, text in enumerate(screen_texts, start=0):
                try: Chat.getLogger().warn(f"screen.getTextFields()[{num}] = {text.getText()}","")
                except: Chat.getLogger().error(f"Unable to get text for textfield {num}")

            def sleep(sec: float=0): Client.waitTick(sec * 20)
            if screen_name is not None and screen_name != "unknown":
                # Chat.log("EventOpenScreen"+": "+screen_name)
                # day_task = GlobalVars.getString("task_day")
                # if day_task and day_task != "#set allowBreak true;#set allowPlace true":
                match screen_name:
                    # case "Title Screen": # Title Screen # class: t.minecraft.class_442 # button: Multiplayer ID: 400310
                    #     sleep(10)
                    #     event.screen.getButtonWidgets()[1].click(True) # click Multiplayer
                    # case "Play Multiplayer": # Play Multiplayer # class: net.minecraft.class_500 # button: Join Server ID: 348948
                    #     sleep(1)
                    #     event.screen.getButtonWidgets()[1].click(True)  # click Direct connect
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
                    case "Disconnected":
                        sleep(0)
                        Chat.getLogger().info(f">>> Disconnected")
                    case "Connection Lost":
                        sleep(0)
                        Chat.getLogger().info(f">>> Connection Lost: {screen_title}")
                        reasonF = Reflection.getDeclaredField(screen, 'field_2457')
                        reasonF.setAccessible(True)
                        Chat.getLogger().info(reasonF.get(event.screen).getString())
                        # text = screen.getComponent("reason").getText()
                        # Chat.getLogger().info(f">>> Connection Lost: {text}")

            elif screen:
                if screen_class == "fudge.notenoughcrashes.gui.CrashScreen":
                    sleep(15)
                    event.screen.getButtonWidgets()[2].click(True)
                    event.screen.getButtonWidgets()[3].click(True)
