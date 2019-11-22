
import random

from pico2d import *

import game_world

import game_framework


class Ball:

    image = None

    def __init__(self):
        if Ball.image == None:

            Ball.image = load_image('ball21x21.png')

        self.x, self.y = random.randint(0, 1600 -1), random.randint(0, 1600 -1)
        self.font = load_font('ENCR10B.TTF', 16)
        self.hp = 100

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def update(self):
        self.y = self.y


    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())
        self.font.draw(self.x - 20, self.y + 20, '%d' % (self.hp), (0, 255, 0))







class BigBall(Ball):

    MIN_FALL_SPEED = 50

    MAX_FALL_SPEED = 200

    image = None



    def __init__(self):

        if BigBall.image == None:

            BigBall.image = load_image('ball41x41.png')

        self.x, self.y = random.randint(0, 1600 -1), random.randint(0, 1600 -1)
        self.font = load_font('ENCR10B.TTF', 16)
        self.hp = 100


    def get_bb(self):

        return  self.x - 20, self.y - 20, self.x + 20, self.y + 20