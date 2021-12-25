if __name__ == "": from JsMacrosAC import *
screen = Hud.getOpenScreen()
Chat.toast(f"{Hud.getOpenScreenName()}","")
for button in screen.getButtonWidgets():
    Chat.getLogger().warn(f"{button.getText()}","")