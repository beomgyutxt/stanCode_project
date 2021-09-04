"""
File: boggle.py
Name: Husan Tung, Lin
----------------------------------------
This program imitates a boggle game.
First, User inputs letters (4*4) to construct a boggle.
	Example:
		f y c l
		i o m g
		o r i l
		h j h u
Then, The program find all meaning words from dictionary in this boggle.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	There is a boggle.
	An user has to input 4 letters each row (total: 4 rows) to build a boggle
	and the program outputs meaning words(length >= 4) in the this game.
	"""
	start = time.time()
	####################
	letters = build_boggle()  # build a boggle
	if letters is None:       # Building a boggle fails --> end the program
		return
	scanning(letters)         # Building a boggle successes --> searching meaning words
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def scanning(ls):
	"""
	The function searching words in a boggle with the help of a helper function (scanning_help()).
	At the end, it prints the total number of words.
	:param ls: list, storing all letters of a boggle
	"""
	n = 0
	for x in range(len(ls)):                # x: which row
		for y in range(len(ls[x])):         # y: which letter
			first = ls[x][y]                # one of letter of the boggle
			lst = read_dictionary()[first]  # list contains all words started with the letter(first)
			n += scanning_help(lst, ls, first, [], [(x, y)])  # how many words are in the boggle
	print(f'There are {n} words in total.')


def scanning_help(lst, ls, current_s, words, used):
	"""
	The function calculates how many words started with the letter are in the boggle.
	It also prints the found words when searching.
	:param lst: list, contains all words started with the letter
	:param ls: list, storing all letters of a boggle
	:param current_s: string, current string
	:param words: list, containing words started with the letter are in the boggle
	:param used: list, recording which letter is used
	:return: int, how many words started with the letter are in the boggle
	"""
	x = used[len(used)-1][0]  # (x, y) the position of the last appended letter
	y = used[len(used)-1][1]
	if current_s in lst and current_s not in words:  # if the current string (not occur before) is in the dictionary
		words.append(current_s)
		print('Found: ' + current_s)
	for i in range(-1, 2):
		for j in range(-1, 2):
			if 0 <= (x+i) <= 3:
				if 0 <= (y+j) <= 3:
					b = ls[x+i][y+j]  # go to neighbor letters
					if (x+i, y+j) in used:
						pass
					else:             # the neighbor is not used
						used.append((x+i, y+j))
						# choose
						current_s += b
						# explore
						if has_prefix(current_s):
							scanning_help(lst, ls, current_s, words, used)
						# un-choose
						current_s = current_s[:-1]
						used.pop()
	return len(words)


def build_boggle():
	"""
	The functions builds a boggle is made up of 16 letters.
	User needs to inputs 4 letters each row and each letter is separated by a space (Example: 'a b c d').
	The function returns a list (boggle).
	:return:x_list, the list consist of 4 lists which contain letters in each row.
			If the format user inputted is wrong, the function return None.
	"""
	x_list = []  # store all letters in each row.
	for i in range(4):
		row = input(f'{i+1} row of letters: ')
		if len(row) == 7:                           # legal format 'a b c d'
			y_list = []                             # store letters in a row
			for j in range(len(row)):
				ch = row[j]
				if j % 2 == 0 and ch.isalpha():     # append a legal letter to a row
					y_list.append(ch)
				elif j % 2 == 1 and ch == ' ':      # pass when a space appears
					pass
				else:                               # illegal format: return None
					return
			x_list.append(y_list)                   # append a legal row to the boggle
		else:                                       # illegal format: return None
			return
	return x_list


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a dictionary.
	The key of the dictionary is each alphabet
	and the value is a list contained the words (length >= 4) which the first letters is key.
	"""
	dic = {}
	with open(FILE, 'r') as f:               # open file
		for line in f:
			if len(line) >= 6:               # len(word) + len('\n') >= 6
				if line[0] not in dic:       # build the dictionary {a:[...], b:[...], c:[...]...}
					lst = [line.strip()]     # remove '\n'
					dic[line[0]] = lst
				else:
					dic[line[0]].append(line.strip())
	return dic


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	dic = read_dictionary()
	lst = dic[sub_s[0]]  # the list contains all words started with the first letter of the substring
	n = 0                # number of words started with the substring
	for words in lst:
		if words.startswith(sub_s):
			n += 1
		if n > 0:
			return True  # There is/are word(s) started with the substring


if __name__ == '__main__':
	main()
