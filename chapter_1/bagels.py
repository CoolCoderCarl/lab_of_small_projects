import random

NUM_DIGITS = 3
MAX_GUESSES = 15


def main():
    print(f'''Bagels, a deductive logic game.

I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.''')

    while True:
        secret_word = get_secret_word()
        print('I have thought up a number.')
        print(f' You have {MAX_GUESSES} guesses to get it.')

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS:
                guess = input(f'Guess #{num_guesses}: > ')

            clues = get_clues(guess, secret_word)
            print(clues)
            num_guesses += 1

            if guess == secret_word:
                break
            if num_guesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print(f'The answer was {secret_word}.')

        if input('Do you want to play again? (yes or no) > ').lower().startswith('n'):
            break
    print('Thanks for playing!')


def get_secret_word() -> str:
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789qwe')
    random.shuffle(numbers)

    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_word) -> str:
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secret_word:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            clues.append('Fermi')
        elif guess[i] in secret_word:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    main()
