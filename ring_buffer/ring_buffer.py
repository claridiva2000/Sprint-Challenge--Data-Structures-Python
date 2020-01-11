from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        self.current = self.storage.head
        count = 0
        while count < self.capacity:
            #check is storage is empty. 
            if self.storage.head is None and self.storage.tail is None:
                #if it is, create a new node to the head and point head & tail to it.
                self.storage.add_to_head(item)
                count += 1
            else:
                # add new node to the tail
                self.storage.add_to_tail(item)
                # turn into a circular linked list by connected head and tail together. like a chain necklace.
                self.storage.tail.next, self.storage.head.prev = self.storage.head, self.storage.tail
                count += 1

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
