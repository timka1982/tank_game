import pygame
import logging
from src.Tank import Tank
from pygame import Vector2
from src.Bullet import Bullet
from pathlib import Path


# general setup
pygame.init()
clock = pygame.time.Clock()

log_file = Path(f"./game_proj.log")
if log_file.is_file():
    log_file.unlink()

logging.basicConfig(filename=f"./game_proj.log", level=logging.INFO)

# game screen
win = pygame.display.set_mode((800, 600), flags=pygame.SCALED)
background = pygame.image.load("./graphics/Environment/sand.png")
pygame.display.set_caption("War of Tanks")
vel = 0.5


def main():
    tank = Tank(Vector2(200, 200), "./graphics/Tanks/tankBlack_outline.png")
    barrel = Tank.Barrel(tank, "./graphics/Tanks/barrelBlack_outline.png", starting_angle=45)
    tanks_group = pygame.sprite.Group()

    tanks_group.add(tank)
    tanks_group.add(barrel)

    run = True

    while run:
        click = False
        fps = clock.get_fps()
        pygame.display.set_caption(f'FPS: {fps}')

        events_list = pygame.event.get()
        for event in events_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        pygame.display.flip()
        for x in range(0, 1024, 128):
            for y in range(0, 768, 128):
                win.blit(background, (x, y))

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

        for event in events_list:
            if event.type == pygame.QUIT:
                run = False

        tanks_group.update()
        tanks_group.draw(win)

        # pygame.draw.circle(win, (0,0,255), tank.rect.midbottom, 1)
        # pygame.draw.circle(win, (255,0,0), barrel.rect.center, 1)

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
