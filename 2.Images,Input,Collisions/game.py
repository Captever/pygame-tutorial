import sys

import pygame

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("ninja game")
        self.screen = pygame.display.set_mode((640, 480))

        self.clock = pygame.time.Clock()

        self.img = pygame.image.load('../resources/data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0, 0, 0)) # black to transparency

        self.img_pos = [160, 260]
        self.movement = [False, False] # up, down movement
        self.move_speed = 5

        self.collision_area = pygame.Rect(50, 50, 300, 50)

    def run(self):
        while True:
            self.screen.fill((14, 219, 248)) # fill with rgb colorkey

            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height()) # x, y, width, height
            # Same as; img_r = pygame.Rect(*self.img_pos, *self.img.get_size())

            # if the image touches the collision area
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0, 50, 155), self.collision_area)

            self.img_pos[1] += (self.movement[1] - self.movement[0]) * self.move_speed
            self.screen.blit(self.img, self.img_pos) # zero by top-left

            for event in pygame.event.get():
                # when quit button is pressed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # when the key is pressed down
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.movement[0] = True
                    if event.key == pygame.K_s:
                        self.movement[1] = True
                # when the key is pressed up
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.movement[0] = False
                    if event.key == pygame.K_s:
                        self.movement[1] = False
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()