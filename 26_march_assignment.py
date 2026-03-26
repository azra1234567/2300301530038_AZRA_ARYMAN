def reorderList(self, head):
        if not head or not head.next:
            return 

        # Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing from middle
        prev = None
        curr = slow.next
        slow.next = None    # split lists

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. Merging two lists
        first, second = head, prev
        while second:
            f_next = first.next
            s_next = second.next

            first.next = second
            second.next = f_next

            first = f_next
            second = s_next