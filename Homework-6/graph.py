"""Graph section of HW 6.

CSE 4256
Author: John Choi
Due: Feb 27, 2022
Version: Feb 27, 2022
"""
from abc import ABC, abstractmethod
from multiprocessing.sharedctypes import Value

class Graph(ABC):
    """Abstract class representing a graph.

    A graph is modeled as a pair of sets (vertices, edges).

    Each element of edges is a tuple (v1, v2) where v1 and v2 are both in vertices.
    """

    @abstractmethod
    def __repr__(self):
        """Returns a string representation of self using the underlying representation."""

        return f"{type(self)}:{str(self)}"

    @property
    @abstractmethod
    def vertices(self) -> set:
        """A set of all vertices in self."""

    @property
    @abstractmethod
    def edges(self):
        """A set of all edges in self.

        Each edge is a collection of two vertices.
        """

    @abstractmethod
    def degree(self, vertex) -> int:
        """Returns the degree of vertex.

        Returns the number of edges incident on vertex.
        """

    @abstractmethod
    def adjacent_to(self, vertex):
        """Returns a set of all vertices in self adjacent to vertex."""

    @abstractmethod
    def add_vertex(self, vertex):
        """Adds vertex to self.vertices."""

    @abstractmethod
    def add_edge(self, edge):
        """Adds edge to self.edges.

        Assumes: edge[0] and edge[1] are both in self.vertices.
        """

    @abstractmethod
    def remove_vertex(self, vertex):
        """Removes vertex and all incident edges from self.

        Assumes: vertex in self.vertices.
        """

    @abstractmethod
    def remove_edge(self, edge):
        """Removes edge from self, leaving the endpoints in self.vertices.

        Assumes: edge in self.edges.
        """

    # Non-abstract methods

    def __eq__(self, other):
        """Returns true iff self.vertices is exactly the same as other.vertices and self.edges is
            exactly the same as other.edges."""

        return self.vertices == other.vertices and self.edges == other.edges

    def __str__(self):
        """Returns a string representation of self as a pair of sets."""

        vertex_set = set(self.vertices)
        edge_set = {tuple(edge) for edge in self.edges}
        return f"({vertex_set}, {edge_set})"

    def __imul__(self, vertex):
        """Adds vertex to self.

        Called by the *= operator.
        """

        self.add_vertex(vertex)

    def __iadd__(self, edge):
        """Adds edge to self.

        Called by the += operator.
        """

        self.add_edge(*edge)

    def __itruediv__(self, vertex):
        """Removes vertex and all incident edges from self.

        Called by the /= operator.
        """

        self.remove_vertex(vertex)

    def __isub__(self, edge):
        """Removes edge from self, leaving the endpoints in self.

        Called by the -= operator.
        """

        self.remove_edge(edge)

    def __iter__(self):
        """Returns an iterator over the vertices of self.

        The implementation provided here does not guarantee any order to the
            vertices seen while iterating.
        """

        # TODO (challenge): Modify __iter__ so that it performs either a depth-
        #     first or breadth-first search of self.vertices.
        # Hint: use one of the generator functions below to do this.
        return iter(self.vertices)

    def depth_first_search(self, start=None):
        """Generator function to perform breadth-first search on self.vertices.

        If start is not specified, then no particular vertex is guaranteed to
            be the first one selected, and all subsequent calls to __next__
            will return one of the vertices adjacent to the previous one, in an
            order consistent with the classical BFS algorithm.

        Note: if self is an unconnected graph, breadth_first_search WILL NOT
            visit all vertices!
        """

        # TODO (challenge): Implement this generator function
        # Hint: make calls to the abstract methods above, making no assumptions
        #     about the representation of self.
        # Hint: the yield from statement helps yield values propagate up the
        #     call stack, allowing for recursive generator functions.
        raise NotImplementedError

    def breadth_first_search(self, start=None):
        """Generator function to perform breadth-first search on self.vertices.

        If start is not specified, then no particular vertex is guaranteed to
            be the first one selected, and all subsequent calls to __next__
            will return one of the vertices adjacent to the previous one, in an
            order consistent with the classical BFS algorithm.

        Note: if self is an unconnected graph, breadth_first_search WILL NOT
            visit all vertices!
        """

        # TODO (challenge): Implement this generator function
        # Hint: make calls to the abstract methods above, making no assumptions
        #     about the representation of self.
        raise NotImplementedError

