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
    def isValidBST(self, root: TreeNode, min_value: int = None, max_value: int = None) -> bool:
        if not root:
            return True
        if min_value and root.val < min_value:
            return False
        if max_value and root.val > max_value:
            return False
        if root.left:
            if root.left.val >= root.val or not self.isValidBST(root.left, min_value, root.val - 1):
                return False
        if root.right:
            if root.right.val <= root.val or not self.isValidBST(root.right, root.val + 1, max_value):
                return False
        return True


def to_tree(root_node: int, tree_structures: List[List[int]]):
    nodes = [TreeNode(k) for k in range(100)]
    for root, left, right in tree_structures:
        nodes[root].left = nodes[left] if left else None
        nodes[root].right = nodes[right] if right else None
    return nodes[root_node]


def to_list(root_nodes_list: List[TreeNode]) -> List[List[int]]:
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

    trees_list = []
    for root_node in root_nodes_list:
        tree = treeNodeToString(root_node)
        trees_list.append(tree)
    return trees_list


if __name__ == '__main__':
    solution = Solution()

    tree_node = to_tree(2, [[2, 1, 3]])
    answer = solution.isValidBST(tree_node)
    print(answer, True)

    tree_node = to_tree(5, [[5, 1, 4], [4, 3, 6]])
    answer = solution.isValidBST(tree_node)
    print(answer, False)

    tree_node = to_tree(5, [[5, 1, 4], [4, 3, 6]])
    answer = solution.isValidBST(tree_node)
    print(answer, False)

    tree_node = to_tree(10, [[10, 5, 15], [15, 6, 20]])
    answer = solution.isValidBST(tree_node)
    print(answer, False)

    answer = solution.isValidBST(None)
    print(answer, True)
