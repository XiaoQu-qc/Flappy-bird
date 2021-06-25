# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 18:46:36 2021

@author: DELL
"""

import pygame as py
from random import randrange,choice
class Pipes:
    '''用于管理管道对象,包含了管道的移动和所有逻辑，因为不需要手动操控'''
    def __init__(self,interface):
        self.settings = interface.settings
        self.screen = interface.screen
        self.pipe_body = py.image.load("images/pipe_body.png")
        self.pipe_end = py.image.load("images/pipe_end.png")
        #该列表用于存储初始位置(x坐标),管道长度,最多可以存放四个管道，有删除和加入
        self.pipes = [[150,4],]
        '''self.direction = [1]'''
        
    def draw_pipes(self):
        for n in range(len(self.pipes)):
            for m in range(self.pipes[n][1]):
                self.screen.blit(self.pipe_body, (self.pipes[n][0], m*32 ))
            for m in range(self.pipes[n][1]+self.settings.pipe_open_width,16):
                self.screen.blit(self.pipe_body, (self.pipes[n][0], m*32 ))
                
            self.screen.blit(self.pipe_end, (self.pipes[n][0], self.pipes[n][1]*32 ))
            self.screen.blit(self.pipe_end, 
            (self.pipes[n][0], (self.pipes[n][1]+self.settings.pipe_open_width-1) * 32 ))
            
            self.pipes[n][0] -= self.settings.pipe_speed
                      
            
    def addordel_pipes(self):
        if len(self.pipes) < 4:
            '''如果管道列表中管道的个数小于4，就要添加列表，x坐标为最后一个管道的位置
                加上管道之间的距离（可以设置）'''
            x = self.pipes[-1][0] + self.settings.pipe_interval
            open_pos = randrange(1,9)
            self.pipes.append([x,open_pos])
            '''self.direction.append(choice([-1,1]))'''
        if self.pipes[0][0] < -100:
            self.pipes.pop(0)
            '''self.direction.pop(0)'''
    
    '''def pipe_updown(self):
        pipes_list = self.pipes
        for i in range(len(self.pipes)):
            self.'''
    
    def control_pipes(self):
        '''该函数包含对管道的一切管理，方便在主程序中调用'''
        self.draw_pipes()
        self.addordel_pipes()