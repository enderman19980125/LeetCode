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
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        if n == 1:
            return [TreeNode(1)]

        ans_list = []
        for root_value in range(1, n + 1):
            root = TreeNode(root_value)
            nums = [i for i in range(1, n + 1)]
            while self._build(root, nums):
                new_root = self._deep_copy(root)
                ans_list.append(new_root)

        return ans_list

    def _build(self, root: TreeNode, nums: List[int]) -> bool:
        if not nums:
            return False

        left_nums = [num for num in nums if num < root.val]
        right_nums = [num for num in nums if num > root.val]

        if root.left is None and root.right is None and (left_nums or right_nums):
            if left_nums:
                left_root = TreeNode(left_nums[0])
                root.left = left_root
                self._build(left_root, left_nums)
            if right_nums:
                right_root = TreeNode(right_nums[0])
                root.right = right_root
                self._build(right_root, right_nums)
            return True

        if root.right and self._build(root.right, right_nums):
            return True

        if root.right and root.right.val + 1 in right_nums:
            root.right = TreeNode(root.right.val + 1)
            self._build(root.right, right_nums)
            return True

        if root.left and self._build(root.left, left_nums):
            if right_nums:
                right_root = TreeNode(right_nums[0])
                root.right = right_root
                self._build(right_root, right_nums)
            return True

        if root.left and root.left.val + 1 in left_nums:
            root.left = TreeNode(root.left.val + 1)
            self._build(root.left, left_nums)
            if right_nums:
                right_root = TreeNode(right_nums[0])
                root.right = right_root
                self._build(right_root, right_nums)
            return True

        return False

    def _count(self, root: TreeNode) -> int:
        num_nodes = 1
        if root.left:
            num_nodes += self._count(root.left)
        if root.right:
            num_nodes += self._count(root.right)
        return num_nodes

    def _deep_copy(self, root: TreeNode) -> TreeNode:
        new_root = TreeNode(root.val)
        if root.left:
            new_root.left = self._deep_copy(root.left)
        if root.right:
            new_root.right = self._deep_copy(root.right)
        return new_root


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

    answer = solution.generateTrees(0)
    print(to_list(answer))
    print([])

    answer = solution.generateTrees(1)
    print(to_list(answer))
    print([[1]])

    answer = solution.generateTrees(2)
    print(to_list(answer))
    print([
        [1, None, 2],
        [2, 1]
    ])

    answer = solution.generateTrees(3)
    print(to_list(answer))
    print([
        [1, None, 3, 2],
        [3, 2, None, 1],
        [3, 1, None, None, 2],
        [2, 1, 3],
        [1, None, 2, None, 3]
    ])

    answer = solution.generateTrees(4)
    print(to_list(answer))
    print([
        [1, None, 2, None, 3, None, 4],
        [1, None, 2, None, 4, 3],
        [1, None, 3, 2, 4],
        [1, None, 4, 2, None, None, 3],
        [1, None, 4, 3, None, 2],
        [2, 1, 3, None, None, None, 4],
        [2, 1, 4, None, None, 3],
        [3, 1, 4, None, 2],
        [3, 2, 4, 1],
        [4, 1, None, None, 2, None, 3],
        [4, 1, None, None, 3, 2],
        [4, 2, None, 1, 3],
        [4, 3, None, 1, None, None, 2],
        [4, 3, None, 2, None, 1]
    ])

    answer = solution.generateTrees(5)
    print(to_list(answer))
    print([
        [1, None, 2, None, 3, None, 4, None, 5],
        [1, None, 2, None, 3, None, 5, 4],
        [1, None, 2, None, 4, 3, 5],
        [1, None, 2, None, 5, 3, None, None, 4],
        [1, None, 2, None, 5, 4, None, 3],
        [1, None, 3, 2, 4, None, None, None, 5],
        [1, None, 3, 2, 5, None, None, 4],
        [1, None, 4, 2, 5, None, 3],
        [1, None, 4, 3, 5, 2],
        [1, None, 5, 2, None, None, 3, None, 4],
        [1, None, 5, 2, None, None, 4, 3],
        [1, None, 5, 3, None, 2, 4],
        [1, None, 5, 4, None, 2, None, None, 3],
        [1, None, 5, 4, None, 3, None, 2],
        [2, 1, 3, None, None, None, 4, None, 5],
        [2, 1, 3, None, None, None, 5, 4],
        [2, 1, 4, None, None, 3, 5],
        [2, 1, 5, None, None, 3, None, None, 4],
        [2, 1, 5, None, None, 4, None, 3],
        [3, 1, 4, None, 2, None, 5],
        [3, 1, 5, None, 2, 4],
        [3, 2, 4, 1, None, None, 5],
        [3, 2, 5, 1, None, 4],
        [4, 1, 5, None, 2, None, None, None, 3],
        [4, 1, 5, None, 3, None, None, 2],
        [4, 2, 5, 1, 3],
        [4, 3, 5, 1, None, None, None, None, 2],
        [4, 3, 5, 2, None, None, None, 1],
        [5, 1, None, None, 2, None, 3, None, 4],
        [5, 1, None, None, 2, None, 4, 3],
        [5, 1, None, None, 3, 2, 4],
        [5, 1, None, None, 4, 2, None, None, 3],
        [5, 1, None, None, 4, 3, None, 2],
        [5, 2, None, 1, 3, None, None, None, 4],
        [5, 2, None, 1, 4, None, None, 3],
        [5, 3, None, 1, 4, None, 2],
        [5, 3, None, 2, 4, 1],
        [5, 4, None, 1, None, None, 2, None, 3],
        [5, 4, None, 1, None, None, 3, 2],
        [5, 4, None, 2, None, 1, 3],
        [5, 4, None, 3, None, 1, None, None, 2],
        [5, 4, None, 3, None, 2, None, 1]
    ])

    answer = solution.generateTrees(6)
    print(to_list(answer))
    print([
        [1, None, 2, None, 3, None, 4, None, 5, None, 6],
        [1, None, 2, None, 3, None, 4, None, 6, 5],
        [1, None, 2, None, 3, None, 5, 4, 6],
        [1, None, 2, None, 3, None, 6, 4, None, None, 5],
        [1, None, 2, None, 3, None, 6, 5, None, 4],
        [1, None, 2, None, 4, 3, 5, None, None, None, 6],
        [1, None, 2, None, 4, 3, 6, None, None, 5],
        [1, None, 2, None, 5, 3, 6, None, 4],
        [1, None, 2, None, 5, 4, 6, 3],
        [1, None, 2, None, 6, 3, None, None, 4, None, 5],
        [1, None, 2, None, 6, 3, None, None, 5, 4],
        [1, None, 2, None, 6, 4, None, 3, 5],
        [1, None, 2, None, 6, 5, None, 3, None, None, 4],
        [1, None, 2, None, 6, 5, None, 4, None, 3],
        [1, None, 3, 2, 4, None, None, None, 5, None, 6],
        [1, None, 3, 2, 4, None, None, None, 6, 5],
        [1, None, 3, 2, 5, None, None, 4, 6],
        [1, None, 3, 2, 6, None, None, 4, None, None, 5],
        [1, None, 3, 2, 6, None, None, 5, None, 4],
        [1, None, 4, 2, 5, None, 3, None, 6],
        [1, None, 4, 2, 6, None, 3, 5],
        [1, None, 4, 3, 5, 2, None, None, 6],
        [1, None, 4, 3, 6, 2, None, 5],
        [1, None, 5, 2, 6, None, 3, None, None, None, 4],
        [1, None, 5, 2, 6, None, 4, None, None, 3],
        [1, None, 5, 3, 6, 2, 4],
        [1, None, 5, 4, 6, 2, None, None, None, None, 3],
        [1, None, 5, 4, 6, 3, None, None, None, 2],
        [1, None, 6, 2, None, None, 3, None, 4, None, 5],
        [1, None, 6, 2, None, None, 3, None, 5, 4],
        [1, None, 6, 2, None, None, 4, 3, 5],
        [1, None, 6, 2, None, None, 5, 3, None, None, 4],
        [1, None, 6, 2, None, None, 5, 4, None, 3],
        [1, None, 6, 3, None, 2, 4, None, None, None, 5],
        [1, None, 6, 3, None, 2, 5, None, None, 4],
        [1, None, 6, 4, None, 2, 5, None, 3],
        [1, None, 6, 4, None, 3, 5, 2],
        [1, None, 6, 5, None, 2, None, None, 3, None, 4],
        [1, None, 6, 5, None, 2, None, None, 4, 3],
        [1, None, 6, 5, None, 3, None, 2, 4],
        [1, None, 6, 5, None, 4, None, 2, None, None, 3],
        [1, None, 6, 5, None, 4, None, 3, None, 2],
        [2, 1, 3, None, None, None, 4, None, 5, None, 6],
        [2, 1, 3, None, None, None, 4, None, 6, 5],
        [2, 1, 3, None, None, None, 5, 4, 6],
        [2, 1, 3, None, None, None, 6, 4, None, None, 5],
        [2, 1, 3, None, None, None, 6, 5, None, 4],
        [2, 1, 4, None, None, 3, 5, None, None, None, 6],
        [2, 1, 4, None, None, 3, 6, None, None, 5],
        [2, 1, 5, None, None, 3, 6, None, 4],
        [2, 1, 5, None, None, 4, 6, 3],
        [2, 1, 6, None, None, 3, None, None, 4, None, 5],
        [2, 1, 6, None, None, 3, None, None, 5, 4],
        [2, 1, 6, None, None, 4, None, 3, 5],
        [2, 1, 6, None, None, 5, None, 3, None, None, 4],
        [2, 1, 6, None, None, 5, None, 4, None, 3],
        [3, 1, 4, None, 2, None, 5, None, None, None, 6],
        [3, 1, 4, None, 2, None, 6, None, None, 5],
        [3, 1, 5, None, 2, 4, 6],
        [3, 1, 6, None, 2, 4, None, None, None, None, 5],
        [3, 1, 6, None, 2, 5, None, None, None, 4],
        [3, 2, 4, 1, None, None, 5, None, None, None, 6],
        [3, 2, 4, 1, None, None, 6, None, None, 5],
        [3, 2, 5, 1, None, 4, 6],
        [3, 2, 6, 1, None, 4, None, None, None, None, 5],
        [3, 2, 6, 1, None, 5, None, None, None, 4],
        [4, 1, 5, None, 2, None, 6, None, 3],
        [4, 1, 6, None, 2, 5, None, None, 3],
        [4, 1, 5, None, 3, None, 6, 2],
        [4, 1, 6, None, 3, 5, None, 2],
        [4, 2, 5, 1, 3, None, 6],
        [4, 2, 6, 1, 3, 5],
        [4, 3, 5, 1, None, None, 6, None, 2],
        [4, 3, 6, 1, None, 5, None, None, 2],
        [4, 3, 5, 2, None, None, 6, 1],
        [4, 3, 6, 2, None, 5, None, 1],
        [5, 1, 6, None, 2, None, None, None, 3, None, 4],
        [5, 1, 6, None, 2, None, None, None, 4, 3],
        [5, 1, 6, None, 3, None, None, 2, 4],
        [5, 1, 6, None, 4, None, None, 2, None, None, 3],
        [5, 1, 6, None, 4, None, None, 3, None, 2],
        [5, 2, 6, 1, 3, None, None, None, None, None, 4],
        [5, 2, 6, 1, 4, None, None, None, None, 3],
        [5, 3, 6, 1, 4, None, None, None, 2],
        [5, 3, 6, 2, 4, None, None, 1],
        [5, 4, 6, 1, None, None, None, None, 2, None, 3],
        [5, 4, 6, 1, None, None, None, None, 3, 2],
        [5, 4, 6, 2, None, None, None, 1, 3],
        [5, 4, 6, 3, None, None, None, 1, None, None, 2],
        [5, 4, 6, 3, None, None, None, 2, None, 1],
        [6, 1, None, None, 2, None, 3, None, 4, None, 5],
        [6, 1, None, None, 2, None, 3, None, 5, 4],
        [6, 1, None, None, 2, None, 4, 3, 5],
        [6, 1, None, None, 2, None, 5, 3, None, None, 4],
        [6, 1, None, None, 2, None, 5, 4, None, 3],
        [6, 1, None, None, 3, 2, 4, None, None, None, 5],
        [6, 1, None, None, 3, 2, 5, None, None, 4],
        [6, 1, None, None, 4, 2, 5, None, 3],
        [6, 1, None, None, 4, 3, 5, 2],
        [6, 1, None, None, 5, 2, None, None, 3, None, 4],
        [6, 1, None, None, 5, 2, None, None, 4, 3],
        [6, 1, None, None, 5, 3, None, 2, 4],
        [6, 1, None, None, 5, 4, None, 2, None, None, 3],
        [6, 1, None, None, 5, 4, None, 3, None, 2],
        [6, 2, None, 1, 3, None, None, None, 4, None, 5],
        [6, 2, None, 1, 3, None, None, None, 5, 4],
        [6, 2, None, 1, 4, None, None, 3, 5],
        [6, 2, None, 1, 5, None, None, 3, None, None, 4],
        [6, 2, None, 1, 5, None, None, 4, None, 3],
        [6, 3, None, 1, 4, None, 2, None, 5],
        [6, 3, None, 1, 5, None, 2, 4],
        [6, 3, None, 2, 4, 1, None, None, 5],
        [6, 3, None, 2, 5, 1, None, 4],
        [6, 4, None, 1, 5, None, 2, None, None, None, 3],
        [6, 4, None, 1, 5, None, 3, None, None, 2],
        [6, 4, None, 2, 5, 1, 3],
        [6, 4, None, 3, 5, 1, None, None, None, None, 2],
        [6, 4, None, 3, 5, 2, None, None, None, 1],
        [6, 5, None, 1, None, None, 2, None, 3, None, 4],
        [6, 5, None, 1, None, None, 2, None, 4, 3],
        [6, 5, None, 1, None, None, 3, 2, 4],
        [6, 5, None, 1, None, None, 4, 2, None, None, 3],
        [6, 5, None, 1, None, None, 4, 3, None, 2],
        [6, 5, None, 2, None, 1, 3, None, None, None, 4],
        [6, 5, None, 2, None, 1, 4, None, None, 3],
        [6, 5, None, 3, None, 1, 4, None, 2],
        [6, 5, None, 3, None, 2, 4, 1],
        [6, 5, None, 4, None, 1, None, None, 2, None, 3],
        [6, 5, None, 4, None, 1, None, None, 3, 2],
        [6, 5, None, 4, None, 2, None, 1, 3],
        [6, 5, None, 4, None, 3, None, 1, None, None, 2],
        [6, 5, None, 4, None, 3, None, 2, None, 1]
    ])

    answer = solution.generateTrees(8)
    print(to_list(answer))
