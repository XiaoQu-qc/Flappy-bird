# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 18:10:45 2021

@author: DELL
"""

class Settings:
    def __init__(self):
        '''保存游戏内的所有设置'''
        self.screen_width = 422         #游戏屏幕宽度
        self.screen_height = 512        #游戏屏幕宽度
        '''接下来七行设置均可以调节游戏难度'''
        self.fps = 60                   #游戏帧数，默认为60
        self.pipe_open_width = 6        #管道的开口大小，默认为6
        self.pipe_interval = 200        #管道之间的间隔，默认200
        self.pipe_speed = 4             #管道移动的速度，即整个画面移动的速度，默认为1，快速4
        self.max_y_vel = 7              #小鸟的最大速度（向下），默认为3，快速7
        self.flap_y_vel = -7.5           #初始的向上速度，也即是扇动翅膀后的向上速度，默认-5，快速-7.5
        self.gravity = 0.5              #小鸟向下的加速度，默认0.5,快速1
        
        self.flap_rotate_angle = 15     #小鸟扇动翅膀后抬头角度
        self.rotate_vel = -3            #小鸟“抬头”的速度
        self.min_rotate_angle = -15     #小鸟转动的角度负方向最大偏移值             
        self.floor_pos = 448            #地板y坐标的位置\
        self.pipe_updown_speed = 0.5