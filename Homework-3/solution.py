"""Homework 3 Template

HW3 in CSE 4256 at The Ohio State University.

Author: John Choi choi.1655@osu.edu
Version: January 31, 2022
"""

# TODO
# Besides the syntax used to create them, what are three fundamental differences
# between a Python \lstinline{set} and a Python \lstinline{list}?
# 1. The order of elements does not matter in Python's set, while it matters in Python's list.
# 2. Python's list requires O(n) time complexity for lookup operations, while Python's set takes O(1).
# 3. Python's list allows duplicate elements while Python's set does not.

def all_unique(ls: list) -> bool:
  """Reports whether the list contains all unique elements.

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

# TODO
# Is this function correct according to the docstring? If not, what's wrong?
# Answer:


def apply_all(s: set, f=lambda x: x + 5):
  """Applies function f to each element of s, updating s in place."""

  # TODO
  pass

# TODO
# Does your solution to apply_all(s, f) work for all f?
# Answer:


def subset_sum(s: set, t: int) -> bool:
  """Solves the Subset Sum problem.
  
  Returns True iff there is a subset of s whose sum is equal to t.

  Positional arguments:
  s -- A set of integers.
  t -- The target sum.  
  """

  # TODO
  pass


def is_subset_sum(sub: set, s: set, t: int) -> bool:
  """Checks a proposed solution to the Subset Sum Problem.

  Returns True iff sub is a subset of s and the sum of the elements of s is
  equal to t.

  Positional arguments:
  sub -- A set of integers; the proposed subset.
  s -- A set of integers.
  t -- The target sum.
  """

  # TODO
  pass


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
