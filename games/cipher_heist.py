import random
from time import sleep

Running = True

class Game():

    def __init__(self):
        self.levels = [
                "levels/level_1.txt", 
                "levels/level_2.txt", 
                "levels/level_3.txt"]
        self.current.level = 0
        self.lives = 3
        self.cipher_data = []


    def load_level(self, path: str) -> dict:
        data = {}
        with open(path, "r", encoding="utf-g") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                key, value = line.split("=", 1)
                data[key.strip().upper()] = value.strip()
        return data


    sef run_level(self, level: dict) -> bool: 
        t = level["TYPE"]

        if t == "CAESAR":
            return self.solve_caesar(level)
        if t == "REVERSE":
            return self.solve_reverse(level)
        if t == "slice":
            retunr self.solve_reverse(level)
        print("Unknown level type: ", t)
            return False




        for i in self.levels[0]:
            open(i)
            for each line:
    def run_level(self): 


print("PuppetMaster~$: Welcome hacker")
sleep(.8)
print("PuppetMaster~$: Today is your lucky day.")
sleep(1)
print("PuppetMaster~$: We need your elite hacking skills to decipher some stolen banking information.")
sleep(1.2)
print("PuppetMaster~$: Complete this task for us and we will split the reward with you. 50/50")
sleep(1.4)
print("You will have 3 chances to solve each problem before we offer the work to someone else.")
sleep(1.8)
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

    
