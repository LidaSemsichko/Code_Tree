from collections import deque

def tree_by_levels(root):
    result = []
    if not root: #якщо пусте, то вертаємо пустий список
        return result
    tree = deque([root]) 
    while tree: # поки є вершина
        node = tree.popleft() #беремо поточну вершину першою з deq
        result.append(node.value) #відправляємо її значення у результат
        if node.left: #якщо є ліва нода, то вставляємо її в deq
            tree.append(node.left)
        if node.right: #якщо є права, то вставляємо її в deq
            tree.append(node.right)
    return result #повертаємо список