class EdgelistGraph(Graph):
    """An edge list representation of a Graph.

    A ListGraph has one private instance variable, _edgelist.
    """

    def __init__(self, edgelist=None):
        """Returns an EdgelistGraph generated from edgelist."""

        self._edgelist = edgelist or []

    def __repr__(self):
        return repr(self._edgelist)

    @property
    def vertices(self) -> set:
        vertices = set()
        for (vertex1, vertex2) in self._edgelist:
            vertices.add(vertex1)
            vertices.add(vertex2)
        return vertices

    @property
    def edges(self) -> set:
        return set(self._edgelist)

    def degree(self, vertex) -> int:
        degree = 0
        for (vertex1, vertex2) in self._edgelist:
            if (vertex1 == vertex or vertex2 == vertex) and vertex1 != vertex2:
                degree += 1
        return degree

    def adjacent_to(self, vertex) -> set:
        vertices = set()
        for (vertex1, vertex2) in self._edgelist:
            if vertex1 == vertex or vertex2 == vertex:
                vertex_to_add = vertex1 if vertex == vertex2 else vertex2
                vertices.add(vertex_to_add)
        return vertices

    def add_vertex(self, vertex):
        self._edgelist.append((vertex, ))

    def add_edge(self, edge):
        self._edgelist.append(edge)

    def remove_vertex(self, vertex):
        for i in range(len(self._edgelist)):
            v1 = self._edgelist[i][0]
            v2 = self._edgelist[i][1]
            if v1 == vertex or v2 == vertex:
                # remove the current tuple
                self._edgelist.pop(i)
                i -= 1  # because the elements will try to fill the gap


    def remove_edge(self, edge):
        # [(0, 1), (0, 2), (2, 1), (2, 3)]
        for i in range(len(self._edgelist)):
            v1 = self._edgelist[i][0]
            v2 = self._edgelist[i][1]
            v_set = set([v1, v2])
            s = set(edge)
            if v_set == s:
                self._edgelist.pop(i)
                i -= 1  # because the elements will try to fill the gap

