# coding=utf8
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
# Chat.getLogger().debug(f"Executing {file.getName()}")
if event.getEventName() == "Key":
    #
    # This script is designed to add events to jsmacros from baritone.
    # I'd suggest putting this on the "Profile Load" event, it only needs to be triggered once on startup.
    # @author Wagyourtail

    def onPathEvent(self, args):
        Chat.log(f"[Baritone] onPathEvent: {args[0]}")

    AbstractGameEventListener = Reflection.getClass("baritone.api.event.listener.AbstractGameEventListener")

    gameEventListenerProxyBuilder = Reflection.createClassProxyBuilder(AbstractGameEventListener)

    gameEventListenerProxyBuilder.addMethod("onPathEvent", JavaWrapper.methodToJavaAsync(onPathEvent))

    listener = gameEventListenerProxyBuilder.buildInstance([])

    Reflection.getClass("baritone.api.BaritoneAPI").getProvider().getPrimaryBaritone().getGameEventHandler().registerEventListener(listener)