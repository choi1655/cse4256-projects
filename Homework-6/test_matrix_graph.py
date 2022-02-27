import unittest
from graph import MatrixGraph

class TestMatrixGraph(unittest.TestCase):

    def setUp(self) -> None:
        matrix = [
            [False, True, True, False],
            [True, False, True, False],
            [True, True, False, True],
            [False, False, True, False]
        ]
        self.graph = MatrixGraph(matrix)
    
    def test_add_vertex(self):
        self.graph.add_vertex(4)
        self.assertEqual(str(self.graph), "({0, 1, 2, 3, 4}, {(0, 1), (1, 2), (2, 1), (2, 0), (2, 3), (0, 2), (1, 0), (3, 2)})")
