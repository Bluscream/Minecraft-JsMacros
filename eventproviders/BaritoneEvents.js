/*
 * This script is designed to add events to jsmacros from baritone.
 * I'd suggest putting this on the "Profile Load" event, it only needs to be triggered once on startup. 
 * @author Wagyourtail
 */
const AbstractGameEventListener = Java.type("baritone.api.event.listener.AbstractGameEventListener");
const gameEventListenerProxyBuilder = Reflection.createClassProxyBuilder(AbstractGameEventListener);
gameEventListenerProxyBuilder.addMethod("onPathEvent", JavaWrapper.methodToJavaAsync((self, args) => {
    Chat.log(args[0]);
}));
const listener = gameEventListenerProxyBuilder.buildInstance([]);
Java.type("baritone.api.BaritoneAPI").getProvider().getPrimaryBaritone().getGameEventHandler().registerEventListener(listener);