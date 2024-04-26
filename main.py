import random
import sys

def main():
    print_welcome_screen()
    
    best_roll: int = 0
    crit_counter: int = 0
    
    #Loops until user exits
    while True:
        user_input: str = input("What combination of dice do you want to throw?").lower()
        
        if user_input == "exit":
            print_end_screen(best_roll, crit_counter)
            sys.exit()
        elif user_input == "help":
            print("""
                  The format of the input should look something like this: 
                  '1d4 3d6 2d20' if you wish to roll one D4, 3 D6s and 2 D20s.
                  """
                  )
            continue
            
        dice_dict = parse_input(user_input)
        total, best_roll, crit_counter = roll_dice(dice_dict, best_roll, crit_counter)
        print(total)
    
def roll_dice(dice_dict, best_roll, crit_counter):
    total: int = 0
    for sides, num_dice in dice_dict.items():
        for _ in range(num_dice):
            roll: int = random.randint(1, sides)
            if sides == 20:
                if roll == 20:
                    crit_counter += 1
            total += roll
    
    if total > best_roll:
        best_roll = total 
        
    return total, best_roll, crit_counter
    
def print_welcome_screen():
    welcome_screen: str = '''
    ______  _               _____  _                                        
    |  _  \(_)             |_   _|| |                                       
    | | | | _   ___   ___    | |  | |__   _ __   ___  __      __  ___  _ __ 
    | | | || | / __| / _ \   | |  | '_ \ | '__| / _ \ \ \ /\ / / / _ \| '__|
    | |/ / | || (__ |  __/   | |  | | | || |   | (_) | \ V  V / |  __/| |   
    |___/  |_| \___| \___|   \_/  |_| |_||_|    \___/   \_/\_/   \___||_|   

    Welcome to this dice throwing app that lets you throw a plethora of dice, all at the same time.
    Commands:
    help -- display a guide for formatting dice throws
    exit -- Exit the game
    '''

    print(welcome_screen)

def print_end_screen(best_roll, crit_counter):
    #TODO: Add the number of critical wins and fails to end screen.
    end_screen = f'''
    Thank you for rolling dice!
    
    -----Stats for the session-----
    Best roll: {best_roll}
    Critical Hits: {crit_counter}
    '''
    print(end_screen)
    
def parse_input(user_input):#format of input string is for example: "1d4 4d12"
    dice_dict: dict = {}
    
    elements: list = user_input.split()
    for element in elements:
        num_dice = int(element.split('d')[0])
        sides = int(element.split('d')[1])
        dice_dict[sides] = num_dice
    return dice_dict

if __name__ == '__main__':
    main()