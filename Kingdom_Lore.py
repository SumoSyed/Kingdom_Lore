import os
import platform
from time import sleep
import random
# ---sleep---(1)

# define our clear function; taken from https://stackoverflow.com/questions/52118317/how-to-clear-the-console-after-a-line-of-code/52118653


def clear():
    # could use something like this instead:
    # command = {"Linux": "clear", "Windows": "cls"}[platform.system()]
    # os.system(command)
    # also, what about Mac?
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')


# Set our NPCs for knights/companions and other possible characters

class NPC:

    def __init__(self, name, charisma, strength, exploration, gold, description):
        self.name = name
        self.charisma = charisma  # Needed for the recruit function
        self.strength = strength  # Sets attack strength in arena or single combat
        # Sets how much experience is gained with each exploration
        self.exploration = exploration
        self.gold = gold
        self.description = description  # description of non_playable_character

    def displayStats(self):
        return f"Name: {self.name}; Charisma: {self.charisma}; Strength: {self.strength}; Exploration: {self.exploration}; Cost: {self.gold}"



    def recruit(self):
        if self.charisma <= 3:
            soldiers = random.randint(2, 4)
        elif self.charisma >= 4 or self.charisma <= 7:
            soldiers = random.randint(5, 9)
        elif self.charisma >= 8 or self.charisma <= 10:
            soldiers = random.randint(10, 14)
        elif self.charisma >= 10:
            soldiers = random.randint(15, 21)

        print(f"Your knight managed to recruit {str(soldiers)} soldiers.")
        input("")
        return soldiers

    def quests(self):
        if self.exploration <= 3:
            gold = random.randint(0, 50)
        elif self.exploration >= 4 or self.charisma <= 7:
            gold = random.randint(51, 100)
        elif self.exploration >= 8 or self.charisma <= 10:
            gold = random.randint(101, 200)
        elif self.exploration >= 10:
            gold = random.randint(201, 500)
        if gold <= 50:
            print(f"Your knight managed to completed a quest and earned {str(gold)} gold.")
        elif gold >= 51 and gold <=100:
            print(f"Your knight managed to complete a few quests and earned {str(gold)} gold.")
        elif gold >= 101 and gold <= 200:
            print(f"Your knight managed to complete various quests and earned {str(gold)} gold.")
        elif gold >= 201:
            print(f"Your knight managed to complete a long quests and earned {str(gold)} gold.")
        input("")
        return gold



def knightQuest():
    while True:
        if len(playerKnights) < 1:
            return 
        elif len(playerKnights) >= 1:
            print("You have chosen to send your knights on a quest. Who would you like to send?")
            print("Here is a list of your knights:")
            print(*[f"{i + 1}. {k}" for i,k in enumerate(playerKnightStats)], sep="\n")   
            value = userChoice()
            clear()
            try:
                if value == 1 or value == 2 or value == 3:
                    selected_knight_stats = playerKnightStats[value - 1]
                    selected_knight = playerKnights[value - 1]
                    print(f"You have chosen to send {selected_knight_stats}")
                    print("What would you like to do with your knight?")
                    print("1. Send to recruit")
                    print("2. Send on a quest")
                    print("3. Send to arena to battle")
                    value = userChoice()
                    result =	{
                        "soldiersRecruited": 0,
                        "quests": 0,
                        "battle": 0,
                        }
                    if value == 1:
                        result["soldiersRecruited"] = selected_knight.recruit()
                    elif value == 2:
                        result["quests"] = selected_knight.quests()
                    elif value == 3:
                        result["battle"] = "You chose to send your knight to battle"
                    else:
                        print("Your choice did not meet expectation.")
                    return result
            except IndexError:
                print(f"You do not have a knight at the {value} number.")
                print("Try again")


