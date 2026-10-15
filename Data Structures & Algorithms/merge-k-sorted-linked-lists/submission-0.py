# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        n = len(lists)

        def mergeTwo(l1,l2):
            if not l1:
                return l2
            
            if not l2:
                return l1
            
            t1 = l1
            t2 = l2
            dummy = ListNode(0)
            curr = dummy

            while t1 and t2:
                if t1.val < t2.val:
                    curr.next = t1
                    t1 = t1.next
                else:
                    curr.next = t2
                    t2 = t2.next
                
                curr = curr.next
            
            while t1:
                curr.next = t1
                t1 = t1.next
                curr = curr.next

            while t2:
                curr.next = t2
                t2 = t2.next
                curr = curr.next 
            
            return dummy.next
        
        def solve(s,e):
            if s == e:
                return lists[s]
            
            mid = (s + e)//2
            
            L1 = solve(s,mid)
            L2 = solve(mid+1,e)

            return mergeTwo(L1,L2)
        
        return solve(0,n-1)
        