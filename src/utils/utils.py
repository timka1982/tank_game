# import numpy as np
from random import randint

class GameUtils:
	def __init__(self):
		pass

	def get_random_coord(self, start, end):
		# random_coord = random.randint(low = start, size=(1,))
		random_coord = randint(start, end)
		# return random_coord[0]
		return random_coord


game_utils = GameUtils()