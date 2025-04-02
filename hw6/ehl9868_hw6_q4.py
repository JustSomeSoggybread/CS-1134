from DoublyLinkedList import DoublyLinkedList

def copy_linked_list(lnk_lst):
    retThis = DoublyLinkedList()
    pointer = lnk_lst.header.next
    while (pointer != lnk_lst.trailer):
        retThis.add_last(pointer.data)
        pointer = pointer.next
    return retThis

def deep_copy_linked_list(lnk_lst):
    retThis = DoublyLinkedList()
    pointer = lnk_lst.header.next
    while (pointer != lnk_lst.trailer):
        if type(pointer.data) == DoublyLinkedList:
            retThis.add_last(deep_copy_linked_list(pointer.data))
        else:
            retThis.add_last(pointer.data)
        pointer = pointer.next
    return retThis