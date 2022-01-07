# coding=utf8
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = event.getEventName()
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case _:
        Client.waitTick()

        # from shutil import copyfile

        # FS.copy(r'C:\tools\multimc\instances\Fabric 1.18.1\minecraft\altoclef_settings.json', r'C:\tools\multimc\instances\Fabric 1.18.1\minecraft\config\jsMacros\Macros\altoclef_settings.json')
        # FS.copy(r'C:\tools\multimc\instances\Fabric 1.18.1\minecraft\altoclef_settings.json', r'C:\tools\multimc\instances\Fabric 1.18.1\minecraft\config\jsMacros\Macros\events\altoclef_settings.json')
        Chat.say("@reload_settings")
        # copyfile(r'C:\tools\multimc\instances\Fabric 1.18.1\minecraft\altoclef_settings.json', r'C:\tools\multimc\instances\Fabric 1.18.1\minecraft\config\jsMacros\Macros\config\sodium-extra-options.json')
        # copyfile(r'C:\tools\multimc\instances\Fabric 1.18.1\minecraft\altoclef_settings.json', r'C:\tools\multimc\instances\Fabric 1.18.1\minecraft\config\jsMacros\Macros\work\config\sodium-extra-options.json')
