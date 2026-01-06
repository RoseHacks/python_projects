import random
from time import sleep

class Game():

    def __init__(self):
        self.levels = [
                "levels/level_1.txt",
                "levels/level_2.txt",
                "levels/level_3.txt"]
        self.current_level = 0
        self.lives = 3

    def load_level(self, path: str) -> dict:
        data = {}
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                key, value = line.split("=", 1)
                data[key.strip().upper()] = value.strip()
        return data

    def run_level(self, level: dict) -> bool:
        t = level["TYPE"].upper()

        if t == "CAESAR":
            return self.solve_caesar(level)
        elif t == "REVERSE":
            return self.solve_reverse(level)
        elif t == "SLICE":
            return self.solve_slice(level)
        else:
            print("Unknown level type: ", t)
            return False

    # prompt the user and compare to ANSWER key
    def solve_caesar(self, level: dict) -> bool:
        print("Challenge: CAESAR")
        sleep(1.5)
        print("Encrypted:", level.get("MESSAGE", ""))
        print("Hint SHIFT:", level.get("SHIFT", ""))
        return self.prompt_until_correct(level)

    def solve_reverse(self, level: dict) -> bool:
        print("Challenge: REVERSE")
        sleep(1.5)
        print("Encrypted:", level.get("MESSAGE", ""))
        return self.prompt_until_correct(level)

    def solve_slice(self, level: dict) -> bool:
        print("Challenge: SLICE")
        sleep(1.5)
        print("Encrypted:", level.get("MESSAGE", ""))
        print("Rule:", level.get("RULE", ""))
        return self.prompt_until_correct(level)

    def prompt_until_correct(self, level: dict) -> bool:
        expected = level.get("ANSWER", "")
        if expected == "":
            print("PuppetMaster~$: Level file missing ANSWER= ...")
            return False

        while self.lives > 0:
            guess = input("Hacker~$: ").strip()
            if guess == expected:
                print("Correct.")
                return True

            self.lives -= 1
            print("Wrong code. Remaining lives:", self.lives)

        return False


g = Game()

print("PuppetMaster~$: Welcome hacker")
sleep(1.2)
print("PuppetMaster~$: Today is your lucky day.")
sleep(1)
print("PuppetMaster~$: We need your elite hacking skills to decipher some stolen banking information.")
sleep(1.6)
print("PuppetMaster~$: Complete this task for us and we will split the reward with you. 50/50")
sleep(1.4)
print("NOTE: You will have 3 chances to solve each problem before we offer the work to someone else.")
sleep(1.8)
print("PuppetMaster~$: Think you're up for the challenge?")
sleep(1.4)

while True:
    users_decision = input("Enter 'Yes' or 'No': " )
    if users_decision not in ("Yes", "No"):
        print("PuppetMaster~$: Please enter a valid response")
        continue
    if users_decision == "No":
        print("PuppetMaster~$: Very well.. your skills will be missed.")
        exit()
    if users_decision == "Yes":
        print("PuppetMaster~$: Wonderful! Solve each challenge to advance closer to the reward.")
        sleep(1.5)
        print("PuppetMaster~$: The first challenge is ready.")
        sleep(2)
        break

# Main game logic and levels
while g.current_level < len(g.levels) and g.lives > 0:
    path = g.levels[g.current_level]
    level_data = g.load_level(path)

    solved = g.run_level(level_data)
    if solved:
        g.current_level += 1
    else:
        break  # if a level fails (likely lives hit 0), stop the game

if g.lives == 0:
    print("PuppetMaster~$: Mission failed.. Contacting another hacker.")
elif g.current_level == len(g.levels):
    print("PuppetMaster~$: Congrats! Here is your reward: ")
else:
    print("PuppetMaster~$: Contract terminated.")
