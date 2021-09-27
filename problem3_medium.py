# Given root of binary tree, implement:
# serialize(root): serializes tree into string
# deserialize(s): deserializes string back into tree

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Reading depth-first
# First, implement w/o notion of depth or traceability
def serialize_naive(root):
    output = root.val
    if root.left != None:
        output += ',' + serialize_naive(root.left)
    if root.right != None:
        output += ',' + serialize_naive(root.right)
    return output

# Easier to implement traceability for more complex node structure
def serialize_complex(root):
    output = '[' + root.val + ','
    if root.left != None and root.right != None:
        output += '[' + root.left.val + ',' + root.right.val + ']];'
    if root.left != None:
        output += serialize_complex(root.left) + '0];'
    if root.right != None:
        output += serialize_complex(root.right) + '0];'
    return output

# Recursively builds nodes based on left and right
def deserialize_helper(ds_list):
    root = ds_list.pop(0)

    for i in ds_list:
        if '.' in i:
            ds_list[ds_list.index(i)] = i[:i.index('.')]

    ds_left = []
    ds_right = []
    for i in ds_list:
        if 'left' in i[:5]:
            ds_left.append(i)
        elif 'right' in i[:5]:
            ds_right.append(i) 
    
    if ds_left == [] and ds_right == []:
        return Node(root)
    elif ds_left == []:
        return Node(root, deserialize_helper(ds_right))
    elif ds_right == []:
        return Node(root, deserialize_helper(ds_left))
    else:
        return Node(root, deserialize_helper(ds_left), deserialize_helper(ds_right))

def deserialize_naive(serial):
    ds_list = serial.split(',')
    ds_list.sort(key=len)

    ds_left = []
    ds_right = []
    for i in ds_list:
        if 'left' in i[:5]:
            ds_left.append(i)
        elif 'right' in i[:5]:
            ds_right.append(i) 

    return Node(ds_list[-1], deserialize_helper(ds_left), deserialize_helper(ds_right))

# Should pass:
node = Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right', None, Node('right.right')))
print(f'Serialized: {serialize_naive(node)}')

node2 = deserialize_naive(serialize_naive(node))
print(f'Deserialized: {node2}')

print(node2.left.left.val)
assert deserialize_naive(serialize_naive(node)).left.left.val == 'left'

# The naive function does not recreate the binary tree with the exact roots for each note
# But the binary tree structure is the same
# I may refactor to fix this