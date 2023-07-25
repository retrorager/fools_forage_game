import os
import time
from player import Elf, Human, Dwarf, Player


def character_select():
    options = {
        "character": False,
        "race": False,
        "weapon": False,
        "magic": False,
        "armour": False,
        "name": False,
    }

    player = Player()

    while not options["character"]:

        while not options["race"]:
            print("\nChoose your character's race:\n")
            print("1) Human 90HP/10ATK/20DFND +3 Potions\n\n"
                  "2) Elf 95HP/15ATK/15DFND +2 Potions\n\n"
                  "3) Dwarf 100HP/20ATK/10DFND +1 Potion\n")
            race = input("Enter your choice: ").title()
            if not options["race"]:
                if race == "Human" or race == "1":
                    player = Human()
                    options["race"] = True
                    break
                elif race == "Elf" or race == "2":
                    player = Elf()
                    options["race"] = True
                    break
                elif race == "Dwarf" or race == "3":
                    player = Dwarf()
                    options["race"] = True
                    break
                else:
                    print("Please select a race from the given options")
                    continue

        while not options["weapon"]:
            time.sleep(.5)
            os.system("cls")
            print("\nChoose your weapon:\n")
            print("1) Dagger +10ATK\n\n2) Sword +15ATK\n\n3) Axe +20ATK\n")
            weapon = input("Enter your choice: ").title()
            if not options["weapon"]:
                if weapon == "Dagger" or weapon == "1":
                    player.weapon = "Dagger"
                    player.damage = player.damage + 10
                    options["weapon"] = True
                    break
                elif weapon == "Sword" or weapon == "2":
                    player.weapon = "Sword"
                    player.damage = player.damage + 15
                    options["weapon"] = True
                    break
                elif weapon == "Axe" or weapon == "3":
                    player.weapon = "Axe"
                    player.damage = player.damage + 20
                    options["weapon"] = True
                    break
                else:
                    print("Please choose a weapon from the given options")
                    continue

        while not options["magic"]:
            time.sleep(.5)
            os.system("cls")
            print("\nChoose your magic item:\n")
            print("1) Necklace +20HP\n\n2) Bracelet +20ATK\n\n3) Cloak +10HP/+10ATK\n")
            magic = input("Enter your choice: ").title()
            if not options["magic"]:
                if magic == "Necklace" or magic == "1":
                    player.magic = "Necklace"
                    player.hp = player.hp + 20
                    options["magic"] = True
                    break
                elif magic == "Bracelet" or magic == "2":
                    player.magic = "Bracelet"
                    player.damage = player.damage + 20
                    options["magic"] = True
                    break
                elif magic == "Cloak" or magic == "3":
                    player.magic = "Cloak"
                    player.hp = player.hp + 10
                    player.damage = player.damage + 10
                    options["magic"] = True
                    break
                else:
                    print("Please choose a magic item from the given options")
                    continue

        while not options["armour"]:
            time.sleep(.5)
            os.system("cls")
            print("\nChoose your armour item:\n")
            print("1) Helmet +20DFND\n\n2) Chestplate +15DFND\n\n3) Shield +10DFND\n")
            armour = input("Choose your armor item: ").title()
            if not options["armour"]:
                if armour == "Helmet" or armour == "1":
                    player.armour = "Helmet"
                    player.defend = player.defend + 20
                    options["armour"] = True
                    break
                elif armour == "Chestplate" or armour == "2":
                    player.armour = "Chestplate"
                    player.defend = player.defend + 15
                    options["armour"] = True
                    break
                elif armour == "Shield" or armour == "3":
                    player.armour = "Shield"
                    player.defend = player.defend + 10
                    options["armour"] = True
                    break
                else:
                    print("Please choose an armour item from the given options")
                    continue

        while not options["name"]:
            time.sleep(.5)
            os.system("cls")
            character = input("\nEnter your character's name: ").title()
            username = input("Enter your initials: ").upper()
            player.username = username
            player.character = character
            options["name"] = True
            break

        time.sleep(.5)
        os.system("cls")
        print("\nPlease review your character choices:")
        print(f"\nPlayer: {player.username}\n"
              f"Character: {player.character}\n"
              f"Race: {player.race}\n"
              f"HP: {player.hp}\n"
              f"Weapon: {player.weapon}\n"
              f"ATK: {player.damage}\n"
              f"Magic: {player.magic}\n"
              f"Potions: {player.potions}\n"
              f"Armour: {player.armour}\n"
              f"DFND: {player.defend}")
        choice = input("\nConfirm character choices (y/n): ").lower()
        if choice == "y":
            options["character"] = True
            player.start_hp = player.hp
            return player
        elif choice == "n":
            options["race"] = False
            options["weapon"] = False
            options["magic"] = False
            options["armour"] = False
            options["name"] = False
            continue
