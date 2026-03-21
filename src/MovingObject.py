import pygame
import threading


class MovingObject(pygame.sprite.Sprite):
    _image_cache = {}

    def __init__(self, pos, image):
        super().__init__()
        self.pos = pos
        if image not in MovingObject._image_cache:
            MovingObject._image_cache[image] = pygame.image.load(image).convert_alpha()
        self.image_origin = MovingObject._image_cache[image]
        self.image = self.image_origin
        self.rect = self.image.get_rect()
        self.alive = True
        self.orientation = None

    def update(self):
        pass

    def move(self, keys, dt):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def check_collisions(self, game_objects):
        pass

    def get_orientation(self):
        return self.orientation

    def set_orientation(self, orientation):
        self.orientation = orientation

    def change_orientation(self, n_orientation):
        # TODO: divide to 4 cases [down, up, right, left], switch case?
        # if self.orientation != n_orientation:
        #     match self.orientation:
        #         case "down":
        #             self._turn_from_down(n_orientation)

                # case "up":
                #     self._turn_from_up(n_orientation)
                #
                # case "right":
                #     self._turn_from_right(n_orientation)
                #
                # case "left":
                #     self._turn_from_left(n_orientation)

        self.set_orientation(n_orientation)

    # def _turn_from_down(self, n_orientation):
    #     match n_orientation:
    #         case "up":
    #             self.image = pygame.transform.rotate(self.image, -180)
    #             # self.image = pygame.transform.rotate(self.image, -180)
    #         case "right":
    #             self.image = pygame.transform.rotate(self.image, 90)
    #         case "left":
    #             self.image = pygame.transform.rotate(self.image, -90)
    #
#     def _turn_from_up(self, n_orientation):
#         match n_orientation:
#             case "down":
#                 self.image = pygame.transform.rotate(self.image, 180)
#             case "right":
#                 self.image = pygame.transform.rotate(self.image, -90)
#             case "left":
#                 self.image = pygame.transform.rotate(self.image, 90)

#     def _turn_from_right(self, n_orientation):
#         match n_orientation:
#             case "left":
#                 self.image = pygame.transform.rotate(self.image, 180)
#             case "up":
#                 self.image = pygame.transform.rotate(self.image, 90)
#             case "down":
#                 self.image = pygame.transform.rotate(self.image, -90)

#     def _turn_from_left(self, n_orientation):
#         match n_orientation:
#             case "right":
#                 self.image = pygame.transform.rotate(self.image, -180)
#             case "up":
#                 self.image = pygame.transform.rotate(self.image, -90)
#             case "down":
#                 self.image = pygame.transform.rotate(self.image, 90)

