import time
import os
from castle import intro, throne_room, main_gate, ending
from forest import forest_intro, forest_cottage
from lake import lake_intro, lake_house
from cave import cave_intro
from character_selection import character_select


def game():

    game_on = True
    while game_on:
        os.system('cls')
        print("\nASCII art by: unknown artist From: https://ascii.co.uk/art/castle")
        print("""                                       ,.=,,==. ,,_
                          _ ,====, _    |I|`` ||  `|I `|
                         |`I|    || `==,|``   ^^   ``  |
                         | ``    ^^    ||_,===TT`==,,_ |
                         |,==Y``Y==,,__| \L=_-`'   +J/`
                          \|=_  ' -=#J/..-|=_-     =|
                           |=_   -;-='`. .|=_-     =|----T--,
                           |=/\  -|=_-. . |=_-/^\  =||-|-|::|____
                           |=||  -|=_-. . |=_-| |  =|-|-||::\____
                           |=LJ  -|=_-. . |=_-|_| =||-|-|:::::::
                           |=_   -|=_-_.  |=_-     =|-|-||:::::::
                           |=_   -|=//^\. |=_-     =||-|-|:::::::
                       ,   |/&_,_-|=||  | |=_-     =|-|-||:::::::
                    ,--``8%,/    ',%||  | |=_-     =||-|-|%::::::
                ,---`_,888`  ,.'''''`-.,|,|/!,--,.&\|&\-,|&#:::::
               |;:;K`__,...;=\_____,=``           %%%&     %#,---
               |;::::::::::::|       `'.________+-------\   ``
              /8M%;:::;;:::::|                  |        `-------
    """)
        print("\nWelcome to Fool's Forage")
        play = input("Press [p] and enter to play or [q] and enter to quit: ")
        if play.lower() == "q":
            break
        elif play.lower() == "p":
            os.system('cls')

            # Character Creation
            player = character_select()

            if not game_on:
                return game()

            # Castle Intro
            decision1 = intro(player)

            if decision1 == game_on:
                decision2 = throne_room()

                if decision2 == game_on:
                    decision3 = main_gate()

                    # Forest Path
                    if decision3 == "forest":
                        forest1 = forest_intro()

                        # In the Cottage
                        if forest1 is True:
                            forest2 = forest_cottage(player)

                            # Check Cabinet or Crate
                            if forest2:
                                quest_complete = cave_intro(player)

                                if quest_complete:
                                    ending()
                                    return game()
                                else:
                                    return game()
                            else:
                                return game()

                        # Pass Forest Cottage, Move to Cave
                        else:
                            quest_complete = cave_intro(player)

                            if quest_complete:
                                ending()
                                return game()
                            else:
                                return game()

                    # Lake Path
                    elif decision3 == "lake":
                        lake1 = lake_intro()

                        # In the House
                        if lake1 is True:
                            lake2 = lake_house(player)

                            # Check Bookshelf or Chest
                            if lake2:
                                quest_complete = cave_intro(player)

                                if quest_complete:
                                    ending()
                                    return game()
                                else:
                                    return game()
                            else:
                                return game()

                        # Pass Lake House, Move to Cave
                        else:
                            quest_complete = cave_intro(player)

                            if quest_complete:
                                ending()
                                return game()
                            else:
                                return game()

                else:
                    return game()
            else:
                return game()

            if not game_on:
                return game()



game()

