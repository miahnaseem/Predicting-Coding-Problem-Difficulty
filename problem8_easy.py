# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# Input: (0, (1), (0, (1, (1), (1)), (0))) Output: 5
#	  0
#	 / \
#	1	0
#  /   /  \
# 1	  1    0
#	 /	\
#	1    1

# Notes: Leafs are conssidered unival subtrees.

# Basic binary tree structure
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursively move through tree, increment count on 
def count_unival_trees(node):
	count = 0
	# Leafs are unival tree, increment count, end recursion
	if node.left == None and node.right == None:
		print(f'leaf: {node.val}')
		print(f'count: {count + 1}')
		return 1
	# Recurse through trees with only right nodes
	elif node.left == None:
		return count + count_unival_trees(node.right)
	# Recurse through trees with only left nodes
	elif node.right == None:
		return count + count_unival_trees(node.left)
	# If tree has both right and left node:
	else:
		# Increment if right and left node equal: unival subtree
		if node.right.val == node.left.val:
			print(f'unival: {node.right.val} {node.left.val}')
			count += 1
			print(f'count: {count}')
		# Recurse through both right and left node
		return count + count_unival_trees(node.right) + count_unival_trees(node.left)

# Test sample inout
node1 = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))

print(count_unival_trees(node1))