import random
import time

Running = True

class Game:
    def __init__(self):
        self.users_bank = 60
        self.house_bank = 60
        self.revives = 1 

    def incrby1(self):
        i = 1
        while i < 4:
            time.sleep(1)
            print(i)
            i += 1
    
    def tricked(self):
        if self.revives == 1:
            print("The house always wins..")
            time.sleep(2)
            print("House gains 100 points")            
            time.sleep(.8)
            self.house_bank += 100
            self.revives -= 1

g = Game()

print("Welcome to The Game!")
time.sleep(.5)
print("Get ready...")

g.incrby1()

while Running:
    user_input = input("Enter a number between 1 and 2 or 'quit': ")

    if user_input not in ("1", "2", "quit"):
        print("Invalid input. Please try again")
        continue

    if user_input == "quit":
        break

    users_number = int(user_input)

    number = random.randint(1, 2)
    print(number)
    
    if users_number == number:
        print("Winner!")
        g.users_bank += 20
        g.house_bank -= 20
        print("User's Balance: ", g.users_bank)
        print("House Balance: ", g.house_bank)
    else:
        print("Loser")
        g.users_bank -= 20
        g.house_bank += 20
        print("User's Balance: ", g.users_bank)
        print("House Balance: ", g.house_bank)

    if g.users_bank <= 0:
        print("Game Over")
        exit()
    if g.house_bank <= 0:
        print("You've beat the house. Congrats!")
        exit()
    if g.house_bank <= 20:
        g.tricked()
