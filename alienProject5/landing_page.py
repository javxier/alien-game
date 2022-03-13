# from decimal import HAVE_CONTEXTVAR
# import imghdr
import pygame as pg
import sys
from alien import Alien
from vector import Vector
from button import Button
from sound import Sound


GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (130, 130, 130)


class LandingPage:
    # alien_one_imgs = [pg.image.load(f'images/tie{n}.png') for n in range(5)]
    # alien_two_imgs = [pg.image.load(f'images/alienOne{n}.png') for n in range(2)]
    # alien_three_imgs = [pg.image.load(f'images/green_alien{n}.png') for n in range(2)]
    # ufo_imgs = [pg.image.load(f'images/alien2_{n}.bmp') for n in range(4)]

    alien_one_imgs = [pg.transform.rotozoom(pg.image.load(f'images/alien__0{n}.png'), 0, 0.25) for n in range(2)]
    alien_two_imgs = [pg.transform.rotozoom(pg.image.load(f'images/alien__1{n}.png'), 0, 0.25) for n in range(2)]
    alien_three_imgs = [pg.transform.rotozoom(pg.image.load(f'images/alien__2{n}.png'), 0, 0.25) for n in range(2)]
    ufo_imgs = [pg.transform.rotozoom(pg.image.load(f'images/ufo__{n}.png'), 0, 0.7) for n in range(2)]

    def __init__(self, game):
        self.sound = game.sound
        self.screen = game.screen
        self.landing_page_finished = False
        self.highscore = game.stats.get_highscore()

        headingFont = pg.font.SysFont(None, 192)
        subheadingFont = pg.font.SysFont(None, 122)
        font = pg.font.SysFont(None, 48)

        strings = [('SPACE', WHITE, headingFont), ('INVADERS', GREEN, subheadingFont),
                ('= 10 PTS', GREY, font), ('= 20 PTS', GREY, font),
                            ('= 40 PTS', GREY, font), ('= ???', GREY, font),
               # ('PLAY GAME', GREEN, font), 
                (f'HIGH SCORE = {self.highscore:,}', GREY, font)]

        self.texts = [self.get_text(msg=s[0], color=s[1], font=s[2]) for s in strings]

        self.posns = [150, 230]
        alien = [65 * x + 350 for x in range(4)]
        # play_high = [x for x in range(650, 760, 80)]
        # play_high = 730
        self.posns.extend(alien)
        self.posns.append(730)

        centerx = self.screen.get_rect().centerx

        self.play_button = Button(self.screen, "PLAY GAME", ul=(centerx - 150, 650))

        n = len(self.texts)
        self.rects = [self.get_text_rect(text=self.texts[i], centerx=centerx, centery=self.posns[i]) for i in range(n)]
        self.alien_one = Alien(game=game, sound=self.sound, alien_index=0, image_list=LandingPage.alien_one_imgs,
                               v=Vector(), ul=(centerx - 140, 335))
        self.alien_two = Alien(game=game, sound=self.sound, alien_index=1, image_list=LandingPage.alien_two_imgs,
                               v=Vector(), ul=(centerx - 140, 400))
        self.alien_three = Alien(game=game, sound=self.sound, alien_index=2, image_list=LandingPage.alien_three_imgs,
                               v=Vector(), ul=(centerx - 140, 465))
        self.ufo = Alien(game=game, sound=self.sound, alien_index=3, image_list=LandingPage.ufo_imgs,
                               v=Vector(), ul=(centerx - 120, 530))

        self.hover = False

    def get_text(self, font, msg, color): return font.render(msg, True, color, BLACK)

    def get_text_rect(self, text, centerx, centery):
        rect = text.get_rect()
        rect.centerx = centerx
        rect.centery = centery
        return rect

    def mouse_on_button(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        return self.play_button.rect.collidepoint(mouse_x, mouse_y)
    
    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                sys.exit()
            if e.type == pg.KEYUP and e.key == pg.K_p:   # pretend PLAY BUTTON pressed
                self.landing_page_finished = True        
            elif e.type == pg.MOUSEBUTTONDOWN:
                if self.mouse_on_button():
                    self.landing_page_finished = True
            elif e.type == pg.MOUSEMOTION:
                if self.mouse_on_button() and not self.hover:
                    self.play_button.toggle_colors()
                    self.hover = True
                elif not self.mouse_on_button() and self.hover:
                    self.play_button.toggle_colors()
                    self.hover = False


    def update(self):       # TODO make aliens move
        pass 

    def show(self):
        while not self.landing_page_finished:
            self.update()
            self.draw()
            self.check_events()   # exits game if QUIT pressed

    def draw_text(self):
        n = len(self.texts)
        for i in range(n):
            self.screen.blit(self.texts[i], self.rects[i])

    def draw(self):
        self.screen.fill(BLACK)
        self.alien_one.draw()
        self.alien_two.draw()
        self.alien_three.draw()
        self.ufo.draw()
        self.draw_text()
        self.play_button.draw()
        # self.alien_fleet.draw()   # TODO draw my aliens
        # self.lasers.draw()        # TODO dray my button and handle mouse events
        pg.display.flip()
