/*
 * This script is designed to add events to jsmacros from baritone.
 * I'd suggest putting this on the "Profile Load" event, it only needs to be triggered once on startup.
 * @author Wagyourtail
 */


// get the class we'll be "extending"
const AbstractGameEventListener = Java.type("baritone.api.event.listener.AbstractGameEventListener");

// event name
const BaritonePathEvent = "BaritonePathEvent";

// create a proxy for "extending" this class
const gameEventListenerProxyBuilder = Reflection.createClassProxyBuilder(AbstractGameEventListener);
JsMacros.createCustomEvent(BaritonePathEvent).registerEvent();

// add a method to the proxy
gameEventListenerProxyBuilder.addMethod("onPathEvent", JavaWrapper.methodToJava((self, args) => {
    const evt = JsMacros.createCustomEvent(BaritonePathEvent);
    // put the path event status into the evt, similarly to how GlobalVar works,
    // this is the event object that scripts recieve so it'll be available there with `event.getString("status")`
    evt.putString("status", args[0].toString());
    // triggers the event to run async, use triggerJoin to wait for completion
    evt.trigger();
}));

//registers event so you can see it in the gui
JsMacros.createCustomEvent(BaritonePathEvent).registerEvent();

// build this class proxy
const listener = gameEventListenerProxyBuilder.buildInstance([]);

//register with baritone api
Java.type("baritone.api.BaritoneAPI").getProvider().getPrimaryBaritone().getGameEventHandler().registerEventListener(listener);