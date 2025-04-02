from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque

class MidStack():
    def __init__(self):
        self.stack = ArrayStack()
        self.deque = ArrayDeque()
        self.isFront = True

    def __len__(self):
        return len(self.stack) + len(self.deque)

    def is_empty(self):
        return self.stack.is_empty() and self.deque.is_empty()

    def push(self, val):
        if (self.stack.is_empty()):
            self.stack.push(val)
        else:
            if len(self.stack) == len(self.deque):
                temp = self.deque.dequeue_first()
                self.stack.push(temp)
            
            self.deque.enqueue_last(val)

    def top(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        if (self.deque.is_empty()):
            return self.stack.top()
        else:
            return self.deque.last()

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        if (self.deque.is_empty()):
            return self.stack.pop()
        else:
            return self.deque.dequeue_last()

    def mid_push(self, val):
        self.deque.enqueue_first(val)