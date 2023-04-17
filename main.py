import pygame
import logging
from src.Tank import Tank


# general setup
pygame.init()
clock = pygame.time.Clock()
logging.basicConfig(filename=f"./game_proj.log", level=logging.INFO)

# game screen
win = pygame.display.set_mode((1024, 768))
background = pygame.image.load("./graphics/Environment/dirt.png")
pygame.display.set_caption("War of Tanks")
vel = 0.5


def main():
    tank = Tank(50, 50, "./graphics/Tanks/tankBlack_outline.png")
    barrel = Tank.Barrel(tank.pos_y, tank.pos_y, "./graphics/Tanks/barrelBlack_outline.png")
    tanks_group = pygame.sprite.Group()
    tanks_group.add(tank)
    tanks_group.add(barrel)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            tank.change_orientation("down")
            tank.pos_y += vel
            barrel.pos_y += vel

        if keys[pygame.K_UP]:
            tank.change_orientation("up")
            tank.pos_y -= vel
            barrel.pos_y -= vel

        if keys[pygame.K_LEFT]:
            tank.change_orientation("left")
            tank.pos_x -= vel
            barrel.pos_x -= vel

        if keys[pygame.K_RIGHT]:
            tank.change_orientation("right")
            tank.pos_x += vel
            barrel.pos_x += vel

        pygame.display.flip()
        for x in range(0, 1024, 128):
            for y in range(0, 768, 128):
                win.blit(background, (x, y))

        tanks_group.draw(win)
        tanks_group.update()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()

