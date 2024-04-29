"""
Math 560
Project 4
Spring 2024

Ruslan Basyrov
Date: 4/28/2023
"""

# Import p4tests.
from p4tests import *

################################################################################

"""
ED: the edit distance function

input:
	source string, destination string,
		and the type of problem (edit distance / approximate string matching)

output:
	number of edits, list of edits
"""

def ED(src, dest, prob='ED'):
	# Check the problem to ensure it is a valid choice.
	if (prob != 'ED') and (prob != 'ASM'):
		raise Exception('Invalid problem choice!')

	n, m = len(src), len(dest)

	# initialise the table with 0s
	dp_table = [[[0, None] for _ in range(m + 1)] for _ in range(n + 1)]

	# filling the base cases
	#   fill the first row with values for 'insert' if the problem is 'ED'
	if prob != 'ASM':
		for j in range(1, m + 1):
			dp_table[0][j] = [j, 'left']
	#   fill the first column with values for 'delete'
	for i in range(1, n + 1):
		dp_table[i][0] = [i, 'up']

	# filling the dp_table by iterating across each row
	for i in range(1, n + 1):
		for j in range(1, m + 1):
			if src[i - 1] == dest[j - 1]:
				dp_table[i][j] = [dp_table[i - 1][j - 1][0], 'diagonally']
			else:
				if dp_table[i][j - 1][0] < dp_table[i - 1][j][0]:
					dp_table[i][j] = [1 + dp_table[i][j - 1][0], 'left']
				elif dp_table[i - 1][j][0] < dp_table[i][j - 1][0]:
					dp_table[i][j] = [1 + dp_table[i - 1][j][0], 'up']
				else:
					dp_table[i][j] = [1 + dp_table[i - 1][j - 1][0], 'diagonally']

	# reconstruct a solution
	dist = dp_table[n][m][0]
	edits = []
	while dp_table[n][m][1] != None:
		if dp_table[n][m][1] == 'left':
			edit = ['insert', dest[m - 1], n]
			m -= 1
		elif dp_table[n][m][1] == 'up':
			edit = ['delete', src[n - 1], n-1]
			n -= 1
		else: 
			if dp_table[n][m][0] == dp_table[n - 1][m - 1][0]:
				edit = ['match', src[n - 1], n - 1]
			else:
				edit = ['sub', dest[m - 1], n - 1]
			n -= 1
			m -= 1
		edits.append(edit)
	return dist, edits

################################################################################

"""
Main function.
"""
if __name__ == "__main__":
    edTests(False)
    print()
    compareGenomes(True, 30, 300, 'ED')
    print()
    compareRandStrings(True, 30, 300, 'ED')
    print()
    compareGenomes(True, 30, 300, 'ASM')
    print()
    compareRandStrings(True, 30, 300, 'ASM')
