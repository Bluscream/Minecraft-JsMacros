
if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
logger = Chat.getLogger()
event_name = (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
# logger.info(f"Executing {file.getName()} on event {event_name}")
match event_name:
    case "BED_START":
        Chat.toast("Bed Start","Bed Start")
    case "BED_END":
        Chat.toast("Bed End","Bed End")
    case "Key":# "DAY_START"|"":
        if event.action == 1:
            if event.key == "key.keyboard.keypad.9":
                Chat.say("@wait")
                # for i in range(1,10):
                #     Chat.say(f"@goto {i} -12398 overworld", True)
                #     RecvMessage_event = JsMacros.waitForEvent("RecvMessage", JavaWrapper.methodToJava(is_finished)).context.releaseLock()
                #     Client.waitTick(2)
                #     Chat.toast("Altoclef Finished",f"@goto {i} -12398 overworld")
                #     sleep(2)
        # def sleep(sec: int): Client.waitTick(sec * 20)
        # def task(task: str):
        #     if not task: return
        #     for cmd in task.split(";"):
        #         if cmd and cmd != "":
        #             Chat.log(f"[{type}] Executing {cmd}")
        #             if (cmd.startswith("/sleep ")):
        #                 slp_time = cmd.replace("/sleep ", "")
        #                 sleep(int(slp_time))
        #             else: Chat.say(cmd, True)
        # Chat.log("Key: " + event_name)
        # Chat.say("@goto 8957 71 -12448 overworld")
        # def is_finished(RecvMessage_event):
        #     message = RecvMessage_event.text.getString()
        #     return "User task FINISHED" in message
        # RecvMessage_event = JsMacros.waitForEvent("RecvMessage", JavaWrapper.methodToJava(is_finished)).event
        # Chat.toast("finished","finished")
        
        # GlobalVars.putString("altoclef_tasks", "@goto 8957 71 -12432 overworld;@goto 8957 71 -12448 overworld")

# last = GlobalVars.getBoolean('is_night')
# timer = True
# while timer:
#     is_night = GlobalVars.getBoolean('is_night')
#     if (is_night != last):
#         last = is_night
#         if (is_night): Chat.log("is_night changed to true")
#         else: Chat.log("is_night changed to false")
#     Client.waitTick(20)