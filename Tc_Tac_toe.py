import math
import random


class player :
    def __init__(self,letter):
        self.letter =letter

    def get_move (self,game):
        pass


class RandomComuterPlayer(player ):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        pass


class humenPlayer (player) :
    def __init__(self, letter):
        super().__init__()

    def get_move(self,game):
        pass
