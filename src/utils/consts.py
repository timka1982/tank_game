from enum import Enum

class ScreenDimensions(Enum):
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080

class FireRanges(Enum):
    TANK_DETECTION_RANGE = 500
    SHELL_FIRE_RANGE = 430

class ObjectTypes(Enum):
    TANK = "TANK"
    TANK_SHELL = "TANK_SHELL"

