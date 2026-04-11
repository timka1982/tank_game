from enum import Enum, Flag, auto

class ScreenDimensions(Enum):
    SCREEN_WIDTH : float = 960
    SCREEN_HEIGHT : float = 720

class TankMovement(Enum):
    INITIAL_VEL = 50
    MAX_VEL = 150
    ACCELERATION = 5
    DECELERATION = 0.05
    START_ANGLE = 270


class FireRanges(Enum):
    TANK_DETECTION_RANGE = 300
    SHELL_FIRE_RANGE = 900

class ObjectTypes(Enum):
    TANK = "TANK"
    TANK_SHELL = "TANK_SHELL"

class TankState(Flag):
    IDLE = 0
    ROTATING = auto()
    MOVING = auto()
    SLOWING_DOWN = auto()



