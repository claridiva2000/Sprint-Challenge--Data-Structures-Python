from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        elif self.storage.length == self.capacity:
            stash = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if stash == self.current:
                self.current = self.storage.tail



    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        
        list_buffer_contents.append(self.current.value)

        if self.current.next is not None:
            #if current isn't the only node in the list
            #store the next node
            next_node = self.current.next
        else:
            next_node = self.storage.head

        while next_node != self.current:
            #traverse the list and add the new node to the array
            list_buffer_contents.append(next_node.value)
            if next_node.next is not None:
                next_node = next_node.next
            else:
                next_node = self.storage.head

        return list_buffer_contents


# My attempt to solve using a circular linked list and no array. mostly because i didn't notice the get function right away. I don't want to delete it because i'm happy to have gotten as far as i did before realizing i was working too hard. also, the test wasn't set up this way, and this self contained method would only work if it was writtend directly inside the linked list class. :-) 

   # self.current = self.storage.head
        # count = 0
        # while count < self.capacity:
        #     #check is storage is empty. 
        #     if self.storage.head is None and self.storage.tail is None:
        #         #if it is, create a new node to the head and point head & tail to it.
        #         self.storage.add_to_head(item)
        #         count += 1
        #     else:
        #         # add new node to the tail
        #         self.storage.add_to_tail(item)
        #         # turn into a circular linked list by connected head and tail together. like a chain necklace.
        #         self.storage.tail.next, self.storage.head.prev = self.storage.head, self.storage.tail
        #         count += 1

        # #if count is equal to capacity,and current is equal to head
        # if self.current == self.storage.head:
        #     #add a new node to tail
        #     self.storage.add_to_tail(item)
        #     #move current to the next oldest item
        #     self.current= self.current.next
        #     #connect the new tail to the new-current & connect the new current back to the new tail. this circumvents the old-current (oldest item)
        #     #it will be handled by garbage-collection.
        #     self.storage.tail.next = self.current
        #     self.current.prev = self.storage.tail
        #     #move head to where tail is, and move tail to the node before it.
        #     self.storage.head, self.storage.tail = self.storage.tail, self.storage.tail.prev
        # else:
        #     #if count is equal capacity and current is not equal to head
        #     #create a new node
        #     new_node = self.storage.make_node(item)
        #     #connect the new node to the node after current
        #     new_node.next = self.current.next 
        #     #connect the node before current to the new node
        #     self.current.next.prev = new_node
        #     #connect the node after current to the new node
        #     self.current.prev.next = new_node
        #     #connect the new node back to the node before current
        #     new_node.prev = self.current.prev
        #     #move current to the next oldest item in the list.
        #     self.current = new_node.next

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
