
### Advanced Topics in Object Oriented Programming

#### game.py
```python
# File for Game class

import pygame
import random

class Game:
  def __init__(self, bird_img, pipe_img, background_img, ground_img):
    self.bird = pygame.image.load(bird_img).convert_alpha()
    self.bird_rect = self.bird.get_rect(center = (70, 180))
    self.pipe = pygame.image.load(pipe_img).convert_alpha()
    self.background = pygame.image.load(background_img).convert_alpha()
    self.ground= pygame.image.load(ground_img).convert()
    self.ground_position = 0
    self.active = True
    self.gravity = 0.05
    self.bird_movement = 0
    self.rotated_bird = pygame.Surface((0, 0))
    self.pipes = []
    self.pipe_height = [280, 425, 562]
    self.score = 0
    self.font = pygame.font.SysFont(None, 48)
    self.high_score = 0

  def resize_images(self):
    self.bird = pygame.transform.scale(self.bird, (51, 34))
    self.pipe = pygame.transform.scale(self.pipe, (80, 438))
    self.ground = pygame.transform.scale(self.ground, (470, 160))
    self.background = pygame.transform.scale(self.background, (400, 720))

  def show_background(self, screen):
    screen.blit(self.background, (0,0))

  def show_ground(self, screen):
    screen.blit(self.ground, (self.ground_position, 650))
    screen.blit(self.ground, (self.ground_position + 470, 650))

  def move_ground(self):
    self.ground_position -= 1
    if self.ground_position <= -400:
      self.ground_position = 0

  def show_bird(self, screen):
    screen.blit(self.rotated_bird, self.bird_rect)

  def update_bird(self):
    self.bird_movement += self.gravity
    self.rotated_bird = self.rotate_bird()
    self.bird_rect.centery += self.bird_movement

  def rotate_bird(self):
    new_bird = pygame.transform.rotozoom(self.bird,-self.bird_movement * 3, 1)
    return new_bird

  def flap(self):
    self.bird_movement = 0
    self.bird_movement -= 2.5

  def add_pipe(self):
    random_pipe_pos = random.choice(self.pipe_height)
    bottom_pipe = self.pipe.get_rect(midtop = (600, random_pipe_pos))
    top_pipe = self.pipe.get_rect(midbottom = (600, random_pipe_pos - 211))
    self.pipes.append(bottom_pipe)
    self.pipes.append(top_pipe)

  def move_pipes(self):
    for pipe in self.pipes:
      pipe.centerx -= 1.75
      if pipe.centerx <= -40:
        self.pipes.remove(pipe)

  def show_pipes(self, screen):
    for pipe in self.pipes:
      if pipe.bottom >= 700:
        screen.blit(self.pipe, pipe)
      else:
        flip_pipe = pygame.transform.flip(self.pipe, False, True)
        screen.blit(flip_pipe, pipe)

  def check_collision(self):
    for pipe in self.pipes:
      if self.bird_rect.colliderect(pipe):
        self.active = False

    if self.bird_rect.top <= -100 or self.bird_rect.bottom >= 650:
      self.active = False

  def update_score(self):
    self.score += 0.01

  def show_score(self, game_state, screen, color):
    score_surface = self.font.render('Score: {:d}'.format(int(self.score)), True, color)
    score_rect = score_surface.get_rect(center=(200, 75))
    screen.blit(score_surface, score_rect)

    if game_state == 'game_over':
      restart_text1 = self.font.render('Press Space Bar', True, color)
      restart_rect1 = restart_text1.get_rect(center=(200, 280))
      screen.blit(restart_text1, restart_rect1)

      restart_text2 = self.font.render('to Play Again', True, color)
      restart_rect2 = restart_text2.get_rect(center=(200, 340))
      screen.blit(restart_text2, restart_rect2)

      high_score_surface = self.font.render('High Score: {:d}'.format(int(self.high_score)), True, color)
      high_score_rect = high_score_surface.get_rect(center=(200, 610))
      screen.blit(high_score_surface, high_score_rect)

  def game_over(self, screen, color):
    self.update_high_score()
    self.show_score('game_over', screen, color)

  def update_high_score(self):
    if self.score > self.high_score:
      self.high_score = self.score

  def restart(self):
    self.active = True
    del self.pipes[:]
    self.bird_rect.center = (70, 180)
    self.bird_movement = 0
    self.score = 0
```

#### lab6.py

```python
# Flappy Bird clone

import pygame
import sys
from game import Game

pygame.init()
screen = pygame.display.set_mode((400, 720))
clock = pygame.time.Clock()

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1800)

game = Game('student_folder/flappy_bird/bird.png', 'student_folder/flappy_bird/pipe.png', 'student_folder/flappy_bird/background.png', 'student_folder/flappy_bird/ground.png')
game.resize_images()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE and game.active:
        game.flap()

      if event.key == pygame.K_SPACE and game.active == False:
        game.restart()

    if event.type == SPAWNPIPE:
      game.add_pipe()

  game.show_background(screen)

  if game.active:
    game.show_bird(screen)
    game.update_bird()
    game.move_pipes()
    game.show_pipes(screen)
    game.check_collision()
    game.update_score()
    game.show_score('playing', screen, (255, 255, 255))
  else:
    game.game_over(screen, (255, 255, 255))

  game.show_ground(screen)
  game.move_ground()

  pygame.display.update()
  clock.tick(120)
```


#### Output

Polymorphism Tutorial Lab 1 Output

<img src="OOP_Unit11_Game1.jpg" alt="Game picture 1" width="500"/>
<img src="OOP_Unit11_Game2.jpg" alt="Game picture 2" width="500"/>

---

[Return to Module 2 Unit 11](OOP_Unit11.md)
