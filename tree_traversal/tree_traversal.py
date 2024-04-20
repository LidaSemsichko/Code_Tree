class Node:
  def __init__(data, left = None, right = None):
    self.data = data
    self.left = left
    self.right = right

# Pre-order traversal
def pre_order(node):
    listik = []
    if node:
        listik.append(node.data)
        listik.extend(pre_order(node.left))
        listik.extend(pre_order(node.right))
    return listik

# In-order traversal
def in_order(node):
    listik = []
    if node:
        listik.extend(in_order(node.left))
        listik.append(node.data)
        listik.extend(in_order(node.right))
    return listik

# Post-order traversal
def post_order(node):
    listik = []
    if node:
        listik.extend(post_order(node.left))
        listik.extend(post_order(node.right))
        listik.append(node.data)
    return listik
