# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 16:44:17 2021

@author: DELL
"""

import sys
import pygame as py
from settings import Settings
from round import Pipes
from bird import Bird
import floor



class Flappy_Bird:
    def __init__(self):
        py.init()
        py.mixer.init()
        self.settings = Settings()
        self.clock = py.time.Clock()
        self.screen = py.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.background = py.image.load('images/background2.png')
        py.display.set_caption('Flappy Bird')
        self.bird = Bird(self)
        self.pipes_class = Pipes(self)
        self.frame = 0
        self.zero = py.image.load('images/0.png')
        self.one = py.image.load('images/1.png')
        self.two = py.image.load('images/2.png')
        self.three = py.image.load('images/3.png')
        self.four = py.image.load('images/4.png')
        self.five = py.image.load('images/5.png')
        self.six = py.image.load('images/6.png')
        self.seven = py.image.load('images/7.png')
        self.eight = py.image.load('images/8.png')
        self.nine = py.image.load('images/9.png')
        self.num_list = [self.zero,self.one,self.two,self.three,self.four,self.five
                         ,self.six,self.seven,self.eight,self.nine]
        '''self.start_mixer = py.mixer.Sound("audio/start.wav")
        self.die_mixer = py.mixer.Sound('audio/die.wav')
        self.hit_mixer = py.mixer.Sound('audio/hit.wav')
        self.flap_mixer = py.mixer.Sound('audio/flap.wav')'''
    
    def run_game(self):
        while True:
            '''self.start_mixer.play()'''
            self.check_events()
            self.bird.cal_score(self.pipes_class.pipes)
            self.update_screen()
           # self.change_speed()
            if self.bird.if_bird_strike(self.pipes_class.pipes):
                '''self.hit_mixer.play()
                self.die_mixer.play()'''
                return
    
    def check_events(self):
        #可以用空格键或者鼠标左键控制控制小鸟扇动翅膀
        self.bird.flap = 0
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            elif event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    '''self.flap_mixer.play()'''
                    self.bird.flap = 1
            elif event.type == py.MOUSEBUTTONDOWN:
                if py.mouse.get_pressed(3) == (1,0,0):
                    '''self.flap_mixer.play()'''
                    self.bird.flap = 1
                       
    def update_screen(self):
        self.screen.blit(self.background, (0,0))
        self.pipes_class.control_pipes()
        floor.load_floor(self)
        self.bird.draw(self)

        #这里有个问题如果把这段代码作为函数的话，得分将无法显示
        #显示得分
        s = str(self.bird.score)
        for m in range(len(s)):
            if m==0:
                self.screen.blit(self.num_list[int(s[m])], 
                (self.settings.screen_width/2-1.5*self.zero.get_width(),64))
            elif m==1:
                self.screen.blit(self.num_list[int(s[m])], 
                (self.settings.screen_width/2-0.5*self.zero.get_width(),64))
            else:
                self.screen.blit(self.num_list[int(s[m])], 
                (self.settings.screen_width/2+0.5*self.zero.get_width(),64))
                
        py.display.flip()
        
        self.clock.tick(self.settings.fps)
        self.update_frame()
        
    def update_frame(self):
        self.frame += 1
        if self.frame > self.settings.fps:
            self.frame = 0
            
    '''def change_speed(self):
        #根据得分情况改变速度，属于游戏的逻辑控制，之后如果有更多的逻辑调整可以放在里面,改变函数的名字
        if 10 <=self.bird.score<= 20 and self.settings.pipe_speed<= 2:
            self.settings.pipe_speed += 0.01
        elif 20 <self.bird.score<= 30 and self.settings.pipe_speed <=3:
            self.settings.pipe_speed += 0.02'''
        
        
    
if __name__ == '__main__':
    fly = Flappy_Bird()
    fly.run_game()
