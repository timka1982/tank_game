from random import randint
import pygame
from src.MovingObject import MovingObject
from src.Barrel import Barrel
from src.Shell import Shell
from pygame import Vector2
from src.utils.utils import game_utils

class Tank(MovingObject):
	def __init__(self, tank_pos, tank_image, barrel_image, is_enemy, player_tank=None):
		super().__init__(tank_pos, tank_image, )
		self.is_enemy=is_enemy
		self.orientation = "down"
		self.vel = 1.5
		self.image = pygame.transform.rotate(self.image, 180)
		self.barrel = Barrel(tank_base=self, barrel_pos=Vector2(tank_pos.x + 1, tank_pos.y + 23),
							 barrel_image=barrel_image, starting_angle = randint(0, 360), player_tank=player_tank)
		self.can_take_hits = 5
		self.shell = None

	def update(self):
		self.rect = self.image.get_rect(center=self.pos)

		# loop that checks that if there is a shell
		# and that shell is outdated [collided with something, got out of the game window
		# or got out of his range]
		if self.shell and not self.shell.alive:
			del self.shell
			self.shell = None

	def draw(self, surface):
		surface.blit(self.image, self.rect)

	# move the pos coordinates of the object
	def move(self, keys):
		if not self.is_enemy:
			if keys[pygame.K_s] and not game_utils.is_outside_the_window(self.pos.x, self.pos.y + self.vel):
				# tank.change_orientation("down")
				self.pos.y += self.vel

			if keys[pygame.K_w] and not game_utils.is_outside_the_window(self.pos.x, self.pos.y - self.vel):
				# tank.change_orientation("up")
				self.pos.y -= self.vel

			if keys[pygame.K_a] and not game_utils.is_outside_the_window(self.pos.x - self.vel, self.pos.y):
				# tank.change_orientation("left")
				self.pos.x -= self.vel

			if keys[pygame.K_d] and not game_utils.is_outside_the_window(self.pos.x + self.vel, self.pos.y):
				# tank.change_orientation("right")
				self.pos.x += self.vel

		else:
			if not game_utils.is_outside_the_window(self.pos.x, self.pos.y - self.vel):
				self.pos.y -= 0.5


	def get_if_enemy(self):
		return self.is_enemy

	def check_collisions(self, game_objects):
		if self.can_take_hits == 0:
			self.alive = False
			self.barrel.alive = False
			return


	def shoot(self, game_surface):
		if self.shell is None:
			self.shell = Shell(self.barrel.image.get_height(),
							self.barrel.angle,
							self.barrel.rect.center,
							"./graphics/Bullets/bulletBeige_outline.png")