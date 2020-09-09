# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        head = ListNode(0,head)
        start = head
        cur = head
        i=0
        while cur.next:
            i+=1
            cur=cur.next
            # print(start.val,cur.val,i)
            if i==k:
                self.move(start.next,cur)
                ne=start.next
                start.next = cur
                start=ne
                i=0
                cur=ne
        return head.next
    
    def move(self,start:ListNode,end:ListNode):
        end=end.next
        cur=start.next
        pre=start
        while cur!=end:
            next = cur.next
            cur.next=pre
            pre = cur
            cur = next
        # next=cur.next
        # cur.next=pre
        start.next = end
        return   