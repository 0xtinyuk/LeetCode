# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        tail = head
        counter = 1
        while not (tail.next is None):
            tail=tail.next
            counter+=1
        return self.mergeSort(head,counter)
    
    def mergeSort(self,head:ListNode, n:int)->ListNode:
        if n==1:
            return head
        if n==2:
            if head.val>head.next.val:
                tail = head.next
                tail.next = head
                head.next = None
                return tail
            return head
        half = n//2
        half_tail = head
        counter = 1
        while counter<half:
            counter+=1
            half_tail = half_tail.next
        half_head = self.mergeSort(half_tail.next,n-half)
        head = self.mergeSort(head,half)
        current = ListNode(-1)
        ans=current
        c1=0
        c2=0
        while (c1<half) or (c2 < (n-half)):
            if (c1>=half) or (((c1<half) and (c2<(n-half))) and (head.val>half_head.val)):
                current.next=half_head
                current=current.next
                half_head=half_head.next
                c2+=1
            else:
                c1+=1
                current.next = head
                current=current.next
                head=head.next
        current.next=None
        return ans.next