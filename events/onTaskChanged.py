if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "TASK_CHANGED"|"Manual":
        Vec3D = Reflection.getClass("xyz.wagyourtail.jsmacros.client.api.sharedclasses.PositionCommon$Vec3D")
        def distance(pos1, pos2): return Vec3D(pos1, pos2).getMagnitude()
        def is_altoclef_finished(RecvMessage_event): return any(x in RecvMessage_event.text.getString() for x in ["§rUser task FINISHED","§rStopped"])
        def wait_for_altoclef():
            Chat.log("Waiting for Altoclef to finish task...")
            JsMacros.waitForEvent("RecvMessage", JavaWrapper.methodToJava(is_altoclef_finished)).context.releaseLock()
            context.releaseLock()
            try: Client.waitTick()
            except Exception as e: Chat.log("§2Could not wait for altoclef to finish task!")
        def task(tasks: str):
            if not tasks: return
            for task in tasks.strip().strip(";").split(";"):
                if task and task != "":
                    Chat.log(f"[TASK] Executing {task}")
                    GlobalVars.putString('last_task', task)
                    command = task.split(" ")
                    cmd = command[0]
                    args = command[1:]
                    arg_str = ' '.join(args)
                    match cmd.lower():
                        case "/sleep": Client.waitTick(int(args[1]))
                        case "@@wait": wait_for_altoclef()
                        case "@@pickup":
                            range = int(args[0])
                            Chat.log("range: " + str(range))
                            playerPos = Player.getPlayer().getPos()
                            def simplePos(pos): return f"{int(pos.getX())} {int(pos.getY())} {int(pos.getZ())}"
                            items = []
                            for entity in World.getEntities():
                                if entity.getType() == "minecraft:item":
                                    if not range or distance(playerPos, entity.getPos()) < range: items.append(entity)
                            item_count = len(items)
                            if item_count > 0:
                                Chat.log(f"Picking up {item_count} dropped items within {range if range else 'infinity'} blocks")
                                for item in items:
                                    Chat.say(f"@goto {simplePos(item.getPos())}", True)
                                    wait_for_altoclef()
                        case _: Chat.say(cmd, True)
        task(GlobalVars.getString("task_now"))
        Chat.log("[JSMacros] Task Finished!")
        GlobalVars.remove("task_now")
