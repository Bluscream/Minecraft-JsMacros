if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
from os import makedirs
from pathlib import Path
def escape(s): return "".join([c for c in s if c.isalpha() or c.isdigit() or c == ' ']).rstrip()
hostname = escape(World.getCurrentServerAddress().split("/")[0])
event_name = escape(event.getEventName())
dir = Path('logs', hostname)
makedirs(dir, exist_ok=True)
with open(dir/f'{event_name}', "a") as myfile: myfile.write(str(vars(event))+"\n")
