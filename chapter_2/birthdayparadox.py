"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, math, simulation"""

import datetime
import random
from typing import List

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')


def get_birthdays(number_of_birthdays) -> List[datetime.date]:
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(number_of_birthdays):
        start_of_year = datetime.date(2001, 1, 1)
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays


def get_match(birthdays):
    """Returns the date object of a birthday that occurs more than once
    in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA


def main(max_birthdays: int = 100):
    print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
    
    The birthday paradox shows us that in a group of N people, the odds
    that two of them have matching birthdays is surprisingly large.
    This program does a Monte Carlo simulation (that is, repeated random
    simulations) to explore this concept.
    
    (It's not actually a paradox, it's just a surprising result.)
    ''')

    while True:
        print(f'How many birthdays shall I generate? (Max {max_birthdays})')
        try:
            num_b_days = int(input('> '))
        except ValueError as val_err:
            print(val_err)
            continue
        if 0 < int(num_b_days) <= max_birthdays:
            break
    print()

    print(f'Here are {num_b_days} birthdays:')
    birthdays = get_birthdays(num_b_days)
    for i, birthday in enumerate(birthdays):
        if i != 0:
            print(', ', end='')
        month_name = MONTHS[birthday.month - 1]
        date_text = f'{month_name} {birthday.day}'
        print(date_text, end='')
    print()
    print()

    match = get_match(birthdays)

    print('In this simulation, ', end='')
    if match != None:
        month_name = MONTHS[match.month - 1]
        date_text = f'{month_name} {match.day}'
        print(f'multiple people have a birthday on {date_text}')
    else:
        print('there are no matching birthdays.')
    print()

    print(f'Generating {num_b_days} random birthdays 100,000 times...')
    input('Press Enter to begin...')

    print('Let\'s run another 100,000 simulations.')
    sim_match = 0
    for i in range(100_000):
        if i % 10_000 == 0:
            print(i, 'simulations run...')
        birthdays = get_birthdays(num_b_days)
        if get_match(birthdays) != None:
            sim_match = sim_match + 1
    print('100,000 simulations run.')

    probability = round(sim_match / 100_000 * 100, 2)
    print(f"""
    Out of 100,000 simulations of {num_b_days} people, there was a matching birthday in that group {sim_match} times. 
    This means that {num_b_days} people have a {probability}% chance of having a matching birthday in their group.
    That\'s probably more than you would think!
    """)


if __name__ == '__main__':
    main(111)
