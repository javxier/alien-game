import pygame as pg
from vector import Vector
from pygame.sprite import Sprite, Group
from timer import Timer
from random import randint


class AlienFleet:
    alien_exploding_images = [pg.image.load(f'images/rainbow_explode{n}.png') for n in range(8)]
    alien_images = [pg.image.load(f'images/alien{n}.bmp') for n in range(2)]

    def __init__(self, game, v=Vector(1, 0)):
        self.game = game
        self.ship = self.game.ship
        self.settings = game.settings
        self.screen = self.game.screen
        self.screen_rect = self.screen.get_rect()
        self.v = v
        alien = Alien(self.game, image_list=AlienFleet.alien_images)
        self.alien_h, self.alien_w = alien.rect.height, alien.rect.width
        self.fleet = Group()
        self.create_fleet()

    def create_fleet(self):
        n_cols = self.get_number_cols(alien_width=self.alien_w)
        n_rows = self.get_number_rows(ship_height=self.ship.rect.height,
                                      alien_height=self.alien_h)
        for row in range(n_rows):
            for col in range(n_cols):
                self.create_alien(row=row, col=col)

    def set_ship(self, ship): self.ship = ship
    def create_alien(self, row, col):
        x = self.alien_w * (2 * col + 1)
        y = self.alien_h * (2 * row + 1)
        images = AlienFleet.alien_images
        # alien = Alien(game=self.game, ul=(x, y), v=self.v, image_list=images, 
        #               start_index=randint(0, len(images) - 1))
        alien = Alien(game=self.game, ul=(x, y), v=self.v, image_list=images)
        self.fleet.add(alien)

    def empty(self): self.fleet.empty()
    def get_number_cols(self, alien_width):
        spacex = self.settings.screen_width - 2 * alien_width
        return int(spacex / (2 * alien_width))

    def get_number_rows(self, ship_height, alien_height):
        spacey = self.settings.screen_height - 3 * alien_height - ship_height
        return int(spacey / (2 * alien_height))

    def length(self): return len(self.fleet.sprites())

    def change_v(self, v):
        for alien in self.fleet.sprites():
            alien.change_v(v)

    def check_bottom(self): 
      for alien in self.fleet.sprites():
        if alien.check_bottom():
            self.ship.hit()
            break
      
    def check_edges(self): 
      for alien in self.fleet.sprites():
        if alien.check_edges(): return True
      return False

    def update(self):
        delta_s = Vector(0, 0)    # don't change y position in general
        if self.check_edges():
            self.v.x *= -1
            self.change_v(self.v)
            delta_s = Vector(0, self.settings.fleet_drop_speed)
        if pg.sprite.spritecollideany(self.ship, self.fleet) or self.check_bottom():
            print("ship hit!")
            self.ship.hit()
        for alien in self.fleet.sprites():
            alien.update(delta_s=delta_s)

    def draw(self):
        for alien in self.fleet.sprites():
            alien.draw()


class Alien(Sprite):
    def __init__(self, game, image_list, start_index=0, ul=(0, 100), v=Vector(1, 0)):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.image = pg.image.load('images/alien0.bmp')
        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = ul
        self.ul = Vector(ul[0], ul[1])   # position
        self.v = v                       # velocity
        self.image_list = image_list
        self.exploding_timer = Timer(image_list=AlienFleet.alien_exploding_images, delay=200, 
                                     start_index=start_index, is_loop=False)
        self.normal_timer = Timer(image_list=image_list, delay=1000, is_loop=True)
        self.timer = self.normal_timer
        self.dying = False

    def change_v(self, v): self.v = v
    def check_bottom(self): return self.rect.bottom >= self.screen_rect.bottom
    def check_edges(self):
        r = self.rect
        return r.right >= self.screen_rect.right or r.left <= 0

    def hit(self): 
      self.timer = self.exploding_timer
      self.dying = True

    def update(self, delta_s=Vector(0, 0)):
        if self.dying and self.timer.is_expired():
          self.kill()
        self.ul += delta_s
        self.ul += self.v * self.settings.alien_speed_factor
        self.rect.x, self.rect.y = self.ul.x, self.ul.y

    def draw(self):  
      image = self.timer.image()
      rect = image.get_rect()
      rect.x, rect.y = self.rect.x, self.rect.y
      self.screen.blit(image, rect)
      # self.screen.blit(self.image, self.rect)

      