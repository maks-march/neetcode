# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None:
            return
        reverse = None
        go = head
        length = 0
        while go != None:
            print(go.val)
            prev = reverse
            reverse = ListNode(go.val)
            reverse.next = prev
            go = go.next
            length += 1

        go = head.next
        go_rev = reverse
        is_rev = True
        i = 1
        while i != length:
            if is_rev:
                head.next = ListNode(go_rev.val)
                head = head.next
                go_rev = go_rev.next
            else:
                head.next = ListNode(go.val)
                head = head.next
                go = go.next
            is_rev = not is_rev
            i += 1
        