"""
Math 560
Project 5
Spring 2024

Ruslan Basyrov

Date: April 29 2024
"""

# Import math, itertools, random, and time.
import math
import itertools
import random
import time

# Import the Priority Queue.
from p5priorityQueue import *

################################################################################

"""
Prim's Algorithm

Input: adjacency list and andjacency matrix of a graph

Output: none, but the behavior is updating the verteces so that they represent
	the minimum spanning tree. The algorithms adds each next closest non- visited
	vertex to a growing tree (which starts at arbitrary vertex).
"""
def prim(adjList, adjMat):
	# initialise the vertices' values to default
	for vertex in adjList:
		vertex.cost = math.inf
		vertex.prev = None
		vertex.visited = False

	# select a random vertex and make it a start
	start = adjList[random.randint(0, len(adjList) - 1)]
	start.cost = 0

	pq = PriorityQueue(adjList)
	# for each vertex ordered by cost in pq, add a neighbor to the tree
	# if it is not visited and the distance to it from the current vertex is
	# smaller than the cost of the neighbor
	while not pq.isEmpty():
		current = pq.deleteMin()
		current.visited = True
		for neighbor in current.neigh:
			if not neighbor.visited:
				if neighbor.cost > adjMat[current.rank][neighbor.rank]:
					neighbor.cost = adjMat[current.rank][neighbor.rank]
					neighbor.prev = current

################################################################################

"""
Kruskal's Algorithm

The algorithm finds a minimum spanning tree in a graph by connecting vertices by 
the next smallest edge if it does not create a cycle

Input: adjacency list and andjacency matrix of a graph

Output: set of the vertices representing the MST
"""
def kruskal(adjList, edgeList):
	forest = []

	# create a disjoint set for each vertex
	for vertex in adjList:
		makeset(vertex)

	# iterate over sorted edges and use them to combine sets if it does not lead
	# to cycles
	for edge in edgeList:
		u, v = edge.vertices[0], edge.vertices[1]
		if find(u) != find(v):
			forest.append(edge)
			union(u, v)
	return forest

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.
"""
def makeset(v):
	v.pi = v
	v.height = 0
	return (v)

"""
find: this function will return the root of the set that contains v.

Finds the root node recursively
"""
def find(v):
	if v != v.pi:
		v.pi = find(v.pi)
	return v.pi

"""
union: this function will union the sets of vertices v and u.
"""
def union(u,v):
	pu = find(u)
	pv = find(v)
	if pu == pv:
		return
	# connect a smaller set to the bigger set or arbitrarily if equal
	if pu.height > pv.height:
		pv.pi = pu
	else:
		pu.pi = pv
		if pu.height == pv.height:
			pv.height += 1

################################################################################

"""
TSP

The algorithm returns a tour (starts and ends at the same vertex) covering all
vertices in an MST.

Input: adjacency list of an MST and the start vertex.

Output: the tour covering all vertices.
"""
def tsp(adjList, start):
	tour  = []
	stack = [start]

	# set the vertices to unvisited (to reuse a graph)
	for vertex in adjList:
		vertex.visited = False

	# using DFS algorithm, traverse the tree and add the current vertix to
	# the tour and its neighbours (in the MST) to the stack to visit later as long
	# as there are not visited vertices (equivalent to the stack not being empty)
	while len(stack) > 0:
		current = stack.pop()
		if not current.visited:
			current.visited = True
			tour.append(current.rank)
			for neighbor in current.mstN:
				stack.append(neighbor)

	# complete the tour at the starting vertix
	tour.append(start.rank)
	return tour

# Import the tests (since we have now defined prim and kpuskal).
from p5tests import *

"""
Main function.
"""
if __name__ == "__main__":
	verb = False # Set to tpue for more printed info.
	print('Testing Prim\n')
	print(testMaps(prim, verb))
	print('\nTesting Kpuskal\n')
	print(testMaps(kruskal, verb))
