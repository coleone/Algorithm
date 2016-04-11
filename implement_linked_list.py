# JL 02/02/16: Initial version
""" Implementation of Linked List """

import sys

class Node(object):
    num_of_node = 0
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node
        Node.num_of_node += 1

    def __del__(self):
        pass

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head = None, next_node = None):
        self.head = head
        self.next_node = next_node

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        count = 0
        current = self.head
        while current != None:
            current = current.get_next()
            count += 1
        print "Linked list size is: " + str(count)
        return count

    def midNode(self):
        current = self.head
        front = self.head
        if current.get_next() != None:
            front = front.get_next()
            while front!= None:
                current = current.get_next()
                if front.get_next()!= None:
                    front = front.get_next().get_next()
                else:
                    front = front.get_next()
        return current

    def printList(self):
        print "Printing linked list: "
        current = self.head
        while current:
            print current.get_data()
            current = current.get_next()

    def search(self, data):
        current = self.head        
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
                print "Found %s!" %data
            else:
                current = current.get_next()
        if current == None:
            raise ValueError("Data is not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
                print "Found it! Going to delete."
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        # delete the head node
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def reverse(self):
        dummy_node = self.head
        first_node = self.head

        while first_node.get_next() != None:
            if first_node.get_next().get_next() != None:
                temp_node = first_node.get_next()
                first_node.set_next(temp_node.get_next())
                temp_node.set_next(dummy_node)
                dummy_node = temp_node
            else:
                temp_node = first_node.get_next()
                first_node.set_next(None)
                temp_node.set_next(dummy_node)
                dummy_node = temp_node

        self.head = dummy_node


if __name__ == "__main__":
    print "START"

    # example 1:
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)
    linked_list.insert(5)
    linked_list.insert(6)

    linked_list.size()
    linked_list.printList()
    print "Mid node data is: " + str(linked_list.midNode().get_data())

    # example 2:
    linked_list.reverse()
    linked_list.printList()
    print "Mid node data is: " + str(linked_list.midNode().get_data())
    
    print "END"
    sys.exit()
