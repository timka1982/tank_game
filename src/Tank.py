from random import randint
import pygame
import operator
from src.MovingObject import MovingObject
from src.Barrel import Barrel
from src.Shell import Shell
from pygame import Vector2
from src.utils.utils import game_utils
from src.utils.consts import TankState, TankMovement

class Tank(MovingObject):
	def __init__(self, tank_pos, tank_image, barrel_image, is_enemy, player_tank=None):
		super().__init__(tank_pos, tank_image, )
		self.is_enemy=is_enemy
		self.orientation = "up"
		self.angle = TankMovement.START_ANGLE.value
		self.vel = TankMovement.INITIAL_VEL.value
		self.barrel = Barrel(tank_base=self, barrel_pos=Vector2(tank_pos.x + 1, tank_pos.y + 23),
							 barrel_image=barrel_image, starting_angle = randint(0, 360), player_tank=player_tank)
		self.can_take_hits = 5
		self.shell = None
		self.state = TankState.IDLE
		self.slowing_down = False
		self.rotation_speed = 0.5
		self.direction_map = {
			pygame.K_w: ("up", Vector2(0, -1)),
			pygame.K_s: ("down", Vector2(0, 1)),
			pygame.K_a: ("left", Vector2(-1, 0)),
			pygame.K_d: ("right", Vector2(1, 0))
		}
		self.op = None

	def update(self):
		if self.state == TankState.ROTATING:
			self.angle = self.op(self.angle, 3) % 360
			self.image = pygame.transform.rotate(self.image_origin, self.angle - 270)
			if self.angle == self.target_angle:
				self.state = TankState.IDLE
				self.target_angle = None

		self.rect = self.image.get_rect(center=self.pos)

		if self.shell and not self.shell.alive:
			del self.shell
			self.shell = None

	def draw(self, surface):
		surface.blit(self.image, self.rect)

	def handle_velocity(self, keys, dt):
		if not any(
				[
					keys[pygame.K_s],
					keys[pygame.K_w],
					keys[pygame.K_d],
					keys[pygame.K_a]
				]
		):
			if self.vel > 0:
				self.state = TankState.SLOWING_DOWN
				self.vel -= TankMovement.DECELERATION.value * dt
				if self.vel < 0:
					self.vel = 0
				self.slow_down_the_vehicle(self.get_orientation(), dt)
			else:
				self.state = TankState.IDLE

	def slow_down_the_vehicle(self, orientation, dt):
		match orientation:
			case "down":
				self.pos.y += self.vel * dt
			case "up":
				self.pos.y -= self.vel * dt
			case "left":
				self.pos.x -= self.vel * dt
			case "right":
				self.pos.x += self.vel * dt

	def is_change_direction(self, current_key_direction):
		if self.orientation != current_key_direction:
			self.state = TankState.ROTATING
			angle_map = {
				"up": {
					"left": 90, 
					"right": -90,
					"down": -180, 
					},
				"down": {
					"up": 180,
					"left": -90,
					"right": 90
				},
				"left": {
					"up": -90,
					"down": 90,
					"right": -180
				},
				"right": {
					"up": 90,
					"down": -90,
					"left": 180
				}
			}
			self.target_angle = (self.angle + angle_map[self.orientation][current_key_direction]) % 360
			print(f"Target angle: {self.target_angle}\nCurrent angle {self.angle}")
			self.op = operator.sub if self.target_angle < self.angle else operator.add
			self.set_orientation(current_key_direction)

	# move the pos coordinates of the object
	def move(self, keys, dt):
		if self.is_enemy:
			return
		
		elif self.state != TankState.ROTATING:
			for key, (direction, vec) in self.direction_map.items():
				if keys[key]:
					self.is_change_direction(direction)
					if self.vel < TankMovement.MAX_VEL.value:
						self.vel += TankMovement.ACCELERATION.value * dt
						self.vel = min(self.vel, TankMovement.MAX_VEL.value)
					displacement = vec * self.vel * dt
					new_pos = self.pos + displacement
					if not game_utils.is_outside_the_window(new_pos.x, new_pos.y):
						self.pos = new_pos
					break

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
							   "./graphics/Bullets/bulletBeige_outline.png"
							   )