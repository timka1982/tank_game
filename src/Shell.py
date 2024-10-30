import math
import pygame
from copy import deepcopy

from pygame import Vector2

from src.MovingObject import MovingObject
from math import sqrt
from src.utils.consts import FireRanges, ObjectTypes
from src.utils.utils import game_utils


class Shell(MovingObject):
    def __init__(self, barrel_height, barrel_angle, barrel_pos, bullet_image):
        super().__init__(barrel_pos, bullet_image)
        self.angle = barrel_angle
        self.pos = Vector2(barrel_pos[0], barrel_pos[1])

        self.image_height = self.image.get_height()

        self.image = pygame.transform.rotate(self.image_origin, self.angle + 180)
        self.pos.x += 1.5 * (barrel_height/2 + self.image_height/2) * math.sin(math.radians(self.angle))
        self.pos.y += 1.5 * (barrel_height/2 + self.image_height/2) * math.cos(math.radians(self.angle))
        self.start_pos = deepcopy(self.pos)

        # create and display animation
        # shoot_animation_pos = (barrel_pos[0] + (barrel_height/2) * math.sin(math.radians(self.angle)), barrel_pos[1] + (barrel_height/2) * math.cos(math.radians(self.angle)))
        # shoot_animation = self.ShootingAnimation(shoot_animation_pos)
        # shoot_animation.animate_shoot(game_surface)

    def update(self):
        self.rect = self.image.get_rect(center=self.pos)

    def move(self, keys):
        self.pos.x += 5 * math.sin(math.radians(self.angle))
        self.pos.y += 5 * math.cos(math.radians(self.angle))

    def check_collisions(self, game_objects):
        if game_utils.is_outside_the_window(self.pos.x, self.pos.y):
            self.alive = False

        else:
            dist = sqrt((self.start_pos.x - self.pos.x) ** 2 + (self.start_pos.y - self.pos.y) ** 2)
            if dist >= FireRanges.SHELL_FIRE_RANGE.value:
                self.alive = False

        for game_obj in game_objects:
            if self.rect.colliderect(game_obj.rect):
                if type(game_obj).__name__.upper() == ObjectTypes.TANK.value:
                    self.alive = False
                    game_obj.can_take_hits -= 1


    # class ShootingAnimation(pygame.sprite.Sprite):
    #     def __init__(self, shoot_pos):
    #         super().__init__()
    #         self.sprites: list = []
    #         for index in range(6):
    #             image_to_add = pygame.image.load(f'./graphics/Smoke/smokeGrey{index}.png')
    #             self.sprites.append( pygame.transform.scale(image_to_add, (image_to_add.get_width()*0.7,
    #                                                                       image_to_add.get_height()*0.7)))
    #
    #         self.current_sprite = 0
    #         self.animation_cooldown = 100
    #         self.last_update = pygame.time.get_ticks()
    #         self.pos = shoot_pos
    #
    #         self.image = self.sprites[self.current_sprite]
    #         self.rect = self.image.get_rect(center=self.pos)
    #
    #     def animate_shoot(self, game_surface):
    #         event_key = threading.Event()
    #         thread_key = threading.Thread(target=self.draw_animation, args=(game_surface, event_key))
    #
    #         thread_key.setDaemon(True)
    #         thread_key.start()
    #
    #     def draw_animation(self, game_surface, event_key):
    #         game_surface.blit(self.image, self.rect.center)
    #         while self.current_sprite < len(self.sprites) - 1:
    #             current_time = pygame.time.get_ticks()
    #             if current_time - self.last_update >= self.animation_cooldown:
    #                 self.current_sprite += 1
    #                 self.image = self.sprites[self.current_sprite]
    #                 # pygame.draw.circle(game_surface, (255, 0, 0), self.pos, 1)
    #                 game_surface.blit(self.image, self.image.get_rect(center=self.pos))
    #                 self.last_update = current_time
    #
    #         event_key.set()
