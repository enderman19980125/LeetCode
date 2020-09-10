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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        nodes = []
        if root.left:
            nodes.extend(self.inorderTraversal(root.left))
        nodes.append(root.val)
        if root.right:
            nodes.extend(self.inorderTraversal(root.right))
        return nodes


def to_tree(root_node: int, tree_structures: List[List[int]]):
    nodes = [TreeNode(k) for k in range(100)]
    for root, left, right in tree_structures:
        nodes[root].left = nodes[left] if left else None
        nodes[root].right = nodes[right] if right else None
    return nodes[root_node]


if __name__ == '__main__':
    solution = Solution()

    tree_node = to_tree(1, [[1, None, 2], [2, 3, None]])
    answer = solution.inorderTraversal(tree_node)
    print(answer, [1, 3, 2])

    tree_node = to_tree(1, [[1, None, 2]])
    answer = solution.inorderTraversal(tree_node)
    print(answer, [1, 2])
