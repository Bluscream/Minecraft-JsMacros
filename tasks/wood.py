
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
match event_name:
    case "NIGHT_START":
        Chat.toast("NIGHT_START","")
    case "JoinServer"|"Key":# "DAY_START"|"":
        if event.action == 1:
            def sleep(sec: int): Client.waitTick(sec * 20)
            def is_finished(RecvMessage_event): return any(x in RecvMessage_event.text.getString() for x in ["§rUser task FINISHED","§rStopped"])
            if event.key == "key.keyboard.keypad.7":
                pass
                # sleep(6)
                # Chat.say("#set disconnectOnArrival false", True)
                # Chat.say("#set allowBreak false", True)
                # Chat.say("#set allowPlace false", True)
                # cmd = "@goto 9067 -12398 overworld"
                # Chat.say(cmd, True)
                # RecvMessage_event = JsMacros.waitForEvent("RecvMessage", JavaWrapper.methodToJava(is_finished)).context.releaseLock()
                # Client.waitTick(2)
                # Chat.toast("Altoclef Finished",cmd)
                # Chat.say("#set allowBreak true", True)
                # Chat.say("#set allowPlace true", True)
                # cmd = "@get log 512"
                # Chat.say(cmd, True)
            elif event.key == "key.keyboard.keypad.8":
                Chat.say("#set disconnectOnArrival false", True)
                Chat.say("#set allowBreak false", True)
                Chat.say("#set allowPlace false", True)
                cmd = f"@goto 8957 71 -12439 overworld" # 
                Chat.say(cmd, True)
                JsMacros.waitForEvent("RecvMessage", JavaWrapper.methodToJava(is_finished)).context.releaseLock()
                context.releaseLock()
                Client.waitTick()
                Chat.toast("Altoclef Finished",cmd)
                Chat.say("@test bed", True)
