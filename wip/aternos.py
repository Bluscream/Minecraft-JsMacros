
from json import dumps
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
from os import environ
from aternos_config import *
aternos_username = environ.get("aternos_username", aternos_username)
if not aternos_username: Chat.getLogger().warn(f"aternos_username not found in environment variables!")
aternos_password = environ.get("aternos_password", aternos_password)
if not aternos_password: Chat.getLogger().warn(f"aternos_password not found in environment variables!")

match event_name:
    case "OpenScreen":
        if __name__ == "":
            button: ButtonWidgetHelper
            screen: IScreen
        screen = event.screen
        if screen is not None:
            screen_name = event.screenName
            if screen_name is not None and screen_name != "unknown":
                match screen_name:
                    case "Connection Lost":
                        def sleep(ticks=0):
                            if hasattr(Client, "waitTick"): Client.waitTick(ticks)
                        sleep(1)
                        from net.minecraft import class_419 as DisconnectScreen
                        reasonF = Reflection.getDeclaredField(DisconnectScreen, 'field_2457')
                        reasonF.setAccessible(True)
                        reason = reasonF.get(event.screen).getString()
                        if reason:
                            # Chat.getLogger().warn(reason)
                            pattern = r"You are trying to connect to ([\w|.]+)\."
                            from re import MULTILINE, finditer
                            matches = list(finditer(pattern, reason, MULTILINE))
                            if len(matches) == 1:
                                match = matches[0]
                                if match:
                                    if "server is offline" in reason:
                                        ip = match.group(1)
                                        Chat.getLogger().info(f"Aternos server {ip} is offline")
                                        def start_server(ip):
                                            Chat.getLogger().warn(f"Starting aternos server {ip or None}")
                                            from python_aternos import Client
                                            aternos = None
                                            try: aternos = Client.restore_session()
                                            except: aternos = Client.from_credentials(aternos_username, aternos_password)
                                            if aternos is None:
                                                Chat.getLogger().warn(f"Could not connect to aternos, login incorrect?")
                                                return
                                            server = None
                                            servers = aternos.list_servers()
                                            for s in servers:
                                                Chat.getLogger().info(f"{s.address};{s.domain};{s.software},{s.version}")
                                                if s.address.lower() == ip.lower(): server = s
                                            if server is None:
                                                Chat.getLogger().warn(f"Server could not be found, maybe no permissions?")
                                                return
                                            else:
                                                Chat.getLogger().warn(f"Starting Aternos Server {server.software}, {server.version}")
                                                sleep(1)
                                                from threading import Thread
                                                Thread(target=(lambda: server.start())).start()
                                                sleep(1)
                                                Hud.getOpenScreen().close()
                                        def callback(self, args): start_server(ip)
                                        for button in screen.getButtonWidgets():
                                            if button.getLabel().getString() == "Back to Server List":
                                               x = button.getX();y = button.getY()+30
                                               Chat.getLogger().warn(f"Attaching aternos button to {x} {y}")
                                               screen.addButton(x, y, button.getWidth(), 20, "START ATERNOS SERVER", JavaWrapper.methodToJavaAsync(callback))
                                               break
                                    elif "different address" in reason:
                                        pattern = r"Â§([\w|.]+)Â§6:(\d+)"
                                        Chat.getLogger().warn(f"{pattern}")
                                        matches = list(finditer(pattern, reason, MULTILINE))
                                        Chat.getLogger().warn(f"{matches}")
                                        if len(matches) == 1:
                                            ip = match.group(1)
                                            port = match.group(2)
                                            Chat.getLogger().warn(f"Aternos server redirect to {ip}:{port}")
                                            Client.connect(ip, port)
                                        Chat.getLogger().warn(f"{reason}")