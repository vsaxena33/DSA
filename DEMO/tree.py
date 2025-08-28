class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f"TreeNode({self.value})"

    def print_tree(self, level=0):
        print("  " * level + str(self.value))
        for child in self.children:
            child.print_tree(level + 1)

# Create nodes
root = TreeNode("Root")
child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")
subchild1 = TreeNode("Subchild 1")

# Build tree
root.add_child(child1)
root.add_child(child2)
child1.add_child(subchild1)

# Print tree
root.print_tree()
