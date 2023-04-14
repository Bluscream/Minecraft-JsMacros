// services start with minecraft, when enabled and are meant to be persistent scripts.
const d2d = Hud.createDraw2D()
let tpsmeter;
d2d.setOnInit(JavaWrapper.methodToJava(() => {
    tpsmeter = d2d.addText(World.getServerTPS(), 0, d2d.getHeight() - 10, 0xFFFFFF, true);
}));
const ticklistener = JsMacros.on("Tick", JavaWrapper.methodToJava(() => {
    tpsmeter?.setText(World.getServerTPS());
}));
Hud.registerDraw2D(d2d);
// this fires when the service is stopped
event.stopListener = JavaWrapper.methodToJava(() => {
    Hud.unregisterDraw2D(d2d);
    JsMacros.off(ticklistener);
});