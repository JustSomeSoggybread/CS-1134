from DoublyLinkedList import DoublyLinkedList

class LinkedQueue:
    def __init__(self):
        self.data = DoublyLinkedList()
    
    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self.data) == 0
    
    def enqueue(self, val):
        self.data.add_last(val)
    
    def dequeue(self):
        if self.data.is_empty == True:
            raise Exception("Empty Queue")
        else:
            return self.data.delete_first()

    def first(self):
        if self.data.is_empty == True:
            raise Exception("Empty Queue")
        
        return self.data.header.next.data
