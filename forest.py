from battle_system import *
from enemy import Bogoblin
from items import Halo, Bangle, Brew, Key, Sharpstone

# create enemy and item objects
bogoblin = Bogoblin()

halo = Halo()
bangle = Bangle()
brew = Brew()
key = Key()
sharp = Sharpstone()


def forest_intro():
    time.sleep(3)
    os.system("cls")
    print("\nAfter traveling through the forest for awhile, seeing nothing but trees, you come across a small"
          " dwelling just off of the main path near a bog.\n")
    time.sleep(3)
    print("You don't see signs of anyone from outside of the cottage.\n")
    time.sleep(3)
    print(f"1) You think if you {yellow('go')} inside you may find something useful to aid you later on journey.\n")
    time.sleep(3)
    print(f"2) You think that if you {yellow('do not')} go inside you may save time"
          f" that may prove valuable in saving the Prince.\n")

    while True:

        choice = input("What do you do: ").lower().strip()

        if choice == "1" or choice == "go":
            print(f"\nYou make your way to the entrance of the cottage and proceed to head inside.\n")
            time.sleep(3)
            inside = True
            return inside

        elif choice == "2" or choice == "do not":
            print("\nYou decide to keep moving and pass by the empty looking cottage,"
                  " as you continue on the path towards the cave.\n")
            time.sleep(3)
            inside = False
            return inside


def forest_cottage(player):
    time.sleep(3)
    os.system("cls")
    print("As you cautiously push open the creaky door of the forest cottage, "
          "a wave of dank air and cobwebs greets you.\n")
    time.sleep(3)
    print("The main room is sparsely populated with dusty furniture,"
          " some faded tapestries and a few containers lying around.\n")
    time.sleep(3)
    print("To your left you see a cabinet with doors that might be hiding something behind them.\n")
    time.sleep(3)
    print("To your right you see a small crate that doesn't appear to be locked.\n")
    time.sleep(3)
    print(f"1) You're curious about the {yellow('cabinet')} and what might be behind its' doors.\n")
    time.sleep(3)
    print(f"2) You feel there's usually something of value saved in a {yellow('crate')}. "
          f"Maybe you should check it out.\n")

    while True:

        choice = input("What do you do: ").lower().strip()

        # Check Cabinet
        if choice == "1" or choice == "cabinet":
            print(f"\nYou walk up to the cabinet and reach to open its' doors.\n")
            time.sleep(3)
            print(f"You look inside and see an item.\n")
            time.sleep(3)
            print(f"It looks to be a flask with a bulbous glass bottom and a thinning neck capped with a cork.\n")
            time.sleep(3)
            print(f"Inside the flask is a shimmering red liquid.\n")
            time.sleep(3)
            print(f"You reach inside the cabinet, grabbing the flask ")
            time.sleep(3)
            print(f"and hold it up to the faint light to observe it better.\n")
            time.sleep(3)
            print(f"After looking at the flask for a brief moment, ")
            time.sleep(3)
            print(f"you uncork the flask and drink its' contents...\n")

            # Acquire Brew of Brawn
            player.items["brew"] = brew
            if player.items["brew"] is not None:
                time.sleep(3)
                print(f"You have acquired the {yellow(player.items['brew'].name)}!")
                brew.powerup(player)
                print(f"Your health has increased by {player.items['brew'].value}\n")
                time.sleep(3)

                # Ambush by Bogoblin
                print(f"You were surprised by a {bogoblin.race} after you finished searching the cabinet!\n")
                bogoblin_battle = battle(player, bogoblin)

                if bogoblin_battle:
                    player.items["key"] = key
                    if player.items["key"] is not None:
                        print(f"You loot the dead body of the {bogoblin.race} and found a mysterious {yellow('key')}!\n")
                        time.sleep(3)
                        print(f"After storing the new key you found, you continue on your path to save the Prince.\n")
                        time.sleep(3)
                        return True
                else:
                    game_on = False
                    return game_on

        # Check the Crate, Acquire Sharpstone
        elif choice == "2" or choice == "crate":
            print(f"\nYou walk over to the crate and reach down to open it.\n")
            time.sleep(3)
            print(f"You look inside and see an item.\n")
            time.sleep(3)
            print(f"It looks to be a stone.\n")
            time.sleep(3)
            print(f"This small rectangular piece of stone looks like the perfect texture to sharpen a blade.\n")
            time.sleep(3)
            print(f"You pick it up and begin to run it against the blade of your {player.weapon}...\n")

            # Acquire Sharpstone
            player.items["sharp"] = sharp
            if player.items["sharp"] is not None:
                time.sleep(3)
                print(f"You have acquired the {yellow(player.items['sharp'].name)}!")
                sharp.powerup(player)
                print(f"Your attack has increased by {player.items['sharp'].value}\n")
                time.sleep(3)


                # Ambush by Bogoblin, Battle, Obtain Key
                print(f"You were surprised by a {bogoblin.race} after you finished searching the crate!\n")
                bogoblin_battle = battle(player, bogoblin)
                if bogoblin_battle:
                    player.items["key"] = key
                    if player.items["key"] is not None:
                        print(f"You loot the dead body of the {bogoblin.race} and found a mysterious {yellow('key')}!\n")
                        time.sleep(3)
                        print(f"After storing the new key you just found, you continue on your path towards the cave.\n")
                        time.sleep(3)
                        return True
                else:
                    game_on = False
                    return game_on

