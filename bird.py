# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 17:51:02 2021

@author: DELL
"""

import pygame as py

class Bird:
    def __init__(self,interface):
        '''Bird类的构造函数'''
        self.settings = interface.settings
        self.screen = interface.screen
        self.wing_up = py.image.load('images/bird_wing_up.png')
        self.wing_down = py.image.load('images/bird_wing_down.png')
        self.bird_image = py.image.load('images/bird_wing_up.png')
        self.rect = self.wing_up.get_rect()
        self.rect.x = 20
        self.rect.y = self.settings.screen_height/2
        self.y_vel = -10                #对应每一帧的y方向速度
        self.rotate_angle = 45          #对应每一帧的旋转角度
        self.flap = 0                   #是否扇动翅膀的标志
        self.score = 0                  #小鸟得分
        
        
    def draw(self,interface):
        '''参数：一个表示游戏的主类，bird复制的位置。将bird的图像画在屏幕的指定位置'''
        self.screen.blit(self.bird_image, self.rect)
        self.update_bird(interface)
        
    def update_bird(self,interface):
        '''更新小鸟的状态'''
        #接下来的if条件判断语句利用帧数，使得小鸟扇动翅膀
        if 0 <=interface.frame<= self.settings.fps/2:
            self.bird_image = self.wing_up
        elif self.settings.fps/2 <interface.frame<= self.settings.fps:
            self.bird_image = self.wing_down
            
        if self.flap:
            self.y_vel = self.settings.flap_y_vel
            self.rotate_angle = self.settings.flap_rotate_angle
        else:
            #每过一帧更新小鸟的速度和y坐标
            self.y_vel = min(self.y_vel+self.settings.gravity, self.settings.max_y_vel)
            #每过一帧更新小鸟图像的旋转角度
            self.rotate_angle = max(self.rotate_angle+self.settings.rotate_vel, self.settings.min_rotate_angle)
        self.bird_image = py.transform.rotate(self.bird_image, self.rotate_angle)
        self.rect.y += self.y_vel
        
    def if_bird_strike(self,pipes_pos):
        #调用该函数时需要提供管道的位置列表，以判断是否碰撞
        flag = 0
        if pipes_pos[0][0] - 30 < self.rect.x < pipes_pos[0][0]+79:
            if self.rect.y < (pipes_pos[0][1]+1)*32-3 or self.rect.y > (pipes_pos[0][1]+4)*32+3:
                #这里减2加2是做了一些微调，实际上，小鸟的头顶距离矩形顶部有一段距离
                flag = 1
        if self.rect.y > self.settings.floor_pos or self.rect.y < 0:
            flag = 1
        return flag
    
    def cal_score(self,pipes_pos):
        if pipes_pos[0][0]+30 == self.rect.x:
            self.score += 1