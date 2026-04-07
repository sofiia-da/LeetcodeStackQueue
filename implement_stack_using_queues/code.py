from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, x: int) -> None:
        self._items.append(x)

    def dequeue(self) -> int:
        return self._items.popleft()

    def peek(self) -> int:
        return self._items[0]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q2.enqueue(x)

        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.dequeue()

    def top(self) -> int:
        return self.q1.peek()

    def empty(self) -> bool:
        return self.q1.is_empty()
