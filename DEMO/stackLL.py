class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  # top points to the head of the linked list

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top  # point new node to current top
        self.top = new_node       # update top to new node

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        popped = self.top.data
        self.top = self.top.next  # move top to the next node
        return popped

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.data

    def display(self):
        current = self.top
        items = []
        while current:
            items.append(current.data)
            current = current.next
        print("Stack (top -> bottom):", items)

if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    stack.display()  # Output: Stack (top -> bottom): [30, 20, 10]

    print("Top element:", stack.peek())  # Output: 30

    print("Popped element:", stack.pop())  # Output: 30

    stack.display()  # Output: Stack (top -> bottom): [20, 10]
