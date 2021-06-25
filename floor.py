# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 10:13:49 2021

@author: DELL
"""

import pygame as py
from settings import Settings
floor_y = Settings().floor_pos
move_speed = Settings().pipe_speed
floors = [0,1439]
def load_floor(interface):
    global floors
    for n in range(len(floors)):
        floor = py.image.load('images/ground.png')
        interface.screen.blit(floor, (floors[n], floor_y))
        floors[n] -= move_speed
        
    if len(floors) < 2:
        x = floors[-1]+1439
        floors.append(x)
    if floors[0] < -1439:
        floors.pop(0)