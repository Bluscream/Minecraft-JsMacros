if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary

def escape(s): return "".join([c for c in s if c.isalpha() or c.isdigit() or c == ' ']).rstrip()
hostname = escape(World.getCurrentServerAddress().split("/")[0])

import sqlite3
conn = sqlite3.connect(f'db/{hostname}.sqlite')
from datetime import datetime
def createTables():
    conn.execute('''CREATE TABLE IF NOT EXISTS "players" (
	"uuid" TEXT NOT NULL,
	"name" TEXT NULL,
	"connects" BIGINT NOT NULL,
	"last_connected" DATETIME NOT NULL,
	"time_online" BIGINT NOT NULL,
	PRIMARY KEY ("uuid"));''')
def addPlayer(uuid, name):
    conn.execute('''INSERT IF NOT EXISTS INTO "players" (
    "uuid", "name", "connects", "last_connected", "time_online"
    ) VALUES (
    '{uuid}', '{name}', 1, '{now}', 0
    );'''.format(uuid=uuid, name=name, now=datetime.now()))


createTables()
addPlayer(event.UUID, event.player.getName())
conn.close()
