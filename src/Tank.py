import pygame
import math


class Tank(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, tank_image):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = pygame.image.load(tank_image)
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.barrel = Tank.Barrel(self, self.pos_x, self.pos_y + 20, "./graphics/Tanks/barrelBlack_outline.png")
        self.orientation = "down"

    def update(self):
        self.rect.center = [self.pos_x, self.pos_y]

    def get_the_barrel(self):
        return self.barrel

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
        def __init__(self, tank_base, pos_x, pos_y, barrel_image):
            super().__init__()
            self.tank_base = tank_base
            self.pos_x = pos_x
            self.pos_y = pos_y
            self.image = pygame.image.load(barrel_image)
            self.rect = self.image.get_rect()
            self.angle = 0

        def update(self):
            self.rect.center = [self.tank_base.pos_x, self.tank_base.pos_y]

        def shoot(self, mouse_pos):
            self.rotate_barrel(mouse_pos)

        def rotate_barrel(self, mouse_pos):
            angle = self.calculate_angle(mouse_pos, (self.tank_base.pos_x, self.tank_base.pos_y))
            self.image = pygame.transform.rotate(self.image, -angle)
            self.rect = self.image.get_rect()


        @staticmethod
        def calculate_angle(target_p, gun_p):
            delta_x = target_p[0] - gun_p[0]
            delta_y = target_p[1] - gun_p[1]

            radian = math.atan2(delta_y, delta_x)
            angle = math.degrees(radian)
            print(f"Angle is {round(angle)}")

            return round(angle)
