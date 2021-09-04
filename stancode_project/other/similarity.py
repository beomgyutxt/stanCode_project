"""
File: similarity.py
Name: Hsuan Tung, Lin
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    User should input a long DNA sequences (s1) and a short DNA sequence (2).
    The program finds the sequence which shares the highest similarity
    between s2 and s1.
    """
    long_sequence = input('Please give me a DNA sequence to search: ')
    long_sequence = long_sequence.upper()  # convert to capital letter
    short_sequence = input('What DNA sequence would you like to match? ')
    short_sequence = short_sequence.upper()
    print('The best match is: '+search(long_sequence, short_sequence))


def search(str1, str2):
    """
    The function finds the sequence has highest similarity.
    :param str1: the long DNA sequence.
    :param str2: the short DNA sequence.
    :return: the sequence has highest similarity.
    """
    highest_similarity_seq = 'No match'     # similarity = 0
    highest_correct = 0
    for i in range(len(str1)-len(str2)+1):  # total runs
        correct = 0                         # how many nucleotides match
        for j in range(len(str2)):          # loop over the sequence
            if str1[i+j] == str2[j]:
                correct += 1
        if correct > highest_correct:       # keep higher number and the sequence
            highest_correct = correct
            highest_similarity_seq = str1[i:i+len(str2)]

    return highest_similarity_seq







###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
