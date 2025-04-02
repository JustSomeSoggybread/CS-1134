from DoublyLinkedList import DoublyLinkedList

class CompactString:
    def __init__(self, orig_str):
        self.cs = DoublyLinkedList()
        for char in orig_str:
            if self.cs.is_empty():
                self.cs.add_last((char, 1))
            elif self.cs.trailer.prev.data[0] == char:
                self.cs.trailer.prev.data = (char, self.cs.trailer.prev.data[1] + 1)
            else:
                self.cs.add_last((char, 1))
    
    def __add__(self, other):
        retThis = CompactString("")
        selfPointer = self.cs.header.next
        otherPointer = other.cs.header.next

        while (selfPointer != self.cs.trailer):
            retThis.cs.add_last(selfPointer.data)
            selfPointer = selfPointer.next

        if (selfPointer.prev.data[0] == otherPointer.data[0]):
            retThis.cs.trailer.prev.data = (retThis.cs.trailer.prev.data[0], retThis.cs.trailer.prev.data[1] + otherPointer.data[1])
            otherPointer = otherPointer.next

        while (otherPointer != other.cs.trailer):
            retThis.cs.add_last(otherPointer.data)
            otherPointer = otherPointer.next
        
        return retThis

    def __lt__(self, other):
        selfPointer = self.cs.header.next
        otherPointer = other.cs.header.next

        while (selfPointer is not self.cs.trailer and otherPointer is not other.cs.trailer):
            if selfPointer.data[0] < otherPointer.data[0]:
                return True
            elif selfPointer.data[0] > otherPointer.data[0]:
                return False
            else:
                if selfPointer.data[1] < otherPointer.data[1]:
                    return False
                elif selfPointer.data[1] > otherPointer.data[1]:
                    return True
                else:
                    selfPointer = selfPointer.next
                    otherPointer = otherPointer.next

        if selfPointer is self.cs.trailer and otherPointer is not other.cs.trailer:
            return True
        else:
            return False

    def __le__(self, other):
        selfPointer = self.cs.header.next
        otherPointer = other.cs.header.next

        while (selfPointer is not self.cs.trailer and otherPointer is not other.cs.trailer):
            if selfPointer.data[0] < otherPointer.data[0]:
                return True
            elif selfPointer.data[0] > otherPointer.data[0]:
                return False
            else:
                if selfPointer.data[1] < otherPointer.data[1]:
                    return False
                elif selfPointer.data[1] > otherPointer.data[1]:
                    return True
                else:
                    selfPointer = selfPointer.next
                    otherPointer = otherPointer.next

        if selfPointer is self.cs.trailer and otherPointer is other.cs.trailer:
            return True
        else:
            return False

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __repr__(self):
        return "".join(letter * count for letter, count in self.cs)