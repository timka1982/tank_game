import pygame
import math
from pygame import Vector2


class Bullet(pygame.sprite.Sprite):
    def __init__(self, barrel_height, angle, barrel_pos, bullet_image, game_surface):
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

        # create and display animation
        shoot_animation = self.ShootingAnimation((50, 50))
        shoot_animation.draw(game_surface)

    def update(self):
        self.pos.x += 10 * math.sin(math.radians(self.angle))
        self.pos.y += 10 * math.cos(math.radians(self.angle))

        self.rect = self.image.get_rect(center=self.pos)

    class ShootingAnimation(pygame.sprite.Sprite):
        def __init__(self, shoot_pos):
            super().__init__()
            self.sprites: list = []
            self.sprites.append(pygame.image.load('./graphics/Smoke/smokeGrey0.png'))
            self.sprites.append(pygame.image.load('./graphics/Smoke/smokeGrey1.png'))
            self.sprites.append(pygame.image.load('./graphics/Smoke/smokeGrey2.png'))
            self.sprites.append(pygame.image.load('./graphics/Smoke/smokeGrey3.png'))
            self.sprites.append(pygame.image.load('./graphics/Smoke/smokeGrey4.png'))
            self.sprites.append(pygame.image.load('./graphics/Smoke/smokeGrey5.png'))
            self.current_sprite = 0
            self.animation_cooldown = 1000
            self.last_update = pygame.time.get_ticks()

            self.image = self.sprites[self.current_sprite]
            self.rect = self.image.get_rect(center=(50, 50))

        def draw(self, game_surface):
            while self.current_sprite < len(self.sprites) - 1:
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update >= self.animation_cooldown:
                    self.current_sprite += 1

                    self.image = self.sprites[self.current_sprite]
                    print(f"Drawing index {self.current_sprite}")
                    game_surface.blit(self.image, self.rect.center)
                    self.last_update = current_time
