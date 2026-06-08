import random

class Setup:
    print("Hello weclome to RPG! \n")
    print("---------------------")

    def menu(self):
        print("Press\n")
        print("1 to combat")
        print("2 to visit shop")
        print("3 to Quit")


    def __init__(self):
        self.playerhealth = 100
        self.attackpower = 10
        self.gold = 20
        self.potion = 1
        self.enemyhealth =100


class Mainmenu(Setup):

    def combat(self):
        try:
            with open("data.txt","w") as file:
                stats = (
                    f"PlayerHealth: {self.playerhealth}\n"
                    f"Attack Power: {self.attackpower}\n"
                    f"Gold: {self.gold}\n"
                    f"Potions: {self.potion}\n"
                    f"EnemyHealth: {self.enemyhealth}\n"
            )
                file.write(stats)

            with open ("data.txt","r") as file:
                stats = file.read()
                print("The player stats",stats)

        except FileNotFoundError:
            print("File not found")

        except Exception as e:
            print("An error occured:",e)

        try:
            while self.enemyhealth >0 and self.playerhealth > 0:
                attack = input("Press a to attack : ").lower()
                if attack == "a":
                    self.enemyhealth -= 10
                else:
                    print("enter 'a' invalid command")
                if self.enemyhealth == 0:
                    print("U Won the game")
                    print("If u want to battle again press 1")

            if self.enemyhealth == 0:
                self.enemyhealth += 100


        except Exception as e:
            print("An error",e)


    def shop(self):
        try:
            with open ("data2.txt","w") as file:
                shop=(
                f"Gold: $10 \n"
                f"Weapon: $3\n"
                f"Health: $1"
                    )
                file.write(shop)

            with open ("data2.txt","r") as file:
                shop = file.read()
                print(shop)

        except Exception as e:
            print("Error",e)



    def game(self): 
        self.menu()      
        while True:
            try :
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.combat()
                elif choice == 2:
                    self.shop()
                elif choice == 3:
                    break
                else:
                    print("Invalid syntax Please select 1-3")

            except ValueError:
                print("Enter valid number")


g = Mainmenu()
g.game()