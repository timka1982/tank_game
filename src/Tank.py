import pygame
import logging
from pygame import Vector2
from math import atan2, degrees


class Tank(pygame.sprite.Sprite):
    def __init__(self, tank_pos, tank_image):
        super().__init__()
        self.pos = tank_pos
        self.image = pygame.image.load(tank_image)
        # self.image = pygame.transform.scale(self.image, (self.image.get_height()/2, self.image.get_width()/2))
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.orientation = "down"

    def update(self):
        self.rect = self.image.get_rect(center=self.pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def get_orientation(self):
        return self.orientation

    def set_orientation(self, orientation):
        self.orientation = orientation

    def change_orientation(self, n_orientation):
        # TODO: divide to 4 cases [down, up, right, left], switch case?
        match self.orientation:
            case "down":
                self._turn_from_down(n_orientation)

            case "up":
                self._turn_from_up(n_orientation)

            case "right":
                self._turn_from_right(n_orientation)

            case "left":
                self._turn_from_left(n_orientation)

        self.set_orientation(n_orientation)

    def _turn_from_down(self, n_orientation):
        match n_orientation:
            case "up":
                self.image = pygame.transform.rotate(self.image, -180)
            case "right":
                self.image = pygame.transform.rotate(self.image, 90)
            case "left":
                self.image = pygame.transform.rotate(self.image, -90)

    def _turn_from_up(self, n_orientation):
        match n_orientation:
            case "down":
                self.image = pygame.transform.rotate(self.image, 180)
            case "right":
                self.image = pygame.transform.rotate(self.image, -90)
            case "left":
                self.image = pygame.transform.rotate(self.image, 90)

    def _turn_from_right(self, n_orientation):
        match n_orientation:
            case "left":
                self.image = pygame.transform.rotate(self.image, 180)
            case "up":
                self.image = pygame.transform.rotate(self.image, 90)
            case "down":
                self.image = pygame.transform.rotate(self.image, -90)

    def _turn_from_left(self, n_orientation):
        match n_orientation:
            case "right":
                self.image = pygame.transform.rotate(self.image, -180)
            case "up":
                self.image = pygame.transform.rotate(self.image, -90)
            case "down":
                self.image = pygame.transform.rotate(self.image, 90)

    class Barrel(pygame.sprite.Sprite):
        def __init__(self, tank_base, barrel_image, starting_angle=0):
            super().__init__()
            self.tank_base = tank_base
            self.angle = starting_angle
            self.pos = Vector2(self.tank_base.pos.x + 1, self.tank_base.pos.y + 23)

            self.image_origin = pygame.image.load(barrel_image)
            self.image = self.image_origin
            self.image_height = self.image.get_height()

            self.rect = self.image.get_rect(center=self.pos)
            self.image, self.rect = rotate_barrel(self.image_origin, self.angle, self.tank_base.pos, self.pos)

        def update(self):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    self.angle = calculate_angle(self.tank_base.pos, pygame.mouse.get_pos())
                    # print(f"My angle is {self.angle}")

            self.pos = Vector2(self.tank_base.pos.x + 1, self.tank_base.pos.y + 23)
            self.image, self.rect = rotate_barrel(self.image_origin, self.angle, self.tank_base.pos, self.pos)

        # def draw(self, surface):
        #     surface.blit(self.image, self.rect)


def rotate_barrel(image, angle, pivot, origin):
    surf = pygame.transform.rotate(image, angle)
    offset = pivot + (origin - pivot).rotate(-angle)
    rect = surf.get_rect(center=offset)

    return surf, rect


def calculate_angle(pivot, mouse_pos):
    delta_x, delta_y = mouse_pos[0] - pivot[0], mouse_pos[1] - pivot[1]

    angle = degrees(atan2(-delta_y, delta_x)) + 90
    return angle
