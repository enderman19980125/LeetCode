# Definition for singly-linked list.
from typing import List


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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        h = ListNode(head.val + 1)
        h.next = head

        p = head
        pre_node = h
        pre_value = h.val
        while p:
            if p.val != pre_value:
                pre_node.next = p
                pre_node = p
            pre_value = p.val
            p = p.next
        pre_node.next = None

        return h.next


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

    first_node = to_link([1, 1, 2])
    answer = solution.deleteDuplicates(first_node)
    print(to_string(answer), "1->2")

    first_node = to_link([1, 1, 2, 3, 3])
    answer = solution.deleteDuplicates(first_node)
    print(to_string(answer), "1->2->3")

    first_node = to_link([1, 1, 1, 2, 3])
    answer = solution.deleteDuplicates(first_node)
    print(to_string(answer), "1->2->3")

    first_node = to_link([1, 2, 3, 3, 3])
    answer = solution.deleteDuplicates(first_node)
    print(to_string(answer), "1->2->3")

    first_node = to_link([1, 2, 2, 2, 3])
    answer = solution.deleteDuplicates(first_node)
    print(to_string(answer), "1->2->3")

    first_node = to_link([1])
    answer = solution.deleteDuplicates(first_node)
    print(to_string(answer), "1")

    first_node = to_link([1, 1])
    answer = solution.deleteDuplicates(first_node)
    print(to_string(answer), "1")

    first_node = to_link([1, 1, 2, 2, 3, 3])
    answer = solution.deleteDuplicates(first_node)
    print(to_string(answer), "1->2->3")
