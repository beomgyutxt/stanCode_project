"""
File: hangman.py
Name: Hsuan Tung, Lin
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    The program plays hangman game.
    User has to guess letters one by one and find the word
    randomly decided by the program in limited chances.
    """
    ans = random_word()        # the answer
    result = dash(len(ans))    # show the length of the word
    turns = N_TURNS            # how many chances
    history = ''               # record the letters user guessed
    while True:
        if turns == 0 or ans == result:  # end the game
            break
        else:
            print('The word looks like '+result)
            print('You have '+str(turns)+' guess left')
            your_guess = input('Your guesses: ')
            your_guess = your_guess.upper()
            history += your_guess
            result = new_result(ans, result, your_guess)  # show the correct letters and their position
            turns = check_your_guess(ans, your_guess, turns, history)
            # calculates how many chances user left
    final(ans, result, turns)                             # show win or lose the game
    print('The word was '+ans)


def dash(n):
    """
    The function turns the answer into dashes and shows the length of the answer.
    :param n: int, the length of the answer.
    :return: str, a string consists of dashes.
    """
    dash = ''
    for i in range(n):
        dash += '-'
    return dash


def new_result(ans, result, your_guess):
    """
    The function shows the correct letters and their position after guess.
    :param ans: str, the answer
    :param result: str, the condition before guess
    :param your_guess: str, the letter user guesses
    :return: str, the result after guess
    """
    n = 0  # int, indexing the answer
    while True:
        cut_ans = ans[n:]
        n += cut_ans.find(your_guess)            # where is the correct letter (previous one)
        if cut_ans.find(your_guess) != -1:       # guess correctly
            if n != 0:                           # the correct letter is not at the beginning
                result = result[:n] + your_guess + result[n+1:]
            elif n == 0:                         # the correct letter is at the beginning
                result = your_guess + result[n + 1:]
            n += 1
            cut_ans = ans                        # reconstruct the answer
        else:
            return result                        # no more correct letters


def check_your_guess(ans, your_guess, turns, history):
    """
    The function checks whether the format of user's guess is correct
    and calculates how many left chances (depends on the format).
    :param ans: str, the answer
    :param your_guess: str, the letter user guesses
    :param turns: int, how many left chances before guess
    :param history: the collection of every letter user guesses
    :return: int, how many left chances after guess
    """
    if not your_guess.isalpha() or len(your_guess) > 1:  # not single alphabet
        print('illegal format.')
    elif your_guess in ans:
        print('You are correct!')  # correct
        if your_guess not in history:  # user guesses the same letter(correct) twice
            turns -= 1
    elif your_guess not in ans:  # wrong
        print('There is no ' + your_guess + "'s in the word.")
        turns -= 1
    return turns


def final(ans, result, turns):
    """
    At the end of game the function announces the result.
        1. win - user finds the answer.
        2. lose (be hung) - user runs out of chances.
    :param ans: str, the answer
    :param result: str, the result after final guess
    :param turns: int, how many left chances
    """
    if turns == 0:
        print('You are completely hung :(')
    elif ans == result:
        print('You win!!')





def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
