class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()  # Placeholder node

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        return elems  # Return the list of elements

    # extractor function - get function

    def get(self,index):
        if index >=self.length():
            print("erorr: get idex out of range!")
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_idx==index: return cur_node.data
            cur_idx+=1
    def erase(self,index):
        if index >=self.length():
            print("erorr: get idex out of range!")
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx+=1

# Instantiate the LinkedList
my_list = LinkedList()

# Append elements
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

# Display list contents
print(my_list.display())  # Now this will print the list contents
my_list.erase(1)
print(my_list.display())
print("element at 2nd index: %d" % my_list.get(2))