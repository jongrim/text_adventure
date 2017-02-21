#! /usr/bin/python
import random

from monsters import Troll, Dragon, Rat


class Room:
    num_of_monsters = 0
    monsters = []

    def __init__(self, lvl_of_difficulty):
        self.num_of_monsters = random.randint(0, 3)

        monster_gen = (add_monster(lvl_of_difficulty) for i in range(self.num_of_monsters))
        self.monsters = [monster for monster in monster_gen]


def add_monster(lvl_of_difficulty):
    r = random.randint(1, 3)
    if r == 1:
        return Troll(lvl_of_difficulty)
    elif r == 2:
        return Rat(lvl_of_difficulty)
    else:
        return Dragon(lvl_of_difficulty)
