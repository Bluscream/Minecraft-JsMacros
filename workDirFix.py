
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")

# from shutil import copyfile
        
original = r'G:\OneDrive\Games\Minecraft\altoclef_settings.json'
paths = [
    r'C:\tools\MultiMC\instances\Fabric 1.18.1\.minecraft\altoclef_settings.json',
    r'G:\OneDrive\Games\Minecraft\config\jsMacros\Macros\altoclef_settings.json',
    r'G:\OneDrive\Games\Minecraft\config\jsMacros\Macros\events\altoclef_settings.json',
    r'G:\OneDrive\Games\Minecraft\config\jsMacros\Macros\tasks\altoclef_settings.json',
    r'G:\OneDrive\Games\Minecraft\config\jsMacros\Macros\work\altoclef_settings.json'
]
for path in paths:
    FS.copy(original, path)
Client.waitTick()
Chat.say("@reload_settings")