class MatrixGraph(Graph):
    """An adjacency-matrix representation of a Graph.

    A MatrixGraph has one private instance variable, _matrix.
    """

    # TODO (challenge): accept and keep track of arbitrary vertex indices.

    def __init__(self, matrix=None):
        """Produces a MatrixGraph generated from matrix."""

        self._matrix = matrix or []

    def __repr__(self):
        return repr(self._matrix)

    @property
    def vertices(self) -> set:
        vertices = set()
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix[i])):
                if self._matrix[i][j]:
                    vertices.add(i)
                    vertices.add(j)
        return vertices

    @property
    def edges(self) -> set:
        edges = set()
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix[i])):
                if self._matrix[i][j]:
                    edges.add((i, j))
        return edges

    def degree(self, vertex) -> int:
        # need to check vertical and horizontal

        # keep a set of pairs to avoid duplicate
        pairs = set()

        # check horizontal
        degree = 0
        for i in range(len(self._matrix[vertex])):
            if self._matrix[vertex][i]:
                degree += 1
                pairs.add((vertex, i))
        # check vertical
        for i in range(len(self._matrix)):
            if self._matrix[i][vertex] and (i, vertex) not in pairs:
                degree += 1
        return degree

    def adjacent_to(self, vertex) -> set:
        # need to check vertical and horizontal
        vertices = set()
        # check horizontal
        for i in range(len(self._matrix[vertex])):
            if self._matrix[vertex][i]:
                vertices.add(i)
        # check vertical
        for i in range(len(self._matrix)):
            if self._matrix[i][vertex]:
                vertices.add(i)
        return vertices

    def add_vertex(self, vertex):
        # check if vertex is out of bounds
        if vertex >= len(self._matrix) or vertex >= len(self._matrix[0]):
            raise ValueError(f'Vertex {vertex} is not valid (out of bounds)')
        self._matrix[vertex][vertex] = True

    def add_edge(self, edge):
        v1 = edge[0]
        v2 = edge[1]
        # check for out of bounds
        if v1 >= len(self._matrix) or v1 >= len(self._matrix[0]) or v2 >= len(self._matrix) or v2 >= len(self._matrix[0]):
            raise ValueError(f'Edge {edge} is not valid (out of bounds)')
        self._matrix[v1][v2] = True
        self._matrix[v2][v1] = True

    def remove_vertex(self, vertex):
        # check if vertex is out of bounds
        if vertex >= len(self._matrix) or vertex >= len(self._matrix[0]):
            raise ValueError(f'Vertex {vertex} is not valid (out of bounds)')
        # need to scan horizontally and vertically
        # scan horizontally
        for i in range(len(self._matrix[vertex])):
            self._matrix[vertex][i] = False
        # scan vertically
        for i in range(len(self._matrix)):
            self._matrix[i][vertex] = False

    def remove_edge(self, edge):
        v1 = edge[0]
        v2 = edge[1]
        # check for out of bounds
        if v1 >= len(self._matrix) or v1 >= len(self._matrix[0]) or v2 >= len(self._matrix) or v2 >= len(self._matrix[0]):
            raise ValueError(f'Edge {edge} is not valid (out of bounds)')
        self._matrix[v1][v2] = False
        self._matrix[v2][v1] = False

class DictGraph(Graph):
    """An adjacency-list representation of a Graph.

    A DictGraph has one private instance variable, _dict.
    """

    def __init__(self, dictionary=None):
        """Produces a DictGraph generated from dictionary."""

        self._dict = dictionary or {}

    def __repr__(self):
        return repr(self._dict)

    @property
    def vertices(self) -> set:
        return set(self._dict.keys())

    @property
    def edges(self) -> set:
        #{0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
        edges = set()
        for vertex1, edge in self._dict.items():
            for vertex2 in edge:
                pair = (vertex1, vertex2)
                if pair not in edges:
                    edges.add(pair)
        return edges

    def degree(self, vertex) -> int:
        if vertex not in self._dict:
            raise ValueError(f'Vertex {vertex} does not exist.')
        return len(self._dict[vertex])

    def adjacent_to(self, vertex) -> set:
        if vertex not in self._dict:
            raise ValueError(f'Vertex {vertex} does not exist.')
        return self._dict[vertex]

    def add_vertex(self, vertex):
        if vertex not in self._dict:
            self._dict[vertex] = []
        # do nothing if vertex already exists

    def add_edge(self, edge: tuple):
        if len(edge) != 2:
            raise ValueError(f'Edge {edge} is not valid.')
        vertex1 = edge[0]
        vertex2 = edge[1]
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        
        self._dict[vertex2].add(vertex1)
        self._dict[vertex1].add(vertex2)

    def remove_vertex(self, vertex):
        if vertex not in self._dict:
            raise ValueError(f'Vertex {vertex} is not valid.')
        self._dict.pop(vertex)

        for key, edge in self._dict.items():
            if vertex in edge:
                self._dict[key].remove(vertex)

    def remove_edge(self, edge: tuple):  # edge: (1, 2)
        if len(edge) != 2 or edge[0] not in self._dict or edge[1] not in self._dict:
            raise ValueError(f'Edge {edge} is not valid.')
        vertex1 = edge[0]
        vertex2 = edge[1]
        
        try:
            self._dict[vertex1].remove(vertex2)
            self._dict[vertex2].remove(vertex1)
            if len(self._dict[vertex1]) == 0:
                self._dict.pop(vertex1)
            if len(self._dict[vertex2]) == 0:
                self._dict.pop(vertex2)
        except KeyError:
            raise ValueError(f'Edge {edge} is not valid.')
