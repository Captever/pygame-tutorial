import sys

import pygame

from scripts.entities import PhysicsEntity
from scripts.utils import load_image, load_images
from scripts.tilemap import Tilemap

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("ninja game")
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

        self.tilemap = Tilemap(self, tile_size = 16)

    def run(self):
        while True:
            self.display.fill((14, 219, 248)) # fill with rgb colorkey

            self.tilemap.render(self.display)

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            for event in pygame.event.get():
                # when quit button is pressed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # when the key is pressed down
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        self.player.velocity[1] = -3
                # when the key is pressed up
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()