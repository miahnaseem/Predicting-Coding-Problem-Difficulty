# Given a list of numbers and a number k, return whether any two numbers from a list add up to k
# e.g. list:[10,15,3,7], k:17 -> true

list = [10,15,3,7]
k = 17

for i in list:
    if k-i in list:
        print(f'True: {i} + {k-i} = {k}')