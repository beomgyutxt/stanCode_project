"""
File: anagram.py
Name: Hsuan Tung, Lin
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
DICTIONARY = []               # stores words from a dictionary


def main():
    """
    User can input interested word(s); then the program prints all the anagrams of the word(s).
    Once user inputs '-1', the program ends. At the meantime it prints the speed of its algorithm on the console.
    """
    start = time.time()
    ####################
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        word = input('Find anagrams for:')
        if word == EXIT:
            break
        else:
            read_dictionary()      # read a file
            find_anagrams(word)    # find anagrams
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    The function reads a dictionary file and stores word in a dictionary.
    :return:
    """
    with open('dictionary.txt', 'r') as f:
        for line in f:
            words = line.strip()  # remove '\n'
            DICTIONARY.append(words)

def find_anagrams(s):
    """
    The function finds anagrams of the interested word through a helper function.
    At the end of the function, it prints all anagrams and the amount.
    :param s: str, the interested word
    :return:
    """
    print('Searching')  # tell user that the program is on-going
    lst = []  # change the word into a list
    result = [0]  # store all anagrams(str) and its total amount(int)
    for ch in s:
        lst.append(ch)
    find_anagrams_helper(lst, [], result, [])  # the helper function
    print(f'{result[0]} anagrams: {result[1:]}')  # print all anagrams and its amount


def find_anagrams_helper(lst, current_lst, result, index):
    """
    The function finds anagrams of the interested word.
    :param lst: list, contain alphabets of the word.
    :param current_lst: list, rearranged alphabets.
    :param result: list, [0]: int, the amount of anagrams, [1:]: str, all anagrams.
    :param index: list, store indexes of each alphabets.
    """
    # base case
    if len(current_lst) == len(lst):
        string = ''.join(current_lst)     # restore the string
        if string not in result:          # avoid repeated answer
            if string in DICTIONARY:      # search in dictionary
                # print('Searching')
                result[0] += 1            # add to result
                result.append(string)
                print(f'Found: {string}')
                print('Searching')
    else:
        for i in range(len(lst)):
            ele = lst[i]
            if len(index) != 0 and i in index:  # the alphabet is used
                pass
            else:
                # choose
                current_lst.append(ele)         # the alphabet is not used
                index.append(i)                 # record the index of the alphabet
                sub_s = ''.join(current_lst)    # restore a sub-string of the word
                if has_prefix(sub_s):           # True: there are words starting with the sub-string in dictionary
                    # explore
                    find_anagrams_helper(lst, current_lst, result, index)
                # un-choose
                current_lst.pop()
                index.pop()


def has_prefix(sub_s):
    """
    The function checks if any words in the dictionary start with the sub-string.
    It can reduce the time of calculation.
    :param sub_s: string, rearranged sub-string of the interested word
    :return: bool, if any words in the dictionary start with the sub-string.
    """
    n = 0
    for words in DICTIONARY:
        if words.startswith(sub_s):
            n += 1
        if n > 0:
            return True





if __name__ == '__main__':
    main()
