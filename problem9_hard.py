c# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# e.g. Input: [2, 4, 6, 2, 5], Output: 13 (add 2, 6, 5)
# Input: [5,1,1,5], Output: 10 (add 5, 5)

input = [5,1,1,5]

def non_adjacent_sum(input):
	# Temp variables to help store sums
	first = 0
	second = 0

	# Iterate down
	for i in range(len(input)-1, -1, -1):
		# compare the max of previous max sum and 
		# the nonadjecent current potential max sum 
		sum = max(input[i] + second, first)
		# Switch the second to first to compare non-adjacents
		second = first
		# First is set to standing largest sum
		first = sum
	return first

print(non_adjacent_sum(input))