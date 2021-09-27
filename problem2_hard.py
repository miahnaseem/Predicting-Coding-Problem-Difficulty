# Given array of integers, return new array such that each element at index i of new array
# is the product of all the numbers in the original array except the one at i

# e.g. input[1,2,3,4,5] -> output[120,60,40,30,24]
# e.g. input[3,2,1] -> [2,3,6]

input = [1,2,3,4,5]

output = []


for i in range(0, len(input)):
    product = 1
    tmp = input[0:i] + input[i+1:len(input)]
    print(tmp)
    for j in tmp:
        product = product * j
    output.append(product)

print(output) 

