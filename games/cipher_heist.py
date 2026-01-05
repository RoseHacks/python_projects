import random
from time import sleep

Running = True

class Game():

    def __init__(self):
        levels = ["levels/level_1.txt", "levels/level_1.txt", "levels/level_1.txt"]
        current.level = 0


    def load_level(self):
        current_level = 0
        current_leevel += 1

print("PuppetMaster~$: Welcome hacker")
sleep(.8)
print("PuppetMaster~$: Today is your lucky day.")
sleep(1)
print("PuppetMaster~$: We need your elite hacking skills to decipher some stolen banking information.")
sleep(1.2)
print("PuppetMaster~$: Complete this task for us and we will split the reward with you. 50/50")
sleep(1.4)
print("PuppetMaster~$: Think you're up for the challenge?")

while Running:

    users_decision = input("Enter 'Yes' or 'No': " )

    if users_decision not in ("Yes", "No"):
        print("PuppetMaster~$: Please enter a valid response")
        continue
    
    if users_decision == "No":
        print("PuppetMaster~$: Very well.. your skills will be missed.")
        break

    else:
        users_decision == "Yes"
        print("PuppetMaster~$: Wonderful! Solve each challenge to advance closer to the reward.")
        sleep(1.5)
        print("PuppetMaster~$: The first challenge is ready.")
        continue

    
