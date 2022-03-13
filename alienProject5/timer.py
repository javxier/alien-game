import pygame as pg


class Timer:
  def __init__(self, image_list, start_index=0, delay=100, is_loop=True): 
    self.image_list = image_list
    self.start_index = start_index
    self.delay = delay 
    self.is_loop = is_loop
    self.last_time_switched = pg.time.get_ticks()
    self.frames = len(image_list)
    self.index = start_index if start_index < len(image_list) - 1 else 0

    
  def next_frame(self): 
    # if a one-pass timer that has finished
    if not self.is_loop and self.index == len(self.image_list) - 1: return 
    now = pg.time.get_ticks()

    if now - self.last_time_switched > self.delay:
      self.index += 1
      if self.is_loop: self.index %= self.frames
      self.last_time_switched = now

  def is_expired(self): 
    return not self.is_loop and self.index == len(self.image_list) - 1

  def reset(self): self.index = self.start_index
  def image(self): 
    self.next_frame()
    return self.image_list[self.index]


class CommandTimer(Timer):
  def __init__(self, image_list, start_index=0, delay=100, is_loop=True): 
    super().__init__(image_list, start_index, delay, is_loop)

def next_frame(self): 
      # if a one-pass timer that has finished
  if not self.is_loop and self.index == len(self.image_list) - 1: return 
  now = pg.time.get_ticks()

  self.index += 1
  if self.is_loop: self.index %= self.frames
  self.last_time_switched = now

  # def is_expired(self): pass 
  # def reset(self): pass 

def image(self): 
  return self.image_list[self.index]
