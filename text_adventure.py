#! /usr/bin/python
import random
import sys
import hero
from room import Room


class Game:
    level_of_difficulty = 1
    monsters_slayed = 0
    rooms_cleared = 0
    room_gen = None
    actions_taken = 0
    hero = hero.Hero()

    def __init__(self):
        self.set_level_of_difficulty()
        self.room_gen = (Room(self.level_of_difficulty) for i in range(5))

    def set_level_of_difficulty(self):
        lvl = None
        while lvl is None:
            lvl = input('Please select your level of difficulty:\n1: Easy\n2: Normal\n3: Hard\n')

            if lvl.isdigit():
                lvl = int(lvl)
                if lvl == 1:
                    self.level_of_difficulty = 1
                elif lvl == 2:
                    self.level_of_difficulty = 2
                elif lvl == 3:
                    self.level_of_difficulty = 3
                else:
                    lvl = None
            else:
                lvl = None

    def reset_game(self):
        self.monsters_slayed = 0
        self.rooms_cleared = 0
        self.actions_taken = 0
        self.hero.hit_points = 50
        self.room_gen = (Room(self.level_of_difficulty) for i in range(5))

    def game_over(self):
        print("Game over!")
        self.print_game_stats()
        play_again = yes_no_response("Play again? (Y\\n)\n")
        if play_again:
            self.reset_game()
            self.clear_rooms()
        else:
            sys.exit(0)

    def print_game_stats(self):
        print(
            'Total monsters slayed: {0}\n'
            'Total rooms cleared: {1}\n'
            'Total actions taken: {2}'.format(self.monsters_slayed, self.rooms_cleared, self.actions_taken)
        )

    def kill_monster(self):
        self.monsters_slayed += 1

    def room_cleared(self):
        self.rooms_cleared += 1

    def clear_rooms(self):
        """
        Moves the player through the rooms of the dungeon. At the beginning of each room it will print the number
        of monsters present.
        :return: None
        """
        room_text()
        for room in self.room_gen:
            if yes_no_response("Proceed to next room? (Y\\n)\n"):
                pass
            else:
                break
                # TODO figure out something better to do if they choose not to go to the next room
            if room.num_of_monsters == 0:
                print('No monsters here!')
                self.room_cleared()
            elif room.num_of_monsters == 1:
                print("There is 1 monster in this room! Looks like it's time to fight!")
                self.battle(room)
            else:
                print("Oh no! There are {} monsters in this room! "
                      "Looks like it's time to fight!".format(room.num_of_monsters))
                self.battle(room)
            # TODO add a check_powerups call - also write check_powerups
        print("Congratulations! All rooms cleared!")
        self.game_over()

    def battle(self, room):
        """
        Controls the battle between a player and all of the monsters in the room.
        :param room: The current room that the player is in
        :return: None
        """
        for monster in room.monsters:
            print("It's a {}!".format(monster))
            while self.hero.hit_points > 0 and monster.hit_points > 0:
                action = self.get_player_action()
                if action == 'attack':
                    self.resolve_attack(monster)
                elif action == 'defend':
                    print("You blocked the monster's blow.")
            if self.hero.hit_points > 0:
                print("You've defeated the {}!".format(monster))
                self.monsters_slayed += 1
            else:
                self.game_over()
        print("All monsters have been defeated!")
        self.room_cleared()

    def get_player_action(self):
        """
        Get the action that the player wants to perform: attack, defend, or quit
        :return: None
        """
        action = None
        while action is None:
            action = input("Choose an action:\n1: Hit\n2: Defend\n3: Give up and print game stats\n")
            if action.isdigit():
                action = int(action)
                if action == 1:
                    self.actions_taken += 1
                    return "attack"
                elif action == 2:
                    self.actions_taken += 1
                    return "defend"
                elif action == 3:
                    self.game_over()
                    break
                else:
                    action = None
            else:
                action = None

    def resolve_attack(self, monster):
        """
        If the player chooses to attack, determine which creature does damage
        :param monster: The current monster the player is battling
        :return: None
        """
        h_attack = random.randint(1, 6)
        m_attack = random.randint(1, 6)
        if h_attack >= m_attack:
            monster.hit_points -= self.hero.damage()
            print("The {} has {} health left.".format(monster, monster.hit_points))
        else:
            self.hero.hit_points -= monster.damage()
            print("You have {} health left.".format(self.hero.hit_points))


def yes_no_response(question):
    response = None
    while response is None:
        response = input(question)
        if response[0].upper() == 'Y':
            return True
        elif response[0].upper() == 'N':
            return False
        else:
            response = None


def intro_text():
    print('Our story begins with a heroic adventurer, on a quest to retrieve a fantastic prize...')


def room_text():
    print("You arrive at the dungeon and bravely enter. Who knows what waits for you on the other side.")


def main():
    intro_text()
    game = Game()
    game.clear_rooms()
    

if __name__ == '__main__':
    main()
