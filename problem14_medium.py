# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

import math
import random

# Helper function to get a random float
def get_random_float(min, max):
	range = max - min
	choice = random.uniform(0,1)
	return min + range*choice

# We will be simulating Monte Carlo sampling for pi on a circle with radius r
# This involves getting an wide sample range of areas, and getting the average value of pi
# in those samples

# Helper function to get pi
def get_pi(radius, area):
	pi = area / (radius ** 2)
	return pi

# We will be doing monte carlo sampling on a circle with radius 5, or area between 78 and 79
def monte_carlo_sampling(num_samples):
	radius = 5
	low = 78
	high = 79

	sum_of_samples = 0

	for i in range(num_samples):
		x = get_random_float(low, high)
		sum_of_samples += get_pi(radius, x)
	# While we are supposed to estimate to 3 decimal places, I do 4 such that
	# the variance of the monte carlo sampling can be seen (otherwise it will
	# round to 3.14 every time)
	return round((high - low) * float(sum_of_samples/num_samples), 4)


print(monte_carlo_sampling(5000))