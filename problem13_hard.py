# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# e.g. Input: s="abcba", k=2 Output: 'bcb'

s = "abcba"
k = 2

# Helper function
def num_distinct(substring):
	# simple memoization
	temp = []
	# check if character is distinct
	# if not, memoize it
	for i in substring:
		if i not in temp:
			temp.append(i)
	# return number of distinct characters
	return len(temp)

def distinct_substring(s, k):
	length = len(s)
	substrings =  []
	# Loop through string to get all substrings
	for i in range(length):
		for j in range(i, length):
			# Check if number of distinct characters is equal to k
			if num_distinct(s[i:j+1]) == 2:
				substrings.append(s[i:j+1])
	# Get the longest string first
	substrings.sort(key=len, reverse=True) 
	return substrings[0]

print(distinct_substring(s,k))