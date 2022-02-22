"""Test runner for HW6 Solution.

Author: Alan Weide
"""

import graph

vertices = {0, 1, 2, 3}
edges = {(0, 1), (0, 2), (1, 2), (2, 3)}

try:
    print("EdgelistGraph")
    edge_g = graph.EdgelistGraph([(0, 1), (0, 2), (2, 1), (2, 3)])
    print(f"{str(edge_g)  = }")
    print(f"{repr(edge_g) = }")
    print()
except NotImplementedError as e:
    print(f"Ignoring {repr(e)}")

try:
    print("MatrixGraph")
    matrix_g = graph.MatrixGraph([
                                    [False, True, True, False],
                                    [True, False, True, False],
                                    [True, True, False, True],
                                    [False, False, True, False]
                                ])
    print(f"{str(matrix_g)  = }")
    print(f"{repr(matrix_g) = }")
    print()
except NotImplementedError as e:
    print(f"Ignoring {repr(e)}")

try:
    print("DictGraph")
    dict_g = graph.DictGraph({0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]})
    print(f"{str(dict_g)  = }")
    print(f"{repr(dict_g) = }")
    print()
except NotImplementedError as e:
    print(f"Ignoring {repr(e)}")

# TODO: Add more test cases
