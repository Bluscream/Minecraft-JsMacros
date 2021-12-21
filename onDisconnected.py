if __name__ == "": from JsMacrosAC import * #Autocomplete, not necessary
server = ""
if (GlobalVars.getString("server")):
    server = GlobalVars.getString("server").split("/")[0]

Chat.toast("Disconnected", server)