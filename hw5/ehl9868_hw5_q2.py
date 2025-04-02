from ArrayStack import ArrayStack

class MaxStack:
    def __init__(self):
        self.data = ArrayStack()
        self.maxNum = 0

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return self.data.is_empty()

    def push(self, val):
        if val > self.maxNum:
            self.maxNum = val
            self.data.push((val, val))
        else:
            self.data.push((val, self.maxNum))

    def top(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data.top()[0]

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data.pop()[0]

    def max(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        self.maxNum = self.data.top()[1]
        return self.maxNum
