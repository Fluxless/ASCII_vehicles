from rich.console import Console
from asciimatics.screen import Screen
from asciimatics.effects import Print
from asciimatics.renderers import FigletText
import time
import random
import shutil
import os

print("test")

car_art = """
     ______
    /|_||_\`.__
    (   _    _ _|
    =`-(_)--(_)-'

"""

boat_art = """
      __|__ |___| |'\`
      |o__| |___| | '\`
      |___| |___| |o '\`
     _|___| |___| |__o'\`
    /...\_____|___|____\_/
    \   o * o * * o o  /
  ~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

heli_art = """

      -----|-----
    *>=====[_]L)
        -'-`-

"""

heli_art_mirror = """

  -----|-----
     (_|[_]=====<*
      -'-`-

"""

plane_art = """
            ______
            _\ _~-\___
    =  = ==(____AA____D
                \_____\___________________,-~~~~~~~`-.._
                /     o O o o o o O O o o o o o o O o  |\_
                `~-.__        ___..----..                  )
                      `---~~\___________/------------`````
                      =  ===(_________D
"""

convoy_art = """
                                                            __________________________
                        /\\      _____          _____       |   |     |     |    | |  \  
        ,-----,       /  \\____/__|__\_    ___/__|__\___   |___|_____|_____|____|_|___\ 
    ,--'---:---`--, /  |  _     |     `| |      |      `| |                    | |    \.
    ==(o)-----(o)==J    `(o)-------(o)=   `(o)------(o)'   `--(o)(o)--------------(o)--'  
    `````````````````````````````````````````````````````````````````````````````````````
"""

car_art2 = """

        ,-----, 
    ,--'---:---`--,
    ==(o)-----(o)==J

"""


bus_art = """
    .-------------------------------------------------------------.
    '------..-------------..----------..----------..----------..--.|
    |       \\            ||          ||          ||          ||  ||
    |        \\           ||          ||          ||          ||  ||
    |    ..   ||  _    _  ||    _   _ || _    _   ||    _    _||  ||
    |    ||   || //   //  ||   //  // ||//   //   ||   //   //|| /||
    |_.------"''----------''----------''----------''----------''--'|
    |)|      |       |       |       |    |      mga|      ||==|  |
    | |      |  _-_  |       |       |    |  .-.    |      ||==| C|
    | |  __  |.'.-.' |   _   |   _   |    |.'.-.'.  |  __  | "__=='
    '---------'|( )|'----------------------'|( )|'----------""

"""



cementmixer_art = """

        _.--,_......----..__
        \  .'          '    ```--...__      \.
            \;           '            .  '.   ||
            :           '            '     \ .''.
        .';          :            '       .|  |.--..___
        /   \         |           :        :|  /.------.\.
        /    .'._      :           |        ||  ||      |\`\`
    /.-. /|-| `-.               :        ;|  ||______|_\`.______
    //  // |-|    \   '           '      / |  ||='      | |      `.
    //  //\\|-|     `-._'           '   .'  |  ||        | |        \.
    /.-.//  \\-|_________```------------` ___'. ||        | '_.--.   <)
    '._.'  /  .-----.   .-----.   .''''''''.    |'--..____| /  _  \   |
        |_/.'   '.\_/.'   '.\_[ [ [  ] ] ]___|_________.'.'   '.\  ]
            :  .-.  : :  .-.  :  '........'    (_________):  .-.  :`-'
            :  '-'  : :  '-'  :                           :  '-'  :
             '._ _.'   '._ _.'                             '._ _.'
"""

pickuptruck_art = """
                                                         o
                                        _.-------._      |
                                        /___________\    |
                                        :.----------,\   |
                                        ||           \\  |
                                        ||            \\ |
                                        ||             \\|_
                                        ||              \\/ .---------.
    .____________________________________||_______________\\_(_________)_
    | .---.                        .---. |                `%,------------~-.
    | |(O)|                        |(O)| |  __             |               |
    (| `---'                        `---' | (- \            |               |)
    (|                                    |  ~~             |               |
    |                                    |                 |               |
    |       __,---,__                    |                `%,  __,---,__   |_
    =|______//       \\___________________|_________________|__//       \\__|_]
            |   .-.   |                                        |   .-.   |
            |   `-'   |                                        |   `-'   |
            \_      _/                                          \_     _/
               `---'                                              `---'
"""

family_car = """
                        ____________________
                        //|           |        \`
                    //  |           |          \`
        ___________//____|___________|__________()\__________________
        /__________________|_=_________|_=___________|_________________{`}`
        [           ______ |           | .           | ==  ______      { }
    __[__        /##  ##\|           |             |    /##  ##\    _{# }_
    {_____)______|##    ##|___________|_____________|___|##    ##|__(______}
                /  ##__##                              /  ##__##        \`

"""


fiat_car = """
                    _________________
                _.-'_____  _________ _`.
                .` ,'      ||         | `.`.
            .` ,'        ||         |   `.`.
            .`  /          ||         |  ,' ] `....___
        _`__.'''''''''''''''''''''''`''''''''|..___ `-.._
        .'                  [='                '     `'-.._`.
    ,:/.'''''''''''''''''''|''''''''''''''''''|'''''''''''\`\`
    //||    _..._         |                  '    _..._  |)|
    /|//   ,',---.`.       |                  |  .',---.`.\>|
    (':/   //' .-. `\\      \_________________/  '/' .-. `\\|_)
    `-...'||  '-'  ||________,,,,,,,,,,,,,,,__.'||  '-'  ||-'
        '.'.___.','                           '.'.___.','
            '-.m.-'                               '-.m.-'
"""

classic_car_art_mirror = """
                ______--------___
                /|             / |
    o___________|_\__________/__|
    ]|___     |  |=   ||  =|___  |"
    //   \\    |  |____||_///   \\|"
    |  X  |\--------------/|  X  |\"
    \___/                  \___/
 """



normal_car_mirror = """
            _______
        //  ||\ \`
    _____//___||_\ \___
    )  _          _    \`
    |_/ \________/ \___|
    ___\_/________\_/______

"""



car2_mirror = """
                                    _______________________________ 
                                _.-'`````-._   ````````-._     ``````-._
                            .'_____________  _____   ______   ________ `. 
                            '.-----..-----. '.-----.|.------.|.---------.|
                            //     //     / //      :|:      :|:         :|
                        //_____//_____/ //       :|:      :|:         :|
            _..----------------='.......'|`-------'|'------'|'---------'|
        .-'        --== ----- ==--   '|.-------.|.------.|.---------.|
    _.' _.-'-._        .----------..._' |:     ->:|:    ->:|: .--------.
    .''.-'_.-'-._`-.''.'              ```\|'-------'|'------' .'          `._
    |()|===========|()|      _____        \.-------.|.------.'  .------.    \]
    .'..'..--'''--..'..'   .' ._._.`.      |:       :|:     /  .'.'-'-'-.`.   \`
    | ||_..--'''--.._||   /..'-'-'-'.\     |'-------'_'----'. / .' .---. .'\   ]
    | ||_..--'''--.._||  /..' .---. .'\    |_`_`_`_`_`_`_`_`_|..' / .^. \ .'`--'
    '.-'-------------'-.| .' / .^. \ .''...' - - - - - - - - '..' \ 'v' / '..
    '-----------------''..' \ 'v' / '..         `..'._._.'.''..'  `---'  '..
        `..'._._.'.'   '..'  `---'  '..           ``'-'-''   `..'._._._.'.. 
        ``'-'-''      `..'._._._.'..                         ``'-'-'-'-'
                      ``'-'-'-'-'
"""


monster_truck_mirror = """
                                    (>|          
                                    (>|======\`\    
                                _________||____ `\`\`
                            _-~~~~~~~~~|~|~~~|~|  |\`\ 
                        /           | |   | |  ||`\`\`
                        /_            | |   | |  ||  `\`\ 
            ____-------(_|____________|_|___| |  ||    ||`                _-~~~|
        _--~~~            |            =|       ||~~~~~~~~~~~~~~~~~~~~~~~~~     |
    |]                 |             |       ||                              |
    |=   /~~~~~~~~~~\  |            /'       ||          /~~~~~~~~~~\        |
    :~~~~/'  _ ----- _ `\~~~~~~~~~~~~~~~~~~~~~~||~~~~~~~~/'  _ ----- _
    `\~~~~~~~~|
    |   | _-~         ~-_|_____________==______||_______| _-~         ~-_|  __--~
    `~~~~/    _-----_    \____________________//_______/-/    _-----_    \~~
        ;    / \ _ / \    .                             :    / \ _ / \    .
        |   | -((*))- |   |                             |   | -((*))- |   |
        |    \  / \  /    |                             |    \  / \  /    ,
        \    ~-----~    /                               \    ~-----~    /
        ~-_         _-~                             _---`-_         _-~
    --~~~|\~~ ----- ~\__--~~-\-^^^^\___-~`~~---___--/       ~ ----- ~ -/_--~~\`
"""


sports_car_art = """
                        ___..............._
                __.. ' _'.""""""\`\""""""""- .`-._
    ______.-'         (_) |      \`\           ` \`\`-. _
    /_       --------------'-------\`\---....______\`\__`.`  -..___
    | T      _.----._           Xxx|x...           |          _.._`--. _
    | |    .' ..--.. `.         XXX|XXXXXXXXXxx==  |       .'.---..`.     -._
    \_j   /  /  __  \  \        XXX|XXXXXXXXXXX==  |      / /  __  \ \        `-.
    _|  |  |  /  \  |  |       XXX|""'            |     / |  /  \  | |          |
    |__\_j  |  \__/  |  L__________|_______________|_____j |  \__/  | L__________J
        `'\ \      / ./__________________________________\ \      / /___________\`
            `.`----'.'                                     `.`----'.'
              `""""'                                         `""""'
"""


fighter_plane_mirror = """
                ____
    |        | ___\          /~~~|
    _:_______|/'(..)`\_______/  | |
    <_|``````  \__~~__/  USAF ___|_|
    :\_____(=========,(*),--\__|_/
    |       \       /---'
            | (*) /
            |____/

            
"""

reverse_boat = """
                                    )___(
                            _______/__/_
                    ___     /===========|   ___
    ____       __   [\\\]___/____________|__[///]   __
    \   \_____[\\]__/___________________________\__[//]___
    \`40A                                                 |
    \                                                   /
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

submarine = """
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~oo~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                    o o
                                    o ooo
                                    o oo
                                        o o      |   #)
                                        oo     _|_|_#_    
                                            o   | 751   |
        __                    ___________________|       |_________________
    |   -_______-----------                                              \`
    >|    _____                                                   --->     )
    |__ -     ---------_________________________________________________ /

"""

battleship = """
                                        |__
                                        |\/
                                        ---
                                        / | [
                                !      | |||
                                _/|     _/|-++'
                            +  +--|    |--|--|_ |-
                        { /|__|  |/\__|  |--- |||__/
                        +---------------___[}-_===_.'____               /\`
                    ____`-' ||___-{]_| _[}-  |     |_[___\==--          \/   _
    __..._____--==/___]_|__|_____________________________[___\==--___,-----' .7
    |                                                                   BB-61/
    \_______________________________________________________________________|

"""

steam_train = """

    _____                 . . . . . o o o o o
    __|[_]|__ ___________ _______    ____      o
    |[] [] []| [] [] [] [] [_____(__  ][]]_n_n__][.
    _|________|_[_________]_[________]_|__|________)<
    oo    oo 'oo      oo ' oo    oo 'oo 0000---oo\_
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

steam_train_reverse = """
        o o o o o o o . . .   ______________________________ _____=======_||____
    o      _____           ||                            | |                 |
    .][__n_n_|DD[  ====_____  |        Luxury Goods        | | General Freight |
    >(________|__|_[_________]_|____________________________|_|_________________|
    _/oo OOOOO oo`  ooo   ooo  'o!o!o                  o!o!o` 'o!o         o!o`
    -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

"""

truck_reverse = """
                        _____________________________________________________
                        |                                                     |
                _______  |                                                     |
                / _____ | |                       ACME MOO-VERS                 |
            / /(__) || |                                                     |
    ________/ / |OO| || |                                                     |
    |         |-------|| |                                                     |
    (|         |     -.|| |_______________________                              |
    |  ____   \       ||_________||____________  |             ____      ____  |
    /| / __ \   |______||     / __ \   / __ \   | |            / __ \    / __ \ |\`
    \|| /  \ |_______________| /  \ |_| /  \ |__| |___________| /  \ |__| /  \|_|/
    | () |                 | () |   | () |                  | () |    | () |
        \__/                   \__/     \__/                    \__/      \__/

"""

sports_car_reverse = """
                                 _..-------++._
                             _.-'/ |      _||  \`--._
                       __.--'`._/_\j_____/_||___\    `----. 
                  _.--'_____    |          \     _____    / 
                _j    /,---.\   |        =o |   /,---.\   |_ 
               [__]==// .-. \\==`===========/==// .-. \`\=[__] 
                 `-._|\ `-' /|___\_________/___|\ `-' /|_.'     
                       `---'                     `---' 

"""



def generate_random_hex_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
    return hex_color


def apply_color(line, color):
    return f"\033[38;2;{int(color[1:3], 16)};{int(color[3:5], 16)};{int(color[5:], 16)}m{line}\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_animate(vehicle, colour):
    def animate(screen):
        colored_text = f"\033[38;2;{int(colour[1:3], 16)};{int(colour[3:5], 16)};{int(colour[5:], 16)}m"
        reset_color = "\033[0m"
        terminal_size = shutil.get_terminal_size()
        terminal_width = shutil.get_terminal_size().columns
        obj_text = f"""
        {colored_text}
        {vehicle}
        """
        lines = obj_text.splitlines()
        max_line_length = max(len(line) for line in lines)
        x = -max_line_length
        while True:
            screen.clear()
            for y, line in enumerate(lines):
                screen.print_at(line, x, y+5)
            x += 1
            screen.refresh()
            if max_line_length < 9:
                time.sleep(0.01)
            else:
                time.sleep(0.02)
            if x > terminal_width + max_line_length:
                clear_screen()
                break
    return animate


def create_animate_reverse(vehicle, colour):
    def animate(screen):
        colored_text = f"\033[38;2;{int(colour[1:3], 16)};{int(colour[3:5], 16)};{int(colour[5:], 16)}m"
        reset_color = "\033[0m"
        terminal_size = shutil.get_terminal_size()
        terminal_width = shutil.get_terminal_size().columns
        obj_text = f"""
        {colored_text}
        {vehicle}
        """
        lines = obj_text.splitlines()
        max_line_length = max(len(line) for line in lines)
        x = terminal_width+max_line_length
        while True:
            screen.clear()
            for y, line in enumerate(lines):
                screen.print_at(line, x, y+5)
            x -= 1
            screen.refresh()
            if max_line_length < 9:
                time.sleep(0.01)
            else:
                time.sleep(0.02)
            if x < 0 - max_line_length:
                clear_screen()
                break
    return animate



def create_animate_glitch(vehicle):
    def animate(screen):
        obj_text = vehicle
        lines = obj_text.splitlines()
        max_line_length = max(len(line) for line in lines)
        x = -max_line_length

        # Using predefined color constants
        text_color = generate_random_hex_color() 
        checks=0
        while True:

            for y, line in enumerate(lines):
                for i in range(0, len(line), max_line_length):
                    text_color = generate_random_hex_color()
                    if 0 <= x + i < screen.width:
                        colored_line = apply_color(line, text_color)
                        screen.print_at(colored_line, x, y+5)
                        if checks==0:
                            clear_screen()
                            checks+=1
                    else:
                        screen.print_at(line, x, y+5)
            x += 1
            screen.refresh()
            if max_line_length < 9:
                time.sleep(0.01)
            else:
                time.sleep(0.02)

            # Break the loop if the object moves off the screen
            if x > screen.width + max_line_length-5:
                break


    return animate

def create_animate_glitch_reverse(vehicle):
    def animate(screen):
        terminal_size = shutil.get_terminal_size()
        terminal_width = shutil.get_terminal_size().columns
        obj_text = vehicle
        lines = obj_text.splitlines()
        max_line_length = max(len(line) for line in lines)
        x = terminal_width+max_line_length

        # Using predefined color constants
        text_color = generate_random_hex_color() 
        checks=0
        while True:

            for y, line in enumerate(lines):
                for i in range(0, len(line), max_line_length):
                    text_color = generate_random_hex_color()
                    if 0 <= x + i < screen.width:
                        colored_line = apply_color(line, text_color)
                        screen.print_at(colored_line, x, y+5)
                        if checks==0:
                            clear_screen()
                            checks+=1
                    else:
                        screen.print_at(line, x, y+5)
            x -= 1
            screen.refresh()
            if max_line_length < 9:
                time.sleep(0.01)
            else:
                time.sleep(0.02)

            # Break the loop if the object moves off the screen
            if x < 0 - max_line_length:
                break


    return animate




vehicles = [car_art, boat_art, heli_art, plane_art, convoy_art, bus_art, cementmixer_art, pickuptruck_art, family_car, fiat_car, sports_car_art, submarine, battleship, steam_train]
reverse_vehicles = [heli_art_mirror, classic_car_art_mirror, normal_car_mirror, classic_car_art_mirror, car2_mirror, monster_truck_mirror, fighter_plane_mirror, reverse_boat, steam_train_reverse, truck_reverse, sports_car_reverse]

while True:
    chance = random.randint(1, 20)
    selected_colour = generate_random_hex_color()
    selected_colour_reverse = generate_random_hex_color()
    selected_vehicle = random.choice(vehicles)
    selected_vehicle_glitch = random.choice(vehicles)
    selected_vehicle_reverse_glitch = random.choice(reverse_vehicles)
    selected_vehicle_reverse = random.choice(reverse_vehicles)
    #if chance == 1:
        #Screen.wrapper(create_animate_glitch(selected_vehicle_glitch))
    #else:
        #Screen.wrapper(create_animate(selected_vehicle, selected_colour))
    clear_screen()
    #Screen.wrapper(create_animate_reverse(selected_vehicle_reverse, selected_colour_reverse))
    clear_screen()
    Screen.wrapper(create_animate_glitch_reverse(selected_vehicle_reverse_glitch))