def knightRecruit():
    while True:
        if len(playerKnights) == 3:
           return f"You already have 3 knights"

        print("Here is a list of available knights. Remember, you can only have 3 knights")
        print(*[f"{i + 1}. {k}" for i,k in enumerate(knightStats)], sep="\n")

        if len(playerKnights) < 3:
            choice = userChoice()          
            if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 or choice == 6 or choice == 7 or choice == 8 or choice == 9:
                playerKnights.append(knightRoster.pop(choice - 1))
                playerKnightStats.append(knightStats.pop(choice - 1))
            else:
                print("You have to select the number shown on the left side of the knights name.")

        print("You now have a knight.")
        print(*[f"{i + 1}. {k}" for i,k in enumerate(playerKnightStats)], sep="\n")
        print(" ")
        while True:
            value = input("Would you like to hire another knight? (yes/no): ").strip().lower()
            if value == "yes":
                break
            elif value == "no":
                clear()
                return
            else:
                print('You have to type "yes" or "no"')
                continue


def userChoice():
    value = input("Choose: ")
    choice = int(value)
    return choice

npc_knight1 = NPC("Timm the Eager", 5, 2, 5, 150, "Young boy Timm was a malicious pervert who is eager to prove his worth; alas not with his sword but with his wits")
npc_knight2 = NPC("Gifford the Smile", 7, 1, 3, 175, "Aaa young Gifford the Smile. His smile was known to the ends of the Marolin. It is said every miller is looking for this poor lads head; alas he is cunning to escape from them albeit they be millers")
npc_knight3 = NPC("Reginalde the Clever", 1, 7, 2, 150, "Reginalde the Clever... Alas, he appears to be the completely the opposite")
npc_knight4 = NPC("Gaiallard the Keen", 8, 4, 2, 200, "There's something intriguing about him, perhaps it's his goodwill or perhaps it's simply his reputation. But nonetheless, people tend to assist him, while training with him whenever he's available.")
npc_knight5 = NPC("Colyne the Horrific", 1, 8, 6, 200, "An old tattoo resembling a sword is displayed on the side of the left eye with a scar on the left and no teeth leaves a lasting impression on those he meets.")
npc_knight6 = NPC("Walter of the Dawn", 7, 6, 2, 200, "There is something captivating about Walter of the Dawn, perhaps it is his fortunate past or perhaps it is simply his blonde and dashing hair. But nonetheless, people tend to follow him, while secretly training to become more like him")
npc_knight7 = NPC("Emericus the Insane", 0, 9, 3, 250, "There is not much to say about him except for....well, Emericus is insane")
npc_knight8 = NPC("Gunter the Stubborn", 1, 10, 1, 300, "Ahhh Stubborn as a bull, sharp as a lightweight pillow")
npc_knight9 = NPC("Owine the Magneficent", 9, 10, 10, 2500, "Owine the magnificient's deed has been heard of throughout the realm. Slaying of the dragon, slaying of the goblin's king. What has this brave knight not done")

#To hold the instances
knightRoster = [npc_knight1, npc_knight2, npc_knight3, npc_knight4, npc_knight5, npc_knight6, npc_knight7, npc_knight8, npc_knight9]

#To call the method to show stats
knightStats = [npc_knight1.displayStats(), npc_knight2.displayStats(), npc_knight3.displayStats(), npc_knight4.displayStats(), npc_knight5.displayStats(), npc_knight6.displayStats(), npc_knight7.displayStats(), npc_knight8.displayStats(), npc_knight9.displayStats()]

#To hold the instances
playerKnights = []
#To call the method of the class NPC
playerKnightStats = []

year = 164
soldiers = 0 #Basics implemented. Yet to define how soldiers work. 
cost = 0
population = 0 #Population system not implemented
moral = 0 #Moral system playerKnightStatsnot implemented
prosperity = 0 #Prosperity system not implemented
gold = 0 #Gold system not implemented

while True:
    print(f"The year is {str(year)}.")
    print(f"You have {str(soldiers)} soldiers at your disposal and {gold} gold. Your army costs {cost}.")
    print("1. Send one of your knights on a task.")
    print("2. Go to the village. |Not implemented|")
    print("3. Tend to your royal duties. |Not implemented|")
    print("4. Go on your own adventure. |Not implemented|")
    print("5. Recruit knights.")
    print("6. End turn.")
    value = userChoice()
    clear()
    if value == 1:
        result = knightQuest()
        if result == None:
            print("You have no knights. Recruit a knight first.")
            print("")
            continue
        soldiers += result["soldiersRecruited"]
        gold += result["quests"]
        cost = soldiers * 5
    elif value == 5:
        knightRecruit()
    elif value == 6:
        gold = gold - cost
        year += 1
