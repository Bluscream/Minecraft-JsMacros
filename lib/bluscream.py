# coding=utf8
# if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
from dataclasses import dataclass
# region Server
from ipaddress import ip_address
@dataclass
class Server:
    """"""
    hostname: str
    address: ip_address
    port: int = 25565
def getServer(server: str) -> Server:
    server_ = server.split("/")
    address = server_[1].split(":")
    return Server(hostname=server_[0], address=ip_address(address[0]), port=int(address[1]))
import string
string.getServer = getServer
del getServer
# endregion

# region enums
from enum import Enum
class EventEnum(Enum):
    AirChange = "AirChange"
    ArmorChange = "ArmorChange"
    BlockUpdate = "BlockUpdate"
    Bossbar = "Bossbar"
    ChunkLoad = "ChunkLoad"
    ChunkUnload = "ChunkUnload"
    CodeRender = "CodeRender"
    CommandContext = "CommandContext"
    Custom = "Custom"
    Damage = "Damage"
    Death = "Death"
    DimensionChange = "DimensionChange"
    Disconnect = "Disconnect"
    EXPChange = "EXPChange"
    EntityDamaged = "EntityDamaged"
    EntityLoad = "EntityLoad"
    EntityUnload = "EntityUnload"
    FallFlying = "FallFlying"
    HeldItemChange = "HeldItemChange"
    HungerChange = "HungerChange"
    ItemDamage = "ItemDamage"
    ItemPickup = "ItemPickup"
    JoinServer = "JoinServer"
    JoinedTick = "JoinedTick"
    Key = "Key"
    OpenScreen = "OpenScreen"
    PlayerJoin = "PlayerJoin"
    PlayerLeave = "PlayerLeave"
    ProfileLoad = "ProfileLoad"
    RecvMessage = "RecvMessage"
    ResourcePackLoaded = "ResourcePackLoaded"
    Riding = "Riding"
    SendMessage = "SendMessage"
    Service = "Service"
    SignEdit = "SignEdit"
    Sound = "Sound"
    Tick = "Tick"
    Title = "Title"

# endregion