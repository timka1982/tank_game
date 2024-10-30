from random import randint
from src.utils.consts import ScreenDimensions

class GameUtils:
	def __init__(self):
		pass

	@staticmethod
	def get_randint(start, end):
		return randint(start, end)

	@staticmethod
	def is_outside_the_window(x_coord, y_coord):
		if ((x_coord > ScreenDimensions.SCREEN_WIDTH.value or x_coord < 0)
				or (y_coord > ScreenDimensions.SCREEN_HEIGHT.value or y_coord < 0)):
			return True
		return False


game_utils = GameUtils()
