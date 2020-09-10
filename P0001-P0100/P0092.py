from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        nodes = []
        p = self
        while p:
            nodes.append(str(p.val))
            p = p.next
        s = "->".join(nodes)
        return s


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head

        node_pre_m, node_m = head, head
        pre_p, p, next_p = new_head, new_head, head

        for i in range(n + 1):
            if m + 1 <= i <= n:
                p.next = pre_p
            if i == m - 1:
                node_pre_m = p
            if i == m:
                node_m = p
            if i == n:
                node_pre_m.next = p
            pre_p = p
            p = next_p
            next_p = next_p.next if next_p else None

        node_m.next = p

        return new_head.next


def to_link(nums: List[int]) -> ListNode:
    nodes = []
    for num in nums:
        p = ListNode(num)
        nodes.append(p)
    for i, _ in enumerate(nodes[:-1]):
        nodes[i].next = nodes[i + 1]
    return nodes[0]


def to_string(head: ListNode) -> str:
    nodes = []
    while head:
        nodes.append(str(head.val))
        head = head.next
    s = "->".join(nodes)
    return s


if __name__ == '__main__':
    solution = Solution()

    first_node = to_link([1, 2, 3, 4, 5])
    answer = solution.reverseBetween(first_node, 2, 4)
    print(to_string(answer), "1->4->3->2->5")

    first_node = to_link([1, 2, 3, 4, 5])
    answer = solution.reverseBetween(first_node, 1, 4)
    print(to_string(answer), "4->3->2->1->5")

    first_node = to_link([1, 2, 3, 4, 5])
    answer = solution.reverseBetween(first_node, 2, 5)
    print(to_string(answer), "1->5->4->3->2")

    first_node = to_link([1, 2, 3, 4, 5])
    answer = solution.reverseBetween(first_node, 1, 5)
    print(to_string(answer), "5->4->3->2->1")

    first_node = to_link([1])
    answer = solution.reverseBetween(first_node, 1, 1)
    print(to_string(answer), "1")

    first_node = to_link([1, 2])
    answer = solution.reverseBetween(first_node, 1, 1)
    print(to_string(answer), "1->2")

    first_node = to_link([1, 2])
    answer = solution.reverseBetween(first_node, 2, 2)
    print(to_string(answer), "1->2")

    first_node = to_link([1, 2])
    answer = solution.reverseBetween(first_node, 1, 2)
    print(to_string(answer), "2->1")
