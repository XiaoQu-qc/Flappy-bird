# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 21:11:52 2021

@author: DELL
"""

from flappy_bird import Flappy_Bird
from guide import Guide
from gameover import Gameover

start = Guide()
play = Flappy_Bird()
end = Gameover()

while True:
    start.execute()
    play.run_game()
    end.execute()
    #这里要注意，每进行完一局游戏都要重新初始化对象
    start = Guide()
    play = Flappy_Bird()
    end = Gameover()