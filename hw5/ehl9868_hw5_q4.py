from ArrayStack import ArrayStack

class Queue:
    def __init__ (self):
        self.inStack = ArrayStack()
        self.outStack = ArrayStack()

    def __len__(self):
        return len(self.inStack) + len(self.outStack)

    def is_empty(self):
        return self.inStack.is_empty() and self.outStack.is_empty()
    
    def enqueue(self, val):

        if (self.outStack.is_empty() == False):
            while self.outStack.is_empty() == False:
                self.inStack.push(self.outStack.pop())
        self.inStack.push(val)
        
    
    def dequeue(self):
        if (self.inStack.is_empty() == False):
            while self.inStack.is_empty() == False:
                self.outStack.push(self.inStack.pop())
        if self.outStack.is_empty():
            raise Exception("Empty queue")
        return self.outStack.pop()  

    def first(self):
        if (self.inStack.is_empty() == False):
            while self.inStack.is_empty() == False:
                self.outStack.push(self.inStack.pop())
        if self.outStack.is_empty():
            raise Exception("Empty queue")
        return self.outStack.top()
    
    def last(self):
        if (self.outStack.is_empty() == False):
            while self.outStack.is_empty() == False:
                self.inStack.push(self.outStack.pop())
        if self.inStack.is_empty():
            raise Exception("Empty queue")
        return self.inStack.top()