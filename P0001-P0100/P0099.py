from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return f"cnt = {self.val} & " \
               f"left = {self.left.val if self.left else None} & " \
               f"right = {self.right.val if self.right else None}"


class Solution:
    def __init__(self):
        self.nodes = []

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.nodes = []
        self._inorder_traversal(root)
        values = sorted([node.val for node in self.nodes])
        n1, n2 = None, None
        for node, value in zip(self.nodes, values):
            if node.val != value:
                if n1 is None:
                    n1 = node
                else:
                    n2 = node
        if n1 and n2:
            n1.val, n2.val = n2.val, n1.val

    def _inorder_traversal(self, root: TreeNode) -> None:
        if root.left:
            self._inorder_traversal(root.left)
        self.nodes.append(root)
        if root.right:
            self._inorder_traversal(root.right)


def to_tree(root_node: int, tree_structures: List[List[int]]):
    nodes = [TreeNode(k) for k in range(100)]
    for root, left, right in tree_structures:
        nodes[root].left = nodes[left] if left else None
        nodes[root].right = nodes[right] if right else None
    return nodes[root_node]


def treeNodeToString(root: TreeNode) -> List[int]:
    if not root:
        return []
    output = []
    queue = [root, ]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1
        if not node:
            output.append(None)
            continue
        output.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while output and output[-1] is None:
        output.pop()
    return output


if __name__ == '__main__':
    solution = Solution()

    tree_node = to_tree(1, [[1, 3, None], [3, None, 2]])
    solution.recoverTree(tree_node)
    print(treeNodeToString(tree_node), [3, 1, None, None, 2])

    tree_node = to_tree(3, [[3, 1, 4], [4, 2, None]])
    solution.recoverTree(tree_node)
    print(treeNodeToString(tree_node), [2, 1, 4, None, None, 3])
