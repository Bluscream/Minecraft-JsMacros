
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
from json import dumps
from datetime import datetime
logger = Chat.getLogger()
event_name = event.getEventName()
def sleep(sec: int): Client.waitTick(sec * 20)
def is_finished(RecvMessage_event): return any(x in RecvMessage_event.text.getString() for x in ["§rUser task FINISHED","§rStopped"])
match event_name:
    case "NIGHT_START":
        Chat.toast("NIGHT_START","")
    case "JoinServer"|"Key":# "DAY_START"|"":
        Chat.getLogger().info(event)
        if event.action == 1:
            if event.key == "key.keyboard.keypad.7":
                pass
                # sleep(6)
                # Chat.say("#set disconnectOnArrival false", true)
                # Chat.say("#set allowBreak false", true)
                # Chat.say("#set allowPlace false", true)
                # cmd = "@goto 9067 -12398 overworld"
                # Chat.say(cmd)
                # RecvMessage_event = JsMacros.waitForEvent("RecvMessage", JavaWrapper.methodToJava(is_finished)).context.releaseLock()
                # Client.waitTick(2)
                # Chat.toast("Altoclef Finished",cmd)
                # Chat.say("#set allowBreak true", true)
                # Chat.say("#set allowPlace true", true)
                # cmd = "@get log 512"
                # Chat.say(cmd)
            elif event.key == "key.keyboard.keypad.8":
                Chat.say("#set disconnectOnArrival false", True)
                Chat.say("#set allowBreak false", True)
                Chat.say("#set allowPlace false", True)
                cmd = f"@goto 9068 -12401 overworld"
                Chat.say(cmd, True)
                # context.releaseLock()
                # JsMacros.waitForEvent("RecvMessage")
                Chat.say(datetime.now(), True)
                JsMacros.waitForEvent("RecvMessage", JavaWrapper.methodToJava(is_finished)).context.releaseLock()
                Chat.say(datetime.now(), True)
                context.releaseLock()
                # Client.waitTick()
                Chat.toast("Altoclef Finished",cmd)
                Chat.say("@test bed", True)
                Chat.say("geht", True)