def deleteduplicatesfromlinkedlist(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        p = head
        prev= head = ListNode(0)
        while p and p.next:
            if p.val == p.next.val:
                while p.next is not None and p.val == p.next.val:
                    p = p.next
                p=p.next
                prev.next = p
            else:
                p = p.next
                prev = prev.next
        return head.next

