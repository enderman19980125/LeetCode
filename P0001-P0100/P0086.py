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
    def partition(self, head: ListNode, x: int) -> ListNode:
        small_head = ListNode(0)
        large_head = ListNode(0)
        small_p = small_head
        large_p = large_head

        while head:
            if head.val < x:
                small_p.next = head
                small_p = small_p.next
            else:
                large_p.next = head
                large_p = large_p.next
            head = head.next

        small_head = small_head.next
        large_head = large_head.next
        small_p.next = large_head
        large_p.next = None

        if small_head is None and large_head is not None:
            return large_head
        else:
            return small_head


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

    first_node = to_link([1, 4, 3, 2, 5, 2])
    answer = solution.partition(first_node, 3)
    print(to_string(answer), "1->2->2->4->3->5")

    first_node = to_link([1])
    answer = solution.partition(first_node, 3)
    print(to_string(answer), "1")

    first_node = to_link([3])
    answer = solution.partition(first_node, 3)
    print(to_string(answer), "3")

    first_node = to_link([3, 1])
    answer = solution.partition(first_node, 3)
    print(to_string(answer), "1->3")

    first_node = to_link([1, 3])
    answer = solution.partition(first_node, 3)
    print(to_string(answer), "1->3")

    first_node = to_link([1, 3, 2, 4])
    answer = solution.partition(first_node, 3)
    print(to_string(answer), "1->2->3->4")
