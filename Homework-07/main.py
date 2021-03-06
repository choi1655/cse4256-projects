"""File: main.py
Author: John Choi choi.1655@osu.edu
Version: March 7, 2022

The Ohio State University CSE4256 SP22 Homework 7.
"""
# Problem 1
def triangles(n):
    """Write a function called triangles(n) that, given a positive integer n, produces
    a list of the first n triangle numbers. You may assume that n is a positive integer.
    """
    numbers = []
    number = 0
    for i in range(1, n + 1):
        numbers.append(number + i)
        number += i
    return numbers

def ctriangles(n):
    """Write a function called ctriangles(n) that produces a list identical to triangles(n), but does so using a
    single-line list comprehension. Hint: the built-in function sum(s) is probably useful here.
    """
    # 1, 3, 6, 10, 15
    # 1, 2, 3, 4, 5
    return [sum([j for j in range(i + 1)]) for i in range(1, n + 1)]

def pascal(r):
    """Write a function called pascal(r) that, given a positive integer r, produces a list containing
    the first r rows of Pascal's Triangle (more precisely, the function should only generate
    all non-zero entries in the triangle). You may assume that r is a positive integer. You should not
    import any modules to complete this task, including the math module.
    Formula for kth element in nth row: (n!) / (k! * (n - k)!)
    """
    def pascal_val(row_num, element_num):
        def factorial(n: int) -> int:
            if n <= 1:
                return n
            return n * factorial(n - 1)

        num = factorial(row_num)
        denom1 = factorial(row_num - element_num)
        denom2 = factorial(element_num)
        denom = denom1 * denom2
        return num // denom if denom != 0 else 1

    return [[pascal_val(row, element) for element in range(row + 1)] for row in range(r)]

##### TEST CODE #####
def assertEqual(actual, expected):
    if actual == expected:
        print('PASS')
    else:
        print('FAIL')

# run the test cases
if __name__ == '__main__':
    # test_triangles
    input = 5
    expected = [1, 3, 6, 10, 15]
    assertEqual(triangles(input), expected)

    # test_triangles_0
    input = 0
    expected = []
    assertEqual(triangles(input), expected)

    # test_triangles_1
    input = 1
    expected = [1]
    assertEqual(ctriangles(input), expected)

    # test_ctriangles
    input = 5
    expected = [1, 3, 6, 10, 15]
    assertEqual(ctriangles(input), expected)

    # test_ctriangles_0
    input = 0
    expected = []
    assertEqual(ctriangles(input), expected)

    # test_ctriangles_1
    input = 1
    expected = [1]
    assertEqual(ctriangles(input), expected)

    # test_pascal_with_0
    input = 0
    expected = []
    assertEqual(pascal(input), expected)

    # test_pascal_with_1
    input = 1
    expected = [[1]]
    assertEqual(pascal(input), expected)

    # test_pascal_with_5
    input = 5
    expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assertEqual(pascal(input), expected)

    # test_pascal_with_10
    input = 10
    expected = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    ]
    assertEqual(pascal(input), expected)