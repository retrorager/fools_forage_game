import os
import time
from simple_colors import *


def intro(player):
    time.sleep(3)
    os.system("cls")
    game_on = True

    print(f"\nAnd so the story of {player.character} the {player.race} begins...\n")
    time.sleep(3)
    print("You are awakened in your sleeping quarters by the King’s closest aid.\n")
    time.sleep(3)
    print("He has called upon you for a special task that he trusts you, alone, to complete.\n")
    time.sleep(3)
    print(f"1) You're tired and think the King won't be mad if you go back to {yellow('sleep')} for a few minutes.\n")
    time.sleep(3)
    print(f"2) You're tired but you should get {yellow('up')}, the King has called and you musn't keep him waiting.\n")

    while True:
        choice = input("What do you do: ").lower().strip()
        if choice == "1" or choice == "sleep":
            print(f"\nYou wake up some amount of time later and realize you're not in your bed but in the dungeon.\n")
            time.sleep(3)
            print(f"The King had you arrested for disobedience and defiance of his orders.\n{red('Game Over', 'bold')}")
            game_on = False
            return game_on
        elif choice == "2" or choice == "up":
            print("\nYou get up, gather your gear and head to the throne room to meet with the King.")
            return game_on


def throne_room():
    time.sleep(3)
    os.system("cls")
    game_on = True
    print("\nYou arrive in the throne room to be greeted by the King and his aid.\n")
    time.sleep(3)
    print("The King tells you his son, the Prince, had left on a cave expedition and has not been heard from in days.\n")
    time.sleep(3)
    print("He tells you there has been word that he was trying to travel and find a long lost relic to prove his"
          " worthiness to his father.\n")
    time.sleep(3)
    print("This, the King says, is a fool's errand as this relic is just a myth that has"
          " yet to be proven to actually exist.\n")
    time.sleep(3)
    print("He has tasked you with retrieving his foolish son (and the relic,"
          " if it exists) before he gets himself in serious danger or possibly killed.\n")
    time.sleep(3)
    print(f"1) You {yellow('accept')} the request and tell the King you have heard of this relic."
          f" You will leave at once to hopefully find and save the Prince before its too late.\n")
    time.sleep(3)
    print(f"2) You {yellow('refuse')} the request and tell the King you have heard of this relic but"
          f" there's no way you can save the Prince if he's really going to find it.\n")
    while True:
        choice = input("What do you do: ").lower().strip()
        if choice == "1" or choice == "accept":
            print("\nThe King is pleased by your response and asks you proceed to the"
                  " castle entrance to begin your quest.\n")
            return game_on
        elif choice == "2" or choice == "refuse":
            print(f"\nThe King is baffled by your response. He has you seized and"
                  f" thrown in the dungeon for disloyalty.\n"
                  f"{red('Game Over', 'bold')}")
            game_on = False
            return game_on


def main_gate():
    time.sleep(3)
    os.system("cls")
    print("You arrive at the main gate of the castle and are met with 2 diverging paths.\n")
    time.sleep(3)
    print(f"One that leads through the {green('Dread Forest')} and another that leads around the {blue('Drowned Lake')}.\n")
    time.sleep(3)
    print("Both paths will lead you to the cave where you have been told you should find the Prince.\n")
    time.sleep(3)
    print(f"1) You think the {green('forest')} path should be the most direct and though most dare not enter,\n"
          f"it should save you time along your journey, if you don't encounter any setbacks along the way.\n")
    time.sleep(3)
    print(f"2) You think the {blue('lake')} path should be the safest, though it could take a bit longer to get around"
          f" the lake.\nIt would be unusual to encounter any trouble on this route.\n")
    while True:
        choice = input("What do you do: ").lower().strip()
        if choice == "1" or choice == "forest":
            print(f"\nYou begin down the path toward the {green('Dread Forest')} on your quest to find the Prince.")
            return "forest"
        elif choice == "2" or choice == "lake":
            print(f"\nYou begin down the path toward the {blue('Drowned Lake')} on your quest to find the Prince")
            return "lake"


def ending():
    time.sleep(3)
    os.system("cls")
    print("You return to the castle with the Prince in tow but without the relic of myth he had been seeking.\n")
    time.sleep(3)
    print("The King thanks you for returning his foolish son and rewards you with a short leave to regroup from your arduous quest.\n")
    time.sleep(3)
    os.system("cls")
    print("You win!!! Thanks for playing!!!")