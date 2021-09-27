# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# Implement car and cdr

# Input: car(cons(3, 4)), output: 3
# Input: cdr(cons(3, 4)), output: 4

# Given

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# Cons returns a function
print(type(cons(3,4)))

# car
def car(pair):
    def left(a, b):
        return a
    return pair(left)

# cdr
def cdr(pair):
    def right(a, b):
        return b
    return pair(right)

print(car(cons(3, 4)))

# Note: My understanding of functional programming is limited
# I used this solution to understand the problem space and function behavior:
# https://galaiko.rocks/posts/dcp/problem-5/