#!/usr/bin/env python
#################################################
""" test_binary_search_tree.py
# # Test for Graph Adjacency List(Edge List) Implementation
#   Tests Un/Directed x Un/Weighted:
#      - Creating a graph, print(GRAPH)
#      - Add_edge, add_edges
#      - Size, is_weighted, is_directed, vertices, contains, adjacent, neighbors.
#      - Remove_edge, remove_vertex, add_vertex, set_edge_weight, get_edge_weight
#      - Traverse:
#          > DFS, BFS
#      - Find_path, topological_sort
"""
#################################################
# ###  Author: Samyuel Danyo
# ###  Date: 30/07/2020
# ###  Last Edit: 30/07/2020
##################################################
# ## imports
# Local Application/Library Specific Imports.
import graph as grph
##################################################
# Test
##################################################
EDGES = [('A', 'B'), ('B', 'C'), ('B', 'D'),
         ('C', 'D'), ('E', 'F'), ('F', 'C')]
print("==== TEST UNDIRECTED UNWEIGHTED GRAPH IMPLEMENTATION ====")
GRAPH = grph.Graph(EDGES, directed=False, weighted=False)
print(GRAPH)
print("Weighted={}, Directed={}".format(GRAPH.is_weighted(), GRAPH.is_directed()))
print(GRAPH.size(), "Vertices:", GRAPH.vertices())
print("Contains(A)={}, Contaians(V)={}".format(GRAPH.contains('A'), GRAPH.contains('V')))
print("Remove edge(B, C)")
GRAPH.remove_edge('B', 'C')
print(GRAPH)
print("Remove vertex B")
GRAPH.remove_vertex('B')
print(GRAPH)
print("Add vertex B")
GRAPH.add_vertex('B')
print(GRAPH)
print("F.adjacent(E)={}, A.adjacent(B)={}, A.adjacent(V)={}".format(GRAPH.adjacent('F', 'E'),
                                                                    GRAPH.adjacent('A', 'B'),
                                                                    GRAPH.adjacent('A', 'V')))
print("C.neightbors()={}, B.neighbors()={}".format(GRAPH.neighbors('C'), GRAPH.neighbors('B')))
print("Edge(C, D) weight Set={}, Get={}".format(GRAPH.set_edge_weight('C', 'D', 4),
                                                GRAPH.get_edge_weight('C', 'D')))
print("Reset Graph.")
GRAPH.add_edges(EDGES)
GRAPH.add_edge('W', 'P')
print(GRAPH)
GRAPH.BFS('A')
GRAPH.DFS('A')
print("Path(A, E) =", GRAPH.find_path('A', 'E'))
print("Path(A, G) =", GRAPH.find_path('A', 'G'))
print("Path(A, W) =", GRAPH.find_path('A', 'W'))
GRAPH.topological_sort()

print("\n==== TEST DIRECTED UNWEIGHTED GRAPH IMPLEMENTATION ====")
GRAPH = grph.Graph(EDGES, directed=True, weighted=False)
print(GRAPH)
print("Weighted={}, Directed={}".format(GRAPH.is_weighted(), GRAPH.is_directed()))
print(GRAPH.size(), "Vertices:", GRAPH.vertices())
print("Contains(A)={}, Contaians(V)={}".format(GRAPH.contains('A'), GRAPH.contains('V')))
print("Remove edge(B, C)")
GRAPH.remove_edge('B', 'C')
print(GRAPH)
print("Remove vertex B")
GRAPH.remove_vertex('B')
print(GRAPH)
print("Add vertex B")
GRAPH.add_vertex('B')
print(GRAPH)
print("F.adjacent(C)={}, A.adjacent(B)={}, A.adjacent(V)={}".format(GRAPH.adjacent('F', 'E'),
                                                                    GRAPH.adjacent('A', 'B'),
                                                                    GRAPH.adjacent('A', 'V')))
print("C.neightbors()={}, B.neighbors()={}".format(GRAPH.neighbors('C'), GRAPH.neighbors('B')))
print("Edge(C, D) weight Set={}, Get={}".format(GRAPH.set_edge_weight('C', 'D', 4),
                                                GRAPH.get_edge_weight('C', 'D')))
print("Reset Graph.")
GRAPH.add_edges(EDGES)
GRAPH.add_edge('W', 'P')
print(GRAPH)
GRAPH.BFS('A')
GRAPH.DFS('A')
print("Path(E, D) =", GRAPH.find_path('E', 'D'))
print("Path(A, G) =", GRAPH.find_path('A', 'G'))
print("Path(A, F) =", GRAPH.find_path('A', 'F'))
GRAPH.topological_sort()

