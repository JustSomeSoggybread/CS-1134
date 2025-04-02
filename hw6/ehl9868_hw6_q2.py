from DoublyLinkedList import DoublyLinkedList
class Integer:
    def __init__(self, num_str):
        self.data = DoublyLinkedList()
        for char in num_str:
            self.data.add_last(int(char))
    
    def __add__(self, other):
        retThis = Integer("")
        selfPoint = self.data.trailer.prev
        otherPoint = other.data.trailer.prev
        ovfl = 0

        if (len(self.data) >= len(other.data)):
            while selfPoint != self.data.header:
                if (otherPoint != other.data.header):
                    tempSum = selfPoint.data + otherPoint.data + ovfl
                    insert = tempSum % 10
                    retThis.data.add_first(insert)
                    ovfl = tempSum // 10
                    selfPoint = selfPoint.prev
                    otherPoint = otherPoint.prev
                else:
                    tempSum = selfPoint.data + ovfl
                    insert = tempSum%10
                    retThis.data.add_first(insert)
                    ovfl = tempSum // 10
                    selfPoint = selfPoint.prev
        
        elif(len(other.data) > len(self.data)):

            while otherPoint != other.data.header:
                if (selfPoint != self.data.header):
                    tempSum = selfPoint.data + otherPoint.data + ovfl
                    insert = tempSum % 10
                    retThis.data.add_first(insert)
                    ovfl = tempSum // 10
                    selfPoint = selfPoint.prev
                    otherPoint = otherPoint.prev
                else:
                    tempSum = otherPoint.data + ovfl
                    insert = tempSum % 10
                    retThis.data.add_first(insert)
                    ovfl = tempSum // 10
                    otherPoint = otherPoint.prev
        
        if ovfl != 0:
            retThis.data.add_first(ovfl)

        
        return retThis

    def __mul__(self, other):
        retThis = Integer("0")
        selfPointer = self.data.trailer.prev
        otherPointer = other.data.trailer.prev
        tenPower = 0
        ovfl = 0

        while selfPointer != self.data.header:
            curSum = Integer("")
            ovfl = 0
            while otherPointer != other.data.header:
                
                prod = selfPointer.data * otherPointer.data + ovfl
                ovfl = prod // 10
                prod = prod % 10
                curSum.data.add_first(prod)
                otherPointer = otherPointer.prev

            if ovfl != 0:
                curSum.data.add_first(ovfl)
            
            for i in range(tenPower):
                curSum.data.add_last(0)
            
            tenPower += 1
            
            retThis += curSum

            selfPointer = selfPointer.prev
            otherPointer = other.data.trailer.prev

        return retThis
        

    def __repr__(self): 
        retPointer = self.data.header.next
        while (retPointer != self.data.trailer):
            if (retPointer.data == 0):
                retPointer = retPointer.next
                self.data.delete_first()
                
            else:
                return "".join(str(i) for i in self.data)
        return "0"