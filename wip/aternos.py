
from json import dumps
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "OpenScreen":
        if __name__ == "":
            button: ButtonWidgetHelper
            screen: IScreen
        screen = event.screen
        if screen is not None:
            screen_name = event.screenName
            def sleep(sec: float=0): Client.waitTick(sec * 20)
            if screen_name is not None and screen_name != "unknown":
                match screen_name:
                    case "Connection Lost":
                        sleep(0)
                        from net.minecraft import class_419 as DisconnectScreen
                        reasonF = Reflection.getDeclaredField(DisconnectScreen, 'field_2457')
                        reasonF.setAccessible(True)
                        reason = reasonF.get(event.screen).getString()
                        if reason:
                            Chat.getLogger().warn(reason)
                            pattern = r"You are trying to connect to ([\w|.]+)\."
                            from re import MULTILINE, finditer
                            matches = list(finditer(pattern, reason, MULTILINE))
                            if len(matches) == 1:
                                match = matches[0]
                                if match and "server is offline" in reason:
                                    ip = match.group(1)
                                    Chat.getLogger().info(f"Aternos server {ip} is offline")
                                    def callback(self, args):
                                        Chat.getLogger().warn(f"Starting aternos server {ip or None}")
                                    screen.addButton(50, 50, 100, 50, "START SERVER", JavaWrapper.methodToJavaAsync(callback))