import pygame
import math
from pygame import Vector2


class Bullet(pygame.sprite.Sprite):
    def __init__(self, barrel_height, angle, barrel_pos, bullet_image):
        super().__init__()
        self.angle = angle
        self.pos = Vector2(barrel_pos[0], barrel_pos[1])

        self.image_origin = pygame.image.load(bullet_image)
        self.image = self.image_origin
        self.image_height = self.image.get_height()

        self.image = pygame.transform.rotate(self.image_origin, self.angle + 180)
        self.pos.x += (barrel_height/2 + self.image_height/2) * math.sin(math.radians(self.angle))
        self.pos.y += (barrel_height/2 + self.image_height/2) * math.cos(math.radians(self.angle))
        self.rect = self.image.get_rect(center=self.pos)

        self.shoot_sprites = []

    def update(self):
        self.pos.x += 10 * math.sin(math.radians(self.angle))
        self.pos.y += 10 * math.cos(math.radians(self.angle))

        self.rect = self.image.get_rect(center=self.pos)
