#!/usr/bin/env python
#################################################
""" graph.py
# # Graph data structure using Adjacency List(Edge List),
# #    undirected, unweighted by default.
#   Supports:
#     - Basic:
#         > add_edge, add_edges, remove_edge, add_vetex, remove_vertex, __str__.
#     - Inspection
#         > size, is_directed, is_weighted, vertices, contains,
#           adjecent, neighbors, get_edge_weight, find_path, BFS, DFS, topological_sort.
#     - Internal:
#         > set_edge_weight
"""
#################################################
# ###  Author: Samyuel Danyo
# ###  Date: 21/07/2020
# ###  Last Edit: 29/06/2020
##################################################
# Implementation
##################################################
from collections import defaultdict

class Graph:
    """Graph data structure using Adjacency List(Edge List), undirected, unweighted by default."""

    def __init__(self, edges=None, directed=False, weighted=False):
        self._directed = directed
        self._weighted = weighted
        if weighted:
            self._graph = defaultdict(dict)
        else:
            self._graph = defaultdict(set)
        if edges:
            self.add_edges(edges)

    def __str__(self):
        def pretty(my_dict, image, indent=0, ind_size='   '):
            for key, value in my_dict.items():
                if isinstance(value, dict):
                    image.extend([ind_size * indent, str(key), ':\n'])
                    pretty(value, image, indent+1)
                else:
                    image.extend([ind_size * (indent), str(key), ': ', str(value), '\n'])
        image = ['Graph {\n']
        pretty(self._graph, image, 1)
        image.append('}')
        return ''.join(image)

    def is_directed(self):
        """Check if the graph is directed."""
        return self._directed

    def is_weighted(self):
        """Check if the graph is weighted (edges have values)."""
        return self._weighted

    def vertices(self):
        """Get all vertices in the graph."""
        return list(self._graph)

    def contains(self, vertex):
        """Check if the graph contains vertex."""
        return vertex in self._graph

    def adjacent(self, vertex1, vertex2):
        """ Check if edge{vertex1 : vertex2} exists (if node1 is connected to node2)."""
        return self.contains(vertex1) and vertex2 in self._graph[vertex1]

    def neighbors(self, vertex):
        """List all vertices y such that there is an edge{vertex : y}."""
        if self.contains(vertex):
            return self._graph[vertex]

    def size(self):
        """Get the number of vertices in the graph."""
        num_vert = 0
        num_edg = 0
        for vertex in self.vertices():
            num_vert += 1
            num_edg += len(self.neighbors(vertex))
        return (num_vert, num_edg)

    def add_edge(self, vertex1, vertex2, weight=None):
        """Add an edge(connection) between vertex1(node1) and vertex2(node2)."""
        if self.is_weighted():
            self._graph[vertex1][vertex2] = weight
            if not self.is_directed():
                self._graph[vertex2][vertex1] = weight
            else:
                if not self.contains(vertex2):
                    self._graph[vertex2] = dict()
        else:
            self._graph[vertex1].add(vertex2)
            if not self.is_directed():
                self._graph[vertex2].add(vertex1)
            else:
                if not self.contains(vertex2):
                    self._graph[vertex2] = set()

    def add_edges(self, edges):
        """Add edges(connections) {list of tuple pairs} to the graph."""
        if self.is_weighted():
            for vertex1, vertex2, weight  in edges:
                self.add_edge(vertex1, vertex2, weight)
        else:
            for vertex1, vertex2  in edges:
                self.add_edge(vertex1, vertex2)

    def remove_edge(self, vertex1, vertex2):
        """Remove edge{vertex1 : vertex2}."""
        if not self.contains(vertex1):
            return False
        if self.contains(vertex2):
            if self.is_weighted():
                del self._graph[vertex1][vertex2]
                if not self._directed:
                    del self._graph[vertex2][vertex1]
            else:
                self._graph[vertex1].remove(vertex2)
                if not self._directed:
                    self._graph[vertex2].remove(vertex1)
            return True

    def add_vertex(self, vertex):
        """Add vertex to the graph."""
        if self.contains(vertex):
            return None
        if self.is_weighted():
            self._graph[vertex] = dict()
        else:
            self._graph[vertex] = set()
        return True

    def remove_vertex(self, vertex):
        """Remove vertex from the graph."""
        if not self.contains(vertex):
            return None
        if self.is_weighted():
            del self._graph[vertex]
            for edges in self._graph.values():
                if vertex in edges:
                    del edges[vertex]
        else:
            del self._graph[vertex]
            for edges in self._graph.values():
                if vertex in edges:
                    edges.remove(vertex)
        return True

    def set_edge_weight(self, vertex1, vertex2, weight):
        """Sets the weight associated with the edge(vertex1, vertex2) to weight."""
        if not self.is_weighted():
            print("WARNING: Graph is NOT weighted!")
            return None
        self._graph[vertex1][vertex2] = weight
        if self.is_directed():
            self._graph[vertex2][vertex1] = weight
        return True

    def get_edge_weight(self, vertex1, vertex2):
        """Returns the weight associated with the edge(vertex1, vertex2)."""
        if not self.is_weighted():
            print("WARNING: Graph is NOT weighted!")
            return None
        if self.adjacent(vertex1, vertex2):
            return self._graph[vertex1][vertex2]

    def find_path(self, start_vertex, end_vertex):
        """Find a path between start_vertex and end_vertex (may not be shortest)."""
        if not self.contains(start_vertex) or not self.contains(end_vertex):
            return None
        path = []
        visited = set()
        self._find_path(start_vertex, end_vertex, path, visited)
        if path[-1] != end_vertex:
            return []
        return path

    def _find_path(self, start, end, path, visited):
        """Utility fundtion to find a path between start and end (may not be shortest)."""
        path.append(start)
        visited.add(start)
        if start == end:
            return path
        for vertex in self.neighbors(start):
            if vertex not in visited:
                if not self._find_path(vertex, end, path, visited):
                    path.remove(vertex)
                else:
                    return True

    def BFS(self, start_vertex, verbose=True):
        """Perform Breadth First Search (traverse) on the graph."""
        if not self.contains(start_vertex):
            return None
        traversal = []
        visited = set()
        for vertex in self.vertices():
            if vertex not in visited:
                self._BFS(vertex, visited, traversal.append)
        if verbose:
            print('BFS(Graph) =', traversal)
        return traversal

    def _BFS(self, start_vertex, visited, callback):
        """Utility function to Breadth First Search (traverse) the graph."""
        queue = []
        queue.insert(0, start_vertex)
        visited.add(start_vertex)
        while queue:
            curr_vertex = queue.pop()
            callback(curr_vertex)
            for vertex in self.neighbors(curr_vertex):
                if vertex not in visited:
                    queue.insert(0, vertex)
                    visited.add(vertex)

    def DFS(self, start_vertex, verbose=True):
        """Perform Depth First Search (traverse) on the graph."""
        if start_vertex is None:
            return None
        traversal = []
        visited = set()
        for vertex in self.vertices():
            if vertex not in visited:
                self._DFS(vertex, visited, traversal.append)
        if verbose:
            print('DFS(Graph) =', traversal)
        return traversal

    def _DFS(self, curr_vertex, visited, callback):
        """Utility function to Depth First Search (traverse) the graph."""
        visited.add(curr_vertex)
        callback(curr_vertex)
        for vertex in self.neighbors(curr_vertex):
            if vertex not in visited:
                self._DFS(vertex, visited, callback)

    def topological_sort(self, verbose=True):
        """Get topological sort stack for the graph."""
        visited = set()
        stack = []
        rec_stack = set()
        for vertex in self.vertices():
            if vertex not in visited:
                if self._topological_sort(vertex, visited, stack, rec_stack):
                    print('ERROR: Graph is cyclic! Cannot perform Topological Sort.')
                    return None
        if verbose:
            print('TopologicalSort(Graph):', stack)
        return stack

    def _topological_sort(self, curr_vertex, visited, stack, rec_stack):
        """Utility function to perform topological sorting on the graph."""
        visited.add(curr_vertex)
        rec_stack.add(curr_vertex)
        for vertex in self.neighbors(curr_vertex):
            if vertex not in visited:
                if self._topological_sort(vertex, visited, stack, rec_stack):
                    return True
            elif vertex in rec_stack:
                return True
        stack.insert(0, curr_vertex)
        rec_stack.remove(curr_vertex)
