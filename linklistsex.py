class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedListQueue:
    def __init__(self):
        self.head = None  # Front of the queue
        self.tail = None  # Rear of the queue

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        removed_value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None  # The queue is empty
        return removed_value

    def peek(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.head.value
queue = LinkedListQueue()

# Enqueue elements
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Dequeue elements
print(queue.dequeue())  # Output: 1
print(queue.peek())     # Output: 2
