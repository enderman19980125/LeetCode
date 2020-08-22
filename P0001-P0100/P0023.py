from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return self._merge2Lists(lists[0], lists[1])
        else:
            mid = len(lists) // 2
            list1 = self.mergeKLists(lists[:mid])
            list2 = self.mergeKLists(lists[mid:])
            return self._merge2Lists(list1, list2)

    def _merge2Lists(self, n1: ListNode, n2: ListNode) -> ListNode:
        head = ListNode()
        p = head
        while n1 is not None and n2 is not None:
            if n1.val < n2.val:
                p.next = n1
                p = p.next
                n1 = n1.next
            else:
                p.next = n2
                p = p.next
                n2 = n2.next
        p.next = n1 if n2 is None else n2
        head = head.next
        return head


if __name__ == '__main__':
    n11 = ListNode(1)
    n12 = ListNode(4)
    n13 = ListNode(5)
    n11.next = n12
    n12.next = n13

    n21 = ListNode(1)
    n22 = ListNode(3)
    n23 = ListNode(4)
    n21.next = n22
    n22.next = n23

    n31 = ListNode(2)
    n32 = ListNode(6)
    n31.next = n32

    solution = Solution()
    answer = solution.mergeKLists([n11, n21, n31])
    nodes_list = []
    while answer is not None:
        nodes_list.append(answer.val)
        answer = answer.next
    nodes = " -> ".join(map(str, nodes_list))
    print(nodes, "1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6")

    answer = solution.mergeKLists([])
    nodes_list = []
    while answer is not None:
        nodes_list.append(answer.val)
        answer = answer.next
    nodes = " -> ".join(map(str, nodes_list))
    print(nodes, "")

    answer = solution.mergeKLists([None])
    nodes_list = []
    while answer is not None:
        nodes_list.append(answer.val)
        answer = answer.next
    nodes = " -> ".join(map(str, nodes_list))
    print(nodes, "")
