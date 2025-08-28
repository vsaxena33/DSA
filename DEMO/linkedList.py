# Node class
class Node:
    def __init__(self, data):
        self.data = data  # Value of the node
        self.next = None  # Pointer to the next node


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # Initially the list is empty

    # Insert a new node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node

    # Print the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' → ')
            current = current.next
        print('None')

    # Insert at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Delete a node by value
    def delete(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return  # Key not found

        prev.next = current.next


# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)
ll.print_list()  # Output: 5 → 10 → 20 → 30 → None

ll.delete(20)
ll.print_list()  # Output: 5 → 10 → 30 → None
