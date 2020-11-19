# Rising Sun Setup
_______

A set-up application for the board game *Rising Sun* to help get your game to the table faster and cut down on the decision making/randomized processes such as who gets which clan, which season card set to add, which/how many provinces are contested each season, and which/how many kickstarter monsters to use.


## Instillation
______
You will need to have downloaded [Python 3]( https://www.python.org/downloads/) as well as the source code file [RisingSunSetup.py](https://github.com/Three21letsjam/Board-Game-Setups/blob/main/RisingSunSetup.py). Open the file through Python then select Run -> run module, and you should be set!

OR 

copy the source code and paste into an online python complier such as: <https://repl.it/languages/python3>

## How it Works
______
While no knowledge of coding in Python is required to use this application you will need to answer some questions throughout your setup process. The general rule of thumb with this program is when the computer poses a question to the user it also provides valid answers in parenthesis. After typing their answer the user must confirm with the **Enter** key in order to proceed with the setup.

### Safeguards
I also made sure that the program would not be too picky over the user's inputs.  As such, capitalization and punctuation is not needed to properly use this app.   Additionally, if the user enters an invalid answer, such as a number of players that cannot play this game, the program will reprompt them for a valid one. In the specific event the user enters six players, but does not choose to add a sixth available clan (either through Dynasty Invasion or the kickstarter exclusive Fox clan) the program will ask the user to pick an expansion or to remove a player so the base game of Risisng Sun can be played with five players. (see below for example)

### However...
There is a bug in this current build: **When being asked for the number of kickstarter exclusive monsters to add to each season only enter a whole number.** Long story short entering anything else like a letter, word, punctuation, or decimal point value will cause the program to crash. I've made the program so that it reminds you when it gets to this point in the setup, but accidents happen and if the program crashes simply rerun the program for a new setup.

## FAQ
___

*Why is there no option to only select additional monsters from the monster pack expansion?*

My logic was that if one was using only monsters from the monster pack expansion and not the kickstarter promos they would include all four due to their game effects, aesthetic value, and lack of analysis paralysis in the set up phase. 

*FAQ will be updated over time if necessary.*

## Support
___
If you still are in need of help, or have any ideas to add to this project feel  free to message me on Board Game Geek @ Three21letsjam.

## Examples
___

### Full setup walkthrough: user inputs in **bold**

*start program*

    Enter player names
**Alex Edward Terrance Jazmine**

    Are you playing with the Dyasty invasion expansion? (yes/no)
**yes**

    Are you playing with the kickstarter exclusive Fox clan? (yes/no)
**no**

    Alex: Koi (honor:1)(coins:5)
    Edward: Sun (honor:2)(coins:7)
    Terrance: Dragonfly (honor:5)(coins:6)
    Jazmine: Moon (honor:8)(coins:4)

    Place kami from left to right.
    Amaterasu
    Fujin
    Ryujin
    Susano'o

    You can add one or more additional season card sets to the pool of those chosen. (mountain, ship, tower) 
**ship mountian**

    The set played will be: ship

    Would you like to add kickstarter exclusive monsters to the game? (yes/no)
**yes**

    How many monsters would you like to add for spring? Note: Not entering a number will cause the program to crash.
**1**

    Phoenix

    How many monsters would you like to add for summer? Note: Not entering a number will cause the program to crash.
**3**

    Fire Dragon
    Sunakake-Baba
    Koneko

    How many monsters would you like to add for autumn? Note: Not entering a number will cause the program to crash.
**2**

    Sacred Warrior
    Kitsune

    Press enter when ready for contested provinces in Spring
*Press enter*

    Spring's provinces in order are:

    1. Shikoku
    2. Kyoto
    3. Nagato
    4. Kyushu
    5. Edo
    6. Oshu

    Press enter when ready for contested provinces in Summer
*Press enter*

    Summer's provinces in order are:

    1. Kansai
    2. Shikoku
    3. Kyoto
    4. Edo
    5. Kyushu
    6. Oshu

    Press enter when ready for contested provinces in Autumn
*Press Enter*

    Autumn's provinces in order are:

    1. Kyoto
    2. Hokkaido
    3. Oshu
    4. Shikoku
    5. Kansai
    6. Edo

*end of program*


### Too many players (add clans path): user inputs in **bold**


    Enter player names
**Alex Edward Terrance Jazmine Kaydra Micheal**

    Are you playing with the Dyasty invasion expansion? (yes/no)
**no**

    Are you playing with the kickstarter exclusive Fox clan? (yes/no)
**no**

    There are not enough clans for the given number of players. Would you like to add clans via expansion or remove a player? (add/remove)
**add**

    Would you like to add clans from the Dynasty Invasion expansion and/or the Fox Clan from the Daimyo Box? (Dynasty/Fox/both)
**both**

    Alex: Fox (honor:6)(coins:5)
    Edward: Sun (honor:2)(coins:7)
    Terrance: Bonsai (honor:7)(coins:4)
    Jazmine: Dragonfly (honor:5)(coins:6)
    Kaydra: Turtle (honor:4)(coins:6)
    Micheal: Koi (honor:1)(coins:5)


### Too many players example (remove path): user inputs in **bold**
    Enter player names
**Alex Edward Terrance Jazmine Kaydra Micheal**

    Are you playing with the Dyasty invasion expansion? (yes/no)
**no**

    Are you playing with the kickstarter exclusive Fox clan? (yes/no)
**no**

    There are not enough clans for the given number of players. Would you like to add clans via expansion or remove a player? (add/remove)
**remove**
    
    Which player would you like to remove?
**Alex**

    Edward: Turtle (honor:4)(coins:6)
    Terrance: Lotus (honor:3)(coins:7)
    Jazmine: Dragonfly (honor:5)(coins:6)
    Kaydra: Bonsai (honor:7)(coins:4)
    Micheal: Koi (honor:1)(coins:5)

# Acknowledgements
Game published by Cool Mini or Not (CMON), designed by Eric Lang, and art by Adrian Smith. 

# License
MIT







