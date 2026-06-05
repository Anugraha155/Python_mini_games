# Rock paper scissors game

import random

class Rockpaperscissor:

    def __init__(self):
        self.computer_score = 0
        self.human_score = 0

    def main(self):
        print("Score card")
        print("Human score",self.human_score)
        print("Computer score",self.computer_score)
        if self.human_score > self.computer_score:
            print("Human won the game")

        elif (self.human_score == self.computer_score):
            print("Its a tie") 

        else: 
            if self.computer_score > self.human_score:
                print("Computer won")

    def computer_action(self):
        possible_actions=["r","p","s"]
        self.computer_move= random.choice(possible_actions)


    def human_action(self):
        self.human_move = input(f"Enter 'R' for Rock 'P' for paper and 'S' for scissors and 'q' to quit : ").lower().strip()
        while self.human_move in ["r","s","p","q"]:
            break
        else:
            print("Invalid syntax")


    def quiet(self):
        self.main()

    def game(self):
        while True:
            self.computer_action()
            self.human_action()
            
            if self.human_move == self.computer_move:
                print("Its a tie")

            elif (self.human_move == "r" and self.computer_move == "s") or \
                 (self.human_move == "s" and self.computer_move == "p") or \
                 (self.human_move == "p" and self.computer_move == "r"):
                print("Human wins this round!")
                self.human_score += 1


            else:
                while self.human_move in ["r","s","p"]:
                    print("Computer won")
                    self.computer_score +=1
                    break
        

            if self.human_move == "q":
                self.quiet()
                break
                


G = Rockpaperscissor()
G.game()