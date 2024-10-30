import pdb
import pygame
from src.MovingObject import MovingObject
from pygame import Vector2
from math import atan2, degrees, sqrt
from src.utils.consts import FireRanges

class Barrel(MovingObject):
    def __init__(self, tank_base, barrel_pos, barrel_image, starting_angle, player_tank=None):
        super().__init__(barrel_pos, barrel_image)
        self.tank_base = tank_base
        self.angle = starting_angle
        self.image, self.rect = self.rotate_barrel(self.image_origin, self.angle, self.tank_base.pos, self.pos)
        self.player_tank = player_tank


    def update(self):
        self.image, self.rect = self.rotate_barrel(self.image_origin, self.angle, self.tank_base.pos, self.pos)

    def move(self, keys):
        if not self.tank_base.is_enemy:
            self.angle = self.calculate_angle(self.tank_base.pos, pygame.mouse.get_pos())

        elif self.tank_base.is_enemy and self.player_is_close(self.player_tank):
            self.angle = self.calculate_angle(self.tank_base.pos, self.player_tank.pos)

        self.pos = Vector2(self.tank_base.pos.x + 1, self.tank_base.pos.y + 23)

    def player_is_close(self, player_tank):
        dist = sqrt((player_tank.pos.x - self.tank_base.pos.x) ** 2 + (player_tank.pos.y - self.tank_base.pos.y) ** 2)

        if dist <= FireRanges.TANK_DETECTION_RANGE.value:
            return True
        return False

    @staticmethod
    def rotate_barrel(image, angle, pivot, origin):
        surf = pygame.transform.rotate(image, angle)
        offset = pivot + (origin - pivot).rotate(-angle)
        rect = surf.get_rect(center=offset)

        return surf, rect

    @staticmethod
    def calculate_angle(pivot, mouse_pos):
        delta_x, delta_y = mouse_pos[0] - pivot[0], mouse_pos[1] - pivot[1]

        angle = degrees(atan2(-delta_y, delta_x)) + 90
        return angle

    def check_collisions(self, game_objects):
        pass
