#rising sun setup
import random

#assigns each player a unique clan
def choose_clans(players):
    clans = ['Koi (honor:1)(coins:5)', 'Lotus (honor:3)(coins:7)',
             'Turtle (honor:4)(coins:6)', 'Dragonfly (honor:5)(coins:6)',
             'Bonsai (honor:7)(coins:4)']
    Dynasty = ['Sun (honor:2)(coins:7)','Moon (honor:8)(coins:4)']
    Fox_clan = ['Fox (honor:6)(coins:5)']

    print('Are you playing with the Dyasty invasion expansion? (yes/no)')
    if input().lower().startswith('y'):
        clans.extend(Dynasty)

    print('Are you playing with the kickstarter exclusive Fox clan? (yes/no)')
    if input().lower().startswith('y'):
        clans.extend(Fox_clan)

    # makes user either add an expansion or remove a player if base game is attempted to be played with 6 players.
    while len(players) > len(clans):
        print('There are not enough clans for the given number of players. Would you like to add clans via expansion or remove a player? (add/remove)')
        choice = input().lower()

        if choice.startswith('a'):
            print('Would you like to add clans from the Dynasty Invasion expansion and/or the Fox Clan from the Daimyo Box? (Dynasty/Fox/both)')
            choice_1 = input().lower()
            if choice_1.startswith('d'):
                clans.extend(Dynasty)
                
            elif choice_1.startswith('f'): 
                clans.extend(Fox_clan)
                
            if choice_1.startswith('b'): 
                clans.extend(Dynasty)
                clans.extend(Fox_clan)
                

        elif choice.startswith('r'):
            print('Which player would you like to remove?')
            remove_player = input().lower()
            if remove_player in players:
                players.remove(remove_player)
            else:
                print('That player is not currently in the game.')
                remove_player = input().lower()
                
            
                    
    selected_clans = [] #chooses x amount of clans to assign to players
    for i in range(len(players)):
        i = clans[random.randint(0,len(clans)-1)]
        while i in selected_clans:
            i = clans[random.randint(0,len(clans)-1)]
        selected_clans.append(i)

    
        
    for i in range(len(players)): #assigns selected clans to players
        players[i] += ': ' + selected_clans[i]
        print(players[i])
      
def choose_kami():
    kami = ['Amaterasu', 'Tsukuyomi', 'Susano\'o', 'Hachiman',
        'Ryujin', 'Fujin', 'Raijin'] 

    selected_kami = [] 
    for i in range(4):
        i = kami[random.randint(0,6)]
        while i in selected_kami:
            i = kami[random.randint(0,6)]
        selected_kami.append(i)
        print(i)
    
def choose_season_set():
    #Chooses a random season card set from the the base game. Allows user to add other sets depending on expansions owned.
    season_set = ['archway', 'teapot', 'horseman']

    
    print('You can add one or more additional season card sets to the pool of those chosen. (mountain, ship, tower)')
    additional_sets = input().lower()
    if 'mountain' in additional_sets:
        season_set.append('mountain')
    if 'ship' in additional_sets:
        season_set.append('ship')
    if 'tower' in additional_sets:
        season_set.append('tower')
    
    chosen_set = season_set[random.randint(0,len(season_set)-1)]       
    print('The set played will be: ' + chosen_set)

def get_provinces(players):
    provinces = ['Kyushu', 'Shikoku', 'Nagato', 'Kansai', 'Kyoto',
                 'Edo', 'Oshu', 'Hokkaido']

    selected_provinces = []
    for i in range(len(players)+2):
        j = provinces[random.randint(0,7)]
        while j in selected_provinces:
            j = provinces[random.randint(0,7)]
        selected_provinces.append(j)
        print('%d. ' % (i+1)+ j)
                 
def add_monsters(season = []):
    if 'Earth Dragon' in season:
        which_season = 'spring'
    elif 'Fire Dragon' in season:
        which_season = 'summer'
    else:
        which_season = 'autumn'

    print('How many monsters would you like to add for ' +which_season+'? Note: Not entering a number will cause the program to crash.')
    amount = int(input())
      
    while not (amount >= 0 and amount <= len(season)):
        print('Please enter a number from 0 to ' + str(len(season))+'.')
        amount = int(input())
          
    selected_monsters = []
    for i in range(amount):
        i = season[random.randint(0,(len(season))-1)]
        while i in selected_monsters:
            i = season[random.randint(0,(len(season)) -1)]
        selected_monsters.append(i)
        print()
        print(i)
    print()
        

# lists of Daimyo box/Monster pack monsters to pass to add_monsters
spring = ['Earth Dragon', 'Jinmenju', 'Jorogumo', 'kotahi', 'Phoenix']            
summer = ['Fire Dragon', 'Jikininki', 'Koneko', 'Nure-Onna', 'Sunakake-Baba']
autumn = ['Daikaiju', 'Kitsune', 'Oni of Plagues', 'Sacred Warrior']

#enters the number of players and rejects if less than 3 or more than 6
print('Enter player names')

players = input().lower().split()

while len(players) < 3 or len(players) > 6:
    print('Enter a valid number of players (3-6)')
    players = input().split()

#prints out clans, kami, and season card set

choose_clans(players)
print()

print('Place kami from left to right.')
choose_kami()
print()

choose_season_set()
print()

#Adds additional KS exclusive monsters 
print('Would you like to add kickstarter exclusive monsters to the game? (yes/no)')
if input().lower().startswith('y'):
    add_monsters(spring)
    add_monsters(summer)
    add_monsters(autumn)

#prints out contested province tiles for all 3 seasons
for i in range(3):
    if i == 2:
        season = 'Autumn'
    elif i == 1:
        season = 'Summer'
    else:
        season = 'Spring'
    print()
    print('Press enter when ready for contested provinces in', season)
    input()
    print(season + '\'s provinces in order are:')
    print()
    get_provinces(players)
    print()
   
    







            


