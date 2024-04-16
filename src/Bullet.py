import math
import pygame
import threading

from pygame import Vector2


class Bullet(pygame.sprite.Sprite):
    def __init__(self, barrel_height, angle, barrel_pos, bullet_image, game_surface):
        super().__init__()
        print(f"My barrel position: {barrel_pos}")
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
        shoot_animation_pos = (barrel_pos[0] + (barrel_height/2) * math.sin(math.radians(self.angle)), barrel_pos[1] + (barrel_height/2) * math.cos(math.radians(self.angle)))
        shoot_animation = self.ShootingAnimation(shoot_animation_pos)
        shoot_animation.animate_shoot(game_surface)
        # shoot_animation.draw(game_surface)

    def update(self):
        self.pos.x += 10 * math.sin(math.radians(self.angle))
        self.pos.y += 10 * math.cos(math.radians(self.angle))

        self.rect = self.image.get_rect(center=self.pos)

    class ShootingAnimation(pygame.sprite.Sprite):
        def __init__(self, shoot_pos):
            super().__init__()
            self.sprites: list = []
            for index in range(6):
                image_to_add = pygame.image.load(f'./graphics/Smoke/smokeGrey{index}.png')
                self.sprites.append(pygame.transform.scale(image_to_add, (image_to_add.get_width()*0.7,
                                                                          image_to_add.get_height()*0.7)))

            self.current_sprite = 0
            self.animation_cooldown = 50
            self.last_update = pygame.time.get_ticks()
            self.pos = shoot_pos

            self.image = self.sprites[self.current_sprite]
            self.rect = self.image.get_rect(center=self.pos)

        def animate_shoot(self, game_surface):
            event_key = threading.Event()
            thread_key = threading.Thread(target=self.draw_animation, args=(game_surface, event_key))

            thread_key.setDaemon(True)
            thread_key.start()

        def draw_animation(self, game_surface, event_key):
            game_surface.blit(self.image, self.rect.center)
            while self.current_sprite < len(self.sprites) - 1:
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update >= self.animation_cooldown:
                    self.current_sprite += 1
                    self.image = self.sprites[self.current_sprite]
                    pygame.draw.circle(game_surface, (255, 0, 0), self.pos, 1)
                    game_surface.blit(self.image, self.image.get_rect(center=self.pos))
                    self.last_update = current_time

            event_key.set()
