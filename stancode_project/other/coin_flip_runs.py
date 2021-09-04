"""
File: coin_flip_runs.py
Name: Husan-Tung, Lin
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the runs!
"""

import random as r


def main():
	"""
	The program flips a coin repeatedly until the total number of consecutive result of coin flips (runs)
	reaches users' request and shows the flipping process at the end.
	"""
	print("Let's flip a coin!")
	num_run = int(input('Number of runs: '))
	run = 0                      # the number of consecutive result
	coin1 = r.randint(0, 1)      # the previous result (1 = Head, 0 = Tail)
	record = str(coin1)          # record process
	in_a_row = False             # non-consecutive
	while True:
		coin2 = r.randint(0, 1)  # the next result
		record += str(coin2)
		if coin1 == coin2:       # previous = next
			if not in_a_row:     # consecutive result occurs
				run += 1
				in_a_row = True
			if run == num_run:   # runs reach users' request
				break
		else:
			in_a_row = False     # non-consecutive
		coin1 = coin2
	coin = ''
	for ht in record:            # show the flipping process
		if ht == '1':
			coin += 'H'
		else:
			coin += 'T'
	print(coin)



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
