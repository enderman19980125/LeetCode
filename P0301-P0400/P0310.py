from typing import Tuple, List


class Solution:
    def __init__(self):
        self.adjacent_nodes = []
        self.heights = {}

    def __get_height(self, from_node: int, to_node: int) -> int:
        key = (from_node, to_node)
        if key in self.heights.keys():
            return self.heights.get(key)

        if len(self.adjacent_nodes[to_node]) == 1:
            self.heights.setdefault(key, 1)

        height = 0
        for node in self.adjacent_nodes[to_node]:
            if node != from_node:
                height = max(height, self.__get_height(to_node, node))
        height += 1
        self.heights.setdefault(key, height)

        return height

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        self.adjacent_nodes = [[] for _ in range(n)]
        for n1, n2 in edges:
            self.adjacent_nodes[n1].append(n2)
            self.adjacent_nodes[n2].append(n1)

        current_height = 1000000
        root_nodes = []

        for root_node in range(n):
            height = 0
            for node in self.adjacent_nodes[root_node]:
                height = max(height, self.__get_height(root_node, node))
            if height == current_height:
                root_nodes.append(root_node)
            elif height < current_height:
                current_height = height
                root_nodes = [root_node]

        return root_nodes


class Solution2:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjacent_nodes = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adjacent_nodes[n1].append(n2)
            adjacent_nodes[n2].append(n1)

        while len(adjacent_nodes) > 2:
            nodes_to_delete = []
            for node, adj_nodes in adjacent_nodes.items():
                if len(adj_nodes) == 1:
                    nodes_to_delete.append(node)
            for node in nodes_to_delete:
                for adj_node in adjacent_nodes[node]:
                    adjacent_nodes[adj_node].remove(node)
                adjacent_nodes.pop(node)

        return list(adjacent_nodes.keys())


def test(input_content: Tuple[int, List[List[int]]], std_answer: List[int]) -> None:
    solution = Solution()
    answer = solution.findMinHeightTrees(input_content[0], input_content[1])
    print(f"%s %s %s" % (sorted(answer) == sorted(std_answer), answer, std_answer))


if __name__ == '__main__':
    test(input_content=(4, [[1, 0], [1, 2], [1, 3]]), std_answer=[1])
    test(input_content=(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]), std_answer=[3, 4])
    test(input_content=(1, []), std_answer=[0])
    test(input_content=(2, [[0, 1]]), std_answer=[0, 1])
    test(input_content=(4, [[0, 1], [1, 2], [2, 3]]), std_answer=[1, 2])
    test(input_content=(5, [[0, 1], [1, 2], [2, 3], [3, 4]]), std_answer=[2])
