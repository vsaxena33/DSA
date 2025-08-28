# #!/usr/bin/python3

# import sys, threading

# sys.setrecursionlimit(10**7) # max depth of recursion
# threading.stack_size(2**25)  # new thread will get stack of such size

# def IsBinarySearchTree(tree):
#   # Implement correct algorithm here
#   if not tree:
#     return True  # Empty tree is valid

#   def is_bst(node_index, min_key, max_key, allow_equal_min, allow_equal_max):
#       if node_index == -1:
#         return True

#       key, left, right = tree[node_index]

#       # Check left child
#       if (not allow_equal_max and key >= max_key) or (allow_equal_max and key > max_key):
#         return False
#       if (not allow_equal_min and key <= min_key) or (allow_equal_min and key < min_key):
#         return False

#       # Left: keys < key
#       left_ok = is_bst(tree[node_index][1], min_key, key, allow_equal_min, False)
#       # Right: keys >= key
#       right_ok = is_bst(tree[node_index][2], key, max_key, True, allow_equal_max)

#       return left_ok and right_ok

#   return is_bst(0, float('-inf'), float('inf'), True, True)

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

        # Check current node respects BST bounds:
        if key < min_key or key > max_key:
            return False

        # Left subtree: keys must be < key → max allowed = key - 1
        if left != -1:
            left_key = tree[left][0]
            if left_key >= key:
                return False
            stack.append((left, min_key, key - 1))

        # Right subtree: keys must be ≥ key → min allowed = key
        if right != -1:
            right_key = tree[right][0]
            if right_key < key:
                return False
            stack.append((right, key, max_key))

    return True


def main():
    n = int(sys.stdin.readline())
    tree = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print("CORRECT" if IsBinarySearchTree(tree) else "INCORRECT")

threading.Thread(target=main).start()
