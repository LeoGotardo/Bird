import pygame as pg
from sys import exit
import random
from icecream import ic

class Game():
    def __init__(self):
        pg.init()
        
        global score
        global bird_start_possiton
        global font
        global win_height
        global win_width
        global game_stopped
        
        scroll_speed = 1
        score = 0
        win_height = 720
        win_width = 551
        bird_start_possiton = (100, 250)
        font = pg.font.SysFont("Segoe", 26)
        game_stopped = True
        
        self.clock = pg.time.Clock()
        
        self.bird_images = [pg.image.load("frames/bird_down.png"),
                            pg.image.load("frames/bird_mid.png"),
                            pg.image.load("frames/bird_up.png")]
        self.skyline_image = pg.image.load("frames/background.png")
        self.ground_image = pg.image.load("frames/floor.png")
        self.top_pipe_image = pg.image.load("frames/pipe_top.png")
        self.bottom_pipe_image = pg.image.load("frames/pipe_bottom.png")
        self.game_over_image = pg.image.load("frames/game_over.png")
        self.start_image = pg.image.load("frames/start.png")
        
        self.window = pg.display.set_mode((win_width, win_height))
        
        self.initialize()
        
    def quit_game(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game_stopped = False
                exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.game_stopped = False
                exit()
                
    def initialize(self):
        bird = pg.sprite.GroupSingle()
        bird.add(Bird(self.bird_images))
        
        pipe_timer = 0
        pipes = pg.sprite.Group()
        
        x_pos_ground, y_pos_ground = 0, 520
        
        ground = pg.sprite.Group()
        ground.add(Ground(x_pos_ground, y_pos_ground, self.ground_image))
        
        self.game_stopped = True
        
        while self.game_stopped:
            self.quit_game()
            
            self.window.fill((0, 0, 0))
            
            user_input = pg.key.get_pressed()
            
            self.window.blit(self.skyline_image, (0, 0))
            
            if len(ground) <= 2:
                ground.add(Ground(win_width, y_pos_ground, self.ground_image))
            
            pipes.draw(self.window)
            ground.draw(self.window)
            bird.draw(self.window)
            
            score_text = font.render('Score: ' + str(score), True, (255, 255, 255))
            self.window.blit(score_text, (20, 20))
           
            if bird.sprite.alive: 
                pipes.update()
                ground.update()
            bird.update(user_input)
            
            collision_pipes = pg.sprite.spritecollide(bird.sprites()[0], pipes, False)
            collision_ground = pg.sprite.spritecollide(bird.sprites()[0], ground, False)
            
            if collision_pipes or collision_ground:
                bird.sprite.alive = False
                if collision_ground:
                    self.window.blit(self.game_over_image, (win_width // 2 - self.game_over_image.get_width() // 2,
                                                            win_height // 2 - self.game_over_image.get_height() // 2))
                    if user_input[pg.K_r]:
                        score = 0
                        break
                        
            
            if pipe_timer <= 0 and not bird.sprite.alive:
                x_top, x_bottom = 550, 550
                y_top = random.randint(-600, -480)
                y_bottom = y_top + random.randint(90, 130) + self.bottom_pipe_image.get_height()

                pipes.add(Pipe(x_top, y_top, self.top_pipe_image , 'top'))
                pipes.add(Pipe(x_bottom, y_bottom, self.bottom_pipe_image, 'bottom'))
                pipe_timer = random.randint(180, 250)
            pipe_timer -= 1
            
            self.clock.tick(60)
            pg.display.update()
    
    def menu(self):
        while game_stopped:
            self.quit_game()
            self.window.fill((0, 0, 0)) 
            self.window.blit(self.skyline_image, (0, 0))
            self.window.blit(self.bird_images[0], (100, 250))
            self.window.blit(win_width // 2 - self.start_image.get_width() // 2,
                            win_height // 2 - self.start_image.get_height() // 2)
            
            user_imput = pg.key.get_pressed()
            
            if user_imput[pg.K_SPACE]:
                self.initialize()


class Ground(pg.sprite.Sprite):
    def __init__(self, x, y, image):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
    
    def update(self):
        self.rect.x -= Game.scroll_speed
        if self.rect.x <= -Game.win_width:
            self.kill()


class Bird(pg.sprite.Sprite):
    def __init__(self, image):
        pg.sprite.Sprite.__init__(self)
        
        self.bird_images = image
        self.image = self.bird_images[0]
        
        self.rect = self.image.get_rect()
        self.rect.center = bird_start_possiton
        
        self.image_index = 0
        self.vel = 0
        self.flap = False
        self.alive = True
            
    def update(self, user_input):
        if self.alive:
            self.image_index += 1
        if self.image_index >= 30:
            self.image_index = 0
        self.image = self.bird_images[self.image_index//10]
        
        self.vel += 0.5
        
        if self.vel > 7:
            self.vel = 7
        if self.rect.y < 500: 
            self.rect.y += int(self.vel)
        if self.vel == 0:
            self.flap = False
        if user_input[pg.K_SPACE] and not self.flap and self.rect.y > 0 and self.alive:
            self.flap = True
            self.vel = -7
            
        self.image = pg.transform.rotate(self.image, self.vel*-7)
        

class Pipe(pg.sprite.Sprite):
    def __init__(self, x, y, image, pipe_type):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.enter, self.exit, self.passed = False, False, False
        self.pipe_type = pipe_type
        
    def update(self):
        self.rect.x -= Game.scroll_speed
        if self.rect.x <= -Game.win_width:
            self.kill()
        if self.pipe_type == 'bottom':
            if bird_start_possiton[0] > self.rect.topleft[0] and not self.passed:
                self.enter = True
            if bird_start_possiton[0] < self.rect.toprigth[0] and not self.exit:
                self.exit = True    
            if self.enter and not self.exit and not self.passed:
                score += 1
        
        
if __name__ == "__main__":
    game = Game()
