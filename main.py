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

log_file = Path("./game_proj.log")
if log_file.is_file():
    log_file.unlink()

logging.basicConfig(filename="./game_proj.log", level=logging.INFO)

# game screen
win = pygame.display.set_mode(size=(ScreenDimensions.SCREEN_WIDTH.value, ScreenDimensions.SCREEN_HEIGHT.value))
background = pygame.image.load("./graphics/Environment/sand.png").convert()
pygame.display.set_caption("War of Tanks")


def main():
    moving_items_group = pygame.sprite.Group()

    player_tank = Tank(tank_pos=Vector2(200, 200),
                tank_image="./graphics/Tanks/tankRed_outline.png",
                barrel_image="./graphics/Tanks/barrelRed_outline.png",
                is_enemy=False)


    moving_items_group.add(player_tank)
    moving_items_group.add(player_tank.barrel)

    # for i in range(2):
    #     enemy_x = game_utils.get_randint(int(ScreenDimensions.SCREEN_WIDTH.value/2), ScreenDimensions.SCREEN_WIDTH.value)
    #     enemy_y = game_utils.get_randint(1, ScreenDimensions.SCREEN_HEIGHT.value)
    #
    #     enemy_tank = Tank(tank_pos=Vector2(enemy_x, enemy_y),
    #                       tank_image="./graphics/Tanks/tankRed_outline.png",
    #                       barrel_image="./graphics/Tanks/barrelRed_outline.png",
    #                       is_enemy=True,
    #                       player_tank=player_tank)
    #
    #     moving_items_group.add(enemy_tank)
    #     moving_items_group.add(enemy_tank.barrel)

    run = True

    while run:
        click = False
        fps = clock.get_fps()
        dt = clock.tick(60) / 1000.0
        pygame.display.set_caption(f'FPS: {fps}')

        events_list = pygame.event.get()
        for event in events_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

            if event.type == pygame.QUIT:
                run = False

        for x in range(0, ScreenDimensions.SCREEN_WIDTH.value, 128):
            for y in range(0, ScreenDimensions.SCREEN_HEIGHT.value, 128):
                win.blit(background, (x, y))

        if click:
            player_tank.shoot(game_surface=win)
            moving_items_group.add(player_tank.shell)

        keys = pygame.key.get_pressed()
        for index, item in enumerate(moving_items_group):
            if item.alive:
                item.move(keys, dt)
                item.check_collisions([remain_item for remain_index, remain_item in enumerate(moving_items_group) if remain_item.alive and remain_index != index])
            else:   
                # if object is "dead" remove it
                moving_items_group.remove(item)

        moving_items_group.update()
        moving_items_group.draw(win)

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    print(sys.version_info)
    main()
