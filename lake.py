from battle_system import *
from enemy import LakeMaiden
from items import Halo, Bangle, Key


# create enemy and item objects
lake_maiden = LakeMaiden()

halo = Halo()
bangle = Bangle()
key = Key()


def lake_intro():
    time.sleep(3)
    os.system("cls")
    print("\nAfter traveling for a bit without seeing much to remark upon, you come across a small"
          " dwelling along the lake's edge.\n")
    time.sleep(3)
    print("You don't see signs of anyone from outside of the house.\n")
    time.sleep(3)
    print(f"1) You think if you {yellow('go')} inside you may find something useful to aid you later on journey.\n")
    time.sleep(3)
    print(f"2) You think that if you {yellow('do not')} go inside you may save time"
          f" that may prove valuable in saving the Prince.\n")

    while True:

        choice = input("What do you do: ").lower().strip()

        if choice == "1" or choice == "go":
            print("\nYou make your way to the entrance of the lake house and proceed to head inside.\n")
            time.sleep(3)
            inside = True
            return inside

        elif choice == "2" or choice == "do not":
            print("\nYou decide to keep moving and pass by the empty looking house,"
                  " as you continue on the path towards the cave.\n")
            time.sleep(3)
            inside = False
            return inside


def lake_house(player):
    time.sleep(3)
    os.system("cls")
    print("As you cautiously push open the creaky door of the lake house, a wave of dank air and cobwebs greets you.\n")
    time.sleep(3)
    print("The main room is sparsely populated with dusty furniture,"
          " some faded tapestries and a few containers lying around.\n")
    time.sleep(3)
    print("\nTo your left you see a bookshelf with doors that might be hiding something behind them.\n")
    time.sleep(3)
    print("To your right you see a small chest that doesn't appear to be locked.\n")
    time.sleep(3)
    print(f"1) You're curious about the {yellow('bookshelf')} and what might be behind its' doors.\n")
    time.sleep(3)
    print(f"2) You feel there's usually something of value saved in a {yellow('chest')}. "
          f"Maybe you should check it out.\n")

    while True:

        choice = input("What do you do: ").lower().strip()

        # Check Inside Bookshelf
        if choice == "1" or choice == "bookshelf":
            print(f"\nYou walk up to the bookshelf and reach to open the doors below its' bottom shelf.\n")
            time.sleep(3)
            print(f"You look inside and see an item.\n")
            time.sleep(3)
            print(f"It looks to be a ring made of silver with a large ruby set into its' face.\n")
            time.sleep(3)
            print(f"There are 3 smaller stones in the ring equally spaced between themselves and the large ruby.\n")
            time.sleep(3)
            print(f"You reach inside to pick it up and place it onto your finger.\n")
            time.sleep(3)
            print(f"Almost immediately you feel a wave of warmth rush over you..\n")
            time.sleep(3)
            print(f"and the fatigue you had been feeling dissipates...\n")

            # Obtain Halo of Hardiness
            player.items["halo"] = halo
            if player.items["halo"] is not None:
                time.sleep(3)
                print(f"You have acquired the {yellow(player.items['halo'].name)}!")
                halo.powerup(player)
                print(f"Your health has increased by {player.items['halo'].value}\n")
                time.sleep(3)

                # Ambush by Lake Maiden
                print(f"You were surprised by a {lake_maiden.race} after you finished searching the bookshelf!\n")
                maiden_battle = battle(player, lake_maiden)
                if maiden_battle:
                    player.items["key"] = key
                    if player.items["key"] is not None:
                        print(f"You loot the dead body of the {lake_maiden.race} and found a mysterious {yellow('key')}!\n")
                        time.sleep(3)
                        print("After assessing your wounds from the battle, you leave the house and head for the cave.\n")
                        time.sleep(3)
                        return True
                else:
                    game_on = False
                    return game_on

        # Check Inside Chest
        elif choice == "2" or choice == "chest":
            print("\nYou walk over to the chest and reach down to open it. You look inside and see an item.\n")
            time.sleep(3)
            print("It looks to be a bracelet made of a dark metal with swirling engravings carved into it.\n")
            time.sleep(3)
            print("Adorned to the outside of the bracelet are a few small gemstones "
                  "encircling a larger stone in the middle.\n")
            time.sleep(3)
            print("You put it on and begin to feel a unknown energy coursing through you ")
            time.sleep(3)
            print("as you feel yourself getting stronger...\n")
            player.items["bangle"] = bangle
            if player.items["bangle"] is not None:
                time.sleep(3)
                print(f"You have acquired the {yellow(player.items['bangle'].name)}!")
                bangle.powerup(player)
                print(f"Your defense has increased by {player.items['bangle'].value}!\n")
                time.sleep(3)

                # Ambush by Lake Maiden
                print(f"You were surprised by a {lake_maiden.race} after you finished searching the chest!\n")
                maiden_battle = battle(player, lake_maiden)
                if maiden_battle:
                    player.items["key"] = key
                    if player.items["key"] is not None:
                        print(f"You loot the dead body of the {lake_maiden.race} and found a mysterious {yellow('key')}!\n")
                        time.sleep(3)
                        print("After assessing your wounds from the battle, you leave the house and head for the cave.\n")
                        time.sleep(3)
                        return True
                else:
                    game_on = False
                    return game_on
