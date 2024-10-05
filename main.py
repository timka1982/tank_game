import sys
import pygame
import logging
from src.Tank import Tank
from pygame import Vector2
from src.Bullet import Bullet
from pathlib import Path
from src.utils.utils import game_utils


# general setup
pygame.init()
clock = pygame.time.Clock()

log_file = Path(f"./game_proj.log")
if log_file.is_file():
    log_file.unlink()

logging.basicConfig(filename=f"./game_proj.log", level=logging.INFO)

# game screen
win = pygame.display.set_mode((1920, 1080), flags=pygame.SCALED)
background = pygame.image.load("./graphics/Environment/sand.png")
pygame.display.set_caption("War of Tanks")
vel = 0.5


def main():
    tanks_group = pygame.sprite.Group()
    tank = Tank(Vector2(200, 200), "./graphics/Tanks/tankBlack_outline.png")
    barrel = Tank.Barrel(tank, "./graphics/Tanks/barrelBlack_outline.png", starting_angle=360)

    tanks_group.add(tank)
    tanks_group.add(barrel)

    enemy_x = game_utils.get_random_coord(int(1920/2), 1920)
    enemy_y = game_utils.get_random_coord(1, 1080)

    enemy_tank = Tank(Vector2(enemy_x, enemy_y), "./graphics/Tanks/tankRed_outline.png")
    enemy_barrel = Tank.Barrel(enemy_tank, "./graphics/Tanks/barrelRed_outline.png", starting_angle=360)

    tanks_group.add(enemy_tank)
    tanks_group.add(enemy_barrel)

    
    run = True

    while run:
        click = False
        fps = clock.get_fps()
        pygame.display.set_caption(f'FPS: {fps}')

        events_list = pygame.event.get()
        for event in events_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip()
        win.fill((255, 255, 255))
        # for x in range(0, 1024, 128):
            # for y in range(0, 768, 128):
                # win.blit(background, (x, y))

        if click:
            bullet = Bullet(barrel.image_height, barrel.angle, barrel.rect.center,
                            "./graphics/Bullets/bulletBeige_outline.png", win)
            tanks_group.add(bullet)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            tank.change_orientation("down")
            tank.pos.y += vel

        if keys[pygame.K_w]:
            tank.change_orientation("up")
            tank.pos.y -= vel

        if keys[pygame.K_a]:
            tank.change_orientation("left")
            tank.pos.x -= vel

        if keys[pygame.K_d]:
            tank.change_orientation("right")
            tank.pos.x += vel

        tanks_group.update()
        tanks_group.draw(win)

        # pygame.draw.circle(win, (0,0,255), tank.rect.midbottom, 1)
        # pygame.draw.circle(win, (255,0,0), barrel.rect.center, 1)

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    print(sys.version_info)
    main()
