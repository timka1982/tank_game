import sys
import pygame
import logging

from src.Tank import Tank
from src.utils.consts import ScreenDimensions
from pygame import Vector2
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
win = pygame.display.set_mode(size=(ScreenDimensions.SCREEN_WIDTH.value, ScreenDimensions.SCREEN_HEIGHT.value),
                              flags=pygame.SCALED)
background = pygame.image.load("./graphics/Environment/sand.png").convert()
pygame.display.set_caption("War of Tanks")
vel = 0.5


def main():
    moving_items_group = pygame.sprite.Group()

    player_tank = Tank(tank_pos=Vector2(200, 200),
                tank_image="./graphics/Tanks/tankBlack_outline.png",
                barrel_image="./graphics/Tanks/barrelBlack_outline.png",
                is_enemy=False)


    moving_items_group.add(player_tank)
    moving_items_group.add(player_tank.barrel)

    for i in range(2):
        enemy_x = game_utils.get_randint(int(1920/2), 1920)
        enemy_y = game_utils.get_randint(1, 1080)

        enemy_tank = Tank(tank_pos=Vector2(enemy_x, enemy_y),
                          tank_image="./graphics/Tanks/tankRed_outline.png",
                          barrel_image="./graphics/Tanks/barrelRed_outline.png",
                          is_enemy=True,
                          player_tank=player_tank)

        moving_items_group.add(enemy_tank)
        moving_items_group.add(enemy_tank.barrel)

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
        for x in range(0, 1920, 128):
            for y in range(0, 1080, 128):
                win.blit(background, (x, y))

        if click:
            player_tank.shoot(game_surface=win)
            moving_items_group.add(player_tank.shell)

        keys = pygame.key.get_pressed()
        for index, item in enumerate(moving_items_group):
            if item.alive:
                item.move(keys)
                item.check_collisions([remain_item for remain_index, remain_item in enumerate(moving_items_group) if remain_item.alive and remain_index != index])
            else:
                # if object is "dead" remove it
                moving_items_group.remove(item)

        moving_items_group.update()
        moving_items_group.draw(win)

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    print(sys.version_info)
    main()
