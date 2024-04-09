"""
Math 560
Project 1
Spring 2024

Ruslan Basyrov
Date: 20 March 2024
"""

"""
SelectionSort

Complexity (average): O(n^2)

TLDR: the algorithm selects the smallest value to be swapped with for each next element of an array.

The algorithm sorts an array by iterating over it. The first iteration starts from the first element,
and the next iterations continue from the elements which immediately follow the previous ones until
all elements played their role as the start of an iteration.
In each iteration, the index of the smallest number is found in the area of search (which is reduced
by one element in each next iteration), in case the element is not equal to the starting element of
the iteration, their values are swapped.
"""
def SelectionSort(listToSort):
	for i in range(len(listToSort)):
		minNumIndex = i
		# finding the index of the smallest element in the area of search
		for j in range(i + 1, len(listToSort)):
			if (listToSort[j] < listToSort[minNumIndex]):
				minNumIndex = j
		# swapping elements
		if minNumIndex > i:
			listToSort[i], listToSort[minNumIndex] = listToSort[minNumIndex], listToSort[i]
	return listToSort

"""
InsertionSort

Complexity (average): O(n^2)

The algorithm sorts an array by inserting each next element from unsorted part into
the sorted one so that the order holds.
"""
def InsertionSort(listToSort):
	n = len(listToSort)
	for i in range(1, n):
		tmp = listToSort[i]
		j = i - 1
		# shift the part of sorted array by one to the right until the position
		#   where the element from the unsorted part should be positioned
		while j >= 0 and tmp < listToSort[j]:
			listToSort[j + 1] = listToSort[j]
			j -= 1
		listToSort[j + 1] = tmp
	return listToSort

"""
BubbleSort

Complexity (average): O(n^2)

The algorithm sorts an array by iterating over the unsorted portion of the array
for each next element from the end and swapping each next two elements if the element
to the right is smaller than the element to the left. If no such swap happened
in an iteration, the algorithm ends as it means the unsorted portion is actually sorted.
"""
def BubbleSort(listToSort):
	size = len(listToSort)
	for i in range(size):
		swapHappened = False
		# iterating over the unsorted part of the array and swapping each next two elements
		#   if the left one is bigger than the right one
		for j in range(0, size - i - 1):
			if listToSort[j] > listToSort[j + 1]:
				swapHappened = True
				listToSort[j], listToSort[j + 1] = listToSort[j + 1], listToSort[j]
		if not swapHappened:
			break
	return listToSort

"""
MergeSort

Complexity (average): O(n log(n))

The algorithm sorts an array recursively by splitting it into two until the base case
(which is sorted) and then merging the results.
"""
def MergeSort(listToSort):

	if len(listToSort) > 1:
		median = len(listToSort) // 2
		left = listToSort[:median]
		right = listToSort[median:]

		# recursively sort the two parts
		MergeSort(left)
		MergeSort(right)

		i = j = k = 0
		# combine the left and right parts by iterating over the left and right parts
		# and choosing the smallest element of them
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				listToSort[k] = left[i]
				i += 1
			else:
				listToSort[k] = right[j]
				j += 1
			k += 1

		# finish the merge by adding the elements left in the left part
		while i < len(left):
			listToSort[k] = left[i]
			i += 1
			k += 1

		# finish the merge by adding the elements left in the right part
		while j < len(right):
			listToSort[k] = right[j]
			j += 1
			k += 1
		
		return listToSort

"""
QuickSort

Complexity (average): O(n log n)

The algorithm sorts an array by recursively choosing a pivot and rearranging the elements
so that all the elements to the left of the pivot are smaller than it and vice versa to the right

The Partition helper function chooses a pivot (the final element of the partition in this case),
rearranged all the elements so that the ones that are lower than pivot are to the left, and
vice versa for bigger elements. Then it puts the pivot value to its place.
"""
def Partition(listToSort, i, j):
	pivot = listToSort[j]
	x = i - 1
	# rearranging the elements relative to pivot
	for y in range(i, j):
		if listToSort[y] <= pivot:
			x = x + 1
			listToSort[x], listToSort[y] = listToSort[y], listToSort[x]
	# positioning pivot in its place 
	listToSort[x + 1], listToSort[j] = listToSort[j], listToSort[x + 1]
	return x + 1

def QuickSort(listToSort, i=0, j=None):
	# set values
	if j == None:
		j = len(listToSort) - 1
	if j == len(listToSort):
		j -= 1

	# recursively sort the array
	if i < j:
		pivot = Partition(listToSort, i, j)
		QuickSort(listToSort, i, pivot - 1)
		QuickSort(listToSort, pivot + 1, j)
	return listToSort


"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('UNSORTED measureTime')
    print()
    measureTime()
    print()
    print('SORTED measureTime')
    print()
    measureTime(True)
