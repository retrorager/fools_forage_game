import os
import random
import time
from simple_colors import *

win = True


# Player Fight
def fight(player, enemy):

    global win

    player_damage = random.randint(int(player.damage / 2), player.damage)
    enemy.hp -= player_damage
    print(f"\n{player.character} the {player.race} {red('attacked')} the {enemy.race} for {player_damage} damage.\n")

    if enemy.hp <= 0:
        print(f"The {enemy.race} was killed!!\n")
        return win

    time.sleep(1.5)
    enemy_damage = random.randint(int(enemy.damage / 2), enemy.damage)
    player.hp -= enemy_damage
    print(f"The {enemy.race} uses its' {random.choice(enemy.action)} attack to strike "
          f"{player.character} the {player.race} for {enemy_damage} damage\n")

    if player.hp <= 0:
        print(f"{player.character} the {player.race} died... {red('Game Over', 'bold')}")
        win = False
        return win


# Player Defend
def defend(player, enemy):
    global win

    enemy_damage = random.randint(enemy.damage // 2, enemy.damage)
    player_block = random.randint(player.defend // 4, player.defend // 2)
    damage_taken = enemy_damage - player_block

    if damage_taken > 0:
        player.hp -= damage_taken
        print(f"\n{player.character} the {player.race} {cyan('defended')} the blow.\n"
              f"The {enemy.race} damaged {player.character} the {player.race} for {enemy_damage} damage.\n")
    else:
        print(f"\n{player.character} the {player.race} {blue('deflected')} the blow and takes no damage.\n")

    if player.hp <= 0:
        print(f"{player.character} the {player.race} died. {red('Game Over', 'bold')}")
        win = False
        return win

    player_damage = random.randint(player.damage // 4, player.damage // 2)
    enemy.hp -= player_damage
    print(f"{player.character} the {player.race} counter strikes the {enemy.race} for {player_damage} damage.\n")

    if enemy.hp <= 0:
        print(f"The {enemy.race} was killed!")
        return win


# Player Heal
def heal(player):
    if player.potions <= 0:
        print(f"\n{player.character} the {player.race} can't heal. They have {player.potions} left.")
    else:
        player.hp = player.start_hp
        player.potions -= 1
        print(f"\n{player.character} the {player.race} has used a potion and is fully {green('healed')}. "
              f"{player.potions} potions remaining.")


# Player vs Enemy Battle
def battle(player, enemy):
    global win

    while player.hp > 0 and enemy.hp > 0:
        time.sleep(2.5)
        os.system("cls")
        print(f"Player: {player.character} the {player.race} {player.hp}/{player.start_hp} vs. "
              f"Enemy: {enemy.race} {enemy.hp}/{enemy.start_hp}")
        print(f"1) {red('[f]ight')}\n2) {blue('[d]efend')}\n3) {green('[h]eal')} {player.potions}/{player.start_pot}")

        action = input("Choose your action: ")

        if action == "1" or action.lower() == "f":
            fight(player, enemy)
        elif action == "2" or action.lower() == "d":
            defend(player, enemy)
        elif action == "3" or action.lower() == "h":
            heal(player)

        if enemy.hp <= 0:
            return win
        elif player.hp <= 0:
            win = False
            return win


