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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


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

    tree_node_1 = to_tree(1, [[1, 2, 3]])
    tree_node_2 = to_tree(1, [[1, 2, 3]])
    answer = solution.isSameTree(tree_node_1, tree_node_2)
    print(answer, True)

    tree_node_1 = to_tree(1, [[1, 2, None]])
    tree_node_2 = to_tree(1, [[1, None, 2]])
    answer = solution.isSameTree(tree_node_1, tree_node_2)
    print(answer, False)

    tree_node_1 = to_tree(1, [[1, 2, 3]])
    tree_node_2 = to_tree(1, [[1, 3, 2]])
    answer = solution.isSameTree(tree_node_1, tree_node_2)
    print(answer, False)

    tree_node_1 = to_tree(1, [[1, 2, 3], [3, 4, None]])
    tree_node_2 = to_tree(1, [[1, 2, 3]])
    answer = solution.isSameTree(tree_node_1, tree_node_2)
    print(answer, False)
