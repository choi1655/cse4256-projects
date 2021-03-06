"""Homework 4 in CSE 4256 at The Ohio State University.

Date: Feb 7, 2022
Author: John Choi choi.1655@osu.edu
Version: Feb 7, 2022

Due date: Feb 13, 2022
"""

# ----------------
#  Argument Types
# ----------------

def printargs0(x, y=0, /, *, z, w):
	print(f"{x = }")
	print(f"{y = }")
	print(f"{z = }")
	print(f"{w = }")

# call the function printargs0
printargs0(1, 2, z = 3, w = 4)


# change the signature of printargs1 to take four arguments, all with default values
def printargs1(x = None, y = None, z = None, k = None):
	# implement the body of printargs1 to print the name and value of each argument
	print(f'x is {x}, y is {y}, z is {z}, and k is {k}')

# call the function printargs1
printargs1()
printargs1(x = 1)
printargs1(x = 1, y = 2)
printargs1(k = 4)

# change the signature of printargs2 to take:
#   * one positional-only argument
#   * two positional-or-keyword arguments
#   * three keyword-only arguments
def printargs2(x, /, y, z, *, a, b, c):
	# implement the body of printargs2 to print the name and value of each argument
	print(f'x is {x}, y is {y}, z is {z}, a is {a}, b is {b}, and c is {c}')

# call the function printargs2
printargs2(1, 2, z = 3, a = 4, b = 5, c = 6)

# change the signature of printargs3 to take four positional-only arguments
def printargs3(a, b, c, d, /):
	# implement the body of printargs3 to print the name and value of each argument
	print(f'a is {a}, b is {b}, c is {c}, and d is {d}')

# call the function printargs3
printargs3(1, 2, 3, 4)

# change the signature of printargs4 to take a variadig argument list
def printargs4(*args):
	# implement the body of printargs4 to print the name and value of each argument
	for key, val in args:
		print(f'{key} is {val}')

# call the function printargs4
printargs4(('a', 1), ('b', 2), ('c', 3), ('d', 4))

# change the signature of printargs5 to take a keyword-variadic argument
def printargs5(**args):
	# implement the body of printargs5 to print the name and value of each argument
	for element in args:
		print(f'{element} is {args[element]}')

# call the function printargs0
printargs5(a = 1, b = 2, c = 3, d = 4)

# --------------
#  Dictionaries
# --------------

"""Returns a dictionary in which each item in `keys` maps to the corresponding item in `values`.

Uses a for-in loop.

Args:
  keys: the list of keys
  values: the list of values
"""
def build_dict1(keys: list, values: list) -> dict:
	d = {}
	for i in range(len(keys)):
		d[keys[i]] = values[i]
	return d

"""Returns a dictionary in which each item in `keys` maps to the corresponding item in `values`.

Uses a dictionary comprehension.

Args:
  keys: the list of keys
  values: the list of values
"""
def build_dict2(keys, values):
	d = {keys[x]:values[x] for x in range(len(keys))}
	return d

"""Returns a dictionary in which each item in `keys` maps to the corresponding item in `values`.

Uses the built-in `zip(seq1, seq2)` function.

Args:
  keys: the list of keys
  values: the list of values
"""
def build_dict3(keys, values):
	# implement this function
	d = dict(zip(keys, values))
	return d

"""Returns a dictionary which maps each letter to the number of times it appears in `s`.

Args:
  s: the string in which to search
"""
def letter_freq(s: str) -> dict:
	d = {}
	for ch in s:
		# check if it is a letter
		if not ch.isalpha():
			continue
		if ch.upper() in d:
			d[ch.upper()] += 1
		else:
			d[ch.upper()] = 1
	return ch

"""Returns the letter in `s` that appears most often.

Args:
  s: the string in which to search
"""
def popular_letter(s: str) -> str:
	d = letter_freq(s)
	max_letter = None
	max_freq = 0
	for letter, freq in d.items():
		if freq > max_freq:
			max_freq = freq
			max_letter = letter
	return max_letter

# ------------------------
#  Generators and Lambdas
# ------------------------

"""Generates the series identified by the Collatz Conjecture starting at `x`.

Args:
  x: the starting number
"""
def collatz(x):
	while x != 1:
		if x % 2 == 0:
			x //= 2
		else:
			x = x * 3 + 1
		yield x


"""Returns the length of the series generated by `collatz(x)`."""
def collatz_len(x):
	collatz_iterator = collatz(x)
	return len(collatz_iterator)

"""Generates the sequence of words in string `s`."""
def words(s):
	word_list = s.split(' ')
	for word in word_list:
		yield word

"""Returns a list created by applying the single-argument function `f` to each item in `lst`.

Args:
  lst: the list
  f: a single-argument function that is applicable to each item in lst
"""
def mapped_list(lst, f):
	return [f(x) for x in lst]

# Call `mapped_list` with a lambda expression such that the generated list consists of the 
#   length of the Collatz Conjecture seires generated starting at the corresponding number in `lst`.

mapped_list([1, 2, 3, 4, 5], f = lambda x: collatz_len(x))

# ----------------------
#  Challenge Activities
# ----------------------

# TODO Fiddle with the apparently-arbitrary values in the `mcg` function and see if the results can
#   be made significantly better or worse by changing them.

# """Simple pseudorandom number generator."""
# def mcg(s=543718):
#     x = s
#     a = 48271
#     c = 1
#     m = 2147483647
#     while True:
#         x = (a*x + c) % m
#         yield x

# """Simulates rolling a `sides`-sided die `samples` times, and prints the results.

# Args:
#   sides: number of sides on the die to simulate
#   samples: number of rolls to simulate
# """
# def diceroller(sides=6, samples=10000):
# 	die = (n % sides + 1 for n in mcg())
#     counts = dict()
#     for i in range(samples):
#         roll = next(die)
#         if roll not in counts:
#             counts[roll] = 0
#         counts[roll] += 1
            
#     # TODO Modify the output of this function so that it displays a "pretty" horizontal bar chart.
#     #   Hint: use the Unicode character FULL BLOCK (U+2588) (in Python: u"\u2588").
#     for value in range(1, sides + 1):
#         print(f"{value}: {counts[value]}")

