import random
from models.player import Player

class Game():

    def game_logic(self, p1, p2):
        rk = 'rock'
        pa = 'paper'
        sc = 'scissors'
        self.p1 = p1
        self.p2 = p2

        if self.p1.choice == self.p2.choice:
            return None
        elif self.p1.choice == rk and self.p2.choice == pa:
            return self.p2
        elif self.p1.choice == rk and self.p2.choice == sc:
            return self.p1
        elif self.p1.choice == pa and self.p2.choice == rk:
            return self.p1
        elif self.p1.choice == pa and self.p2.choice == sc:
            return self.p2
        elif self.p1.choice == sc and self.p2.choice == pa:
            return self.p1
        elif self.p1.choice == sc and self.p2.choice == rk:
            return self.p2

    def play_computer(self):
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        return computer_choice
