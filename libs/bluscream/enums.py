
def test_path(Chat):
    import sys
    for path in sys.path:
        Chat.log(path)


# region enums
from enum import Enum, auto
class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name
class Events(AutoName):
    AirChange = auto()
    ArmorChange = auto()
    BlockUpdate = auto()
    Bossbar = auto()
    ChunkLoad = auto()
    ChunkUnload = auto()
    CodeRender = auto()
    CommandContext = auto()
    Custom = auto()
    Damage = auto()
    Death = auto()
    DimensionChange = auto()
    Disconnect = auto()
    EXPChange = auto()
    EntityDamaged = auto()
    EntityLoad = auto()
    EntityUnload = auto()
    FallFlying = auto()
    HeldItemChange = auto()
    HungerChange = auto()
    ItemDamage = auto()
    ItemPickup = auto()
    JoinServer = auto()
    JoinedTick = auto()
    Key = auto()
    OpenScreen = auto()
    PlayerJoin = auto()
    PlayerLeave = auto()
    ProfileLoad = auto()
    RecvMessage = auto()
    ResourcePackLoaded = auto()
    Riding = auto()
    SendMessage = auto()
    Service = auto()
    SignEdit = auto()
    Sound = auto()
    Tick = auto()
    Title = auto()

# endregion