"""  ----- Simulation -----  """
import random
# import time (optional)

number_of_rounds = 0
current_number = 12
numbers_not_colored_yet = [1,2,3,4,5,6,7,8,9,10,11]
count_each_number = { #maybe later i will use it
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
    12: 1,
}
last_number = 0

print(f" Starting ts")
while last_number == 0:
    direction = random.choice([-1, 1]) #+1 clockwise -1 counter
    print(f"From {current_number} --> {current_number + direction}")
    current_number += direction
    if current_number == 0:
        current_number = 12
    elif current_number == 13:
        current_number = 1
    count_each_number[current_number] += 1 # will use later
    number_of_rounds += 1 # will use later
    # time.sleep(0.1) if you wanna see it type
    # check if the last number to check colored
    if current_number in numbers_not_colored_yet:
        numbers_not_colored_yet.remove(current_number) 
    if not numbers_not_colored_yet:
        last_number = current_number
        print(f"The last number to get colored was: {last_number}")
        

