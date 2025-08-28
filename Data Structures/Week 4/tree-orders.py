# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for _ in range(self.n)]
    self.left = [0 for _ in range(self.n)]
    self.right = [0 for _ in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    def in_order_traverse(node):
        if node == -1:
            return
        in_order_traverse(self.left[node])
        self.result.append(self.key[node])
        in_order_traverse(self.right[node])
    in_order_traverse(0)
    return self.result

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    def pre_order_traverse(node):
        if node == -1:
            return
        self.result.append(self.key[node])
        pre_order_traverse(self.left[node])
        pre_order_traverse(self.right[node])
    pre_order_traverse(0)
    return self.result

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    def post_order_traverse(node):
        if node == -1:
            return
        post_order_traverse(self.left[node])
        post_order_traverse(self.right[node])
        self.result.append(self.key[node])
    post_order_traverse(0)
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
