# Implement an XOR linked list; it has an add(element) and a get(index)
# add(element) adds the element to the end
# get(index) returns the node at index

# My understanding of pointers in python is limited
# Thus, I will be listing a complete solution posted
# and commenting my understanding of it

# Source: https://www.geeksforgeeks.org/implementation-of-xor-linked-list-in-python/

# import required module
# Provides C compatible data types
import ctypes



# create node class
class Node:
	def __init__(self, value):
		self.value = value
        # From my understanding, this will be used to store list index/reference information of the node.
        # When you XOR 0 and npx, it will return the same value as the address
        # of the node behind it
        # The starting npx of 0 will XOR addresses following, which in chain stores index information
        # as a double linked list
		self.npx = 0


		
# create linked list class
class XorLinkedList:

	# constructor
    # "__nodes" is key to implementation here. __ is used to store objects of node,
    # preventing it from becoming garbage
	def __init__(self):
		self.head = None
		self.tail = None
		self.__nodes = []

	# method to insert node at beginning
	def InsertAtStart(self, value):
		node = Node(value)
        # if there is no head node, list is empty, inserted node
        # will be both head and tail
		if self.head is None: # If list is empty
			self.head = node
			self.tail = node
        # otherwise, the new head will be the XOR (^ operator) of the index of
        # the inserted node and the previous head node
		else:
			self.head.npx = id(node) ^ self.head.npx
		# After setting the head reference node npx, convert the inserted node's
        # index to that npx
			node.npx = id(self.head)
			self.head = node
        # You can simply append the node to a list, as the next/prev information will
        # be in the address and can be collected through XOR operations
		self.__nodes.append(node)

	# method to insert node at end
	def InsertAtEnd(self, value):
		node = Node(value)
        # if there is no head node, list is empty, inserted node
        # will be both head and tail
		if self.head is None: # If list is empty
			self.head = node
			self.tail = node
		# otherwise, the new tail will be the XOR (^ operator) of the index of
        # the inserted node and the previous tail node
		else:
			self.tail.npx = id(node) ^ self.tail.npx
            # After setting the tail reference node npx, convert the inserted node's
            # index to that npx
			node.npx = id(self.tail)
			self.tail = node
		self.__nodes.append(node)

	# method to remove node at beginning
	def DeleteAtStart(self):
		if self.isEmpty(): # If list is empty
			return "List is empty !"
        # If list has only one node, both head and tail can be set to null
		elif self.head == self.tail: # If list has 1 node
			self.head = self.tail = None
        # If the XOR of the head npx and 0 is equal to the reference address of tail
        # that means there must be two nodes: just head and tail: delete the head.
		elif (0 ^ self.head.npx) == id(self.tail): # If list has 2 nodes
			self.head = self.tail
            # Set npx to 0 as that will work as the start to the XOR indexing structure 
			self.head.npx = self.tail.npx = 0
		else: # If list has more than 2 nodes
            # store the value of the node to be deleted, to return
			res = self.head.value
            # As commented, x holds address of the next node
			x = self.__type_cast(0 ^ self.head.npx) # Address of next node
            # As commented, y jp;ds address of the next of the next node
			y = (id(self.head) ^ x.npx) # Address of next of next node
            # The new head is x, and x's npx value is set to 0 XOR y.
            # This maintains the XOR indexing throughout the double linked list
			self.head = x
			self.head.npx = 0 ^ y
			return res

	# method to remove node at end
	def DeleteAtEnd(self):
		if self.isEmpty(): # If list is empty
			return "List is empty !"
        # If list has only one node, both head and tail can be set to null
		elif self.head == self.tail: # If list has 1 node
			self.head = self.tail = None
        # If the XOR of the head npx and 0 is equal to the reference address of tail
        # that means there must be two nodes: just head and tail: delete the tail.
		elif self.__type_cast(0 ^ self.head.npx) == (self.tail): # If list has 2 nodes
			self.tail = self.head
			self.head.npx = self.tail.npx = 0
		else: # If list has more than 2 nodes
            # temp values for getting second to last node npx
			prev_id = 0
			node = self.head
			next_id = 1
            # I believe this loops through the node list, starting at the head,
            # until next_id is set to 0 (thus reaching the end). Then the node before tail,
            # as prev_id, is set to a pointer where it's "__type_cast()"
            # will maintain the XOR linked list, and can be used as the new tail
			while next_id:
				next_id = prev_id ^ node.npx
				if next_id:
					prev_id = id(node)
					node = self.__type_cast(next_id)
			res = node.value
            # x holds the npx of node before the new tail
			x = self.__type_cast(prev_id).npx ^ id(node)
            # y holds the reference of the new tail
			y = self.__type_cast(prev_id)
            # y's npx is set to be XOR of the node before the new tail, and the new tail
			y.npx = x ^ 0
            # Set y to tail as it maintains XOR double linked list
			self.tail = y
			return res

	# method to traverse linked list
    # Not included in the dailycoding problem, but useful for reference
	def Print(self):
		"""We are printing values rather than returning it bacause
		for returning we have to append all values in a list
		and it takes extra memory to save all values in a list."""

		if self.head != None:
			prev_id = 0
			node = self.head
			next_id = 1
			print(node.value, end=' ')
			while next_id:
				next_id = prev_id ^ node.npx
				if next_id:
					prev_id = id(node)
					node = self.__type_cast(next_id)
					print(node.value, end=' ')
				else:
					return
		else:
			print("List is empty !")

	# method to traverse linked list in reverse order
    # Not included in the dailycoding problem, but useful for reference
	def ReversePrint(self):

		# Print Values is reverse order.
		"""We are printing values rather than returning it bacause
		for returning we have to append all values in a list
		and it takes extra memory to save all values in a list."""

		if self.head != None:
			prev_id = 0
			node = self.tail
			next_id = 1
			print(node.value, end=' ')
			while next_id:
				next_id = prev_id ^ node.npx
				if next_id:
					prev_id = id(node)
					node = self.__type_cast(next_id)
					print(node.value, end=' ')
				else:
					return
		else:
			print("List is empty !")

	# method to get length of linked list
    # Not included in the dailycoding problem, but useful for reference
	def Length(self):
		if not self.isEmpty():
			prev_id = 0
			node = self.head
			next_id = 1
			count = 1
			while next_id:
				next_id = prev_id ^ node.npx
				if next_id:
					prev_id = id(node)
					node = self.__type_cast(next_id)
					count += 1
				else:
					return count
		else:
			return 0

	# method to get node data value by index
	def PrintByIndex(self, index):
        # prev_id used to loop through list, starting at head
		prev_id = 0
		node = self.head
        # loop until position of `index`
		for i in range(index):
            # As per XOR double linked list structure, we take prev_id XOR node.npx to
            # get reference of the next node
			next_id = prev_id ^ node.npx

            # If the next node exists, the node at index is set to `prev_node`
			if next_id:
				prev_id = id(node)
                # next node is set to node at index
				node = self.__type_cast(next_id)
			else:
				return "Value isn't; found index out of range."
        # After looping through range(index), we are end up at desired index, and can
        # return it's value
		return node.value

	# method to check if the liked list is empty or not
    # Not included in the dailycoding problem, but useful for reference
	def isEmpty(self):
		if self.head is None:
			return True
		return False

	# method to return a new instance of type
	def __type_cast(self, id):
		return ctypes.cast(id, ctypes.py_object).value


		
# Driver Code
# Test if XOR double linked list works as intended 

# create object
obj = XorLinkedList()

# insert nodes
obj.InsertAtEnd(2)
obj.InsertAtEnd(3)
obj.InsertAtEnd(4)
obj.InsertAtStart(0)
obj.InsertAtStart(6)
obj.InsertAtEnd(55)

# display length
print("\nLength:", obj.Length())

# traverse
print("\nTraverse linked list:")
obj.Print()

print("\nTraverse in reverse order:")
obj.ReversePrint()

# display data values by index
print('\nNodes:')
for i in range(obj.Length()):
	print("Data value at index", i, 'is', obj.PrintByIndex(i))

# removing nodes
print("\nDelete Last Node: ", obj.DeleteAtEnd())
print("\nDelete First Node: ", obj.DeleteAtStart())

# new length
print("\nUpdated length:", obj.Length())

# display data values by index
print('\nNodes:')
for i in range(obj.Length()):
	print("Data value at index", i, 'is', obj.PrintByIndex(i))

# traverse
print("\nTraverse linked list:")
obj.Print()

print("\nTraverse in reverse order:")
obj.ReversePrint()

