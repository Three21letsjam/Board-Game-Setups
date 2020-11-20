import random
import sys


class Seasons:
    SPRING = 'spring'
    SUMMER = 'summer'
    AUTUMN = 'autumn'


class Monsters:
    monster_dict    =   {
                            Seasons.SPRING: ['Earth Dragon', 'Jinmenju', 'Jorogumo', 'kotahi', 'Phoenix'],          
                            Seasons.SUMMER: ['Fire Dragon', 'Jikininki', 'Koneko', 'Nure-Onna', 'Sunakake-Baba'],
                            Seasons.AUTUMN: ['Daikaiju', 'Kitsune', 'Oni of Plagues', 'Sacred Warrior'],
                        }
    @staticmethod
    def add_monsters(season):
        try:
            amount  = int(input(f'How many monsters would you like to add for {season}?'))
            amount  = amount if 0 <= amount <= 5 else random.randint(0, 5)
        except ValueError:
            amount  = random.randint(0, 5)
        finally:
            ret     = set()
            while len(ret) < amount:
                ret.add(random.choice(Monsters.monster_dict[season]))
            return ret

class Clan:
    CORE    = 'core'
    DYNASTY = 'dynasty'
    KSE     = 'kse'

    def __init__(self, expansion, name, honor, coins):
        self.expansion  = expansion
        self.name       = name
        self.honor      = honor
        self.coins      = coins
        self.player     = ""

    def __repr__(self):
        return self.string()

    def __str__(self):
        return f"Set({self.expansion}) Clan({self.name}) Honor({self.honor}) Coins({self.coins}) Player({self.player})"


def get_player_names():
    name_list = []
    print("Enter the name of each player on a new line")
    while len(name_list) < 6:
        name = input("name (or <ENTER> when done) >>> ")
        if not name:
            if len(name_list) < 3:
                print("Min player count is 3")
                continue
            else:
                break
        name_list.append(name)
    return name_list


def choose_clans(player_list):
    clans   =   [
        Clan(Clan.CORE,    'Koi',       1, 5),
        Clan(Clan.CORE,    'Lotus',     3, 7),
        Clan(Clan.CORE,    'Turtle',    4, 6),
        Clan(Clan.CORE,    'Dragonfly', 5, 6),
        Clan(Clan.CORE,    'Bonsai',    7, 4),
    ]

    if input('Are you playing with the Dyasty invasion expansion? (y/n)').lower().startswith('y'):
        clans.append(Clan(Clan.DYNASTY, 'Sun',       2, 7))
        clans.append(Clan(Clan.DYNASTY, 'Moon',      8, 4))

    if input('Are you playing with the kickstarter exclusive Fox clan? (y/n)').lower().startswith('y'):
        clans.append(Clan(Clan.KSE,     'Fox',       6, 5))

    if len(player_list) > len(clans):
        print("Not enough clans for this player count, exiting")
        sys.exit(0)
    
    for player in player_list:      
        while True: # not efficient, but good enough
            clan = random.choice(clans)
            if not clan.player:
                clan.player = player
                print(clan)
                break


def choose_kami():
    kami            = ['Amaterasu', 'Tsukuyomi', 'Susano\'o', 'Hachiman', 'Ryujin', 'Fujin', 'Raijin'] 
    selected_kami   = set()
    while len(selected_kami) < 4:
        k = random.choice(kami)
        kami.remove(k)
        selected_kami.add(k)
    print('\n'.join(list(selected_kami)))


def choose_season_set():
    #Chooses a random season card set from the the base game. Allows user to add other sets depending on expansions owned.
    season_set = ['archway', 'teapot', 'horseman']

    if input('Add mountain set to list of available card sets (y/n)? ').startswith('y'):
        season_set.append('mountain')
    if input('Add ship set to list of available card sets (y/n)? ').startswith('y'):
        season_set.append('ship')
    if input('Add tower set to list of available card sets (y/n)? ').startswith('y'):
        season_set.append('tower')

    print(f'The set played will be: {random.choice(season_set)}')


def get_provinces(player_list):
    provinces           = ['Kyushu', 'Shikoku', 'Nagato', 'Kansai', 'Kyoto', 'Edo', 'Oshu', 'Hokkaido']
    selected_provinces  = set()
    while len(selected_provinces) < (len(player_list) + 2):
        p = random.choice(provinces)
        provinces.remove(p)
        selected_provinces.add(p) 
    print('\n'.join(list(selected_provinces)))

    
def main():
    random.seed()

    players = get_player_names()
    print()
    
    choose_clans(players)
    print()

    print('Place kami from left to right.')
    choose_kami()
    print()

    choose_season_set()
    print()

    if input('Would you like to add kickstarter exclusive monsters to the game? (y/n)').lower().startswith('y'):
        print(f"Add {Monsters.add_monsters(Seasons.SPRING)} to the {Seasons.SPRING} set")
        print(f"Add {Monsters.add_monsters(Seasons.SUMMER)} to the {Seasons.SUMMER} set")
        print(f"Add {Monsters.add_monsters(Seasons.AUTUMN)} to the {Seasons.AUTUMN} set")

    #prints out contested province tiles for all 3 seasons
    for season in [Seasons.SPRING, Seasons.SUMMER, Seasons.AUTUMN]:
        print()
        input(f"Press enter when ready for contested provinces in {season}")
        print(f"{season}'s provinces in order are:")
        print()
        get_provinces(players)
        print()


if __name__ == "__main__":
    main()
