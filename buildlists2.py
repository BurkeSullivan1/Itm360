class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()  # Placeholder node to simplify append operations
        self.tail = self.head  # Start with tail as the placeholder node

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node  # Link the new node to the last node
        self.tail = new_node  # Update the tail to be the new node

    def length(self):
        total = 0
        current = self.head.next  # Start with the first real node
        while current:
            total += 1
            current = current.next
        return total

    def display(self):
        elems = []
        current = self.head.next  # Start with the first real node
        while current:
            elems.append(current.data)
            current = current.next
        return elems

    def get(self, index):
        if index >= self.length():
            print("Error: Index out of range!")
            return None
        current_index = 0
        current_node = self.head.next  # Start with the first real node
        while current_node:
            if current_index == index:
                return current_node.data
            current_index += 1
            current_node = current_node.next

    def erase(self, index):
        if index >= self.length():
            print("Error: Index out of range!")
            return None
        current_index = 0
        current_node = self.head  # Start with the placeholder node to simplify removal
        while current_node.next:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                # If we're removing the tail, update it to the last_node
                if current_node == self.tail:
                    self.tail = last_node
                return
            current_index += 1

# Test the LinkedList
my_list = LinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

print(my_list.display())  # [1, 2, 3, 4]
my_list.erase(1)
print(my_list.display())  # [1, 3, 4]
print("Element at 2nd index:", my_list.get(2))  # Element at 2nd index: 4

