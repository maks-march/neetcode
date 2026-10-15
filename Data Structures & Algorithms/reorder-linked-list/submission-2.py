# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None:
            return
        
        fast = head
        slow = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        
        reverse = slow.next
        go = slow.next
        prev = None

        while go != None:
            reverse = go
            go = go.next
            reverse.next = prev
            prev = reverse

        go = head.next
        go_rev = reverse
        is_rev = True
        while go_rev and go != go_rev:
            if is_rev:
                head.next = ListNode(go_rev.val)
                head = head.next
                go_rev = go_rev.next
            else:
                head.next = ListNode(go.val)
                head = head.next
                go = go.next
            is_rev = not is_rev
        head.next = ListNode(go.val)
        