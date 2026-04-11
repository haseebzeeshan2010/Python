class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#       A
#      / \
#     B   C
#    / \
#   D   E


root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")


def dfs(node):
    if node is None:
        return
    print(node.value)
    dfs(node.left)
    dfs(node.right)

dfs(root)