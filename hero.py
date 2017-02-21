#! /usr/bin/python
import random


class Hero:
    attack_damage = 5
    hit_points = 50

    def __init__(self):
        pass

    def take_damage(self, damage):
        self.hit_points -= damage

    def damage(self):
        r = random.randint(1, 20)
        if r == 1:
            print("You swing wide and miss!")
            return 0
        elif r == 20:
            print("You got a critical hit! Double damage.")
            return self.attack_damage * 2
        else:
            print("Your attack does {} damage".format(self.attack_damage))
            return self.attack_damage
