# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
# Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

# e.g. Input: 4, Output: 5
# - 1,1,1,1
# - 2,1,1
# - 1,2,1
# - 1,1,2
# - 2,2

steps = [1,2]

def stair_climber(num_stairs, steps):
	count = 0
	all_step_lists = []
	steps_list = []
	steps_left = num_stairs
	while steps_left > 0:
		for i in steps:
			if steps_left - i <= 0:
				steps_list.append(i)
				steps_left = steps_left -1
			else:
				steps_list.append(i)
				steps_left = steps_left -1
	return steps_list

print(stair_climber(4, steps))

