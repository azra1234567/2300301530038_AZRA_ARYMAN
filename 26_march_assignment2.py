class Solution(object):
    def partition(self, head, x):
        small_head = small = ListNode(0)
        big_head = big = ListNode(0)

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next

        big.next = None
        small.next = big_head.next
        return small_head.next