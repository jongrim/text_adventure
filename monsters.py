#! /usr/bin/python
import random


class Monster:
    modifier = 1
    attack_damage = 1
    hit_points = 10

    def __init__(self, base_mod, level_of_difficulty):
        self.modifier = base_mod * level_of_difficulty
        self.attack_damage *= self.modifier
        self.hit_points *= self.modifier

    def take_damage(self, damage):
        self.hit_points -= damage

    def damage(self):
        r = random.randint(1, 20)
        if r == 1:
            print("The monster's attack missed!")
            return 0
        elif r == 20:
            print("The monster got a critical hit! Double damage")
            return self.attack_damage * 2
        else:
            print("The monster's attack does {} damage".format(self.attack_damage))
            return self.attack_damage


class Troll(Monster):
    
    modifier = 2

    def __init__(self, level_of_difficulty):
        super().__init__(base_mod = Troll.modifier, level_of_difficulty = level_of_difficulty)

    def __str__(self):
        return 'Troll'


class Dragon(Monster):
    
    modifier = 3

    def __init__(self, level_of_difficulty):
        super().__init__(base_mod = Dragon.modifier, level_of_difficulty = level_of_difficulty)

    def __str__(self):
        return 'Dragon'


class Rat(Monster):

    modifier = 1

    def __init__(self, level_of_difficulty):
        super().__init__(base_mod=Rat.modifier, level_of_difficulty=level_of_difficulty)

    def __str__(self):
        return 'Rat'
