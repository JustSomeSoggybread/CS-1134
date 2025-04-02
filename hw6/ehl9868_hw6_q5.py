from DoublyLinkedList import DoublyLinkedList

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    
    def merge_sublists(pointerA, pointerB, dll):
        if (pointerA == srt_lnk_lst1.trailer and pointerB == srt_lnk_lst2.trailer):
            return dll
        elif (pointerA == srt_lnk_lst1.trailer):
            dll.add_last(pointerB.data)
            return merge_sublists(pointerA, pointerB.next, dll)
            
        elif (pointerB == srt_lnk_lst2.trailer):
            dll.add_last(pointerA.data)
            return merge_sublists(pointerA.next, pointerB, dll)

        elif (pointerA.data < pointerB.data):
            dll.add_last(pointerA.data)
            return merge_sublists(pointerA.next, pointerB, dll)

        elif (pointerB.data <= pointerA.data):
            dll.add_last(pointerB.data)
            return merge_sublists(pointerA, pointerB.next, dll)

        return dll
        
    return merge_sublists(srt_lnk_lst1.header.next, srt_lnk_lst2.header.next, DoublyLinkedList())