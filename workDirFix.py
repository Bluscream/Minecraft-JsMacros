if __name__ == "": from JsMacrosAC import *
Chat.log(f"Executing {file.getName()}")

Client.waitTick()

# from shutil import copyfile

FS.copy(r'S:\multimc\instances\Fabric 1.18.1\minecraft\altoclef_settings.json', r'S:\multimc\instances\Fabric 1.18.1\minecraft\config\jsMacros\Macros\altoclef_settings.json')
Chat.say("@reload_settings")
# copyfile(r'S:\multimc\instances\Fabric 1.18.1\minecraft\altoclef_settings.json', r'S:\multimc\instances\Fabric 1.18.1\minecraft\config\jsMacros\Macros\config\sodium-extra-options.json')
# copyfile(r'S:\multimc\instances\Fabric 1.18.1\minecraft\altoclef_settings.json', r'S:\multimc\instances\Fabric 1.18.1\minecraft\config\jsMacros\Macros\work\config\sodium-extra-options.json')
