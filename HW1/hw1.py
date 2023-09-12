#Name:	
#ID:    
#Email: mroland@unomaha.edu 	


# You are not allowed to modify this class
class Node:
	def __init__(self, data):
		## data of the node
		self.data = data

		## next pointer
		self.next = None

# You can modify this class as you want
class LinkedList:
	def __init__(self):
		## initializing the head with None
		self.head = None
		self.n = 0

	def display(self):
		## variable for iteration
		temp_node = self.head

		## iterating until we reach the end of the linked list
		while temp_node != None:
			## printing the node data
			print(temp_node.data, end='->')

			## moving to the next node
			temp_node = temp_node.next

		print('Null')

	##############################################
	## Implement functions belows
	##############################################
	# add new node and sort the list
	# You can change the return values (from void to any) for each function as you want 
	# you can add functions as you want 
	def sortedAdd(self, value):
		pass

	def remove(self, idx):
		pass

	# find the maximum values in the list
	def findMax(self):
		# return max_value in the list
		pass

	# print linkedlist in a reversed order
	def printReversedList(self):
		pass


	# Extra functions
	def add(self, value):
		pass



if __name__ == '__main__':
	## instantiating the linked list
	l = LinkedList()

	# Your testcase will be here.
 	# This is a testcase example.
	l.sortedAdd(5)
	l.sortedAdd(2)
	l.sortedAdd(9)
	l.sortedAdd(1)
	l.sortedAdd(7)

	print(l.findMax())

	l.printReversedList()
    #################################
