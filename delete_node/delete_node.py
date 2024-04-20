# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: # якщо дерево пусте
            return None
        # якщо видалити треба листок
        if key < root.val: # так як дерево бінарного пошуку, то дивимось чи ключ менше і добираємось так до самого листка
            root.left = self.deleteNode(root.left, key)
        elif key > root.val: # так само як з лівим ( менше ), то і з більшим теж
            root.right = self.deleteNode(root.right, key)
        else: #Якщо видалити треба не листок
            if not root.left:  # якщо немає лівого піддерева, то повертаємо праве піддерево
                return root.right
            elif not root.right:  # якщо немає правого, то ліве
                return root.left
            
            # Якщо є обидва
            next_node = root.right  # шукаємо наступне - найлівіший вузол у правому піддереві
            while next_node.left: 
                next_node = next_node.left
            
            root.val = next_node.val # заміна того, що треба видалити, на наступний
            root.right = self.deleteNode(root.right, next_node.val) # видаляємо того наступного з правого піддерева, бо він вже посунувся вище
        return root