EDGES = [('A', 'B', 3), ('B', 'C', 4), ('B', 'D', 2),
         ('C', 'D', 6), ('E', 'F', 2), ('F', 'C', 1)]
print("\n==== TEST UNDIRECTED WEIGHTED GRAPH IMPLEMENTATION ====")
GRAPH = grph.Graph(EDGES, directed=False, weighted=True)
print(GRAPH)
print("Weighted={}, Directed={}".format(GRAPH.is_weighted(), GRAPH.is_directed()))
print(GRAPH.size(), "Vertices:", GRAPH.vertices())
print("Contains(A)={}, Contaians(V)={}".format(GRAPH.contains('A'), GRAPH.contains('V')))
print("Remove edge(B, C)")
GRAPH.remove_edge('B', 'C')
print(GRAPH)
print("Remove vertex B")
GRAPH.remove_vertex('B')
print(GRAPH)
print("Add vertex B")
GRAPH.add_vertex('B')
print(GRAPH)
print("F.adjacent(E)={}, A.adjacent(B)={}, A.adjacent(V)={}".format(GRAPH.adjacent('F', 'E'),
                                                                    GRAPH.adjacent('A', 'B'),
                                                                    GRAPH.adjacent('A', 'V')))
print("C.neightbors()={}, B.neighbors()={}".format(GRAPH.neighbors('C'), GRAPH.neighbors('B')))
print("Edge(C, D) weight Set={}, Get={}".format(GRAPH.set_edge_weight('C', 'D', 4),
                                                GRAPH.get_edge_weight('C', 'D')))
print("Edge(C, E) weight Set={}, Get={}".format(GRAPH.set_edge_weight('C', 'E', 8),
                                                GRAPH.get_edge_weight('C', 'E')))
print("Reset Graph.")
GRAPH.add_edges(EDGES)
GRAPH.add_edge('W', 'P', 7)
print(GRAPH)
GRAPH.BFS('A')
GRAPH.DFS('A')
print("Path(A, E) =", GRAPH.find_path('A', 'E'))
print("Path(A, G) =", GRAPH.find_path('A', 'G'))
print("Path(A, W) =", GRAPH.find_path('A', 'W'))
GRAPH.topological_sort()

print("\n==== TEST DIRECTED WEIGHTED GRAPH IMPLEMENTATION ====")
GRAPH = grph.Graph(EDGES, directed=True, weighted=True)
print(GRAPH)
print("Weighted={}, Directed={}".format(GRAPH.is_weighted(), GRAPH.is_directed()))
print(GRAPH.size(), "Vertices:", GRAPH.vertices())
print("Contains(A)={}, Contaians(V)={}".format(GRAPH.contains('A'), GRAPH.contains('V')))
print("Remove edge(B, C)")
GRAPH.remove_edge('B', 'C')
print(GRAPH)
print("Remove vertex B")
GRAPH.remove_vertex('B')
print(GRAPH)
print("Add vertex B")
GRAPH.add_vertex('B')
print(GRAPH)
print("F.adjacent(C)={}, A.adjacent(B)={}, A.adjacent(V)={}".format(GRAPH.adjacent('F', 'E'),
                                                                    GRAPH.adjacent('A', 'B'),
                                                                    GRAPH.adjacent('A', 'V')))
print("C.neightbors()={}, B.neighbors()={}".format(GRAPH.neighbors('C'), GRAPH.neighbors('B')))
print("Edge(C, D) weight Set={}, Get={}".format(GRAPH.set_edge_weight('C', 'D', 4),
                                                GRAPH.get_edge_weight('C', 'D')))
print("Edge(C, E) weight Set={}, Get={}".format(GRAPH.set_edge_weight('C', 'E', 8),
                                                GRAPH.get_edge_weight('C', 'E')))
print("Reset Graph.")
GRAPH.add_edges(EDGES)
GRAPH.add_edge('W', 'P', 7)
print(GRAPH)
GRAPH.BFS('A')
GRAPH.DFS('A')
print("Path(E, D) =", GRAPH.find_path('E', 'D'))
print("Path(A, G) =", GRAPH.find_path('A', 'G'))
print("Path(A, F) =", GRAPH.find_path('A', 'F'))
GRAPH.topological_sort()
