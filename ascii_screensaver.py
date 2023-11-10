import time
import random
import os
import shutil
import random


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def spell_name(name):
    for n in name:
        print(n)
        time.sleep(1)
    print(f"Your name is {len(name)} letters!")



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
                                       _.-------._     |
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
         \_     _/                                          \_     _/
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
 \___/                  \___/"""



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




def print_car(vehicle, color="#000000"):
        colored_text = f"\033[38;2;{int(color[1:3], 16)};{int(color[3:5], 16)};{int(color[5:], 16)}m"
        reset_color = "\033[0m"
        terminal_size = shutil.get_terminal_size()
        terminal_height = round(terminal_size.lines * 0.5)
        terminal_width = shutil.get_terminal_size().columns
        num_newlines = random.randint(1, terminal_height)
        space = "\n" * num_newlines
        car = f"""
        {colored_text}
        {space}
        {vehicle}
        {reset_color} 
        """
        car_lines = car.splitlines()
        max_line_length = max(len(line) for line in car_lines)
        n=1
        terminal_size = shutil.get_terminal_size()
        terminal_width = shutil.get_terminal_size().columns
        trim_val = 0
        for i in range(60000):
            clear_screen()
            n += 1

            if trim_val == 0:
                for j in range(len(car_lines)):
                    spaces = " " * n
                    print(spaces + car_lines[j])
            else:
                for j in range(len(car_lines)):
                    spaces = " " * n
                    trimmed_line = car_lines[j][:-trim_val]
                    trimmed_line = colored_text + spaces + trimmed_line + reset_color
                    print(trimmed_line)

            total_len = len(spaces) + max_line_length - trim_val
            time.sleep(0.05)
            if trim_val >= max_line_length:
                clear_screen()
                break
            elif total_len > terminal_width:
                trim_val += 1

#car lines is a list - So it needs to work like this

## When the car reaches the edge of the screen it needs to somehow work out which lines are hitting the edge of the terminal
## Then it needs to trim one character per frame from the end of that line, as the spaces are added. But this has to be calculated for each line separately, instead of the max line like we're doing now. 
## Then it needs to calculate when the vehicle object has been fully trimmed. So like...for that we can use max. When trim_value = max_line_length or something, would be the new break condition.



def print_car_reverse(vehicle, color="#000000"):
    colored_text = f"\033[38;2;{int(color[1:3], 16)};{int(color[3:5], 16)};{int(color[5:], 16)}m"
    reset_color = "\033[0m"
    terminal_size = shutil.get_terminal_size()
    terminal_height = round(terminal_size.lines * 0.5)
    terminal_width = shutil.get_terminal_size().columns
    num_newlines = random.randint(1, terminal_height)
    space = "\n" * num_newlines
    car = f"""
    {colored_text}
    {space}
    {vehicle}
    {reset_color} 
    """
    car_lines = car.splitlines()
    max_line_length = max(len(line) for line in car_lines)
    terminal_width = shutil.get_terminal_size().columns
    n = terminal_width-max_line_length 

    for i in range(60000):  # Number of animation frames
        clear_screen()
        n -= 1
        if n < 0:
            n = 0
        for j in range(len(car_lines)):
            spaces = " " * n
            print(spaces + car_lines[j])
        time.sleep(0.05) #Animation speed

        if n == 0:
            clear_screen()
            break





def generate_random_hex_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
    return hex_color

vehicles = [car_art, boat_art, heli_art, plane_art, convoy_art, bus_art, cementmixer_art, pickuptruck_art, family_car, fiat_car, sports_car_art, submarine, battleship, steam_train]
reverse_vehicles = [heli_art_mirror, classic_car_art_mirror, normal_car_mirror, classic_car_art_mirror, car2_mirror, monster_truck_mirror, fighter_plane_mirror, reverse_boat, steam_train_reverse, truck_reverse, sports_car_reverse]

while True:
    selected_vehicle = random.choice(vehicles)
    selected_mirror_vehicle = random.choice(reverse_vehicles)
    selected_color = generate_random_hex_color()
    selected_mirror_color = generate_random_hex_color()
    print_car(selected_vehicle, selected_color)
    print_car_reverse(selected_mirror_vehicle,selected_mirror_color)