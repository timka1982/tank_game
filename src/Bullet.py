import pygame
import math
from pygame import Vector2


class Bullet(pygame.sprite.Sprite):
    def __init__(self, angle, barrel_pos, bullet_image):
        super().__init__()
        self.angle = -(180 - angle)
        self.pos = Vector2(barrel_pos[0], barrel_pos[1])

        self.image_origin = pygame.image.load(bullet_image)
        self.image = self.image_origin

        self.image = pygame.transform.rotate(self.image_origin, self.angle)
        self.rect = self.image.get_rect(center=self.pos)

    def update(self):
        self.pos.x = self.pos.x + (3*math.cos(math.radians(self.angle)))
        self.pos.y = self.pos.y + (3*math.sin(math.radians(self.angle)))

        self.rect = self.image.get_rect(center=self.pos)
