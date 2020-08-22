# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        p = head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                p.next = l1
                p = l1
                l1 = l1.next
            else:
                p.next = l2
                p = l2
                l2 = l2.next
        p.next = l1 if l2 is None else l2
        head = head.next
        return head


if __name__ == '__main__':
    n11 = ListNode(1)
    n12 = ListNode(2)
    n13 = ListNode(4)
    n11.next = n12
    n12.next = n13

    n21 = ListNode(1)
    n22 = ListNode(3)
    n23 = ListNode(4)
    n21.next = n22
    n22.next = n23

    solution = Solution()
    answer = solution.mergeTwoLists(n11, n21)
    nodes_list = []
    while answer is not None:
        nodes_list.append(answer.val)
        answer = answer.next
    nodes_str = " -> ".join(map(str, nodes_list))
    print(nodes_str, "1 -> 1 -> 2 -> 3 -> 4 -> 4")
