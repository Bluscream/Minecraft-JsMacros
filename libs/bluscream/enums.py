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

class InventorySlots(Enum):
    Crafting_upper_left = 1
    Crafting_upper_right = 2
    Crafting_lower_left = 3
    Crafting_lower_right = 4
    Helmet = 5
    Chestplate = 6
    Leggings = 7
    Shoes = 8
    Inventory1 = 9
    Inventory27 = 35
    Hotbar1 = 36
    Hotbar9 = 44
    Offhand = 45
# endregion