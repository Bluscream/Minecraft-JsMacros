var h2d = Hud.createDraw2D();
h2d.setOnInit(JavaWrapper.methodToJava(function () {
    var binds = KeyBind.getKeyBindings();
    Array.from(binds.keySet())
        .forEach(function (k, i) {
        var lines = 50;
        var width = 300;
        h2d.addText(k + ": " + binds.get(k), 20 + width * Math.floor(i / lines), 10 * (i % lines), 0x00ff00, false);
    });
    return Client;
}));
h2d.register();
event.stopListener = JavaWrapper.methodToJava(function () {
    h2d.unregister();
});