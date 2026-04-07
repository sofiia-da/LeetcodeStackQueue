class Stack:
    def __init__(self):
        self._items = []

    def push(self, x: int) -> None:
        self._items.append(x)

    def pop(self) -> int:
        return self._items.pop()

    def peek(self) -> int:
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

class MyQueue:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def push(self, x: int) -> None:
        self.stack_in.push(x)

    def _move(self) -> None:
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())

    def pop(self) -> int:
        self._move()
        return self.stack_out.pop()

    def peek(self) -> int:
        self._move()
        return self.stack_out.peek()

    def empty(self) -> bool:
        return self.stack_in.is_empty() and self.stack_out.is_empty()
