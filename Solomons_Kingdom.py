#Solomon's Kingdom (Text-based adventure game)
import time
import textwrap
import sys
from sys import exit
import os
import random
import cmd

screen_width = 100

### TITLE SCREEN ###

def title_screen():
    os.system("clear")
    print("/////////////////////////////////////////////////////////////////////////////////")
    print("//////////////////////////////// SOLOMON'S KINGDOM //////////////////////////////")
    print("/////////////////////////////////////////////////////////////////////////////////")
    print("++++++++++++++++++++++++++++++++++++++++PLAY+++++++++++++++++++++++++++++++++++++")
    print("----------------------------------------QUIT-------------------------------------\n\n")
    print("                         © Copyright © 2019 Tyler Gorsulowsky\n")

def title_screen_selectors():
    options = input(">>> ")
    if options.lower() == "play":
        start_game()
    elif options.lower() == "quit":
        quit_game()
    while options.lower() not in ["play", "quit"]:
        print("cmd invalid")
        options = input(">>> ")
        if options.lower() == "play":
            start_game()
        elif options.lower() == "quit":
            quit_game()


def quit_game():
    options = "quit"
    print("QUITING...")
    sys.exit(0)

### Player Setup ###
class player:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mp = 0
yourPlayer = player()

def start_game():
    time.sleep(2)
    name = input("What is your name Adventurer?: ")
    answer1 = "y"
    answer2 = "n"
    prompt = "Will you accept this quest?(y/n): "

    print("\n\nGOD: Hello, " + name)
    print("After Solomon's death the world has been in a grave state of termoil.")
    print("Hadad of Edom, Razon of Zobah, and Jeroboam of Ephraim have all been dividing up the land and causing mayham within the kingdom.")
    print("All of this is meaningless, because the Demon King that Solomon had sealed long ago was released.")
    print(name + " we need your help to defeat the Demon King and reunite Solomon's Kingdom!")

    print("\n\n")

    while True:
        letter = input(prompt)
        if letter in answer1:
            print(name +", I a God thanks you for your true courage. I have the upmost faith in you to complete your mission!")
            break
        if letter in answer2:
            print("WELL FUCK YOU NO IS NOT AN OPTION LOL!!!!!")
            break
        else:
            print("You must be retarded you either need to pick a y or a n redo it idiot!")



def choose_class():

    classes = "Mage", "Warrior", "Hunter", "Necromancer", "Assassin", "Priest"



    
    print("""
            
           Classes      Strength     Intellect    Agility    Adapt     Regeneratio
          ---------    ----------   -----------  ---------  -------   --------------
            Mage           1            10           2         2             5
            Warrior        10            1           5         4             3
            Hunter         5             4           8         10            4
            Necromancer    3             8           3         5             4
            Assassin       5             3           10        8             3
            Priest         1             8           3         3             10
            """)

    adventurer = input("""As an adventurer pick a class: """)
    

    if adventurer == "Mage":
        print("""You have Chosen the Mage class their intellect and casting abilities is fierce.
                Spells     Damage(Depends on type of opponent)
               --------   -------------------------------------
               Fireball                   10+
               Ice Blast                  8+
               Self Aid                   +4(recovery move)
               Gravity Bomb(Special)      15+
               """)
    if adventurer == "Warrior":
        print("""You have chosen the Warrior class their strength has been blessed by ME!
                Spells     Damage(Depends on type of opponent)
               --------   -------------------------------------
               Sword Strike               8+
               counter Strike             5+
               Self Aid                   +4(recovery move)
               Berserker Rage             12+
               """)

    if adventurer == "Hunter":
        print("""You have chosen the Hunter class as a hunter you get a loyal wolf as a pet.
               Spells     Damage(Depends on type of opponent)
              --------   -------------------------------------
              Wolf Strike               8+
              Killer Instinct           +5(to all Damage)
              Self Aid                   +4(recovery move)
              Howling Fang              10+
              """)
    if adventurer == "Assassin":
        print("""You have chosen the Assassin class. They are very cunning and illusive individuals.
               Spells     Damage(Depends on type of opponent)
              --------   -------------------------------------
              Vanish                     0
              Hidden Blade               10+
              Self Aid                   +4(recovery move)
              Dance of Blades            15+
              """)
    if adventurer == "Priest":
        print("""You have chosen the Priest class. Just because they are a healing class doesn't mean they cant fight!
               Spells     Damage(Depends on type of opponent)
              --------   -------------------------------------
              Smite                      +10
              Heal                        8+
              Light Attack               +5
              God's Blessing              10+
              """)

    if adventurer == "Necromancer":
        print("""You have chosen the Necromancer. Don't be surprised with the sheer amount of creepiness you get from being them.
               Spells     Damage(Depends on type of opponent)
              --------   -------------------------------------
              Raise Dead                  8+
              Death Strike                10+
              Self Aid                   +4(recovery move)
              Zombie Armada               15+
              """)
    if adventurer != classes:
        print("""DO IT AGIAN""")

def starter_zone():
    time.sleep(3)
    print("\n")
    countdown = 10
    while countdown:
        print (countdown),
        countdown -= 1
    print("""\n\nPFFFFFT You are now in Edom!!!! Please don't die I will have to reincarnate
somebody else all over agian. It will surely be annoying. Best of luck on your Journey!!!""")

title_screen()
title_screen_selectors()
choose_class()
starter_zone()
