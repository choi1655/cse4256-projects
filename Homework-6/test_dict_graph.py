import unittest
from graph import DictGraph

class DictGraphTest(unittest.TestCase):

    def setUp(self) -> None:
        graph_dict = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
        self.graph = DictGraph(graph_dict)
    
    def test_add_vertex(self):
        self.graph.add_vertex(4)
        string = str(self.graph)
        self.assertEqual(string, "({0, 1, 2, 3, 4}, {(0, 1), (1, 2), (2, 1), (2, 0), (2, 3), (0, 2), (1, 0), (3, 2)})")