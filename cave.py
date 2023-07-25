from battle_system import *
from enemy import Troll
from items import Key

key = Key()
troll = Troll()


def cave_intro(player):

    time.sleep(3)
    os.system('cls')

    print("After a while longer you arrive at the entrance to the cave.\n")
    time.sleep(3)
    print("With an opening partially shrouded by tree branches and bushes, ")
    time.sleep(3)
    print("you can see the faint glow of candles coming from the darkness of the cave.\n")
    time.sleep(3)
    print("You've reached your destination, hopefully in time to find "
          "the Prince before he's gotten into too much trouble.\n")
    time.sleep(3)
    print("You step into the cave to find another fork in your journey.\n")
    time.sleep(3)
    print(f"1) To your {yellow('left')} is a dimly lit hallway that disappears into darkness.\n")
    time.sleep(3)
    print(f"2) To your {yellow('right')} is another dark hallway that's nearly identical to the other.\n")

    while True:

        choice = input("What do you do: ").lower().strip()

        if choice == "1" or choice == "left":
            print(f"\nYou make your way down the hallway to your left, "
                  f"moving cautiously as you make your way deeper into the cave.\n")
            time.sleep(3)
            return left_path(player)

        elif choice == "2" or choice == "right":
            print("\nYou choose the path to your right and begin to quickly "
                  "make your way down the faintly illuminated hallway.\n")
            time.sleep(3)
            return right_path(player)


def left_path(player):

    time.sleep(3)
    os.system('cls')

    print("You walk carefully but swiftly through the hallway and "
          "begin to see more light coming from the empty arch at the end of the hall.\n")
    time.sleep(3)
    print("Just a few steps from the archway you step on something and feel your foot partially sink into the floor.\n")
    time.sleep(3)
    print("You activated a swinging trap that narrowly misses you, as you back up to assess what to do next.\n")
    time.sleep(3)
    print("Feeling that you may have little time to spare, "
          "you decide you must make a decision quickly to pass this trap and reach the Prince in time.\n")
    time.sleep(3)
    print(f"1) You think there may be something in your {yellow('pack')} that could help you to disable this trap.\n")
    time.sleep(3)
    print(f"2) You decide there's no time to waste and you'll try to time the swings to {yellow('avoid')} the trap.\n")

    while True:

        choice = input("What do you do: ").lower().strip()

        if choice == "1" or choice == "pack":
            if player.items["key"] is not None:
                print("\nYou remember you acquired a mysterious key on your way here.\n")
                time.sleep(3)
                print("You see a hole in the wall near you that looks like it might fit with the key you found earlier.\n")
                time.sleep(3)
                print("You put the key in the hole and hear a click.\n")
                time.sleep(3)
                print("The trap slows its' swing to a stop and you pass by it unharmed.\n")
                return final_room(player)
            else:
                print("\nYou see a hole in the wall near you that looks like it might fit with something,\n")
                time.sleep(3)
                print("but nothing in your pack looks small enough to use.\n")
                continue

        elif choice == "2" or choice == "avoid":
            print("\nYou can't waste anymore time and you hurry to get past the trap.\n")
            time.sleep(3)
            print("You miss-time your avoidance attempt and are grazed by the swinging trap.\n")
            player.take_damage(10)
            print("You lost 10HP but made it past the trap.")
            time.sleep(3)
            return final_room(player)


def right_path(player):

    time.sleep(3)
    os.system('cls')

    print("As you walk attentively and agilely through the hallway,\n"
          "begin to see more light coming from the empty arch at the end of the hall.\n")
    time.sleep(3)
    print("Just a few steps from the archway you step on something and feel your foot partially sink into the floor.\n")
    time.sleep(3)
    print("You activated a pit trap that, had you taken one step further,\n"
          "would have meant certain end for your journey.\n")
    time.sleep(3)
    print("Feeling that you may have little time to spare,\n"
          "you decide you must make a decision quickly to pass this trap and reach the Prince in time.\n")
    time.sleep(3)
    print(f"1) You think there may be something in your {yellow('pack')} that could help you to disable this trap.\n")
    time.sleep(3)
    print(f"2) You decide there's no time to waste and you'll try to jump over the trap to {yellow('avoid')} it.\n")

    while True:

        # Prompt Player Choice
        choice = input("What do you do: ").lower().strip()

        # Check Your Pack For The Key
        if choice == "1" or choice == "pack":
            if player.items["key"] is not None:
                print("\nYou remember you acquired a mysterious key on your way here.\n")
                time.sleep(3)
                print("You see a hole in the wall near you that looks like it might fit with the key you found earlier.\n")
                time.sleep(3)
                print("You put the key in the hole and hear a click.\n")
                time.sleep(3)
                print("The trap slows its' swing to a stop and you pass by it unharmed.\n")
                return final_room(player)
            else:
                print("\nYou see a hole in the wall near you that looks like it might fit with something,\n")
                time.sleep(3)
                print("but nothing in your pack looks small enough to use.\n")
                continue

        # Try To Avoid The Trap
        elif choice == "2" or choice == "avoid":
            print("\nYou can't waste anymore time and you hurry to get past the trap.\n")
            time.sleep(3)
            print("You miss-time your avoidance attempt and your leg clips the edge of the pit.\n")
            player.take_damage(10)
            print("You lost 10HP but made it past the trap.")
            time.sleep(3)
            return final_room(player)

# Player Enters Final Room
def final_room(player):

    time.sleep(3)
    os.system('cls')

    print("You step through the archway after making it past the trap and are greeted by a large room.\n")
    time.sleep(3)
    print("The ground is rocky and uneven with small streams trickling down some of the cracks in the walls.\n")
    time.sleep(3)
    print("You enter the room quietly as you see 2 figures, a large one standing over the smaller one.\n")
    time.sleep(3)
    print("The large creature has its' back turned to you, while the smaller, "
          "human-looking body lies motionless on the ground.\n")
    time.sleep(3)
    print(f"1) You can {yellow('sneak')} up on the creature and "
          f"get the first strike in, to gain an advantage in the inevitable fight to come.\n")
    time.sleep(3)
    print(f"2) You can {yellow('shout')} to draw the creatures attention and "
          f"maybe the motionless body may have a chance to get to safety.\n")

    while True:

        # Sneak up on Troll
        choice = input("What do you do: ").lower().strip()
        if choice == "1" or choice == "sneak":
            print(f"\nYou decide to sneak up on the creature and catch it by surprise!!\n")
            damage_taken = player.deal_damage()
            troll.take_damage(damage_taken)
            time.sleep(3)
            print(f"The {troll.race} was damaged for {damage_taken}...\n")
            time.sleep(3)
            print("Let the final battle begin!!")
            return battle(player, troll)

        # Shout at Troll
        elif choice == "2" or choice == "shout":
            print("\nYou shout at the creature and draw its' attention but the body remains motionless...\n")
            time.sleep(3)
            print(f"The {troll.race} lumbers towards you, intent to submit you to the same fate...\n")
            time.sleep(3)
            print("Let the final battle begin!!")
            return battle(player, troll)
