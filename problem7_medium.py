# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# Input: '111', Output: 3 ('111' can be decoded as 'aaa', 'ka', or 'ak')
# Note: single length messages will not be used.
input = '111'

# Using combinations, we can quickly see all number of ways to decode
# This can be implemented using itertools very quickly, but we will
# produce a homebrew solution
def decoder(input):
	# count is the counter for decoded solutions
	count = 0
	# As per the note, messages of length 1 will not be counted // ends recursion
	if len(input) == 0 or len(input) == 1:
			return 0
	else:
		# Count combination of messages starting with the first letter
		# of length 2 or greater
		for i in range(len(input)+1):
			if len(input[:i]) == 0 or len(input[:i]) == 1:
				pass
			else:
				print(f'message: {input[:i]}')
				count += 1
	# Add all further counts, beginning with the next letter with recursion
	count += decoder(input[1:])
	return count
	

print(decoder(input))