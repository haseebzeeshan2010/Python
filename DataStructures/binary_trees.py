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


def dfs(node): # Using pre order traversal
    if node is None:
        return
    print(node.value)
    dfs(node.left)
    dfs(node.right)

def bfs(root): # Simple Breadth First Search
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

dfs(root)
print()
bfs(root)