# coding=utf8
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
start = event.message.split(" ")[0].lower()
ignored_cmds = ["stop","cancel","pause","resume"]
if start.startswith("#"):
    if start[1:] not in ignored_cmds: GlobalVars.putString("last_baritone_task", event.message[1:])
elif start.startswith("@"):
    if start[1:] not in ignored_cmds: GlobalVars.putString("last_altoclef_task", event.message[1:])