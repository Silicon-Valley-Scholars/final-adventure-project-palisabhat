import random
import time

name = input("Enter your name: ")
gold = 0

print("Welcome " + name + "!")
print("In this game your objective will be to beat as many tower masters as possible.")
print("There is a chamber of gold at the top of the magic tower you will be playing in.")
print("Each level will have a different boss/ a tower master that you have to beat to with a chance to earn gold.")
print("Each level going up will have a stronger tower master. The level of gold from each level will also increase the higher up you go.")
print("Try to beat the final boss!")

bossList = ["The Wizard of DEATH", "Dr. Distster", "Dragon King", "Mistress Poison", "Queen of Malice"]

time.sleep(10)

bossList = ["Dragon King", "Shadow Witch", "Cyber Golem", "Toxic Hydra"]

counter = 0
while counter < 1:
    print("Choose the boss you want to battle...")
    print("1. Dragon King")
    print("2. Shadow Witch")
    print("3. Cyber Golem")
    print("4. Toxic Hydra")

    choice = input("Enter the number: ")

    if choice == "1":
        boss = "Dragon King"
        counter = counter + 1
    elif choice == "2":
        boss = "Shadow Witch"
        counter = counter + 1
    elif choice == "3":
        boss = "Cyber Golem"
        counter = counter + 1
    elif choice == "4":
        boss = "Toxic Hydra"
        counter = counter + 1
    else:
        print("That is not a valid option. Try again.")

time.sleep(2)
boss_power = 10
print("You will battle " + boss + " with a power level of " + str(boss_power))

time.sleep(2)
player_power = random.randint(2, 8)

def fight_boss(boss, boss_power, gold):
    player_power = random.randint(2, 8)
    if player_power < boss_power:
        gold += 10
    return gold
    
print("You are fighting " + boss + "!")
print(boss + " charges at you!")
time.sleep(2)
print("You pick up your weapon and get ready...")
time.sleep(2)

print("The Wizard of Death's power is: " + str(boss_power))
time.sleep(2)
print("Your power is: " + str(player_power))

time.sleep(2)
print("The battle begins!")
time.sleep(2)
print("You swing your sword!")
time.sleep(2)
print(boss + " swings his axe!")
time.sleep(2)

if player_power >= boss_power:
    print("Oh no! " + boss + " is too strong!")
    print("You get knocked down...")
    time.sleep(2)
    print("You dont get any gold.")

else:
    print("You hit " + boss + " and win the fight!")
    print("He falls to the ground!")
    time.sleep(5)
    gold = gold + 10
    print("You get 10 gold.")
    print("You find 3 mysterious treasure chests...")
i = 1
while i <= 3:
    print("Opening chest number " + str(i))
    time.sleep(2)
    coins = random.randint(5, 15)
    print("You found " + str(coins) + " coins")
    gold = gold + coins
    i = i + 1

print("You now have " + str(gold) + " gold")
print("Congratulations on making it to the end of Level 1.")
