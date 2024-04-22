"""
Math 560
Project 2
Spring 2024

project2.py

Ruslan Basyrov
Date: April 21 2024
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
resetMazeTraversal

WHAT DESCRIPTION DOES
The function resets the path and the vertices to their default values.

INPUTS
maze: A Maze object representing the maze.

OUTPUTS
No output
"""
def resetMazeTraversal(maze):
	for node in maze.adjList:
		node.dist = math.inf
		node.visited = False
		node.prev = None  
	maze.path = []


"""
BFS/DFS function

DESCRIPTION
The function traverses the maze from the start until it finds the exit if any

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The path from maze.start to maze.exit.
"""
def bdfs(maze, alg):
	# If the alg is not BFS or DFS, raise exception.
	if (alg != 'BFS') and (alg != 'DFS'):
		raise Exception('Incorrect alg! Need BFS or DFS!')

	resetMazeTraversal(maze)

	if alg == 'BFS':
		nodes_to_visit = Queue()
	else:
		nodes_to_visit = Stack()

	# initialise the start of the algorithm
	current = None
	maze.start.dist = 0
	maze.start.visited = True
	nodes_to_visit.push(maze.start)

	# traverse the maze until the exit was found or all vertices were visited
	while not nodes_to_visit.isEmpty():
		current = nodes_to_visit.pop()

		if current.isEqual(maze.exit):
			break

		for neighbor in current.neigh:
			if not neighbor.visited:
				nodes_to_visit.push(neighbor)
				neighbor.dist = current.dist + 1
				neighbor.prev = current
				neighbor.visited = True
		# setting the current to None in case the loop finishes
		#   before finding exit
		current = None

	# return empty list if the exit was not found
	if current is None:
		return []

	# record the vertices between the exit and the start
	while True:
		maze.path.append(current.rank)
		if current.prev is None:
			break
		current = current.prev

	# reverse the recorded vertices along the direction start -> exit
	maze.path.reverse()

	return maze.path


"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)
