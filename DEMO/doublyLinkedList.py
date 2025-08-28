# Node class for Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Append to end
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # Empty list
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    # Prepend to beginning
    def prepend(self, data):
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    # Delete a node by value
    def delete(self, key):
        current = self.head

        while current:
            if current.data == key:
                # Node is head
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                    current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                return  # Node deleted
            current = current.next

    # Print list forward
    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=' ⇄ ')
            last = current
            current = current.next
        print('None')

    # Print list backward
    def print_backward(self):
        current = self.head
        if not current:
            print('List is empty')
            return

        # Go to the end
        while current.next:
            current = current.next

        # Traverse backward
        while current:
            print(current.data, end=' ⇄ ')
            current = current.prev
        print('None')


# Example usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.prepend(5)

print("Forward:")
dll.print_forward()    # Output: 5 ⇄ 10 ⇄ 20 ⇄ 30 ⇄ None

print("Backward:")
dll.print_backward()   # Output: 30 ⇄ 20 ⇄ 10 ⇄ 5 ⇄ None

dll.delete(20)

print("After deleting 20:")
dll.print_forward()    # Output: 5 ⇄ 10 ⇄ 30 ⇄ None
