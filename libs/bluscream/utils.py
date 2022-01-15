if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
#from dataclasses import dataclass

# class Utils
class Utils:
    @staticmethod
    def sleep(secs: int, Client: FClient):
        for _ in range(secs): Client.waitTick()
    @staticmethod
    def getEventName(event: None): return (event.eventName if hasattr(event, 'eventName') else event.getEventName()) if event else "Manual"
#endregion