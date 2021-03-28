import os
import platform
from time import sleep
import random
# ---sleep---(1)

# define our clear function; taken from https://stackoverflow.com/questions/52118317/how-to-clear-the-console-after-a-line-of-code/52118653


def clear():
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
            print("Amount of soldiers hired:__" + str(soldiers))
            return soldiers
        elif self.charisma >= 4 or self.charisma <= 7:
            soldiers = random.randint(5, 9)
            print("Amount of soldiers hired:__" + str(soldiers))
            return soldiers
        elif self.charisma >= 8 or self.charisma <= 10:
            self.soldiers = random.randint(10, 14)
            print("Amount of soldiers hired:__" + str(soldiers))
            return soldiers
        elif self.charisma >= 10:
            soldiers = random.randint(15, 21)
            print("Amount of soldiers hired:__" + str(soldiers))
            return soldiers
        
def menu():
    print(f"The year is {int(year)}.")
    print("1. Send one of your knights on a task.")
    print("2. Go to the village. |Not implemented|")
    print("3. Tend to your royal duties. |Not implemented|")
    print("4. Go on your own adventure. |Not implemented|")
    print("5. Recruit knights.")
    print("6. End turn.")
    value = userChoice()
    if value == 1:
        clear()
        knightQuest()
    elif value == 5:
        clear()
        knightRecruit()
    elif value == 6:
        yearEnd()
        clear()
        menu()

def yearEnd():
    return    year + 1

def knightQuest():
    if len(playerKnights) < 1:
        print("You have no knights. Recruit a knight first.")
        input("Press enter to go back to the menu")
        clear()
        menu()
    elif len(playerKnights) >= 1:
        print("You have chosen to send your knights on a quest. Who would you like to send?")
        print("Here is a list of your knights:")
        print(*playerKnights, sep = "\n")
        value = userChoice()
        if value == 1:
            print(f"You have chose to send {playerKnights[0]}")
        elif value == 2:
            print(f"You have chose to send {playerKnights[1]}")
        elif value == 3:
            print(f"You have chose to send {playerKnights[2]}")
        else:
            print("You have to pick a number between 1 and 3.")
            print("Try again")
            knightQuest()

def knightRecruit():
    print("Here is a list of available knights. Remember, you can only have 3 knights")
    print(*[f"{i + 1}. {k}" for i,k in enumerate(knightRoster)], sep="\n")
    if len(playerKnights) < 3:
        choice = userChoice()            
        if choice == 1:
            playerKnights.append(knightRoster.pop(0))
        elif choice == 2:
            playerKnights.append(knightRoster.pop(1))
        elif choice == 3:
            playerKnights.append(knightRoster.pop(2))
        elif choice == 4:
            playerKnights.append(knightRoster.pop(3))
        elif choice == 5:
            playerKnights.append(knightRoster.pop(4))
        elif choice == 6:
            playerKnights.append(knightRoster.pop(5))
        elif choice == 7:
            playerKnights.append(knightRoster.pop(6))
        elif choice == 8:
            playerKnights.append(knightRoster.pop(7))
        elif choice == 9:
            playerKnights.append(knightRoster.pop(8))

        print("You now have a knight.")
        print(playerKnights)
    elif len(playerKnights) == 3:
        f"You already have 3 knights"
    menu()

def userChoice():
    value = input("Choose: ")
    choice = int(value)
    return choice

year = 164
soldiers = 0 #Basics implemented. Yet to define how soldiers work. 
population = 0 #Population system not implemented
moral = 0 #Moral system not implemented
prosperity = 0 #Prosperity system not implemented
gold = 0 #Gold system not implemented

npc_knight1 = NPC("Timm the Eager", 5, 2, 5, 150, "Young boy Timm was a malicious pervert who is eager to prove his worth; alas not with his sword but with his wits")
npc_knight2 = NPC("Gifford the Smile", 7, 1, 3, 175, "Aaa young Gifford the Smile. His smile was known to the ends of the Marolin. It is said every miller is looking for this poor lads head; alas he is cunning to escape from them albeit they be millers")
npc_knight3 = NPC("Reginalde the Clever", 1, 7, 2, 150, "Reginalde the Clever... Alas, he appears to be the completely the opposite")
npc_knight4 = NPC("Gaiallard the Keen", 8, 4, 2, 200, "There's something intriguing about him, perhaps it's his goodwill or perhaps it's simply his reputation. But nonetheless, people tend to assist him, while training with him whenever he's available.")
npc_knight5 = NPC("Colyne the Horrific", 1, 8, 6, 200, "An old tattoo resembling a sword is displayed on the side of the left eye with a scar on the left and no teeth leaves a lasting impression on those he meets.")
npc_knight6 = NPC("Walter of the Dawn", 7, 6, 2, 200, "There is something captivating about Walter of the Dawn, perhaps it is his fortunate past or perhaps it is simply his blonde and dashing hair. But nonetheless, people tend to follow him, while secretly training to become more like him")
npc_knight7 = NPC("Emericus the Insane", 0, 9, 3, 250, "There is not much to say about him except for....well, Emericus is insane")
npc_knight8 = NPC("Gunter the Stubborn", 1, 10, 1, 300, "Ahhh Stubborn as a bull, sharp as a lightweight pillow")
npc_knight9 = NPC("Owine the Magneficent", 9, 10, 10, 2500, "Owine the magnificient's deed has been heard of throughout the realm. Slaying of the dragon, slaying of the goblin's king. What has this brave knight not done")

knightRoster = [npc_knight1.displayStats(), npc_knight2.displayStats(), npc_knight3.displayStats(), npc_knight4.displayStats(), npc_knight5.displayStats(), npc_knight6.displayStats(), npc_knight7.displayStats(), npc_knight8.displayStats(), npc_knight9.displayStats()]
playerKnights = []

menu()
