# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 09:17:54 2021

@author: DELL
"""

import sys
import pygame as py
py.init()

screen = py.display.set_mode((1000,800))
speed = [1,1]

ball = py.image.load('intro_ball.gif')
ball_rect = ball.get_rect()

angle=0
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            #sys.exit()
    '''ball_rect = ball_rect.move(speed)
    if ball_rect.left < 0 or ball_rect.right > screen.get_width():
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > screen.get_height():
        speed[1] = -speed[1]'''
    
    angle += 2
    ball1 = py.transform.rotate(ball, angle)
    ball_rect = ball1.get_rect()
    ball_rect.center=(100,100)
    print(ball_rect.top)
    
    screen.fill(color='pink')
    screen.blit(ball1,ball_rect)
    py.display.flip()
    py.time.delay(10)
        