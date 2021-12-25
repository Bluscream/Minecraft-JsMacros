# coding=utf8
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = event.getEventName()
# Chat.getLogger().debug(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "SendMessage":
        start = event.message.split(" ")[0].lower()
        ignored_cmds = ["stop","cancel","pause","resume"]
        if start.startswith("#"):
            if start[1:] not in ignored_cmds: GlobalVars.putString("last_baritone_task", event.message[1:])
        elif start.startswith("@"):
            if start[1:] not in ignored_cmds: GlobalVars.putString("last_altoclef_task", event.message[1:])
    case "Key":
        Baritone = Reflection.getClass("baritone.api.BaritoneAPI").getProvider().getPrimaryBaritone()
        Selection = Reflection.getClass("baritone.ff")
        FillSchematic = Reflection.getClass("baritone.api.schematic.FillSchematic")
        ReplaceSchematic = Reflection.getClass("baritone.api.schematic.ReplaceSchematic")
        BetterBlockPos = Reflection.getClass("baritone.api.utils.BetterBlockPos")
        SelectionManager = Baritone.getSelectionManager()

        # newSelection = Selection(BetterBlockPos(0, 70, 0), BetterBlockPos(10, 110, 10))
        # SelectionManager.addSelection(newSelection)
        # size = newSelection.size()
        # schematic = FillSchematic(size.getX(), size.getY(), size.getZ(), type)
        # schematic = ReplaceSchematic()

        Baritone.getCommandManager().execute("sel clear")
        Baritone.getCommandManager().execute("sel pos1 0 50 0")
        Baritone.getCommandManager().execute("sel pos2 10 70 10")
        Baritone.getCommandManager().execute("sel replace grass_block stone")