#Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

# I do not prefer using external packages in my solution, but in this case
# for delays, I could not find any solution besides using the time.sleep function
from time import sleep

# Simple print to monitor function status
def printer():
	print("Running")

# Quick use with time package
def job_scheduler(f, n):
	# Error checking since we will be using user input
	assert len(n) > 0, "Must enter an input"
	assert type(float(n)) is float, "Must enter a number"

	# Loop through continuously and use n millisecond delay
	while 1:
		# Must convert n to float
		sleep(float(n)*.001)
		f()

n = input("Scheduler down time (in milliseconds): ")

job_scheduler(printer, n)
