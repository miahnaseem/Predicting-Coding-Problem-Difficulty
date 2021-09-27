# Given an array of integers, find the first missing positive integer in linear time and constant space.
# Find the lowest posuitive integer that does not exist in the array

# input: [3,4,-1,1], output: 2
# input: [1,2,0], output: 3

input = [5,3,4,4,-1,1,1]

def first_missing_integer(input):
    # Sort to help ensure constant space (we are allowed to modify)
    input.sort(reverse=True)

    # Ensure that function only reads positive integers
    if 0 in input:
        input = input[:input.index(0)+1]

    prev = input[0] + 1
    # If all numbers exist in array, "missing number" should be the number after max of list 
    output = input[0] + 1
    
    # Linear time
    for i in input:
        # Check if list skips number or is a duplicate
        if i != prev-1 and i != prev:
            return prev-1
        prev = i
    return output


print(first_missing_integer(input))