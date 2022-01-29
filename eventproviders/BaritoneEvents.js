/*
 * This script is designed to add events to jsmacros from baritone.
 * I'd suggest putting this on the "Profile Load" event, it only needs to be triggered once on startup.
 * @author Wagyourtail
 */

// get the class we'll be "extending"
const AbstractGameEventListener = Java.type("baritone.api.event.listener.AbstractGameEventListener");
// const BlockPos = Java.type("net.minecraft.util.math.BlockPos");

// event name
const BaritoneEvents = {
  "PathEvent": { "status": "string" },
  "BlockInteractEvent": { "pos": "BlockPos", "int": "type" }
};

// create a proxy for "extending" this class
const gameEventListenerProxyBuilder = Reflection.createClassProxyBuilder(AbstractGameEventListener);

// iterate over BaritoneEvents dictionary
Object.keys(BaritoneEvents).forEach(function(event_name) {
  JsMacros.createCustomEvent(event_name).registerEvent();
  let event_args = BaritoneEvents[event_name];
  // add a method to the proxy
  gameEventListenerProxyBuilder.addMethod(
    "onBaritone"+event_name,
    JavaWrapper.methodToJava((self, args) => {
      const evt = JsMacros.createCustomEvent("Baritone"+event_name);
      // put the path event status into the evt, similarly to how GlobalVar works,
      // this is the event object that scripts recieve so it'll be available there with `event.getString("status")`
      let i = 0;
      Object.keys(BaritoneEvents[event_name]).forEach(function(event_arg) {
        let event_arg_type = event_args[event_arg];
        if (event_arg_type == "string") evt.putString(event_arg, args[i].toString());
        else if (event_arg_type == "int") evt.putInt(event_arg, args[i]);
        else evt.putObject(event_arg, args[i]);
        i++;
      });
      // triggers the event to run async, use triggerJoin to wait for completion
      evt.trigger();
    })
  );
  //registers event so you can see it in the gui
  JsMacros.createCustomEvent("Baritone"+event_name).registerEvent();
});



// build this class proxy
const listener = gameEventListenerProxyBuilder.buildInstance([]);

//register with baritone api
Java.type("baritone.api.BaritoneAPI")
  .getProvider()
  .getPrimaryBaritone()
  .getGameEventHandler()
  .registerEventListener(listener);
