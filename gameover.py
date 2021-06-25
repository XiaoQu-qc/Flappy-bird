# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 19:03:24 2021

@author: DELL
"""

import sys
import pygame as py
from settings import Settings
import floor

class Gameover:
    def __init__(self):
        py.init()
        self.settings = Settings()
        self.clock = py.time.Clock()
        self.screen = py.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        py.display.set_caption('Flappy Bird')
        
        self.background = py.image.load('images/background2.png')
        self.gameover_image = py.image.load('images/gameover.png')
        
        self.gameover_x = (self.settings.screen_width-self.gameover_image.get_width())/2
        self.gameover_y = (self.settings.floor_pos-self.gameover_image.get_height())/2
        #self.frame = 0
        
    def execute(self):
        while True:
            for event in py.event.get():
                if event.type ==py.QUIT:
                    py.quit()
                    sys.exit()
                if event.type == py.KEYDOWN and event.key == py.K_SPACE:
                    return
                if event.type == py.MOUSEBUTTONDOWN:
                    if py.mouse.get_pressed(3) == (1,0,0):
                        return
                    
            self.screen.blit(self.background, (0,0))
            floor.load_floor(self)
            self.screen.blit(self.gameover_image,(self.gameover_x,self.gameover_y))
            #self.screen.blit(self.bird_image, (self.settings.screen_width*0.2,self.settings.screen_height/2))
            py.display.flip()
            self.clock.tick(self.settings.fps)
            