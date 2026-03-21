from enum import Enum, Flag, auto

class ScreenDimensions(Enum):
    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 720

class TankMovement(Enum):
    INITIAL_VEL = 50
    MAX_VEL = 150
    ACCELERATION = 5
    DECELERATION = 0.05

class FireRanges(Enum):
    TANK_DETECTION_RANGE = 300
    SHELL_FIRE_RANGE = 270

class ObjectTypes(Enum):
    TANK = "TANK"
    TANK_SHELL = "TANK_SHELL"

class TankState(Flag):
    IDLE = 0
    ROTATING = auto()
    MOVING = auto()
    SLOWING_DOWN = auto()



