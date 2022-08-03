from urllib.parse import quote


if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "TASK_CHANGED"|"Manual":
        from os import environ
        from datetime import datetime
        from urllib.parse import quote_plus
        def AutoMagic(path: str, params = {}):
            try: Request.get(f"http://{environ.get('IP_Timo-Tablet')}:1122/{path}?{'&'.join([k+'='+quote_plus(v) for (k,v) in params.items()])}&password={environ.get('AMAPI_PW')}")
            except Exception as ex: Chat.getLogger().error(f"Could not send AutoMagic request: {ex}")
        Vec3D = Reflection.getClass("xyz.wagyourtail.jsmacros.client.api.sharedclasses.PositionCommon$Vec3D")
        def distance(pos1, pos2): return Vec3D(pos1, pos2).getMagnitude()
        def is_altoclef_finished(RecvMessage_event): return any(x in RecvMessage_event.text.getString() for x in ["§rUser task FINISHED","§rStopped"])
        def wait_for_altoclef(task: str):
            Chat.log("Waiting for Altoclef to finish task...")
            # Chat.log("Waiting for Altoclef"+": "+task)
            JsMacros.waitForEvent("RecvMessage", JavaWrapper.methodToJava(is_altoclef_finished)).context.releaseLock()
            context.releaseLock()
            try: Client.waitTick()
            except Exception as e: Chat.log("§2Could not wait for altoclef to finish task!")
        def task(tasks: str):
            if not tasks: return
            tasks = tasks.strip().strip(";").split(";;")
            for task in tasks:
                if task and task != "":
                    Chat.log(f"[TASK] Executing {task}")
                    Chat.getLogger().info(f"[TASK] Executing {task}")
                    GlobalVars.putString('last_task', task)
                    command = task.split(" ")
                    cmd = command[0]
                    args = command[1:]
                    # arg_str = ' '.join(args)
                    match cmd.lower():
                        case ",sleep": Client.waitTick(int(args[1]))
                        case ",disconnect": Client.disconnect()
                        case ",quit"|",exit": Client.shutdown()
                        case "@@wait": wait_for_altoclef(task)
                        case "@@pickup"|"##pickup":
                            range = int(args[0]) if len(args) > 0 else 0
                            target_id = args[1].lower() if len(args) > 1 else None
                            playerPos = Player.getPlayer().getPos()
                            def simplePos(pos): return f"{int(pos.getX())} {int(pos.getY())} {int(pos.getZ())}"
                            items = dict()
                            for entity in World.getEntities():
                                if entity.getType() == "minecraft:item":
                                    pos = entity.getPos()
                                    if not range or distance(playerPos, pos) < range: items[pos] = entity
                            item_count = len(items)
                            if item_count > 0:
                                Chat.log(f"Picking up {item_count} dropped items within {range if range else 'infinity'} blocks")
                                for pos, item in items.items():
                                    if item.isAlive() and (target_id is None or item.asItem().getItemID()==target_id):
                                        Chat.say(f"{cmd[0]}goto {simplePos(pos)}", True)
                                        wait_for_altoclef(task)
                                Chat.log("JsMacros"+": "+f"Finished picking up {item_count} dropped items")
                        case _: Chat.say(task, True)
            msg = f"Finished {len(tasks)} tasks"
            Chat.log("JSMacros"+": "+msg)
            Client.waitTick()
            AutoMagic("screen/on")
            Client.waitTick(10)
            AutoMagic("notification/create", {"title": f'[JSMacros] {msg}', "bigmessage": str(datetime.now()), "icon": "app.icon://com.mojang.minecraftpe"})
        task(GlobalVars.getString("task_now"))
        GlobalVars.remove("task_now")
