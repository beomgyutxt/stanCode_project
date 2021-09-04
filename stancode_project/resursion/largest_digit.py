"""
File: largest_digit.py
Name: Hsuan Tung, Lin
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	"""
	The program prints the biggest digit in a integer.
	:return:
	"""
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	The function modifies the integer(parameter) and finds the largest digit
	in the integer trough the help of helper function.
	:param n: int.
	:return: int, the largest digit.
	"""
	if n < 0:
		n *= (-1)  # Positive integer
	largest = 0    # storing largest digit
	return largest_digit_helper(n, largest)


def largest_digit_helper(n, l_n):
	"""
	The function returns the largest digit in the integer.
	:param n: int.
	:param l_n: int, the largest digit.
	"""
	if n < 10:
		if n > l_n:
			l_n = n
		return l_n
	else:
		k = n % 10     # get units digit
		if k > l_n:    # get largest digit
			l_n = k
		n //= 10       # divide by 10
		return largest_digit_helper(n, l_n)


if __name__ == '__main__':
	main()
