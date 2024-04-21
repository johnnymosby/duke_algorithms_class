"""
Math 560
Project 3
Spring 2024

Ruslan Basyrov
Date: April 20 2024
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
findCycle

Functionality:

Input:
The arguments are the adjacency list of edges and the adjacency matrix
of their weights. Optional argument of the floating point precision.

Output:
None if no cycle was found, and the vertix of the negative cycle which distance
could be change because of the cycle.
"""
def findCycle(adjList, adjMat, tol=1e-15):
	for tail in adjList:
		for head in tail.neigh:
			# return head if the edge can be changed because of a negative cycle
			if head.dist > tail.dist + adjMat[tail.rank][head.rank] + tol:
				head.prev = tail
				return head
	return None


"""
iterateOverEdges

Functionality:
The function relaxes (or not) each edge (with the direction from tail to head)
V - 1 times starting from the start node set up in adjList.

Input:
The arguments are the adjacency list of edges and the adjacency matrix
of their weights. Optional argument of the floating point precision.

Output:
No output.
"""
def iterateOverEdges(adjList, adjMat, tol=1e-15):
	for tail in adjList:
		for head in tail.neigh:
			# relax the edge to a shorter distance if possible
			if head.dist > tail.dist + adjMat[tail.rank][head.rank] + tol:
				head.dist = tail.dist + adjMat[tail.rank][head.rank]
				head.prev = tail


"""
detectArbitrage

Functionality:
The function finds a negative cycle in a graph using Bellman-Ford algorithm.

Input:
The arguments are the adjacency list of edges and the adjacency matrix of their weights.

Output:
Empty list if no negative cycle was found, and a list of vertices of a negative cycle otherwise.
"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
	# setting up the starting vertix
	start = 0
	adjList[start].dist = 0

	# iterating V - 1 relaxing the edges
	for _ in range(0, len(adjList) - 1):
		iterateOverEdges(adjList, adjMat)

	current = findCycle(adjList, adjMat)
	# if no negative cycle:
	if current is None:
		return []

	# finding the first vertix of the cycle
	visited = [False for _ in adjList]
	while visited[current.rank] is False:
		visited[current.rank] = True
		current = current.prev
	first = current

	cycle = [first.rank]
	current = first.prev
	# recording the vertices of the cycles
	while not current.isEqual(first):
		cycle.append(current.rank)
		current = current.prev
	cycle.append(current.rank)

	# reversing the order of the cycle
	#   so that the vertices follow the direction of the edges
	cycle.reverse()

	return cycle

################################################################################

"""
rates2mat

Functionality:
Changes rates to a representation which allows to use them in a graph. Namely,
by taking the negative logarithm of a rate, it is possible to find a negative
cycle (meaning arbitrage opportunity) in the graph of rates

Input:
The matrix of rates

Output:
The matrix of -log(rates)
"""
def rates2mat(rates):
    return [[-math.log(R) for R in row] for row in rates]

"""
Main function.
"""
if __name__ == "__main__":
    testRates()
