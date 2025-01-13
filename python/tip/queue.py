class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        new = Node(value)
        if self.is_empty():
            self.head = new
            self.tail = new
            return

        self.tail.next = new
        self.tail = new

    def dequeue(self):
        toDequeue = self.head
        self.head = self.head.next
        return toDequeue

    def peek(self):
        return self.head


# [4] -> [2] -> [3]
queue = Queue()
queue.enqueue(4)
queue.enqueue(2)
queue.enqueue(3)

print(queue.peek().data)
popped = queue.dequeue()
print(popped.data)
print(queue.peek().data)
