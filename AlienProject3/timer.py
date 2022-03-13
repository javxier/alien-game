import pygame as pg


class Timer:
  def __init__(self, image_list, start_index=0, delay=100, is_loop=True): 
    self.image_list = image_list
    self.delay = delay 
    self.is_loop = is_loop
    self.last_time_switched = pg.time.get_ticks()
    self.frames = len(image_list)
    self.index = start_index if start_index < len(image_list) - 1 else 0

    
  def next_frame(self): 
    now = pg.time.get_ticks()
    if now - self.last_time_switched > self.delay:
      self.index += 1
      if self.is_loop: self.index %= self.frames
      self.last_time_switched = now

  def is_expired(self): return not self.is_loop and self.index == len(self.image_list) - 1

  def image(self): 
    self.next_frame()
    return self.image_list[self.index]

# this code goes in Alien class
# alien_images = [pg.image.load(f'images/alien{n}.bmp') for n in range(4)]
# alien_explosion_images = [pg.image.load(f'images/alien_explosion{n}.bmp') for n in range(6)]

# self.regular_timer = Timer(image_list=alien_images)
# self.explosion_timer = Timer(image_list=alien_explosion_images, delay=200, is_loop=False)
# self.timer = self.regular_timer

# def update(self): 
#   # ...
#   # if killed... logic
#     self.timer = self.explosion_timer
#     self.timer = self.regular_timer

#   def draw(self):  
#     image = self.timer.image()
#     rect = image.get_rect()
#     self.screen.blit(image, rect)