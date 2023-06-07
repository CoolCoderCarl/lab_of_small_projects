"""Deep Cave, by Al Sweigart al@inventwithpython.com
An animation of a deep cave that goes forever into the earth.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, scrolling, artistic"""

import random
import sys
import time

# Set up the constants:
WIDTH = 60  # (!) Try changing this to 10 or 30.
PAUSE_AMOUNT = 0.05  # (!) Try changing this to 0 or 1.0.

print('Deep Cave, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to stop.')
time.sleep(2)

left_width = 20
gap_width = 10

while True:
    # Display the tunnel segment:
    right_width = WIDTH - gap_width - left_width
    print(('#' * left_width) + (' ' * gap_width) + ('#' * right_width))

    # Check for Ctrl-C press during the brief pause:
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.

    # Adjust the left side width:
    dice_roll = random.randint(1, 6)
    if dice_roll == 1 and left_width > 1:
        left_width = left_width - 1  # Decrease left side width.
    elif dice_roll == 2 and left_width + gap_width < WIDTH - 1:
        left_width = left_width + 1  # Increase left side width.
    else:
        pass  # Do nothing; no change in left side width.

    # Adjust the gap width:
    # (!) Try uncommenting out all the following code:
    dice_roll = random.randint(1, 6)
    if dice_roll == 1 and gap_width > 1:
        gap_width = gap_width - 1  # Decrease gap width.
    elif dice_roll == 2 and left_width + gap_width < WIDTH - 1:
        gap_width = gap_width + 1  # Increase gap width.
    else:
        pass  # Do nothing; no change in gap width.
