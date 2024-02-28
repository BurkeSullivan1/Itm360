class Node:
    def __init__(self, d=None, l=None):
        self._data = d
        self._link = l
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, d):
        self._data = d
    @property
    def link(self):
        return self._link
    @link.setter
    def link(self, l):
        self._link = l

def print_list(node):
    current = node
    while current is not None:
        print(current.data, end=" -> " if current.link else "")
        current = current.link
    print()  # for newline

# Creating a linked list with a single node containing the value 5
head = Node(5)
tail = head
print_list(head)  # Output: 5

# Appending a node with the value 10 to the end of the list
tail.link = Node(10)
tail = tail.link  #update tail to be this new node
print_list(head)  # Output: 5 -> 10


# Values to be added
values = [15, 20, 25, 30, 35, 40]
for value in values:
    tail.link = Node(value)
    tail = tail.link
print_list(head)  # Output: 5 -> 10 -> 15 -> 20 -> 25 -> 30 -> 35 -> 40

# Create the new node with value 12
new_node = Node(12)
current = head
#starting from the head, find the position to insert the new node
while current.link is not None and current.link.data < new_node.data:
    current = current.link
#insert the new node
new_node.link = current.link
current.link = new_node
print_list(head)  # Output: 5 -> 10 -> 12 -> 15 -> 20 -> 25 -> 30 -> 35 -> 40


# Since the value 5 is at the head, simply move the head pointer to the next node
head = head.link  # Move head to the next node, effectively removing the first node
print_list(head)  # Output: 10 -> 12 -> 15 -> 20 -> 25 -> 30 -> 35 -> 40


# Starting from the head, square the value of each node
current = head
while current is not None:
    current.data = current.data ** 2
    current = current.link # move to the next node
print_list(head)  # Output: 100 -> 144 -> 225 -> 400 -> 625 -> 900 -> 1225 -> 1600

