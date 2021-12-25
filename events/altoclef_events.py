# coding=utf8
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = event.getEventName()
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "ProfileLoad":
        #
        # This script is designed to add events to jsmacros from baritone.
        # I'd suggest putting this on the "Profile Load" event, it only needs to be triggered once on startup.
        # @author Wagyourtail
        #

        def onAltoClefInit(self, args):
            Chat.log(f"[AltoClef] onAltoClefInit: {args[0]}")

        altoclef = Reflection.getClass("adris.altoclef.AltoClef")

        gameEventListenerProxyBuilder = Reflection.createClassProxyBuilder()

        altoclef.subscribeToPostInit(onAltoClefInit)