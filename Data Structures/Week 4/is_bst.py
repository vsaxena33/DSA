# #!/usr/bin/python3

# import sys, threading

# sys.setrecursionlimit(10**7) # max depth of recursion
# threading.stack_size(2**25)  # new thread will get stack of such size

# def IsBinarySearchTree(tree):
#   # Implement correct algorithm here
#   if not tree:
#     return True  # Empty tree is a valid BST

#   def is_bst(node_index, min_key, max_key):
#       if node_index == -1:
#         return True

#       key, left, right = tree[node_index]

#       # BST property check: current key must be in (min_key, max_key)
#       if key <= min_key or key >= max_key:
#         return False

#       # Left subtree: keys < current key
#       # Right subtree: keys > current key
#       return is_bst(left, min_key, key) and is_bst(right, key, max_key)

#   return is_bst(0, float('-inf'), float('inf'))


# def main():
#   nodes = int(sys.stdin.readline().strip())
#   tree = []
#   for i in range(nodes):
#     tree.append(list(map(int, sys.stdin.readline().strip().split())))
#   if IsBinarySearchTree(tree):
#     print("CORRECT")
#   else:
#     print("INCORRECT")

# threading.Thread(target=main).start()
#!/usr/bin/python3

import sys, threading

def IsBinarySearchTree(tree):
    if not tree:
        return True

    stack = [(0, float('-inf'), float('inf'))]  # (node_index, min_key, max_key)

    while stack:
        node_index, min_key, max_key = stack.pop()
        if node_index == -1:
            continue

        key, left, right = tree[node_index]

        if key <= min_key or key >= max_key:
            return False

        # Right child must be > current key
        stack.append((right, key, max_key))
        # Left child must be < current key
        stack.append((left, min_key, key))

    return True

def main():
    n = int(sys.stdin.readline())
    tree = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print("CORRECT" if IsBinarySearchTree(tree) else "INCORRECT")

threading.Thread(target=main).start()
