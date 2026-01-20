"""  ----- Simulation -----  """
from itertools import count
import random
import pprint
# import time (optional)


total_rounds = int(input(f"How many rounds do you want to run? "))
if total_rounds > 0:
    print(f" Starting ts")
    count_each_winning_number = { 
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            10: 0,
            11: 0,
            12: 0,
        }
    continue_playing = True
    while continue_playing:
        for round in range(total_rounds):
            number_of_rounds_played = 0
            current_number = 12
            numbers_not_colored_yet = [1,2,3,4,5,6,7,8,9,10,11]
            last_number = 0
            while last_number == 0:
                direction = random.choice([-1, 1]) #+1 clockwise -1 counter
                # print(f"From {current_number} --> {current_number + direction}")
                current_number += direction
                if current_number == 0:
                    current_number = 12
                elif current_number == 13:
                    current_number = 1
                number_of_rounds_played += 1 # will use later
                # time.sleep(0.03) if you wanna see it type
                # check if the last number to check colored
                if current_number in numbers_not_colored_yet:
                    numbers_not_colored_yet.remove(current_number) 
                if not numbers_not_colored_yet:
                    last_number = current_number
                    print(f"The last number to get colored was: {last_number}")
                    
            count_each_winning_number[last_number] += 1 
            last_number = 0
            round += 1
        print(f"--------------------------------")
        print(f"Winners:")
        print(f"--------------------------------")
        want_to_print_zeros = 0 #1 for yes 0 for no
        if want_to_print_zeros == 1:
            pprint.pprint(count_each_winning_number, width=1)
        elif want_to_print_zeros == 0:
            for key,value in count_each_winning_number.items():
                if value != 0:
                    print(f"{key} : {value}")
        continue_playing = False
        a = input(f"Want to run another simulation? [Y/N]")
        if a == "Y" or a =="y":
            continue_playing = True
            b = input(f"Want to change amount of rounds? [Y/N]")
            if b == "Y" or b == "y":
                total_rounds = int(input(f"How many rounds do you want to run? "))



