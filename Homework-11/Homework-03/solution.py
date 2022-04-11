"""Homework 3

HW3 in CSE 4256 at The Ohio State University.

Author: John Choi choi.1655@osu.edu
Version: January 31, 2022
"""

# Problem 1.
# Besides the syntax used to create them, what are three fundamental differences
# between a Python \lstinline{set} and a Python \lstinline{list}?
# 1. The order of elements does not matter in Python's set, while it matters in Python's list.
# 2. Python's list requires O(n) time complexity for lookup operations, while Python's set takes O(1).
# 3. Python's list allows duplicate elements while Python's set does not.

def all_unique(ls: list) -> bool:
  """Problem 2.
  Reports whether the list contains all unique elements.

  Positional Arguments:
  ls -- A list of hashable items, such as ints.
  """

  elements = set()
  for element in ls:
    if element in elements:
      return False
    elements.add(element)
  return True


def maybe_apply_all(s: set, f=lambda x: x + 5):
  """Applies function f to each element of s, updating s in place."""

  for x in s:
    x = f(x)

# Problem 3
# Is this function correct according to the docstring? If not, what's wrong?
# Answer: No. It applies the lambda function to each element in s, but it does not actually update the elements in s.


def apply_all(s: set, f=lambda x: x + 5):
  """
  Problem 4.
  Applies function f to each element of s, updating s in place."""

  s_copy = [x for x in s]
  s.clear()
  
  for x in s_copy:
    s.add(f(x))

# Does your solution to apply_all(s, f) work for all f?
# Answer: The solution to apply_all(s, f) will only work if f is a lambda (anonymous) function.


def subset_sum(s: set, t: int) -> bool:
  """Problem 5.
  Solves the Subset Sum problem.
  
  Returns True iff there is a subset of s whose sum is equal to t.

  Positional arguments:
  s -- A set of integers.
  t -- The target sum.  
  """

  """
                                                    1, 3, 5, 7, 9
  3, 5, 7, 9                            1, 3, 7, 9                 1, 3, 5, 9               1, 5, 7, 9

  5, 7, 9   3, 7, 9    3, 5, 9    3, 5, 7  |  3, 7, 9    1, 7, 9   1, 3, 9   1, 3, 7 | 3, 5, 9   1, 5, 9   1, 3, 9   1, 3, 5

  """
  # 1, 3, 5, 7, 9
  # target = 10
  ls = list(s)
  queue = []
  queue.append(ls)

  while len(queue) != 0:
    current_list = queue.pop()
    if sum(current_list) == t:
      return True
    
    # if not target, make all possible lists
    for i in range(len(current_list)):
      child_list = current_list[0:i] + current_list[i + 1:len(current_list)]
      if len(child_list) == 0:  # we don't want empty list
        continue
      queue.append(child_list) 
    
  return False


def is_subset_sum(sub: set, s: set, t: int) -> bool:
  """Problem 6.
  Checks a proposed solution to the Subset Sum Problem.

  Returns True iff sub is a subset of s and the sum of the elements of s is
  equal to t.

  Positional arguments:
  sub -- A set of integers; the proposed subset.
  s -- A set of integers.
  t -- The target sum.
  """

  return sub.issubset(s) and subset_sum(s, t)


# **********************
#  Challenge Activities
# **********************


def subset_sum_approx(s: set, t: int) -> bool:
  """Approximates the Subset Sum problem.
  
  Returns True iff there is a subset of s whose sum is approximately t.

  Positional arguments:
  s -- A set of integers.
  t -- The target sum.  
  """

  # TODO
  pass


def subset_sum_dyn(s: set, t: int) -> bool:
  """Solves the Subset Sum problem using dynamic programming.
  
  Returns True iff there is a subset of s whose sum is approximately t.
  Implemented using Dynamic Programming.

  Positional arguments:
  s -- A set of integers.
  t -- The target sum.  
  """

  # TODO
  pass


def subset_sum_h_s(s: set, t: int) -> bool:
  """Solves the Subset Sum problem using the Horowitz-Sahni algorithm.
  
  Returns True iff there is a subset of s whose sum is approximately t.
  Implemented using the Horowitz-Sahni algoritm. 

  Positional arguments:
  s -- A set of integers.
  t -- The target sum.  
  """

  #TODO
  pass
